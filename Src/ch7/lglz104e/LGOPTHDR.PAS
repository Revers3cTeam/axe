{$M 8192,66000,600000}
uses Dos;
label l0,l1;
type	pw=^word;pp=^par;par=array [0..24571] of word;
type	header=record
		sign:array [1..2] of char;
		bytes,pages,reloc,paragr,
		minmem,maxmem,ss,sp,crc,ip,cs,reladr,
		ovnum:word;
	end;
	ofseg=record
		offset,segment:word;
	end;
	pofs=^off;
	off=array [0..12284] of ofseg;
var	f:file;head:header;
	inbuf:pp;entries,kolread,i:word;
	ofs:pofs absolute inbuf;
	se:SearchRec;
	x,dt:longint;
	dn:DirStr;
	nn:NameStr;
	en:ExtStr;


procedure QuickSort(start,finish:integer);
var     left, right : integer;
	pivot, temp : ofseg;
begin
	left := start;  right := finish;pivot := ofs^[(start+finish) div 2];
	repeat
		while (ofs^[left].segment < pivot.segment) or
		((ofs^[left].segment = pivot.segment) and
		(ofs^[left].offset < pivot.offset))
		do Inc(left);
		while (ofs^[right].segment > pivot.segment) or
		((ofs^[right].segment = pivot.segment) and
		(ofs^[right].offset > pivot.offset))
		do Dec(right);
		if left <= right then begin
			if left<right then begin
				temp:=ofs^[left];
				ofs^[left]:=ofs^[right];
				ofs^[right]:=temp;
			end;
			Inc(left);Dec(right);
		end;
	until right <= left;
	if start < right then QuickSort(start, right);
	if left < finish then QuickSort(left, finish);
end;

begin
	Writeln(
'EXE-header optimization program LGOPTHDR v1.0         (c) George Lyapko 1996');
	if ParamCount=0 then begin
		Writeln('Usage: LGOPTHDR File_mask');
		Halt(1)
	end;
	if MaxAvail<SizeOf(par) then begin
		Writeln('Memory fault');
		Halt(6);
	end;
	GetMem(inbuf,SizeOf(par));
	FSplit(ParamStr(1),dn,nn,en);
	FindFirst(ParamStr(1),AnyFile,se);
	while DosError=0 do begin
		{$I-}Assign(f,dn+se.name);Reset(f,1);{$I+}
		if IOResult<>0 then begin
			Writeln('Can''t open ',dn+se.name);goto l1;
		end;
		Write(dn+se.name);
		GetFTime(f,dt);
		BlockRead(f,head,SizeOf(header),kolread);
		if (head.sign[1]<>'M') or (head.sign[2]<>'Z') then begin
			Writeln(' - not EXE-file');goto l1;
		end;
		Seek(f,head.reladr);
		if head.reloc>SizeOf(par) div 4 then begin
			Writeln(' - too big header');goto l0;
		end;
		BlockRead(f,inbuf^,head.reloc*4);
		for i:=0 to Pred(head.reloc) do begin
			x:=Longint(ofs^[i].segment)*$10+ofs^[i].offset;
			ofs^[i].segment:=(x shr 16) shl 12;
			ofs^[i].offset:= x and $FFFF;
		end;
		QuickSort(0,Pred(head.reloc));
		Seek(f,head.reladr);
		BlockWrite(f,inbuf^,head.reloc*4);
		Writeln(' - optimized');
		SetFTime(f,dt);
l0:		Close(f);
l1:		FindNext(se);
	end;
end.
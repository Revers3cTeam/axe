#include <stdio.h>
#include <conio.h>
#include <stdint.h>
#include <windows.h>

// REB{VM_P4CK3R5_AR3_S0_TRICKY_MR_L337}

int code[500] = { 0x01020000, 0x0c220002, 0x01020001, 0x0c230002, 0x0900000D, 0x01020002, 0x0c220002,
				  0x010200FF, 0x0c240002, 0x01020003, 0x0c220002, 0x01020000, 0x0c240002, 0x07010000,
				  0x02000001, 0x00000004, 0x06000004, 0x08000015, 0x0b000005, 0x07010001, 0x02000001,
				  0x0000001c, 0x06000002, 0x08000030, 0x0b000005, 0x07010002, 0x02000001, 0x0000000a,
				  0x03000005, 0x08000047, 0x0b000005, 0x07010003, 0x02000001, 0x0600000f, 0x00000005,
				  0x0800000d, 0x0b000005, 0x07010006, 0x02000001, 0x0400001a, 0x05000006, 0x0800019e,
				  0x0b000005, 0x07010005, 0x02000001, 0x06000004, 0x00000003, 0x08000016, 0x0b000005,
				  0x07010004, 0x02000001, 0x0600001e, 0x00000005, 0x08000007, 0x0b000005, 0x07010007,
				  0x02000001, 0x06000003, 0x00000004, 0x0800001e, 0x0b000005, 0x07010008, 0x02000001,
				  0x0400000a, 0x05000006, 0x08000174, 0x0b000005, 0x07010009, 0x02000001, 0x06000013,
				  0x00000006, 0x08000009, 0x0b000005, 0x0701000a, 0x02000001, 0x03000007, 0x00000006,
				  0x0800004a, 0x0b000005, 0x0701000b, 0x02000001, 0x03000013, 0x00000006, 0x08000026,
				  0x0b000005, 0x0701000c, 0x02000001, 0x00000010, 0x03000004, 0x0800005e, 0x0b000005,
				  0x0701000d, 0x02000001, 0x0000001d, 0x06000003, 0x0800001b, 0x0b000005, 0x0701000e,
				  0x02000001, 0x00000003, 0x06000002, 0x08000031, 0x0b000005, 0x0701000f, 0x02000001,
				  0x0300001c, 0x00000005, 0x0800002a, 0x0b000005, 0x07010010, 0x02000001, 0x0300001c,
				  0x00000004, 0x0800003a, 0x0b000005, 0x07010011, 0x02000001, 0x03000010, 0x00000003,
				  0x08000026, 0x0b000005, 0x07010012, 0x02000001, 0x06000011, 0x00000004, 0x08000009,
				  0x0b000005, 0x07010013, 0x02000001, 0x0300000b, 0x00000002, 0x0800004a, 0x0b000005,
				  0x07010014, 0x02000001, 0x0600001e, 0x00000005, 0x08000006, 0x0b000005, 0x07010015,
				  0x02000001, 0x03000013, 0x00000006, 0x08000052, 0x0b000005, 0x07010016, 0x02000001,
				  0x04000002, 0x00000025, 0x0800007b, 0x0b000005, 0x07010017, 0x02000001, 0x0000000e,
				  0x05000004, 0x08000180, 0x0b000005, 0x07010018, 0x02000001, 0x0000001a, 0x03000005,
				  0x0800005e, 0x0b000005, 0x07010019, 0x02000001, 0x00000002, 0x03000002, 0x08000043,
				  0x0b000005, 0x0701001a, 0x02000001, 0x00000003, 0x05000002, 0x0800009c, 0x0b000005,
				  0x0701001b, 0x02000001, 0x0000000d, 0x0400001f, 0x08000079, 0x0b000005, 0x0701001c,
				  0x02000001, 0x0000000f, 0x06000002, 0x08000037, 0x0b000005, 0x0701001d, 0x02000001,
				  0x0600000e, 0x00000003, 0x08000008, 0x0b000005, 0x0701001e, 0x02000001, 0x0000001d,
				  0x06000005, 0x08000016, 0x0b000005, 0x0701001f, 0x02000001, 0x03000006, 0x00000002,
				  0x0800005b, 0x0b000005, 0x07010020, 0x02000001, 0x06000016, 0x00000004, 0x08000007,
				  0x0b000005, 0x07010021, 0x02000001, 0x04000011, 0x0000003b, 0x0800005d, 0x0b000005,
				  0x07010022, 0x02000001, 0x03000005, 0x00000002, 0x08000030, 0x0b000005, 0x07010023,
				  0x02000001, 0x00000004, 0x06000002, 0x0800001d, 0x0b000005, 0x07010024, 0x02000001,
				  0x00000009, 0x05000004, 0x08000218, 0x0b000005, 0x0a000009 };


const char* data[] = { "Enter Password: ","%s","Wrong","Correct!!!" };


enum
{
	R_R0 = 0,
	R_R1,
	R_R2,
	R_ZF,
	R_PC /* program counter */
};
int reg[5] = { 0,0,0,0,0 };

enum
{
	OP_ADD = 0,
	OP_MOV,
	OP_MOVR,
	OP_SUB,
	OP_XOR,
	OP_MUL,
	OP_DIV,
	OP_LOAD,
	OP_CMP,
	OP_JMP,
	OP_JE,
	OP_JNE,
	OP_TRAP
};

enum
{
	TRAP_OUT = 0x22,
	TRAP_IN = 0x23,
	TRAP_HALT = 0x24,
};

char mem[256];

int main(int argc, char argv[]) {
	while (true)
	{
		char  opcode = (code[reg[R_PC]] >> 24) & 0xFF;
		char  operand1 = (code[reg[R_PC]] >> 16) & 0xFF;
		short operand2 = (code[reg[R_PC]] & 0x0000FFFF);
		switch (opcode)
		{
			case OP_ADD:
			{
				reg[operand1] = reg[operand1] + operand2;
			}
			break;
			case OP_SUB:
			{
				reg[operand1] = reg[operand1] - operand2;
			}
			break;
			case OP_XOR:
			{
				reg[operand1] = reg[operand1] ^ operand2;
			}
			break;
			case OP_MUL:
			{
				reg[operand1] = reg[operand1] * operand2;
			}
			break;
			case OP_DIV:
			{
				reg[operand1] = reg[operand1] / operand2;
			}
			break;
			case OP_MOV:
			{
				reg[operand1] = operand2;
			}
			break;
			case OP_MOVR:
			{
				reg[operand1] = reg[operand2];
			}
			break;
			case OP_LOAD:
			{
				reg[operand1] = mem[operand2];
			}
			break;
			case OP_CMP:
			{
				if (reg[operand1] == operand2) {
					reg[R_ZF] = 1;
				}
				else {
					reg[R_ZF] = 0;

				}
				break;
			case OP_JMP:
			{
				reg[R_PC] = operand2 - 1;
			}
			break;
			case OP_JE:
			{
				if (reg[R_ZF] == 1) {
					reg[R_PC] = operand2 - 1;
				}
			}
			break;
			case OP_JNE:
			{
				if (reg[R_ZF] == 0) {
					reg[R_PC] = operand2 - 1;
				}
			}
			break;
			case OP_TRAP:
				switch (operand1)
				{
				case TRAP_OUT:
				{
					printf(data[reg[R_R2]]);
				}
				break;
				case TRAP_IN:
				{
					scanf_s(data[reg[R_R2]], mem, _countof(mem));
				}
				break;
				case TRAP_HALT:
				{
					return reg[R_R2];
				}
				break;
				}
			default:
				break;
			}
		}
		reg[R_PC]++;
	}
}
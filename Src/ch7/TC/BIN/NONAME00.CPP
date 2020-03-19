#include <stdio.h>

int stringLen(char* pointer);
void reverseXorString(char* s);
int check(char* input);

void reverseXorString(char* s)
{
	int length, c;
	char* begin, * end, temp;

	length = stringLen(s);
	begin = s;
	end = s;

	for (c = 0; c < length - 1; c++)
		end++;

	for (c = 0; c < length / 2; c++)
	{
		temp = *end;
		*end = *begin;
		*begin = temp;

		begin++;
		end--;
	}
	begin = s;
	for (c = 0; c < length; c++) {
		*begin = *begin ^ 0x5;
		begin++;
	}
}

int stringLen(char* pointer)
{
	int c = 0;

	while (*(pointer + c) != '\0')
		c++;

	return c;
}

int check(char* input) {
	reverseXorString(input);
	if (input[2] != 36) { goto bad; }
	if (input[4] != 75) { goto bad; }
	if (input[9] != 52) { goto bad; }
	if (input[1] != 36) { goto bad; }
	if (input[19] != 75) { goto bad; }
	if (input[33] != 83) { goto bad; }
	if (input[11] != 72) { goto bad; }
	if (input[38] != 64) { goto bad; }
	if (input[29] != 52) { goto bad; }
	if (input[26] != 90) { goto bad; }
	if (input[28] != 75) { goto bad; }
	if (input[39] != 87) { goto bad; }
	if (input[7] != 90) { goto bad; }
	if (input[27] != 66) { goto bad; }
	if (input[31] != 87) { goto bad; }
	if (input[34] != 54) { goto bad; }
	if (input[14] != 90) { goto bad; }
	if (input[12] != 86) { goto bad; }
	if (input[32] != 64) { goto bad; }
	if (input[3] != 36) { goto bad; }
	if (input[8] != 86) { goto bad; }
	if (input[0] != 120) { goto bad; }
	if (input[10] != 90) { goto bad; }
	if (input[24] != 52) { goto bad; }
	if (input[22] != 81) { goto bad; }
	if (input[21] != 54) { goto bad; }
	if (input[36] != 126) { goto bad; }
	if (input[20] != 54) { goto bad; }
	if (input[17] != 71) { goto bad; }
	if (input[6] != 67) { goto bad; }
	if (input[37] != 71) { goto bad; }
	if (input[35] != 87) { goto bad; }
	if (input[5] != 80) { goto bad; }
	if (input[18] != 90) { goto bad; }
	if (input[25] != 86) { goto bad; }
	if (input[16] != 52) { goto bad; }
	if (input[15] != 50) { goto bad; }
	if (input[30] != 48) { goto bad; }
	if (input[23] != 93) { goto bad; }
	if (input[13] != 49) { goto bad; }

	return 1;
bad:
	return 0;
}

int main() {
	char input[50];

	printf("           ________                        \n");
	printf("          / ______ \                       \n");
	printf("          || _  _ ||     ----------------  \n");
	printf("          ||| || |||     YOU NEED THE KEY  \n");
	printf("          |||_||_|||     TO OPEN THE DOOR  \n");
	printf("          || _  _o|| (o) ----------------  \n");
	printf("          ||| || |||          //           \n");
	printf("          |||_||_|||      ^~^  ,           \n");
	printf("          ||______||     ('Y') )           \n");
	printf("         /__________\\    /   \\/          \n");
	printf(" ________|__________|__ (\\|||/) _________ \n");
	printf("        /____________\\                    \n");
	printf("        |____________|                     \n");

	printf(">> ");
	scanf("%50s", input);
	if (check(input)) {
		printf("      ______________  \n");
		printf("	|\ ___________ /| \n");
		printf("	| |  /|,| |   | | \n");
		printf("	| | |,x,| |   | | \n");
		printf("	| | |,x,' |   | | \n");
		printf("	| | |,x   ,   | | \n");
		printf("	| | |/    |===| | \n");
		printf("	| |    /] ,   | | \n");
		printf("	| |   [/ ()   | | \n");
		printf("	| |       |   | | \n");
		printf("	| |       |   | | \n");
		printf("	| |       |   | | \n");
		printf("	| |      ,'   | | \n");
		printf("	| |   ,'      | | \n");
		printf("	|_|,'_________|_| \n");
		printf("	YOU CAN NOW ENTER \n");
		printf("	  THE 1337 DOOR   \n");
	}
	else {
		printf("	           -------------------\n");
		printf("	           You're Under Arrest\n");
		printf("	           -------------------\n");
		printf("	               //             \n");
		printf("	 __  _.-'- -'-.               \n");
		printf("	/||\'._ __{}_(                \n");
		printf("	||||  |'--.__\\               \n");
		printf("	|  L.(   ^_\\^                \n");
		printf("	\\ .-' |   _ |                \n");
		printf("	| |   )\\___/                 \n");
		printf("	|  \\-'-:._]                  \n");
		printf("	\\__/;      '-.               \n");
		printf("	   -o     __ \\               \n");
		printf("	   -o     )( /                \n");
		printf("	   -o     \\/ \\              \n");
	}
	return 0;
}

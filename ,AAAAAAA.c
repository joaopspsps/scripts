#include <stdio.h>
#define p(c)fputc_unlocked(c,stdout)
main(){for(;;)p('A'),p('\n');}

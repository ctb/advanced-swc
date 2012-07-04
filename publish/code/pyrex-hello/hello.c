#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char * hello(char * name)
{
  char * buf;
  buf = (char *) malloc(strlen("hello, ") + strlen(name) + 1);

  sprintf(buf, "hello, %s", name);
  return buf;
}

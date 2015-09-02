#include <stdio.h>
#include <string.h>

void reverse(char *);
void reverse2(char *);

int main(){
  char hi[] = "hello";
  printf("%s\n", hi);
  reverse(hi);
  printf("%s\n", hi);
  reverse2(hi);
  printf("%s\n", hi);
  return 0;
}

void reverse(char * s) {
  int length = strlen(s);
  for(int i=0; i<length/2; i++){
    char t = s[i];
    s[i] = s[length-i-1];
    s[length-i-1] = t;
  }
  return;
}

void reverse2(char * s){
  char * end = s;
  char tmp;
  while(*end){ end++; };
  end--;

  while(s<end){
    tmp = *s;
    *s = *end;
    *end = tmp;
    s++;
    end--;
  }
}

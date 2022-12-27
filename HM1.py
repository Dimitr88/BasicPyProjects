first_string = '\timport antigravity\n\timport __hello__\n\tfrom __future__ import braces'
print(first_string)

my_name ='*'*10+"    "+"*"+"\t\t\t  *"+"\t *"+"\t\t\t *"+"  "+'*'*11+"  "+'*'*10+"\t\t   "+"******"\
"\n*\t\t  *\t  **\t\t **\t  *\t\t\t*\t\t *\t\t *\t\t\t*\t*\t\t   *" \
"\n*\t\t   *  * *\t\t* *\t   *\t   *\t\t *\t\t *\t\t\t*  *\t\t\t*" \
"\n*\t\t   *  *  *     *  *\t\t*\t  *\t\t\t *\t\t *\t\t\t*  *\t\t\t*" \
"\n*\t\t   *  *   *   *   *\t\t *\t *\t\t\t *"+"\t\t "+'*'*11+"   *\t\t\t*" \
"\n*\t\t   *  *    * *    *\t\t  * *\t\t\t *\t\t *\t\t\t*  *\t\t\t*" \
"\n*\t\t   *  *\t\t\t  *\t\t   *\t\t\t *\t\t *\t\t\t * *\t\t\t*" \
"\n*\t\t  *   *\t\t\t  *\t\t   *\t\t\t *\t\t *\t\t\t *  *\t\t   *"\
'\n'+'*'*10+"\t  *\t\t\t  *\t\t   *\t\t\t *\t\t *\t\t\t *\t   ******"
print(my_name)

escape_sequences = '\\a  \tBell (alert)\n\\b  \tBackspace\n\\n  \tNew line ' \
    '\n\\t  \tHorizontal tab\n\\\  \tBackslash\n\\"  \tDouble quotation mark " ' \
    "\n\\'  \tDouble quotation mark'"
print(escape_sequences)

#Task 1
apples = int(input('Enter number of apples: '))
pupils = int(input('Enter number of pupils: '))
print(f'Number of apples for each pupil: {apples} / {pupils} = {apples // pupils}')
print(f'Number of apples in the backet: {apples} % {pupils} = {apples % pupils}')

#Task 2
first_class = int(input('Enter number of pupils for the first class: '))
second_class = int(input('Enter number of pupils for the second class: '))
third_class = int(input('Enter number of pupils for the third: '))
print(f'required number of school desks: ({first_class //2} + {first_class %2} = {first_class // 2 + first_class % 2})'
      f' + ({second_class //2} + {second_class %2} = {second_class // 2 + second_class % 2})'
      f' + ({third_class //2} + {third_class %2} = {third_class // 2 + third_class % 2})'
      f' = {first_class // 2 + first_class % 2 + second_class // 2 + second_class % 2 + third_class // 2 + third_class % 2}')
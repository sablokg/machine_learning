# given and string print the occurences of the given string in the same order as in the alphabet 
a= 'hadoop'
[sorted(a).count(i) for i in sorted(list(''.join({chr(c+65) for c in range(26)}).lower()))]

# write a hadoop python reducer fort he following string
a = '''Hadoop is The Elephant King A yellow and elegant thing A wonderful King is Hadoop
        The Elephant plays well with Sqoop But what helps Hadoop to thrive 
            Are Impala and Hive and HDFS in the group'''
[print(j, len(list(map(lambda n: 0 if n in 
                                [list(''.join({chr(c+65) for c in range(26)}).lower())] else 1, j))))
                                for j in [list(i) for i in a.split()]]
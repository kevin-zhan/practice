#coding=utf8
import os
import time 
import string

#判断记录文件是否存在，若不存在则创建一个记录文件
filename = "code_record"
if not os.path.exists(filename):
	file = open(filename,'w+')
	file.write("上次记录时间:" + "1995-04-17-00:00" + "\n")
	file.write("数据格式为:  『日期::::新增代码行数』\n")
	file.close()
#获取上次运行此脚本的时间
file = open(filename,"r")
pre_time = file.readline()
pre_time = pre_time[19:35]
file.close()
#更新运行此脚本的时间
now_time = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
file = open(filename,'r+')
file.write("上次记录时间:" + now_time + "\n")
file.close()

#计算自上一次运行此脚本以来，提交了多少行代码
cmd = "git log --shortstat --since==" + pre_time
output = os.popen(cmd)
content = output.read()
commits = content.split("commit") #用"commit"作关键字分隔每次提交的commit
add_line = []
sub_line = []
for commit in commits[1:]:
	str1 = "changed, "
	str2 = " insertions(+)"
	str3 = " deletions(-)"
	pos1 = commit.find(str1)+len(str1)
	pos2 = commit.find(str2)
	pos3 = commit.find(str3)
	if pos1<len(str1):
		continue
	if pos2<0:
		add_line.append(0)
		sub_line.append(string.atoi(commit[pos1:pos3]))
		continue
	add_line.append(string.atoi(commit[pos1:pos2]))
	pos2 = pos2 + len(str2)+2
	if pos3<0:
		sub_line.append(0)
		continue
	sub_line.append(string.atoi(commit[pos2:pos3]))
code_line = sum(add_line)-sum(sub_line)
if code_line != 0:	
	file = open(filename,'a+')
	file.write(now_time + "::::%d\n"%code_line)
	file.close()
print "统计完成，自" + pre_time + "开始，到现在(" + now_time + ")共添加了%d行代码。"%code_line
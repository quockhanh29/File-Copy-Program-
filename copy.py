import os
import shutil
import glob


def func_user_init():	#Initialization
	print('-----Start Init()-----')
	print('-----Stop Init()-----')


def func_user_main():	#main function
	print('-----Start main()-----')
	try:
		fPath = open("1_path.txt", 'r', encoding='utf-8')	#open path.txt
		f = open("2_target_file_list.txt", 'r', encoding='utf-8')	#open target_file_list.txt
		scrpath = fPath.readline()	#1st - read source path
		dstpath = fPath.readline()	#2nd - read destination path
		print('Clear dst path...')
		files = glob.glob(dstpath.rstrip() + '/*')
		for fn in files:
			os.remove(fn)

		fExt = ['.h', '.c']		#target file extension
		print('Copying...')
		for fname in f:
			for index in range(len(fExt)):
				target_file = fname.rstrip() + fExt[index]
				path = scrpath.rstrip() + target_file
				if os.path.isfile(path):
					print(path + ' has been copied successfully')
					shutil.copy2( path, dstpath)
				else:
					print(path + ' does NOT exist')
	finally:
		f.close()
		fPath.close()
		print('-----Stop main()-----')

#Software starts here
if __name__ == "__main__":
    func_user_init()
    func_user_main()

import time








def main():
	ticks = time.time()
	local = time.localtime(time.time())

	while local.tm_min < 31:
		temp_local = time.localtime(time.time())
		if temp_local.tm_sec != local.tm_sec:
			print(temp_local)
			local = temp_local

if __name__ == "__main__":
	main()
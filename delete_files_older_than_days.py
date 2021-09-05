import os
from datetime import date, timedelta

count = 0

older_than = date.today() - timedelta(days=2)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f.endswith('.zip') or f.endswith('.gz'):
		if date.fromtimestamp(os.path.getmtime(f)) < older_than:
			count += 1
			os.remove(f)
			print('Deleted:',f)
print('Total files deleted:',count)
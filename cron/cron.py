from crontab import CronTab

my_cron = CronTab(user='root')
job1 = my_cron.new(command='python /home/thiru/k1groups/cron/main.py')
job1.minute.every(5)
my_cron.write()

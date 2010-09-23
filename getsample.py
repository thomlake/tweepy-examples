import tweepy, sys

class StreamController:
	def __init__(self, uname, pword):
		self.n = 10
		self.handler = StreamHandler(self)
		self.stream = tweepy.Stream(uname, pword, self.handler, timeout=None)
		self.ctr = 0
		self.tweetlist = []
	
	def start_sample(self):
		self.stream.sample()
	
	def stop_sample(self):
		self.stream.disconnect()
		for i, twit in enumerate(self.tweetlist):
			print i, ":", twit

class StreamHandler(tweepy.StreamListener):
	def __init__(self, controller = None):
		super(StreamHandler, self).__init__()
		self.controller = controller
		self.count = 0
	
	def on_status(self, status):
		if self.count < self.controller.n:
			if status.author.lang == "en":
				self.count += 1
				self.controller.tweetlist.append(status.text)
		else:
			self.controller.stop_sample()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "usage: tweepstream.py  <username> <password>"
		sys.exit()
	uname = sys.argv[1]
	pword = sys.argv[2]
	twit = StreamController(uname, pword)
	twit.start_sample()

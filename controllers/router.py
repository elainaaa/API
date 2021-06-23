from tornado.web import RequestHandler
from routes import beatmap, user
from osutools import OsuClient
from decouple import config

client = OsuClient(config('OSU_API_KEY'))

class MainHandler(RequestHandler):
	def get(self):
		self.write(f"<p>GET /api/user/[username]card<br>" \
		+ f"GET /api/beatmaps/[map-id]/scores/[username]<br>" \
		+ f"GET /api/beatmaps/[map-id]/card</p>")
		self.finish()

router = [
	(r"/", MainHandler),
	(r"/api/user/(.*)/card", user.UserCardHandler, dict(client=client)),
	#(r"/api/beatmaps/(.*)/scores/(.*)", beatmap.BeatmapScoresHandler),
	(r"/api/beatmaps/(.*)/card", beatmap.BeatmapCardHandler, dict(client=client))
]
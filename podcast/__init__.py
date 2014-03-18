import logging
import os
from mediagoblin.tools.pluginapi import get_config, register_routes, register_template_path

_log = logging.getLogger(__name__)

PLUGIN_DIR = os.path.dirname(__file__)

def setup_plugin():
	_log.info("Starting podcaster")
	config = get_config('podcast')
	if config:
		_log.info("CONFIG FOUND")
	else:
		_log.info("CONFIG NOT FOUND")

	register_routes([('makeapodcast','/makeapodcast.html','podcast.views:register_podcast'),
		('podcast.rssfeed', '/u/<string:user>/podcast', 'podcast.views:get_podcasts'),
		('podcast.createpodcast','/podcast/create','podcast.views:create_podcast'),
		('podcast.listpodcast', '/u/<string:user>/listpodcast', 'podcast.views:list_podcast')])
	register_template_path(os.path.join(PLUGIN_DIR, 'templates'))

hooks = {'setup':setup_plugin}

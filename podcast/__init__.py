import logging
from mediagoblin.tools.pluginapi import get_config, register_routes

_log = logging.getLogger(__name__)

def setup_plugin():
	_log.info("Starting podcaster")
	config = get_config('podcast')
	if config:
		_log.info("CONFIG FOUND")
	else:
		_log.info("CONFIG NOT FOUND")

	register_routes(('podcast', '/u/<string:user>/podcast', 'podcast.views:get_podcasts'))

hooks = {'setup':setup_plugin}

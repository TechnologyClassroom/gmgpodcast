from mediagoblin.tools.response import json_response, render_to_response
from mediagoblin.tools.pluginapi import get_config
from mediagoblin.decorators import require_active_login
from podcast import forms
from mediagoblin.submit.lib import get_upload_file_limits

import logging
import time
import datetime

from lxml.etree import tostring
import lxml.etree as etree

from werkzeug.wrappers import Response as wz_Response

_log = logging.getLogger(__name__)
conifg = get_config('podcast')

def get_podcasts(request):
	_log.info(request.url)
	username = request.url[request.url.find("u/")+2:request.url.rfind("/podcast")]
	_log.info(username)
	#all according to a rss feed for a itunes podcast
	NSMAP = {"atom":"http://www.w3.org/2005/Atom",
		"itunes":"http://www.itunes.com/dtds/podcast-1.0.dtd",
		"cc":"http://web.resource.org/cc/", 
		"media":"http://search.yahoo.com/mrss/", 
		"rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns"}
	xml = etree.Element("rss", version="2.0",nsmap=NSMAP)
	channel = etree.Element("channel")

	atom = etree.Element("{%s}link"%NSMAP['atom'],href="s", rel="self", type="application/rss+xml")
	channel.append(atom)
	
	title = etree.Element("title")
	title.text = "SAM's Podcast"
	channel.append(title)

	#not sure what these times are actually supposed to be
	pubdate = etree.Element("pubDate")
	lastBuildDate = etree.Element("lastBuildDate")
	t = datetime.datetime.fromtimestamp(time.time()).strftime('%a, %d %b %Y %T')+'+0000'
	pubdate.text = t
	lastBuildDate.text = t
	channel.append(pubdate)
	channel.append(lastBuildDate)

	generator = etree.Element("generator")
	generator.text = "GNU MediaGoblin"
	channel.append(generator)

	link = etree.Element("link")
	link.text = "http://google.com"#hostname of the instance
	channel.append(link)

	language = etree.Element("language")
	language.text = "en"
	channel.append(language)

	copyright = etree.Element("copyright")#some CDATA nonsense going on here
	copyright.text = "GPL"
	channel.append(copyright)

	docs = etree.Element("docs")
	docs.text = ""#hostname goes here 
	channel.append(docs)

	managingEditor = etree.Element("managingEditor")
	managingEditor.text = "ss" #email for user or similar
	channel.append(managingEditor)

	description = etree.Element("description")
	description.text = "Description" #description goes here
	channel.append(description)

	image = etree.Element("image")
	url = etree.Element("url")
	url.text = "URL" #url goes here
	img_title = etree.Element("title")
	img_title.text = "TITLE" #title goes here
	link = etree.Element("link")
	link.text = "URL" #same as link?
	image.append(url)
	image.append(img_title)
	image.append(link)
	channel.append(image)

	author = etree.Element("{%s}author"%NSMAP['itunes'])
	author.text = "AUTHOR" #author/user here
	channel.append(author)

	keywords = etree.Element("{%s}keywords"%NSMAP['itunes'])
	keywords.text = "" #use tags maybe?
	channel.append(keywords)

	category = etree.Element("{%s}category"%NSMAP['itunes'],text="Cats")
	channel.append(category)
	
	ituneimage = etree.Element("{%s}image"%NSMAP['itunes'], href="")#image url
	channel.append(ituneimage)
	
	#explicit = etree.Element("{%s}explicit
	
	xml.append(channel)
#	_log.info(tostring(xml,xml_declaration=True))
	return wz_Response(tostring(xml, xml_declaration=True, pretty_print=True))

#called when /makeapodcast.html is visited
@require_active_login
def register_podcast(request):
	
	upload_limit, max_file_size = get_upload_file_limits(request.user)
	
	podcast_form = forms.podcast_create_form(
		request.form,
		license=request.user.license_preference,
		max_file_size = max_file_size,
		upload_limit = upload_limit,
		uploaded = request.user.uploaded)
	return render_to_response(request, '/podcast/makeapodcast.html', {'podcast_form':podcast_form})

#called when create button is pressed in /makeapodcast.html
def create_podcast(request):
	_log.info(request.files['file'])
	save_settings_for_user(request.form, request.user)
	
	return list_podcast(request)
	
def list_podcast(request):
	podcast_list = ['s','s','a']
		
	add_podcast_form = forms.add_podcast(request.form)
	return render_to_response(request, '/podcast/podcastlist.html', {'podcast_list':podcast_list, 'add_podcast':add_podcast_form})

def save_settings_for_user(form,user):
	_log.info(user.id)
	_log.info(form.get('title'))
	pass
	
def edit_podcast(request):
	pass

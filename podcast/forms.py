import wtforms

from mediagoblin.tools.translate import lazy_pass_to_ugettext as _

def podcast_create_form(form, **kwargs):
	max_file_size = kwargs.get('max_file_size')
	desc = None
	if max_file_size:
		desc = _('Max file size: {0} mb'.format(max_file_size))
		
	class PodcastCreateForm(wtforms.Form):
		file = wtforms.FileField(
			_('Image'),
			description=desc)
		title = wtforms.TextField(
			_('Title'),
			[wtforms.validators.Length(min=0, max=500)])
		adminemail = wtforms.TextField(
			_('Admin Email'),
			[wtforms.validators.Length(min=0, max=500)])					
		description = wtforms.TextAreaField(
			_('Description of the Podcast'))

		
		
		max_file_size = wtforms.HiddenField('')
		upload_limit = wtforms.HiddenField('')
		uploaded = wtforms.HiddenField('')
		
	return PodcastCreateForm(form, **kwargs)
	
def add_podcast(form, **kwargs):
	max_file_size = kwargs.get('max_file_size')
	desc = None
	if max_file_size:
		desc = _('Max file size: {0} mb'.format(max_file_size))	
	class AddPodcastForm(wtforms.Form):
		file = wtforms.FileField(
			_('Audio'),
			description = desc)
		title = wtforms.TextField(
			_('Title'),
			[wtforms.validators.Length(min=0, max=500)])
		keywords = wtforms.TextField(
			_('Keywords'),
			description=_("Separate keywords by commas"))
		description = wtforms.TextAreaField(
			_('Description of the Podcast'))
		
		#keywords to add in addition to default ones already set when podcast created
		keywords = wtforms.TextField(
			_('Keywords'),
			description=_('Separate tags by comma'))
		max_file_size = wtforms.HiddenField('')
		upload_limit = wtforms.HiddenField('')
		uploaded = wtforms.HiddenField('')
		
		
	return AddPodcastForm(form, **kwargs)

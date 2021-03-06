from django.conf import settings
CACHE_KEY_UNTRACK_UA='key_untracked_uas'
CACHE_KEY_BANED_IP='key_baned_ips'
CACHE_KEY_CONTENTTYPE='key_content_type'
CACHE_TIME=getattr(settings,'REAL_ESTATE_APP_CACHE_TIME_BANNED_IPS',3600)
CACHE_TIME_CONTENTTYPE=getattr(settings,'REAL_ESTATE_APP_CACHE_TIME_CONTENTTYPE',3600)
VISIT_URLS_VIEW_CHECK_CLICK=getattr(settings,'REAL_VIEWS_CHECK_CLICKS',[])
DEFAULT_VISIT_URL=[
									 'newspapers-list''newspapers-detail','newspapers-feeds','newspapers-sitemap',
									 'apps-photos',
									 'propretry-list','property-detail','property-feeds','property-sitemap',
									 'visitcalendar-list','visitcalendar-detail','visitcalendar-create-object',
									 'real-estate-app-contact','real-estate-app-share-send-content'
]
if type(VISIT_URLS_VIEW_CHECK_CLICK) is not list:
	VISIT_URLS_VIEW_CHECK_CLICK=[VISIT_URLS_VIEW_CHECK_CLICK,]
VISIT_URLS_VIEW_CHECK_CLICK+=DEFAULT_VISIT_URL
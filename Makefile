lint:
	black pelican/plugins/feed_xslt
	mypy --strict pelican/plugins/feed_xslt
	pylint pelican/plugins/feed_xslt

sample:
	cd sample; pelican --debug

.PHONY: lint sample

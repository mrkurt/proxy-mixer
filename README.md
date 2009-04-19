# Proxy Mixer
This is a very, very early stage attempt to creating a reverse-HTTP proxy with some brains.  The idea is that the proxy itself will process some basic javascript in files with special markup (`<script runat="proxy">/* Some js */</script>`) and use the results to "mix" other resources in.  In the simplest use case, this provides "proxy-side includes".

## More interesting scenarios
Proxy side includes are somewhat interesting, but there's more!  The plan is to make requests for includes happen in parallel, and allow developers to define strict timeouts (and fallback messages) for each.  If you want to add a recommendation engine to a high volume site, and ensure that it won't slow down overall response times, this would give you the means to do that.

This also creates some interesting caching scenarios that I'd like to investigate when I get the basics up and running.

## Requirements
At the moment, all you'll need over a vanilla Python install is Paul Davis's [python-spidermonkey package](http://github.com/davisp/python-spidermonkey/tree/master)
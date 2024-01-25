# static_binary_selenium_webdriver_chrome_121
A boilerplate setup for selenium scripts using chrome 121.x.x.x and webdriver 121.x.x.x


# What's the Point?:
I spent like two whole days figuring out how to set up selenium with a chrome webdriver for some really basic browser automation.

Apparently this area of expertise is growing, because in the last 4 months there's been a release of a major toolkit that automatically finds and installs a webdriver, in response to a new release/policy (as of the past year) from google that allowied developers to pin their google chrome version at all.

A new opensource library and new company policy change both in the past year seems pretty 'breaking-changes' to me, so I'm hoping to preserve the two days of my time by making a boilerplate repo that can use the webdriver with a venv and binaries both contained in the same repo.--This is as opposed to the opensource library's approach of always installing new webdrivers, and probably pointless.

If not pointless, it's the tinned fish of SDET for webapps; at least that's the dream.

# Setup:
1) install and open PyCharm: https://www.jetbrains.com/pycharm/
2) clone as a new project
3) in that project make a /binaries folder
4) download/unzip both the needed chrome browser and chrome driver version from https://googlechromelabs.github.io/chrome-for-testing/#stable (mine is mac-x64)
5) move both the chrome browser and driver folders to ../binaries/
6) if needed, change <chrome_browser_binary_path> and <chrome_driver_path> in webdriver.py
7) run webdriver.py as main

# Docs used:
- https://sdetunicorns.com/blog/setting-up-selenium-python-chromedriver-in-pycharm/
- https://www.youtube.com/watch?v=jQW2fjgUJrY
- https://googlechromelabs.github.io/chrome-for-testing/
- https://pypi.org/project/webdriver-manager/
- https://github.com/orgs/community/discussions/44279

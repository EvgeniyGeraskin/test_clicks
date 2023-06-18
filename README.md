# test_clicks

It is solution for test task from Mayflower.

Solution is an autotest written in Python (with pytest and selenium).

Tested browser:
- Google Chrome

Tested resolutions:
- 1920 x 1080
- 1366 x 768
- 1440 x 900
- 768 x 1024

There is a single autotest separated in 4: test is parametrized for each resolution.

If necessary test may be expanded for more browsers. But for the test task there is only Google Chrome.

# How to run
- Docker should be installed.
- Download all files from the repository.
- Inside directory with download files run command: *docker build . --tag 'selenium_test'*
- Run command: *docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e WEBSITE_LOGIN='' -e WEBSITE_PASSWORD='' selenium_test*
  - Env variables WEBSITE_LOGIN and WEBSITE_PASSWORD should take values with username and password from test account.

**Solution was tested only on WSL with Ubuntu-22.04 installed on Windows 11.**

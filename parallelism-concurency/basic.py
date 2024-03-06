import requests
import timeit

"""
Threading and asyncio both run on a single processor and therefore only run
one at a time.They just cleverly find ways to take turns to speed up the
overall process. Even though they don’t run different trains of thought
simultaneously, we still call this concurrency.


With multiprocessing, Python creates new processes.
A process here can be thought of as almost a completely different program,
though technically they’re usually defined as a collection of resources
where the resources include memory, file handles and things like that.
One way to think about it is that each process runs in its own Python
interpreter.
"""
"""
Because they are different processes, each of your trains of thought in a
multiprocessing program can run on a different core. Running on a different
core means that they actually can run at the same time, which is fabulous.
There are some complications that arise from doing this,
but Python does a pretty good job of smoothing them over most of the time.
"""


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = timeit.default_timer()
    download_all_sites(sites)
    duration = timeit.default_timer() - start_time
    print(f"Downloaded {len(sites)} in {duration: .3f} seconds")

"""
As you can see, this is a fairly short program. download_site() just
downloads the contents from a URL and prints the size. One small thing to
point out is that we’re using a Session object from requests.

It is possible to simply use get() from requests directly, but creating a
Session object allows requests to do some fancy networking tricks and really
speed things up.
"""

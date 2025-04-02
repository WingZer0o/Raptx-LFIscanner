# utils/validators.py
import argparse
import urllib.parse
from banner.banner import RED_PLAIN as RED, END_PLAIN as END

def validate_positive_integer(value):
    """Validate positive integers for walkcount."""
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{RED}[ERROR]{END} {value} is not a positive integer")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{RED}[ERROR]{END} {value} is not a valid integer")

def validate_url(url):
    """Validate the target URL format."""
    parsed_url = urllib.parse.urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise argparse.ArgumentTypeError(f"{RED}[ERROR]{END} {url} is not a valid URL")
    return url

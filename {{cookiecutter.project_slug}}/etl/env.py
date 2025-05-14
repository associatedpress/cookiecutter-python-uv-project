#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime

REQUEST_HEADERS = {
    "From": "ckeller@ap.org",
    "Reason": "Research for news story",
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/122.0",
]

# make a path to a log file
LOG_FILE = f"{os.getcwd()}/log.txt"

# identify data directory
DATA_ROOT = f"{os.getcwd()}/data"

# identify directory to source data
SOURCE_PATH = os.path.join(DATA_ROOT, "source")

# identify directory to processed data
PROCESSED_PATH = os.path.join(DATA_ROOT, "processed")

# identify where to download files
DWNLD_DIR = ""

# create path to downloaded files
DWNLD_PATH = os.path.join(DATA_ROOT, DATA_SOURCE, DWNLD_DIR)

# check whether path to downloaded files exists or not
DWNLD_PATH_EXIST = os.path.exists(DWNLD_PATH)

# identify where to unzip files
UNZIP_DIR = ""

# create path to unzipped files
UNZIP_PATH = os.path.join(DATA_SOURCE, UNZIP_DIR)

# check whether path to downloaded files exists or not
UNZIP_PATH_EXIST = os.path.exists(UNZIP_PATH)

STARTTIME = time.time()

YEAR = datetime.date.today().year

# MOST_RECENT_DATA = os.path.join(RAW_PATH, f"{YEAR}-nbi-all-records.csv")

# state dictionaries
US_STATE_TO_ABBR = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

ABBR_TO_US_STATE = dict(map(reversed, US_STATE_TO_ABBR.items()))

def MAKE_SLUG(row, columns):
    """
    use slugify to create comparison slugs
    """
    values = [str(row[col]) for col in columns]
    output_string = "-".join(values)
    output_slug = slugify(output_string)
    return output_slug


def MAKE_REQUEST(url, params):
    """
    Given a url, makes a HTTP request and
    returns the response content
    """
    try:
        # make a request to a url
        response = requests.get(url, headers=REQUEST_HEADERS, params=params)
        # return the url response
        return response
    # catch our exceptions
    except requests.exceptions.HTTPError as e:
        logger.info(f"Encountered HTTPError. {e.status} {e.reason}")
        logger.info(f"Failed to retrieve {url}")
        # return nothing
        return None
    except requests.exceptions.InvalidURL as e:
        logger.info(f"Encountered InvalidURL. {e.status} {e.reason}")
        # return nothing
        return None
    except requests.exceptions.Timeout:
        logger.info.error("Request timed out")
        # return nothing
        return None
    except requests.exceptions.RequestException as e:
        logger.info(f"Encountered {e}")
        # return nothing
        return None

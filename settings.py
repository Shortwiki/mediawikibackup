#!/usr/bin/python3
import pickle
import os


if __name__ == "__main__":
    SECRET = input("please type bucket id.")
    NGINX = input("please type nginx site setting file in site-available.")
    DB_HOST = input("please type DB_HOST.")
    DB_USER = input("please type DB_USER.")
    DB_USER_PASSWORD = input("please type DB_USER_PASSWORD.")
    DB_NAME = input("please type DB_NAME.")
    WIKI_PATH = input("please type wiki folder path.")
    LOG = input("please type log file path.")
    dump = {
        "NGINX":NGINX,
        "SECRET":SECRET,
        "DB_HOST":DB_HOST,
        "DB_USER":DB_USER,
        "DB_USER_PASSWORD":DB_USER_PASSWORD,
        "DB_NAME":DB_NAME,
        "WIKI_PATH":WIKI_PATH,
        "LOG":LOG
    }
    with open(os.path.dirname(os.path.realpath(__file__)) + "/settings", "wb") as w:
        pickle.dump(dump, w)

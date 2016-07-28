import os
import sys
import argparse as ap
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.io import fits
import astropy.units as u

def argParse():
    parser = ap.ArgumentParser()
    parser.add_argument()
    return parser.parse_args()

if __name__ == '__main__':
    args = argParse()

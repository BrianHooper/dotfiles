##############################
#   Python Scripting tools   #
#       Brian Hooper         #
#        9/13/2019           #
##############################

from pathlib import Path
from shutil import rmtree
from sys import stdout, stderr
from os.path import exists
from subprocess import Popen, PIPE
from collections import deque
import numpy as np
import re


def __decode_pipe__(pipe):
    """
    Decodes output from stdout or stderr as UTF-8
    """
    if pipe is not None and len(pipe) > 0:
        return pipe.decode("UTF-8")
    else:
        return None


def run_command(command, shell=['cmd', '/c']):
    """
    Runs a command on the specified shell

    Possible shells (Windows):
    ["cmd", "/c"]
    ["powershell"]

    Possible shells (Linux):
    (untested)

    The command can either be a single string, such as "ls -a",
    or a list containing a command and parameters, such as ["ls", "-a"]

    The output is a tuple, with (stdout, stderr, return_code), or None if the
    command is not valid
    """
    if not isinstance(command, list):
        try:
            command = [str(command)]
        except ValueError:
            print("Error, invalid input to run_command", file=stderr)
            return None
    command = shell + command
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    pipe = process.communicate()
    stdout_decoded = __decode_pipe__(pipe[0])
    stderr_decoded = __decode_pipe__(pipe[1])
    return_code = process.returncode

    return stdout_decoded, stderr_decoded, return_code


def dev_clean(root_path, path):
    """
    Attempts to remove a directory, regardless of if it is empty or read-only

    The location of the folder should be the absolute path, split into 
    the parent folder and the name of the folder, for example:

    dev_clean(r"C:/users/v-brhoop/Downloads", "example_folder")

    """

    if not isinstance(root_path, Path):
        root_path = Path(root_path)

    if not exists(root_path / path):
        print("Warning: " + str(path) + " does not exist", file=stderr)
        return True
    try:
        rmtree(root_path / path, ignore_errors=True)
        if not exists(root_path / path):
            print("Sucuessfully removed " + str(path))
            return True
        else:
            print("Error removing " + str(path), file=stderr)
            return False
    except OSError:
        print("Error removing " + str(path), file=stderr)
        return False


def progress_bar(percent, width=50):
    """
    prints a progress bar to the console
    :param percent: current percentage completed
    :param width: number of characters wide to make the progress bar
    :return: None
    """
    num_pounds = int(percent * width)
    pounds = "#" * num_pounds
    dashes = "-" * (width - num_pounds)

    if percent == 1.0:
        endl = "\n"
    else:
        endl = ""

    print("\rProgress: %7.2f%% %s%s" % (percent * 100, pounds, dashes), end=endl)


class AverageTime:
    def __init__(self, max_items=10):
        self.times = deque()
        self.max_items = max_items

    def update(self, time):
        if len(self.times) >= 9:
            self.times.popleft()
        self.times.append(time)
        return np.average(self.times)

    def estimate(self, time, remaining_items):
        avgtime = self.update(time)
        remaining_time = avgtime * remaining_items

        if remaining_time < 10:
            return "{:.2f} seconds remain".format(remaining_time)
        elif remaining_time < 60:
            return "{:d} seconds remain".format(int(remaining_time))
        elif remaining_time < 3600:
            remaining_time = int(remaining_time)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            return "{:d} min and {:d} sec remain".format(minutes, seconds)
        else:
            remaining_time = int(remaining_time)
            hours = remaining_time // 3600
            remaining_time = remaining_time % 3600
            minutes = remaining_time // 60
            seconds = remaining_time % 60

            hour_str = "hours" if hours > 1 else "hour"
            return "{:d} {:s}, {:d} min, and {:d} sec remain".format(hours, hour_str, minutes, seconds)


def divide_chunks(data, chunk_size):
    return [data[i * chunk_size:(i + 1) * chunk_size] for i in range((len(data) + chunk_size - 1) // chunk_size )]

def multi_split(delimiters, to_split):
    keys = {
        " ": "[\s]+",
        ",": "[,]+",
        "\t": "[\t]+",
    }

    for index, value in enumerate(delimiters):
        if value in keys:
            delimiters[index] = keys[value]
        else:
            delimiters[index] = "[" + value + "]+"
    pattern = re.compile("|".join(delimiters))
    return pattern.split(to_split)

"""
Required: Python 3

Implement a UNIX commandline interpreter for Windows machine by prompt and
let user enter commands to run until user enters "exit" command.

This interpreter recognizes the following commands:

    pwd     - print the current working directory
    cd      - change the current working directory
    ls      - list files in a given directory
    mkdir   - make directory
    cp      - copy files
    mv      - move files
    rm      - remove files
    exit    - terminate the interpreter

Usages:

Unix commands includes a complex command-line options that are not all
implemented by this interpreter. The following usages of each command
above are implemented:

pwd
cd [path]
ls [file ...]
mkdir directory ...
cp source_file target_file
cp source_file ... target_directory
mv source_file target_file
mv source_file ... target_directory
rm [-R] file ...
"""


import os           # for accessing file system
import getopt       # for parsing command-line parameters
import shutil       # for high-level file operations


def ls(params):
    """
    Simulation of ls command: Print the file listing of the given path
    """

    # parse the command-line parameters for ls command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    if len(args) == 0:
        # Use the current directory if the path is not specified
        args.append(".")

    for path in args:

        # make sure the path exist
        if not os.path.exists(path):
            print("ls:", path + ": No such file or directory")

        # check whether the path is a directory or file
        elif os.path.isdir(path):

            # print the current path if multiple paths are given
            if len(args) > 1:
                print(path + ":")

            # print content of the directory
            for fn in os.listdir(path):
                print(fn)

        else:
            # or just print the file path
            print(path)

        print()


def pwd(params):
    """
    Simulation of pwd command: Print out the current working directory
    """

    # parse the command-line parameters for pwd command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    # just print the current working directory, as managed by the os module
    print(os.getcwd())


def cd(params):
    """
    Simulation of cd command: Change the current working directory
    """

    # parse the command-line parameters for cd command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    if len(args) > 0:
        # use the first parameter as the path
        path = args[0]

        # make sure the path exist
        if not os.path.exists(path):
            print("cd:", path + ": No such file or directory")
            return

        # make sure the path is a directory
        if not os.path.isdir(path):
            print("cd:", path + ": Not a directory")
            return

        # change the current directory to the given path
        os.chdir(path)


def mkdir(params):
    """
        Simulation of mkdir command: Make directory
        """

    # parse the command-line parameters for mkdir command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    # validate command-line parameters
    if len(args) < 1:
        print("usage: mkdir directory ...")
        return

    # for each given param, create a directory
    for path in args:
        # make sure the path does not exist
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("mkdir:", path + ": File exists")


def cp(params):
    """
    Simulation of cp command: copy file from a path to another
    """

    # parse the command-line parameters for cp command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    # validate command-line parameters
    if len(args) < 2:
        print("usage: cp source_file target_file")
        print("       cp source_file ... target_directory")
        return

    sources = args[0:-1]    # list of source files
    target = args[-1]       # last param is the target

    # for multiple source files, target must be a directory
    if len(sources) > 1 and not os.path.isdir(target):
        print("usage: cp source_file target_file")
        print("       cp source_file ... target_directory")
        return

    # copy source files to the target using shutil module
    for src in sources:
        try:
            shutil.copy(src, target)
        except Exception as e:
            print("cp: Error copy file", src, ":", e)





def rm(params):
    """
    Simulation of rm command: remove file
    """

    # parse the command-line parameters for rm command
    try:
        # no options are supported by now
        opts, args = getopt.getopt(params.split(), "R")
    except getopt.GetoptError as e:
        # command-line error
        print(e)
        return

    # validate command-line parameters
    if len(args) < 1:
        print("usage: rm [-R] file ...")
        return

    # Command-line option:
    rm_recursive = False        # to remove a directory recursively

    # Check command line option
    for opt in opts:
        if opt[0] == '-R':
            rm_recursive = True

    # remove each path given in the argument list
    for path in args:
        try: # to remove the given path, print error if any

            # remove directory or normal file
            if rm_recursive:
                os.rmdir(path)
            else:
                os.remove(path)

        except Exception as e:
            print("rm:", path + ":", e)


def main():
    """
    The main loop that simulates an Unix shell. It prompts user to enter a
    command until user enters "exit". If the command is recognized, it is
    executed and prints result to screen. Otherwise, a message is printed
    indicating the command is not recognized or implemented.
    """

    while True:

        # Prompt and get user input a command
        command = input("unix> ")
        command = command.strip()

        # Parse the command for command name and parameters
        cmd, _, params = command.partition(" ")

        try:
            # Call the function to handle the corresponding command
            if cmd == "ls":
                ls(params)
            elif cmd == "cd":
                cd(params)
            elif cmd == "pwd":
                pwd(params)
            elif cmd == "mkdir":
                mkdir(params)
            elif cmd == "cp":
                cp(params)
            elif cmd == "mv":
                mv(params)
            elif cmd == "rm":
                rm(params)

            # or finish the program if user typed 'exit'
            elif cmd == "exit":
                print("[Session completed]")
                return

            else:
                print("** Unrecognized command:", cmd)

        except Exception as e:
            # catch any exception so that the program is not terminated in
            # case of any unexpected error.
            print("** Unexpected error:", e)


if __name__ == '__main__':
    main()

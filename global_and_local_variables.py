#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program shows how the global and local variable works

# global variable
variable_X = 25


def local_variable():
    # shows what happenens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def global_variable():
    # shows what happens with global variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_Z))


def main():
    # shows how the global and local variable works

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()

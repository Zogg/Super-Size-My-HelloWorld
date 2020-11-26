from subprocess import call

with open("whitespace.py", "w") as f:
    f.write("print")
    for i in range(7000000):
        f.write("                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    "\
                "                                                                                                    ")
    f.write("('Hellow World')")

call(['python', 'whitespace.py'])

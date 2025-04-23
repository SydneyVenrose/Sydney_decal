# hw2.py

# 1) Suppose your current working directory is ~/Desktop/classes/python_decal/.
# What command would allow you to navigate directly to ~/Desktop?
question_1 = "cd ~/Desktop"

# 2) What does ~/ mean?
question_2 = "'~/' is shorthand for the home directory (e.g. /Users/sydneyrowe)."

# 3) What's the difference between an absolute and a relative path in your terminal?
question_3 = ("An absolute path starts from the root (e.g. /Users/sydneyrowe/Desktop), "
              "while a relative path starts from the current directory (e.g. ../Desktop).")

# 4) What command would bring you back to your home directory?
question_4 = "cd or cd ~"

# 5) If you called rm ./ in your current working directory, what would it do?
question_5 = ("It would try to delete the current directory ('.'), but would usually fail "
              "unless dangerous flags like -rf are used. Be careful with rm!")

# 6) In your current working directory, what does calling:
#    - git add
#    - git commit
#    - git push
question_6 = {
    "git add": "Stages changes to be committed.",
    "git commit": "Records the staged changes with a message.",
    "git push": "Sends the commit to the remote GitHub repository."
}

# 7) Let's say you call "git add" and then "git status". What message would appear?
question_7 = ("Git would show that the files are staged with something like:\n"
              "'Changes to be committed: new file: filename.txt'. "
              "This means they’re ready to be committed.")

# 8) What has been the most frustrating error or bug you've encountered in this class so far?
question_8 = ("Getting 'Permission denied (publickey)' when pushing to GitHub. "
              "I fixed it by generating an SSH key, adding it to GitHub, and testing with ssh -T.")

# 9) How does cloning a repository differ from pulling from a repository?
question_9 = ("Cloning copies a remote repository to your computer once. "
              "Pulling fetches the latest changes from the remote into your existing local repo.")

# 10) Tell me a fun fact!
question_10 = "Octopuses have three hearts and their blood is blue!"

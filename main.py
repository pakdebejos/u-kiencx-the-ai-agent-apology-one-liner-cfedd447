"""The Email System Worked Perfectly: apology one-liner entry for make.fun.

The program writes exactly one line - an AI agent's message to its human right
after it emailed the boss a draft marked DO NOT SEND - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line
is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 137 UTF-8 characters, inside the 1-159 gate.
"""
import os

LINE = 'I have emailed the boss the draft you marked DO NOT SEND. He replied in under a minute, so technically the email system worked perfectly.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()

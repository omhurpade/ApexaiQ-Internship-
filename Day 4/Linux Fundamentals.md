# Linux Fundamentals 

---

## 1. What is Linux?

Linux is an **open-source operating system**.

Just like Windows and macOS, Linux helps us run programs, manage files, use hardware, and perform different tasks.

Linux is commonly used in:

- Servers
- Cloud computing
- Software development
- Networking
- Cybersecurity
- DevOps

### Why use the terminal?

In Linux, we can do many tasks by typing commands instead of clicking buttons.

For example:

```bash
pwd
```

This command tells us where we are currently located.

---

## 2. Linux Distributions

Linux comes in different versions called **distributions (distros)**.

Some common examples are:

- Ubuntu
- Debian
- Fedora
- CentOS

The basic Linux concepts are similar, but the tools and default software can be different.

---

## 3. Linux File System

Linux organizes files and folders in a tree-like structure.

The top of the filesystem is called the **root directory**:

```text
/
```

Some important directories are:

| Directory | Simple Meaning |
|---|---|
| `/` | Starting point of the whole filesystem |
| `/home` | Personal files of normal users |
| `/etc` | System configuration files |
| `/bin` | Important system commands |
| `/var` | Changing data such as logs |
| `/tmp` | Temporary files |
| `/root` | Home directory of the root user |

### Easy way to remember

Think of `/` as the **main folder** of Linux.  
All other folders are inside it.

---

# 4. Terminal Basics

The **terminal** is where we type Linux commands.

A **shell** is the program that reads our commands and executes them.  
One common shell is **Bash**.

---

## 5. Checking Where We Are

### `pwd`

`pwd` means **Print Working Directory**.

It tells us our current location.

```bash
pwd
```

Example output:

```text
/home/user
```

### Simple explanation

If someone asks:

> "Where are you currently working?"

Use:

```bash
pwd
```

---

# 6. Listing Files

### `ls`

The `ls` command shows files and folders in the current directory.

```bash
ls
```

### Detailed list

```bash
ls -l
```

This gives extra information such as permissions, owner, size, and date.

### Show hidden files

```bash
ls -a
```

### Detailed list including hidden files

```bash
ls -la
```

---

# 7. Changing Directories

### `cd`

`cd` means **Change Directory**.

For example:

```bash
cd Documents
```

This moves us into the `Documents` folder.

### Go one level back

```bash
cd ..
```

### Go to home directory

```bash
cd ~
```

### Easy example

```bash
pwd
ls
cd Documents
pwd
cd ..
pwd
```

This helps us understand how navigation works.

---

# 8. Creating Files and Folders

## Create a file

Use `touch`:

```bash
touch notes.txt
```

This creates an empty file called `notes.txt`.

## Create a folder

Use `mkdir`:

```bash
mkdir projects
```

This creates a folder called `projects`.

---

# 9. Copying Files

Use `cp` to copy files.

```bash
cp notes.txt backup.txt
```

This creates a copy of `notes.txt` named `backup.txt`.

To copy a file into a folder:

```bash
cp notes.txt projects/
```

---

# 10. Moving and Renaming Files

The `mv` command is used for both **moving** and **renaming**.

### Rename a file

```bash
mv notes.txt linux_notes.txt
```

### Move a file

```bash
mv linux_notes.txt projects/
```

### Easy idea

```text
mv = move or rename
```

---

# 11. Deleting Files and Folders

## Delete a file

```bash
rm notes.txt
```

## Delete a folder and its contents

```bash
rm -r projects
```

> ⚠️ Be careful with `rm`. Linux normally does not move deleted files to a recycle bin.

---

# 12. Reading Files

There are several commands for viewing file contents.

## `cat`

Displays the complete file.

```bash
cat notes.txt
```

## `less`

Useful for reading large files one screen at a time.

```bash
less notes.txt
```

## `head`

Shows the beginning of a file.

```bash
head notes.txt
```

## `tail`

Shows the end of a file.

```bash
tail notes.txt
```

---

# 13. Editing a File

A simple terminal editor is `nano`.

```bash
nano notes.txt
```

This opens the file so we can edit it.

---

# 14. Linux File Permissions

Linux controls who can use a file through **permissions**.

There are three main categories:

```text
Owner
Group
Others
```

There are also three basic permissions:

| Permission | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute |

For example:

```text
-rwxr-xr--
```

We can check permissions using:

```bash
ls -l
```

---

# 15. Changing Permissions

The `chmod` command is used to change file permissions.

Example:

```bash
chmod +x script.sh
```

This gives execute permission to the file.

### Simple meaning

```text
chmod = change permissions
```

---

# 16. Changing File Ownership

The `chown` command is used to change the owner of a file.

```bash
chown user file.txt
```

### Simple meaning

```text
chown = change owner
```

---

# 17. Useful System Commands

Linux provides commands to get basic system information.

### Current user

```bash
whoami
```

Shows the username of the current user.

### Date and time

```bash
date
```

Shows the current date and time.

### Disk space

```bash
df -h
```

Shows available and used disk space in an easy-to-read format.

### Running processes

```bash
top
```

Shows currently running processes and system resource usage.

### Command history

```bash
history
```

Shows commands that were previously executed.

---

# 18. Root User

The **root user** is the administrator of a Linux system.

Root has very high-level access and can perform system-level operations.

For administrative commands, we often use:

```bash
sudo
```

Example:

```bash
sudo apt update
```

### Simple meaning

```text
sudo = run a command with administrator privileges
```

---

# 19. Installing Software

Linux uses **package managers** to install and manage software.

For Ubuntu and Debian-based systems, a common package manager is `apt`.

### Update package information

```bash
sudo apt update
```

### Install a package

```bash
sudo apt install package-name
```

Other Linux distributions may use package managers such as:

```text
dnf
yum
```

---

# 20. Important Linux Terms

| Term | Easy Meaning |
|---|---|
| Linux | Open-source operating system |
| Terminal | Place where we type commands |
| Shell | Program that executes commands |
| Root | Top-level administrator user |
| Directory | Another name for a folder |
| Command | Instruction given to the system |
| Permission | Controls access to files |
| Package Manager | Tool used to install/manage software |

---

# 21. Most Important Commands

| Command | Purpose |
|---|---|
| `pwd` | Show current location |
| `ls` | Show files and folders |
| `cd` | Move to another directory |
| `cd ..` | Go back one directory |
| `cd ~` | Go to home directory |
| `touch` | Create a file |
| `mkdir` | Create a directory |
| `cp` | Copy a file |
| `mv` | Move or rename |
| `rm` | Delete a file |
| `rm -r` | Delete a directory |
| `cat` | Display file contents |
| `less` | Read a file page by page |
| `head` | Show beginning of a file |
| `tail` | Show end of a file |
| `nano` | Edit a file |
| `ls -l` | Show detailed file information |
| `chmod` | Change permissions |
| `chown` | Change ownership |
| `whoami` | Show current user |
| `df -h` | Show disk usage |
| `top` | Show running processes |
| `history` | Show previous commands |
| `sudo` | Run command with admin privileges |

---

# 22. Small Practice Exercise

Try these commands one by one:

```bash
mkdir linux-practice
cd linux-practice
touch hello.txt
echo "Hello Linux" > hello.txt
cat hello.txt
cp hello.txt copy.txt
ls -l
mv copy.txt final.txt
ls
rm final.txt
cd ..
rm -r linux-practice
```

### What happened?

1. Created a folder.
2. Entered the folder.
3. Created a file.
4. Added text to the file.
5. Read the file.
6. Created a copy.
7. Checked the files.
8. Renamed the copy.
9. Deleted the renamed file.
10. Returned to the previous directory.
11. Removed the practice folder.

---

# 23. Quick Revision

Remember these groups:

### Navigation

```text
pwd → Where am I?
ls  → What is here?
cd  → Move somewhere
```

### File Management

```text
touch → Create
cp    → Copy
mv    → Move/Rename
rm    → Delete
```

### File Reading

```text
cat   → Read
less  → Read page by page
head  → Beginning
tail  → End
nano  → Edit
```

### System Information

```text
whoami  → Current user
date    → Date/time
df -h   → Disk space
top     → Running processes
history → Previous commands
```

### Permissions

```text
chmod → Change permissions
chown → Change owner
```

---

# 24. Final Takeaway

Linux may look difficult at first, but the basic idea is simple:

```text
Navigate → Create → Read → Modify → Move → Delete
```

The most important thing is **practice**.

Start with these commands:

```bash
pwd
ls
cd
mkdir
touch
cp
mv
rm
cat
nano
```

Once these become comfortable, learning advanced Linux, networking, Docker, and DevOps becomes much easier.

---

## 🎯 Day 1 Goal

By the end of this lesson, you should be able to:

- Explain what Linux is
- Understand the basic Linux filesystem
- Use the terminal
- Navigate between directories
- Create and manage files
- Read and edit files
- Understand basic permissions
- Check basic system information
- Understand `sudo` and package management

**Practice the commands instead of only memorizing them.**


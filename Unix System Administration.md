## Topics

- [x] Introduction to Linux
  - [x] Understanding the history and philosophy of Linux
  - [x] Differences between Linux distributions (distros)
  - [x] Basic command-line usage and navigation

- [x] Linux File System Hierarchy
  - [x] Understanding the file system structure (/bin, /etc, /var, /home, etc.)
  - [x] File types
  - [x] File permissions and ownership

- [x] Package Management
  - [x] Package managers like apt (Debian/Ubuntu), yum/dnf (Red Hat/CentOS), and pacman (Arch)
  - [x] Installing, updating, and removing software packages

- [x] User and Group Management
  - [x] Creating, modifying, and deleting user accounts
  - [x] Managing user privileges and groups
  - [x] Password policies and authentication methods

- [ ] File System Management
  - [ ] Mounting and unmounting file systems
  - [ ] Disk partitioning with tools like fdisk or GParted
  - [ ] File system maintenance and repair (e.g., fsck)

- [ ] Process Management
  - [ ] Viewing and managing processes (ps, top, kill, etc.)
  - [ ] Understanding process priorities (nice, renice)
  - [ ] Job control (bg, fg, jobs)

- [ ] Shell Scripting
  - [ ] Writing and executing shell scripts (Bash scripting)
  - [ ] Understanding variables, loops, conditionals, and functions

- [ ] Networking
  - [ ] Configuring network interfaces
  - [ ] IP addressing, subnetting, and routing
  - [ ] Firewalls (e.g., iptables or firewalld)
  - [ ] Network troubleshooting

- [ ] Security and Permissions
  - [ ] Securing the system with firewalls, SELinux, or AppArmor
  - [ ] Managing file permissions
  - [ ] Regular system updates and patch management

- [ ] System Monitoring and Performance Tuning
  - [ ] Monitoring system resources (CPU, memory, disk usage, etc.)
  - [ ] Identifying and resolving performance bottlenecks
  - [ ] Tools like sar, iostat, vmstat, and htop

- [ ] Backup and Recovery
  - [ ] Setting up regular backups (e.g., using rsync or tar)
  - [ ] Planning for disaster recovery
  - [ ] Restore procedures

- [ ] Virtualization and Containerization
  - [ ] Virtualization technologies like KVM or VirtualBox
  - [ ] Containerization with Docker or Podman
  - [ ] Managing virtual machines and containers

- [x] Web Servers and Services
  - [ ] Installing and configuring web servers (e.g., Apache or Nginx)
  - [ ] Managing web hosting configurations
  - [ ] Setting up SSL certificates

- [x] Database Management
  - [ ] Installing and configuring databases (e.g., MySQL, PostgreSQL)
  - [ ] Database backup and maintenance

- [x] Automation and Configuration Management
  - [ ] Tools like Ansible, Puppet, or Chef for automation
  - [ ] Managing configuration files and version control

- [ ] Logging and Monitoring
  - [ ] Centralized logging with tools like syslog or rsyslog
  - [ ] Setting up monitoring solutions (e.g., Nagios or Prometheus)

- [ ] Security Best Practices
  - [ ] Implementing security policies and practices
  - [ ] Intrusion detection and prevention
  - [ ] Security audits and vulnerability assessments

- [ ] Cloud Computing and Containers Orchestration
  - [ ] Working with cloud providers (e.g., AWS, Azure, GCP)
  - [ ] Container orchestration with Kubernetes

- [ ] High Availability and Load Balancing
  - [ ] Setting up high availability clusters
  - [ ] Load balancing with tools like HAProxy

- [ ] Disaster Recovery Planning
  - [ ] Creating disaster recovery plans and procedures
  - [ ] Testing and documenting disaster recovery processes


## 1- Linux basic commands

- `ls` (List Files and Directories)
  - Description: List files and directories in the current directory.
  - Important Flags:
    - `-l`: Long format, displays detailed information about files.
    - `-a`: Show hidden files (those starting with a dot).
  - Example: `ls -la`

- `cd` (Change Directory)
  - Description: Change the current working directory.
  - Important Flags: None
  - Example: `cd /path/to/directory`

- `pwd` (Print Working Directory)
  - Description: Display the current working directory.
  - Important Flags: None
  - Example: `pwd`

- `diff` (File Comparison)
  - Description: Compare two files line by line and show the differences.
  - Important Flags:
    - `-u`: Unified format, displays differences in a more human-readable way.
  - Example: `diff -u file1.txt file2.txt`

- `touch` (Create Empty File)
  - Description: Create an empty file or update the timestamp of an existing file.
  - Important Flags: None
  - Example: `touch newfile.txt`

- `cat` (Concatenate and Display File Content)
  - Description: Display the content of one or more files.
  - Important Flags: None
  - Example: `cat file.txt`

- `echo` (Print Text)
  - Description: Display text or variables to the terminal.
  - Important Flags: None
  - Example: `echo "Hello, World!"`

- `rm` (Remove Files or Directories)
  - Description: Delete files or directories.
  - Important Flags:
    - `-r`: Recursively delete directories.
    - `-f`: Forcefully delete without confirmation.
  - Example: `rm -rf directory`

- `mkdir` (Make Directory)
  - Description: Create a new directory.
  - Important Flags: None
  - Example: `mkdir new_directory`

- `cp` (Copy Files and Directories)
  - Description: Copy files or directories from one location to another.
  - Important Flags:
    - `-r`: Recursively copy directories.
    - `-i`: Interactive mode, prompt before overwriting.
  - Example: `cp -ri source/ destination/`

- `mv` (Move or Rename Files and Directories)
  - Description: Move files or directories to a different location or rename them.
  - Important Flags: None
  - Example: `mv file.txt new_location/`

- `grep` (Search Text Using Patterns)
  - Description: `grep` searches for text patterns within files or input streams. It's a powerful tool for finding and filtering text.
  - Important Flags:
    - `-i`: Ignore case while searching.
    - `-r`: Recursively search in directories.
    - `-o`: Print only the matched parts of the line.
  - Example:
    - Search for "error" in a log file: `grep "error" logfile.txt`
    - Search for email addresses in a text file: `grep -Eo "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}" text.txt`

- `uniq` (Remove Duplicate Lines)
  - Description: Remove consecutive duplicate lines from a sorted file.
  - Important Flags: None
  - Example: `sort file.txt | uniq`

- `sort` (Sort Lines in Text Files)
  - Description: Sort lines in a text file.
  - Important Flags:
    - `-n`: Sort numerically.
    - `-r`: Reverse the sorting order.
  - Example: `sort -n file.txt`

- `systemctl` (Control Systemd Services)
  - Description: Manage and control systemd services on a Linux system.
  - Important Flags:
    - `start`: Start a service.
    - `stop`: Stop a service.
    - `status`: Display the status of a service.
  - Example: `systemctl start service-name`

- `find` (Search for Files and Directories)
  - Description: Search for files and directories based on various criteria.
  - Important Flags:
    - `-name`: Search by file/directory name.
    - `-type`: Specify file type (e.g., `-type d` for directories).
  - Example: `find /path/to/search -name "*.txt"`

- `chmod` (Change File Permissions)
  - Description: Change file or directory permissions.
  - Important Flags: None
  - Example: `chmod 644 file.txt`

- `timedatectl` (Control System Time and Date)
  - Description: View and modify system time and date settings.
  - Important Flags:
    - `status`: Display time and date information.
    - `set-time`: Set the system time.
  - Example: `timedatectl status`

- `awk` (Text Processing)
  - Description: Awk is a versatile text processing tool that processes text line by line. It's especially useful for data extraction and manipulation.
  - Important Flags:
    - `-F`: Specify a field separator (e.g., `-F,` for comma-separated values).
    - `'{print $1}'`: Print the first field of each line (fields are separated by the specified separator).
    - `'{sum += $2} END {print sum}'`: Calculate the sum of values in the second field and print it at the end.
  - Example: 
    - Print the first column of a CSV file: `awk -F, '{print $1}' data.csv`
    - Calculate the sum of values in the second column: `awk '{sum += $2} END {print sum}' data.txt`

- `ssh` (Secure Shell)
  - Description: Securely access and manage remote servers.
  - Important Flags:
    - `-i`: Specify an identity file.
    - `-p`: Specify a port.
  - Example: `ssh -i key.pem user@remote-server`

- `shred` (Secure File Deletion)
  - Description: Permanently delete files by overwriting their content.
  - Important Flags:
    - `-u`: Remove the file after shredding.
  - Example: `shred -u sensitive-file.txt`

- `ln` (Create Symbolic Links)
  - Description: Create symbolic links to files and directories.
  - Important Flags:
    - `-s`: Create a symbolic link.
  - Example: `ln -s target-file link-name`

- `man` (Manual Pages)
  - Description: Display manual pages for commands and programs.
  - Important Flags: None
  - Example: `man ls`

- `curl` (Transfer Data with URLs)
  - Description: Fetch data from or send data to a URL.
  - Important Flags:
    - `-o`: Save output to a file.
    - `-X`: Specify HTTP request method.
  - Example: `curl -o output.txt https://example.com`

- `zip` and `unzip` (Compress and Extract Zip Archives)
  - Description: Create and extract compressed zip archives.
  - Important Flags:
    - `-r`: Recursively zip/unzip directories.
  - Example (zip): `zip -r archive.zip directory/`
  - Example (unzip): `unzip archive.zip`

- `less` (View File Content Page by Page)
  - Description: Display the content of a file one page at a time.
  - Important Flags:
    - `Space`: Move forward one page.
    - `q`: Quit.
  - Example: `less file.txt`

- `ps` (Process Status)
  - Description: Display information about running processes.
  - Important Flags:
    - `-e`: Show all processes.
    - `-f`: Full format, displays more details.
  - Example: `ps -ef`

- `df` (Disk Space Usage)
  - Description: Display disk space usage information.
  - Important Flags:
    - `-h`: Human-readable output.
  - Example: `df -h`

- `kill` and `pkill` (Terminate Processes)
  - Description: Terminate processes by their process ID or name.
  - Important Flags: Varies by use case.  
  - Example `kill awk`
  
- `ss` (Socket Statistics)
    - Description: Display socket statistics, including information about network connections.
    - Important Flags:
      - `-t`: Display TCP sockets.
      - `-u`: Display UDP sockets.
      - `-n`: Show numerical addresses.
    - Example: `ss -tuln`

- `ping` (Network Connectivity Test)
    - Description: Send ICMP echo requests to a host to check network connectivity.
    - Important Flags:
      - `-c`: Specify the number of packets to send.
    - Example: `ping -c 5 google.com`








## 2- File system Hierarchy

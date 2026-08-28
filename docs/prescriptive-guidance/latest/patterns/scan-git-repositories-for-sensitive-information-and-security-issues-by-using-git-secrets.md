---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets.html
---

# Scan Git repositories for sensitive information and security issues by using git-secrets
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets"></a>

*Saurabh Singh, Amazon Web Services*

## Summary
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-summary"></a>

This pattern describes how to use the open-source [git-secrets](https://github.com/awslabs/git-secrets) tool from AWS Labs to scan Git source repositories and find code that might potentially include sensitive information, such as user passwords or AWS access keys, or that has any other security issues.

`git-secrets` scans commits, commit messages, and merges to prevent sensitive information such as secrets from being added to your Git repositories. For example, if a commit, commit message, or any commit in a merge history matches one of your configured, prohibited regular expression patterns, the commit is rejected.

## Prerequisites and limitations
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A Git repository that requires a security scan
+ A Git client (version 2.37.1 and later) installed

## Architecture
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-architecture"></a>

**Target architecture **
+ Git
+ `git-secrets`

![Using the git-secrets tool to scan Git source repositories for sensitive information.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4a18e0c8-0935-4ee2-86bf-c1dfcfbc1bcb/images/e4813a76-83c2-4254-b5f4-aafe2b8f2127.png)

## Tools
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-tools"></a>
+ [git-secrets](https://github.com/awslabs/git-secrets) is a tool that prevents you from committing sensitive information into Git repositories.
+ [Git](https://git-scm.com/) is an open-source distributed version control system.

## Best practices
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-best-practices"></a>
+ Always scan a Git repository by including all revisions:

  ```
  git secrets --scan-history
  ```

## Epics
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-epics"></a>

### Connect to an EC2 instance
<a name="connect-to-an-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to an EC2 instance by using SSH. | Connect to an Amazon Elastic Compute Cloud (Amazon EC2) instance by using SSH and a key pair file. <br />You can skip this step if you are scanning a repository on your local machine. | General AWS |

### Install Git
<a name="install-git"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Git. | Install Git by using the command:<pre>yum install git -y</pre><br />If you are using your local machine, you can install a Git client for a specific OS version. For more information, see the [Git website](https://git-scm.com/downloads/guis). | General AWS |

### Clone the source repository and install git-secrets
<a name="clone-the-source-repository-and-install-git-secrets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the Git source repository. | To clone the Git repository that you want to scan, choose the **Git clone** command from your home directory. | General AWS |
| Clone git-secrets. | Clone the `git-secrets` Git repository.<pre>git clone https://github.com/awslabs/git-secrets.git</pre><br />Place `git-secrets` somewhere in your `PATH `so that Git picks it up when you run `git-secrets`. | General AWS |
| Install git-secrets. | **For Unix and variants (Linux/macOS):**<br />You can use the `install` target of the `Makefile` (provided in the `git-secrets` repository) to install the tool. You can customize the installation path by using the `PREFIX` and `MANPREFIX` variables.<pre>make install</pre><br />**For Windows:**<br />Run the PowerShell `install.ps1` script provided in the `git-secrets` repository. This script copies the installation files to an installation directory (`%USERPROFILE%/.git-secrets` by default) and adds the directory to the current user `PATH`.<pre>PS > ./install.ps1</pre><br />**For Homebrew (macOS users):**<br />Run:<pre>brew install git-secrets</pre> | General AWS |

### Scan git code repository
<a name="scan-git-code-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Go to the source repository. | Switch to the directory for the Git repository that you want to scan:<pre>cd my-git-repository</pre> | General AWS |
| Register the AWS rule set (Git hooks). | To configure `git-secrets` to scan your Git repository on each commit, run the command: <pre>git secrets --register-aws</pre> | General AWS |
| Scan the repository. | Run the following command to start scanning your repository:<pre>git secrets -–scan</pre> | General AWS |
| Review the output file. | The tool generates an output file if it finds a vulnerability in your Git repository. For example:<pre>example.sh:4:AWS_SECRET_ACCESS_KEY = *********<br /><br />[ERROR] Matched one or more prohibited patterns<br /><br />Possible mitigations:<br />- Mark false positives as allowed using: git config --add secrets.allowed ...<br />- Mark false positives as allowed by adding regular expressions to .gitallowed at repository's root directory<br />- List your configured patterns: git config --get-all secrets.patterns<br />- List your configured allowed patterns: git config --get-all secrets.allowed<br />- List your configured allowed patterns in .gitallowed at repository's root directory<br />- Use --no-verify if this is a one-time false positive</pre> | General AWS |

## Related resources
<a name="scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets-resources"></a>
+ [git-secrets tool](https://github.com/awslabs/git-secrets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

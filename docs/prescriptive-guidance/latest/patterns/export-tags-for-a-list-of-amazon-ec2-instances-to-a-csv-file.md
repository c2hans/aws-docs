---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file.html
---

# Export tags for a list of Amazon EC2 instances to a CSV file
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file"></a>

*Sida Ju and Pac Joonhyun, Amazon Web Services*

## Summary
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file-summary"></a>

This pattern shows how to programmatically export tags for a list of Amazon Elastic Compute Cloud (Amazon EC2) instances to a CSV file.

By using the example Python script provided, you can reduce how long it takes to review and categorize your Amazon EC2 instances by specific tags. For example, you could use the script to quickly identify and categorize a list of instances that your security team has flagged for software updates.

## Prerequisites and limitations
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file-prereqs"></a>

**Prerequisites**
+ Python 3 installed and configured
+ AWS Command Line Interface (AWS CLI) installed and configured

**Limitations**

The example Python script provided in this pattern can search Amazon EC2 instances based on the following attributes only:
+ Instance IDs
+ Private IPv4 addresses
+ Public IPv4 addresses

## Tools
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.
+ [virtualenv](https://virtualenv.pypa.io/en/latest/) helps you create isolated Python environments.

**Code repository**

The example Python script for this pattern is available in the GitHub [search-ec2-instances-export-tags](https://github.com/aws-samples/search-ec2-instances-export-tags) repository.

## Epics
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file-epics"></a>

### Install and configure the prerequisites
<a name="install-and-configure-the-prerequisites"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | If you receive errors when running AWS CLI commands, [make sure that you’re using the most recent AWS CLI version](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html).Clone the GitHub [search-ec2-instances-export-tags](https://github.com/aws-samples/search-ec2-instances-export-tags) repository by running the following Git command in a terminal window:<pre>git clone https://github.com/aws-samples/search-ec2-instances-export-tags.git</pre> | DevOps engineer |
| Install and activate virtualenv. | 1. Install virtualenv by running the following command:<pre>python3 -m pip install virtualenv</pre><br />2. Create a new virtual environment by running the following command:<pre>python3 -m venv env</pre><br />3. Activate the new virtual environment by running the following command:<pre>source env/bin/activate</pre>For more information, see the [virtualenv documentation](https://virtualenv.pypa.io/en/latest/how-to/install.html). | DevOps engineer |
| Install dependencies. | 1. Open the code directory by running the following command in the terminal:<pre>cd search-ec2-instances-export-tags</pre><br />2. Install the `requirements.txt` file by running the following pip command:<pre>pip3 install -r requirements.txt</pre> | DevOps engineer |
| Configure an AWS named profile. | If you haven’t already, configure an AWS named profile that includes the required credentials to run the script. To create a named profile, run the [aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) command.<br />For more information, see [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) in the AWS CLI documentation. | DevOps engineer |

### Configure and run the Python script
<a name="configure-and-run-the-python-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the input file. | Create an input file that contains a list of the Amazon EC2 instances that you want the script to search and export tags for. You can list instance IDs, private IPv4 addresses, or public IPv4 addresses.Make sure that each Amazon EC2 instance is listed on its own line in the input file.<br />**Input file example**<pre>1    i-0547c351bdfe85b9f<br />2    54.157.194.156<br />3    172.31.85.33<br />4    54.165.198.144<br />5    i-0b6223b5914111a4b<br />6    172.31.85.44<br />7    54.165.198.145<br />8    172.31.80.219<br />9    172.31.94.199</pre> | DevOps engineer |
| Run the Python script. | Run the script by running the following command in the terminal:<pre>python search_instances.py -i INPUTFILE -o OUTPUTFILE -r REGION [-p PROFILE]</pre>Replace `INPUTFILE` with the name of your input file. Replace `OUTPUTFILE` with the name you want to give the CSV output file. Replace `REGION` with the AWS Region that your Amazon EC2 resources are in. If you’re using an AWS named profile, replace `PROFILE` with the named profile that you’re using.<br />To get a list of supported parameters and their description, run the following command:<pre>python search_instances.py -h</pre><br />For more information and to see an output file example, see the `README.md` file in the GitHub [search-ec2-instances-export-tags](https://github.com/aws-samples/search-ec2-instances-export-tags) repository. | DevOps engineer |

## Related resources
<a name="export-tags-for-a-list-of-amazon-ec2-instances-to-a-csv-file-resources"></a>
+ [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) (AWS CLI documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

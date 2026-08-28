---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python.html
---

# Convert and unpack EBCDIC data to ASCII on AWS by using Python
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python"></a>

*Luis Gustavo Dantas, Amazon Web Services*

## Summary
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-summary"></a>

Because mainframes typically host critical business data, modernizing data is one of the most important tasks when migrating data to the Amazon Web Services (AWS) Cloud or other American Standard Code for Information Interchange (ASCII) environment. On mainframes, data is typically encoded in extended binary-coded decimal interchange code (EBCDIC) format. Exporting database, Virtual Storage Access Method (VSAM), or flat files generally produces packed, binary EBCDIC files, which are more complex to migrate. The most commonly used database migration solution is change data capture (CDC), which, in most cases, automatically converts data encoding. However, CDC mechanisms might not be available for these database, VSAM, or flat files. For these files, an alternative approach is required to modernize the data.

This pattern describes how to modernize EBCDIC data by converting it to ASCII format. After conversion, you can load the data into distributed databases or have applications in the cloud process the data directly. The pattern uses the conversion script and sample files in the [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) GitHub repository.

## Prerequisites and limitations
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An EBCDIC input file and its corresponding common business-oriented language (COBOL) copybook. A sample EBCDIC file and COBOL copybook are included in the [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) GitHub repository. For more information about COBOL copybooks, see [Enterprise COBOL for z/OS 6.4 Programming Guide](https://publibfp.dhe.ibm.com/epubs/pdf/igy6pg40.pdf) on the IBM website.

**Limitations**
+ File layouts defined inside COBOL programs are not supported. They must be made available separately.

**Product versions**
+ Python version 3.8 or later

## Architecture
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-architecture"></a>

**Source technology stack**
+ EBCDIC data on a mainframe
+ COBOL copybook

**Target technology stack**
+ Amazon Elastic Compute Cloud (Amazon EC2) instance in a virtual private cloud (VPC)
+ Amazon Elastic Block Store (Amazon EBS)
+ Python and its required packages, JavaScript Object Notation (JSON), sys, and datetime
+ ASCII flat file ready to be read by a modern application or loaded in a relational database table

**Target architecture**

![EBCDIC data converted to ASCII on an EC2 instance by using Python scripts and a COBOL copybook](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f5907bfe-7dff-4cd0-8523-57015ad48c4b/images/4f97b1dd-3f20-4966-a291-22180680ea99.png)

The architecture diagram shows the process of converting an EBCDIC file to an ASCII file on an EC2 instance:

1. Using the **parse\_copybook\_to\_json.py** script, you convert the COBOL copybook to a JSON file.

1. Using the JSON file and the **extract\_ebcdic\_to\_ascii.py** script, you convert the EBCDIC data to an ASCII file.

**Automation and scale**

After the resources needed for the first manual file conversions are in place, you can automate file conversion. This pattern doesn’t include instructions for automation. There are multiple ways to automate the conversion. The following is an overview of one possible approach:

1. Encapsulate the AWS Command Line Interface (AWS CLI) and Python script commands into a shell script.

1. Create an AWS Lambda function that asynchronously submits the shell script job into an EC2 instance. For more information, see [Scheduling SSH jobs using AWS Lambda](https://aws.amazon.com/blogs/compute/scheduling-ssh-jobs-using-aws-lambda/).

1. Create an Amazon Simple Storage Service (Amazon S3) trigger that invokes the Lambda function every time a legacy file is uploaded. For more information, see [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html).

## Tools
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/?id=docs_gateway) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need, and quickly scale them up or down.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**Other tools**
+ [GitHub](https://github.com/) is a code-hosting service that provides collaboration tools and version control.
+ [Python](https://www.python.org/) is a high-level programming language.

**Code repository**

The code for this pattern is available in the [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) GitHub repository.

## Epics
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-epics"></a>

### Prepare the EC2 instance
<a name="prepare-the-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch an EC2 instance. | The EC2 instance must have outbound internet access. This allows the instance to access the Python source code available on GitHub. To create the instance:1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2).<br />2. Launch an EC2 Linux instance. Use a public IP address and allow inbound access through port 22. Ensure that the storage size of the instance is at least twice the size of the EBCDIC data file. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/index.html). | General AWS |
| Install Git. | 1. Using a secure shell (SSH) client, connect to the EC2 instance you just launched. For more information, see [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html).<br />2. In the Amazon EC2 console, run the following command. This installs Git on the EC2 instance.<pre>sudo yum install git</pre><br />3. Run the following command and confirm that Git has been successfully installed.<pre>git --version</pre> | General AWS, Linux |
| Install Python. | 1. In the Amazon EC2 console, run the following command. This installs Python on the EC2 instance.<pre>sudo yum install python3</pre><br />2. In the Amazon EC2 console, run the following command. This installs Pip3 on the EC2 instance.<pre>sudo yum install python3-pip</pre><br />3. In the Amazon EC2 console, run the following command. This installs AWS SDK for Python (Boto3) on the EC2 instance.<pre>sudo pip3 install boto3</pre><br />4. In the Amazon EC2 console, run the following command, where `<us-east-1>` is the code for your AWS Region. For a complete list of Region codes, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in the Amazon EC2 documentation.<pre>export AWS_DEFAULT_REGION=<us-east-1></pre> | General AWS, Linux |
| Clone the GitHub repository. | 1. In the Amazon EC2 console, run the following command. This clones the **mainframe-data-utilities** repository from GitHub and opens the default copy location, the `home` folder.<pre>git clone https://github.com/aws-samples/mainframe-data-utilities.git</pre><br />2. In the `home` folder, confirm that the `mainframe-data-utilities` folder is present. | General AWS, GitHub |

### Create the ASCII file from the EBCDIC data
<a name="create-the-ascii-file-from-the-ebcdic-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Parse the COBOL copybook into the JSON layout file. | Inside the `mainframe-data-utilities` folder, run the **parse\_copybook\_to\_json.py** script. This automation module reads the file layout from a COBOL copybook and creates a JSON file. The JSON file contains the information required to interpret and extract the data from the source file. This creates the JSON metadata from the COBOL copybook. <br />The following command converts the COBOL copybook to a JSON file.<pre>python3 parse_copybook_to_json.py \<br />-copybook LegacyReference/COBPACK2.cpy \<br />-output sample-data/cobpack2-list.json \<br />-dict sample-data/cobpack2-dict.json \<br />-ebcdic sample-data/COBPACK.OUTFILE.txt \<br />-ascii sample-data/COBPACK.ASCII.txt \<br />-print 10000</pre><br />The script prints the received arguments.<pre>-----------------------------------------------------------------------<br />Copybook file...............| LegacyReference/COBPACK2.cpy<br />Parsed copybook (JSON List).| sample-data/cobpack2-list.json<br />JSON Dict (documentation)...| sample-data/cobpack2-dict.json<br />ASCII file..................| sample-data/COBPACK.ASCII.txt<br />EBCDIC file.................| sample-data/COBPACK.OUTFILE.txt<br />Print each..................| 10000<br />-----------------------------------------------------------------------</pre><br />For more information about the arguments, see the [README file](https://github.com/aws-samples/mainframe-data-utilities/blob/main/README.md) in the GitHub repository. | General AWS, Linux |
| Inspect the JSON layout file. | 1. Navigate to the output path defined in the **parse\_copybook\_to\_json.py** script.<br />2. Check the creation time of the **sample-data/cobpack2-list.json** file to confirm that you have selected the appropriate JSON layout file.<br />3. Examine the JSON file and confirm that the contents are similar to the following.<pre> "input": "extract-ebcdic-to-ascii/COBPACK.OUTFILE.txt",<br /> "output": "extract-ebcdic-to-ascii/COBPACK.ASCII.txt",<br /> "max": 0,<br /> "skip": 0,<br /> "print": 10000,<br /> "lrecl": 150,<br /> "rem-low-values": true,<br /> "separator": "|",<br /> "transf": [<br /> {<br /> "type": "ch",<br /> "bytes": 19,<br /> "name": "OUTFILE-TEXT"<br /> } </pre>The most important attributes of the JSON layout file are:+ `input` – Contains the path of the EBCDIC file to be converted<br />+ `output` – Defines the path where the ASCII file will be generated<br />+ `lrecl` – Specifies the size in bytes of the logical record length<br />+ `transf` – Lists all fields and their size in bytes<br />For more information about the JSON layout file, see the [README file](https://github.com/aws-samples/mainframe-data-utilities/blob/main/README.md) in the GitHub repository. | General AWS, JSON |
| Create the ASCII file.  | Run the **extract\_ebcdic\_to\_ascii.py** script, which is included in the cloned GitHub repository. This script reads the EBCDIC file and writes a converted and readable ASCII file.<pre>python3 extract_ebcdic_to_ascii.py -local-json sample-data/cobpack2-list.json</pre><br />As the script processes the EBCDIC data, it prints a message for every batch of 10,000 records. See the following example.<pre>------------------------------------------------------------------<br />2023-05-15 21:21:46.322253 | Local Json file   | -local-json | sample-data/cobpack2-list.json<br />2023-05-15 21:21:47.034556 | Records processed | 10000<br />2023-05-15 21:21:47.736434 | Records processed | 20000<br />2023-05-15 21:21:48.441696 | Records processed | 30000<br />2023-05-15 21:21:49.173781 | Records processed | 40000<br />2023-05-15 21:21:49.874779 | Records processed | 50000<br />2023-05-15 21:21:50.705873 | Records processed | 60000<br />2023-05-15 21:21:51.609335 | Records processed | 70000<br />2023-05-15 21:21:52.292989 | Records processed | 80000<br />2023-05-15 21:21:52.938366 | Records processed | 89280<br />2023-05-15 21:21:52.938448 Seconds 6.616232</pre><br />For information about how to change the print frequency, see the [README file](https://github.com/aws-samples/mainframe-data-utilities/blob/main/README.md) in the GitHub repository. | General AWS |
| Examine the ASCII file. | 1. Check the creation time of the **extract-ebcdic-to-ascii/COBPACK.ASCII.txt** file to verify that it was recently created.<br />2. In the Amazon EC2 console, enter the following command. This opens the first record of the ASCII file.<pre>head sample-data/COBPACK.ASCII.txt -n 1| xxd</pre><br />3. Examine the contents of the first record. Because EBCDIC files are usually binary, they don't have carriage return and line feed (CRLF) special characters. The **extract\_ebcdic\_to\_ascii.py** script adds a pipe character as a column separator, which is defined in the script parameters. If you used the sample EBCDIC file provided, the following is the first record in the ASCII file.<pre>00000000: 2d30 3030 3030 3030 3030 3130 3030 3030  -000000000100000<br />00000010: 3030 307c 3030 3030 3030 3030 3031 3030  000|000000000100<br />00000020: 3030 3030 3030 7c2d 3030 3030 3030 3030  000000|-00000000<br />00000030: 3031 3030 3030 3030 3030 7c30 7c30 7c31  0100000000|0|0|1<br />00000040: 3030 3030 3030 3030 7c2d 3130 3030 3030  00000000|-100000<br />00000050: 3030 307c 3130 3030 3030 3030 307c 2d31  000|100000000|-1<br />00000060: 3030 3030 3030 3030 7c30 3030 3030 7c30  00000000|00000|0<br />00000070: 3030 3030 7c31 3030 3030 3030 3030 7c2d  0000|100000000|-<br />00000080: 3130 3030 3030 3030 307c 3030 3030 3030  100000000|000000<br />00000090: 3030 3030 3130 3030 3030 3030 307c 2d30  0000100000000|-0<br />000000a0: 3030 3030 3030 3030 3031 3030 3030 3030  0000000001000000<br />000000b0: 3030 7c41 7c41 7c0a                      00|A|A|.</pre> | General AWS, Linux |
| Evaluate the EBCDIC file. | In the Amazon EC2 console, enter the following command. This opens the first record of the EBCDIC file.<pre>head sample-data/COBPACK.OUTFILE.txt -c 150 | xxd</pre><br />If you used the sample EBCDIC file, the following is the result.<pre> 00000000: 60f0 f0f0 f0f0 f0f0 f0f0 f1f0 f0f0 f0f0 `...............<br /> 00000010: f0f0 f0f0 f0f0 f0f0 f0f0 f0f0 f1f0 f0f0 ................<br /> 00000020: f0f0 f0f0 f0f0 f0f0 f0f0 f0f0 f0f0 f1f0 ................<br /> 00000030: f0f0 f0f0 f0f0 d000 0000 0005 f5e1 00fa ................<br /> 00000040: 0a1f 0000 0000 0005 f5e1 00ff ffff fffa ................<br /> 00000050: 0a1f 0000 000f 0000 0c10 0000 000f 1000 ................<br /> 00000060: 0000 0d00 0000 0000 1000 0000 0f00 0000 ................<br /> 00000070: 0000 1000 0000 0dc1 c100 0000 0000 0000 ................<br /> 00000080: 0000 0000 0000 0000 0000 0000 0000 0000 ................<br /> 00000090: 0000 0000 0000 ......</pre><br />To evaluate the equivalence between the source and target files, comprehensive knowledge of EBCDIC is required. For example, the first character of the sample EBCDIC file is a hyphen (`-`). In hexadecimal notation of the EBCDIC file, this character is represented by `60`, and in hexadecimal notation of the ASCII file, this character is represented by `2D`. For an EBCDIC-to-ASCII conversion table, see [EBCDIC to ASCII](https://www.ibm.com/docs/en/iis/11.3?topic=tables-ebcdic-ascii) on the IBM website. | General AWS, Linux, EBCDIC |

## Related resources
<a name="convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python-resources"></a>

**References**
+ [The EBCDIC character set](https://www.ibm.com/docs/en/zos-basic-skills?topic=mainframe-ebcdic-character-set) (IBM documentation)
+ [EBCDIC to ASCII](https://www.ibm.com/docs/en/iis/11.3?topic=tables-ebcdic-ascii) (IBM documentation)
+ [COBOL](https://www.ibm.com/docs/en/i/7.1?topic=languages-cobol) (IBM documentation)
+ [Basic JCL concepts](https://www.ibm.com/docs/en/zos-basic-skills?topic=collection-basic-jcl-concepts) (IBM documentation)
+ [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) (Amazon EC2 documentation)

**Tutorials**
+ [Scheduling SSH jobs using AWS Lambda](https://aws.amazon.com/blogs/compute/scheduling-ssh-jobs-using-aws-lambda/) (AWS blog post)
+ [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) (AWS Lambda documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

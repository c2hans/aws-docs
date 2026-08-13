---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/using-qnabot-on-aws-command-line-interface-cli.html
---

# Using QnABot on AWS Command Line Interface (CLI)
<a name="using-qnabot-on-aws-command-line-interface-cli"></a>

The QnABot on AWS CLI supports the capability to import and export questions and answers from your QnABot setup.

## Setup prerequisites
<a name="setup-prerequisites"></a>

To use the CLI, the following prerequisites are required:
+ Download the source directory from code base of the QnABot on AWS guidance (version 5.2.0 or higher) in the GitHub repository.
+  [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/).
+ Python version 3.7 or higher. For more information on installing Python, see [Python Setup and Usage](https://docs.python.org/3/using/index.html).
+ IAM permissions having the following [IAM policy](#iam-policy). Attach the following IAM policy to the IAM user or IAM Role that you are using for the AWS CLI. Replace the following values when creating the IAM policy:

 **AWS\_REGION** - The AWS Region where you have deployed the QnABot on AWS guidance.

 **AWS\_ACCOUNT\_ID** - The AWS Account ID where you have deployed the QnABot on AWS guidance.

 **YOUR\_QNABOT\_IMPORT\_BUCKET\_NAME** - The name of the QnABot on AWS import bucket name. This can be found by navigating to the Resources section (in AWS CloudFormation) of the deployed QnABot on AWS CloudFormation template.

 **YOUR\_QNABOT\_EXPORT\_BUCKET\_NAME** - The name of the QnABot on AWS export bucket name. This can be found by navigating to the Resources section (in AWS CloudFormation) of the deployed QnABot on AWS CloudFormation template.

 **YOUR\_QNABOT\_STACK\_NAME** - The name of the QnABot on AWS stack that you deployed via AWS CloudFormation.

## IAM policy
<a name="iam-policy"></a>

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ReadWriteStatement",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:AWS_REGION:AWS_ACCOUNT_ID:YOUR_QNABOT_IMPORT_BUCKET_NAME/*",
                "arn:aws:s3:AWS_REGION:AWS_ACCOUNT_ID:YOUR_QNABOT_EXPORT_BUCKET_NAME/*",
            ]
        },
        {
            "Sid": "CloudFormationDescribeStatement",
            "Effect": "Allow",
            "Action": "cloudformation:DescribeStackResource",
            "Resource": "arn:aws:cloudformation:AWS_REGION:AWS_ACCOUNT_ID:stack/YOUR_QNABOT_STACK_NAME/*"
        }
    ]
}
```

## Environment setup
<a name="environment-setup"></a>

Get started by installing the Python packages required for the CLI module. Navigate to source/cli directory inside the QnABot on AWS codebase and run the following commands to setup Python environment and install dependencies:

```
poetry install
source $(poetry env info --path)/bin/activate
```

## Set environment variables
<a name="set-environment-variables"></a>

Set the environment variable for your AWS Region. For example, to use the us-east-1 Region, run the following command:

```
export AWS_REGION='us-east-1'
```

Set the Python path using the following command:

```
export PYTHONPATH=${PWD}:$PYTHONPATH
```

## Available commands
<a name="available-commands"></a>

The `qnabot_cli.py` file is located in the `source/aws_solutions/qnabot/cli` directory. Run python3 `aws_solutions/qnabot/cli/qnabot_cli.py` using the following syntax:

 **Usage:** `qnabot_cli.py [OPTIONS] COMMAND [ARGS]…​`

 **Options:**

 `-h, --help Show this message and exit.`

 **Commands:**

```
export Export QnABot questions and answers from your QnABot setup.
import Import QnABot questions and answers to your QnABot setup.
```

## Using the import command
<a name="using-the-import-command"></a>

 **Usage:** `qnabot_cli.py import [OPTIONS]`

Import QnABot questions and answers to your QnABot setup. This command requires two (2) parameters: `<cloudformation-stack-name>`, and `<source-filename>`. The **cloudformation-stack-name** parameter is used to know the QnABot on AWS deployment to use to support the import process.

 **Options:**

```
  -s, --cloudformation-stack-name TEXT
                                  Provide the name of the CloudFormation stack
                                  of your QnABot on AWS deployment  [required]
  -f, --source-filename TEXT      Provide the filename along with path where
                                  the file to be imported is located
                                  [required]
  -fmt, --file-format [JSON|JSONL|XLSX]
                                  Provide the file format to use for import
                                  [default: JSON]
  -d, --delete-existing-content BOOLEAN
                                  Use this parameter if all existing QnABot
                                  {qids} in your QnABot deployment should be
                                  deleted before the import process.
                                  [default: False]
  -h, --help                      Show this message and exit.
```

A successful import will output status with the following information:

```
{
    "number_of_qids_imported": <number>,
    "number_of_qids_failed_to_import": <number>,
    "import_starttime": <datetime in UTC>,
    "import_endtime": <datetime in UTC>",
    "status": "Complete",
    "error_code": "none"
}
```

 **Example:**

```
{
    "number_of_qids_imported": 9,
    "number_of_qids_failed_to_import": 0,
    "import_starttime": "2022-03-20T21:39:28.455Z",
    "import_endtime": "2022-03-20T21:39:32.193Z",
    "status": "Complete",
    "error_code": "none"
}
```

## Using the export command
<a name="using-the-export-command"></a>

 **Usage:** `qnabot_cli.py export [OPTIONS]`

Export QnABot questions and answers from your QnABot setup. This command requires two (2) parameters: `<cloudformation-stack-name>`, and `<export-filename>`. The **cloudformation-stack-name** parameter is used to know the QnABot on AWS deployment to use to support the export process.

 **Options:**

```
-s, --cloudformation-stack-name TEXT
                                  Provide the name of the CloudFormation stack
                                  of your QnABot on AWS deployment  [required]
  -f, --export-filename TEXT      Provide the filename along with path where
                                  the exported file should be downloaded to
                                  [required]
  -qids, --export-filter TEXT     Export {qids} that start with this filter
                                  string. Exclude this option to export all
                                  {qids}
  -fmt, --file-format [JSON|JSONL]
                                  Provide the file format to use for export
                                  [default: JSON]
  -h, --help                      Show this message and exit.
```

A successful import will output status with the following information:

```
{
    "export_directory": <string>,
    "status": "Downloaded",
    "comments": <string>,
    "error_code": "none"
}
```

 **Example:**

```
{
    "export_directory": "../export/qna.json",
    "status": "Downloaded",
    "comments": "Check the export directory for the downloaded export.",
    "error_code": "none"
}
```

## Running qnabot\_cli.py as a shell script
<a name="running-qnabot-cli.py-as-a-shell-script"></a>

 **Import example:**

```
#!/bin/bash
export AWS_REGION='us-east-1'
shell_output=$(python3 qnabot_cli.py import -s qnabot-stack -f ../import/qna_import.json -fmt json)
STATUS="${?}"
if [ "${STATUS}" == 0 ];
then
    echo "AWS QnABot import completed successfully"
    echo "$shell_output"
else
    echo "AWS QnABot import failed"
    echo "$shell_output"
fi
```

 **Export example**

```
#!/bin/bash
export AWS_REGION='us-east-1'
shell_output=$(python3 qnabot_cli.py export -s qnabot-stack -f ../export/qna_export.json -fmt json)
STATUS="${?}"
if [ "${STATUS}" == 0 ];
then
    echo "AWS QnABot export completed successfully"
    echo "$shell_output"
else
    echo "AWS QnABot export failed"
    echo "$shell_output"
fi
```

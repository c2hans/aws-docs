---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda.html
---

# Convert mainframe files from EBCDIC format to character-delimited ASCII format in Amazon S3 using AWS Lambda
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda"></a>

*Luis Gustavo Dantas, Amazon Web Services*

## Summary
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-summary"></a>

This pattern shows you how to launch an AWS Lambda function that automatically converts mainframe Extended Binary Coded Decimal Interchange Code (EBCDIC) files to character-delimited American Standard Code for Information Interchange (ASCII) files. The Lambda function runs after the ASCII files are uploaded to an Amazon Simple Storage Service (Amazon S3) bucket. After the file conversion, you can read the ASCII files on x86-based workloads or load the files into modern databases.

The file conversion approach demonstrated in this pattern can help you overcome the challenges of working with EBCDIC files on modern environments. Files encoded in EBCDIC often contain data represented in a binary or packed decimal format, and fields are fixed-length. These characteristics create obstacles because modern x86-based workloads or distributed environments generally work with ASCII-encoded data and can’t process EBCDIC files.

## Prerequisites and limitations
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon S3 bucket
+ An AWS Identity and Access Management (IAM) user with administrative permissions
+ AWS CloudShell
+ [Python 3.8.0](https://www.python.org/downloads/release/python-380/) or later
+ A flat file encoded in EBCDIC and its corresponding data structure in a common business-oriented language (COBOL) copybook

**Note**
This pattern uses a sample EBCDIC file ([CLIENT.EBCDIC.txt](https://github.com/aws-samples/mainframe-data-utilities/blob/main/sample-data/CLIENT.EBCDIC.txt)) and its corresponding COBOL copybook ([COBKS05.cpy](https://github.com/aws-samples/mainframe-data-utilities/blob/main/LegacyReference/COBKS05.cpy)). Both files are available in the GitHub [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) repository.

**Limitations**
+ COBOL copybooks usually hold multiple layout definitions. The [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) project can parse this kind of copybook but can't infer which layout to consider on data conversion. This is because copybooks don't hold this logic (which remains on COBOL programs instead). Consequently, you must manually configure the rules for selecting layouts after you parse the copybook.
+ This pattern is subject to [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).

## Architecture
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-architecture"></a>

**Source technology stack**
+ IBM z/OS, IBM i, and other EBCDIC systems
+ Sequential files with data encoded in EBCDIC (such as IBM Db2 unloads)
+ COBOL copybook

**Target technology stack**
+ Amazon S3
+ Amazon S3 event notification
+ IAM
+ Lambda function
+ Python 3.8 or later
+ Mainframe Data Utilities
+ JSON metadata
+ Character-delimited ASCII files

**Target architecture**

The following diagram shows an architecture for converting mainframe EBCDIC files to ASCII files.

![Architecture for converting mainframe EBCDIC files to ASCII files](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/97ab4129-2639-4733-86cb-962d91526df4/images/3ca7ca44-373a-434f-8c40-09e7c2abf5ec.png)

The diagram shows the following workflow:

1. The user runs the copybook parser script, which converts the COBOL copybook into a JSON file.

1. The user uploads the JSON metadata to an Amazon S3 bucket. This makes the metadata readable by the data conversion Lambda function.

1. The user or an automated process uploads the EBCDIC file to the Amazon S3 bucket.

1. The Amazon S3 notification event triggers the data conversion Lambda function.

1. AWS verifies the Amazon S3 bucket read-write permissions for the Lambda function.

1. Lambda reads the file from the Amazon S3 bucket and locally converts the file from EBCDIC to ASCII.

1. Lambda logs the process status in Amazon CloudWatch.

1. Lambda writes the ASCII file back to Amazon S3.

**Note**
The copybook parser script runs a single time to perform the metadata conversion to JSON format, which is subsequently stored in an Amazon S3 bucket. After the initial conversion, all subsequent EBCDIC files that reference the same JSON file in the Amazon S3 bucket will use the existing metadata configuration.

## Tools
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications that you run on AWS in real time.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) is a browser-based shell that you can use to manage AWS services by using the AWS Command Line Interface (AWS CLI) and a range of preinstalled development tools.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. Lambda runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Other tools**
+ [GitHub](https://github.com/) is a code-hosting service that provides collaboration tools and version control.
+ [Python](https://www.python.org/) is a high-level programming language.

**Code**

The code for this pattern is available in the GitHub [mainframe-data-utilities](https://github.com/aws-samples/mainframe-data-utilities) repository.

## Best practices
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-best-practices"></a>

Consider the following best practices:
+ Set the required permissions at the Amazon Resource Name (ARN) level.
+ Always grant least-privilege permissions for IAM policies. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-epics"></a>

### Create environment variables and a working folder
<a name="create-environment-variables-and-a-working-folder"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the environment variables. | Copy the following environment variables to a text editor, and then replace the `<placeholder>` values in the following example with your resource values:<pre>bucket=<your_bucket_name><br />account=<your_account_number><br />region=<your_region_code></pre>You will create references to your Amazon S3 bucket, AWS account, and AWS Region later.<br />To define environment variables, open the [CloudShell console](https://console.aws.amazon.com/cloudshell/), and then copy and paste your updated environment variables onto the command line.You must repeat this step every time the CloudShell session restarts. | General AWS |
| Create a working folder. | To simplify the resource clean-up process later on, create a working folder in CloudShell by running the following command:<pre>mkdir workdir; cd workdir</pre>You must change the directory to the working directory (`workdir`) every time you lose a connection to your CloudShell session. | General AWS |

### Define an IAM role and policy
<a name="define-an-iam-role-and-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a trust policy for the Lambda function. | The EBCDIC converter runs in a Lambda function. The function must have an IAM role. Before you create the IAM role, you must define a trust policy document that enables resources to assume that policy.<br />From the CloudShell working folder, create a policy document by running the following command:<pre>E2ATrustPol=$(cat <<EOF<br />{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "Service": "lambda.amazonaws.com"<br />            },<br />            "Action": "sts:AssumeRole"<br />        }<br />    ]<br />}<br />EOF<br />)<br />printf "$E2ATrustPol" > E2ATrustPol.json</pre> | General AWS |
| Create the IAM role for Lambda conversion. | To create an IAM role, run the following AWS CLI command from the CloudShell working folder:<pre>aws iam create-role --role-name E2AConvLambdaRole --assume-role-policy-document file://E2ATrustPol.json</pre> | General AWS |
| Create the IAM policy document for the Lambda function. | The Lambda function must have read-write access to the Amazon S3 bucket and write permissions for Amazon CloudWatch Logs.<br />To create an IAM policy, run the following command from the CloudShell working folder:<pre>E2APolicy=$(cat <<EOF<br />{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "Logs",<br />            "Effect": "Allow",<br />            "Action": [<br />                "logs:PutLogEvents",<br />                "logs:CreateLogStream",<br />                "logs:CreateLogGroup"<br />            ],<br />            "Resource": [<br />                "arn:aws:logs:*:*:log-group:*",<br />                "arn:aws:logs:*:*:log-group:*:log-stream:*"<br />            ]<br />        },<br />        {<br />            "Sid": "S3",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:GetObject",<br />                "s3:PutObject",<br />                "s3:GetObjectVersion"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::%s/*",<br />                "arn:aws:s3:::%s"<br />            ]<br />        }<br />    ]<br />}<br />EOF<br />)<br />printf "$E2APolicy" "$bucket" "$bucket" > E2AConvLambdaPolicy.json</pre> | General AWS |
| Attach the IAM policy document to the IAM role. | To attach the IAM policy to the IAM role, enter the following command from your CloudShell working folder:<pre>aws iam put-role-policy --role-name E2AConvLambdaRole --policy-name E2AConvLambdaPolicy --policy-document file://E2AConvLambdaPolicy.json</pre> | General AWS |

### Create the Lambda function for EBCDIC conversion
<a name="create-the-lam-function-for-ebcdic-conversion"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the EBCDIC conversion source code. | From the CloudShell working folder, run the following command to download the mainframe-data-utilities source code from GitHub:<pre>git clone https://github.com/aws-samples/mainframe-data-utilities.git mdu</pre> | General AWS |
| Create the ZIP package. | From the CloudShell working folder, enter the following command to create the ZIP package that creates the Lambda function for EBCDIC conversion:<pre>cd mdu; zip ../mdu.zip *.py; cd ..</pre> | General AWS |
| Create the Lambda function. | From the CloudShell working folder, enter the following command to create the Lambda function for EBCDIC conversion:<pre>aws lambda create-function \<br />--function-name E2A \<br />--runtime python3.9 \<br />--zip-file fileb://mdu.zip \<br />--handler extract_ebcdic_to_ascii.lambda_handler \<br />--role arn:aws:iam::$account:role/E2AConvLambdaRole \<br />--timeout 10 \<br />--environment "Variables={layout=$bucket/layout/}"</pre> The environment variable layout tells the Lambda function where the JSON metadata resides. | General AWS |
| Create the resource-based policy for the Lambda function. | From the CloudShell working folder, enter the following command to allow your Amazon S3 event notification to trigger the Lambda function for EBCDIC conversion:<pre>aws lambda add-permission \<br />--function-name E2A \<br />--action lambda:InvokeFunction \<br />--principal s3.amazonaws.com \<br />--source-arn arn:aws:s3:::$bucket \<br />--source-account $account \<br />--statement-id 1</pre> | General AWS |

### Create the Amazon S3 event notification
<a name="create-the-s3-event-notification"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the configuration document for the Amazon S3 event notification. | The Amazon S3 event notification initiates the EBCDIC conversion Lambda function when files are placed in the input folder.<br />From the CloudShell working folder, run the following command to create the JSON document for the Amazon S3 event notification:<pre>S3E2AEvent=$(cat <<EOF<br />{<br />"LambdaFunctionConfigurations": [<br />    {<br />      "Id": "E2A",<br />      "LambdaFunctionArn": "arn:aws:lambda:%s:%s:function:E2A",<br />      "Events": [ "s3:ObjectCreated:Put" ],<br />      "Filter": {<br />        "Key": {<br />          "FilterRules": [<br />            {<br />              "Name": "prefix",<br />              "Value": "input/"<br />            }<br />          ]<br />        }<br />      }<br />    }<br />  ]<br />}<br />EOF<br />)<br />printf "$S3E2AEvent" "$region" "$account" > S3E2AEvent.json</pre> | General AWS |
| Create the Amazon S3 event notification. | From the CloudShell working folder, enter the following command to create the Amazon S3 event notification:<pre>aws s3api put-bucket-notification-configuration --bucket $bucket --notification-configuration file://S3E2AEvent.json</pre> | General AWS |

### Create and upload the JSON metadata
<a name="create-and-upload-the-json-metadata"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Parse the COBOL copybook. | From the CloudShell working folder, enter the following command to parse a sample COBOL copybook into a JSON file (which defines how to read and slice the data file properly):<pre>python3       mdu/parse_copybook_to_json.py \<br />-copybook     mdu/LegacyReference/COBKS05.cpy \<br />-output       CLIENT.json \<br />-output-s3key CLIENT.ASCII.txt \<br />-output-s3bkt $bucket \<br />-output-type  s3 \<br />-print        25</pre> | General AWS |
| Add the transformation rule. | The sample data file and its corresponding COBOL copybook is a multi-layout file. This means that the conversion must slice data based on certain rules. In this case, bytes on position 3 and 4 in each row define the layout.<br />From the CloudShell working folder, edit the `CLIENT.json` file and change the contents from `"transf-rule": [],` to the following:<pre>"transf-rule": [<br />{<br />"offset": 4,<br />"size": 2,<br />"hex": "0002",<br />"transf": "transf1"<br />},<br />{<br />"offset": 4,<br />"size": 2,<br />"hex": "0000",<br />"transf": "transf2"<br />}<br />],</pre> | General AWS, IBM Mainframe, Cobol |
| Upload the JSON metadata to the Amazon S3 bucket. | From the CloudShell working folder, enter the following AWS CLI command to upload the JSON metadata to your Amazon S3 bucket:<pre>aws s3 cp CLIENT.json s3://$bucket/layout/CLIENT.json</pre> | General AWS |

### Convert the EBCDIC file
<a name="convert-the-ebcdic-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send the EBCDIC file to the Amazon S3 bucket. | From the CloudShell working folder, enter the following command to send the EBCDIC file to the Amazon S3 bucket:<pre>aws s3 cp mdu/sample-data/CLIENT.EBCDIC.txt s3://$bucket/input/</pre> We recommend that you set different folders for input (EBCDIC) and output (ASCII) files to avoid calling the Lambda conversion function again when the ASCII file is uploaded to the Amazon S3 bucket. | General AWS |
| Check the output. | From the CloudShell working folder, enter the following command to check if the ASCII file is generated in your Amazon S3 bucket:<pre>aws s3 ls s3://$bucket/</pre> The data conversion can take several seconds to happen. We recommend that you check for the ASCII file a few times.<br />After the ASCII file is available, enter the following command to view the contents of the converted file in the Amazon S3 bucket. As needed, you can download it or use it directly from the Amazon S3 bucket:<pre>aws s3 cp s3://$bucket/CLIENT.ASCII.txt - | head</pre><br />Check the ASCII file content:<pre>0|0|220|<br />1|1|HERBERT MOHAMED|1958-08-31|BACHELOR|0010000.00|<br />1|2|36|THE ROE AVENUE|<br />2|1|JAYLEN GEORGE|1969-05-29|ELEMENTARY|0020000.00|<br />2|2|365|HEATHFIELD ESPLANADE|<br />3|1|MIKAEEL WEBER|1982-02-17|MASTER|0030000.00|<br />3|2|4555|MORRISON STRAND|<br />4|1|APRIL BARRERA|1967-01-12|DOCTOR|0030000.00|<br />4|2|1311|MARMION PARK|<br />5|1|ALEEZA PLANT|1985-03-01|BACHELOR|0008000.00|</pre> | General AWS |

### Clean the environment
<a name="clean-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Prepare the variables and folder. | If you lose connection with CloudShell, reconnect and then enter the following command to change the directory to the working folder:<pre>cd workdir</pre><br />Ensure that the environment variables are defined:<pre>bucket=<your_bucket_name><br />account=<your_account_number><br />region=<your_region_code></pre> | General AWS |
| Remove the notification configuration for the bucket. | From the CloudShell working folder, run the following command to remove the Amazon S3 event notification configuration:<pre>aws s3api put-bucket-notification-configuration \<br />--bucket=$bucket \<br />--notification-configuration="{}"</pre> | General AWS |
| Delete the Lambda function. | From the CloudShell working folder, enter the following command to delete the Lambda function for the EBCDIC converter:<pre>aws lambda delete-function \<br />--function-name E2A</pre> | General AWS |
| Delete the IAM role and policy. | From the CloudShell working folder, enter the following command to remove the EBCDIC converter role and policy:<pre>aws iam delete-role-policy \<br />--role-name E2AConvLambdaRole \<br />--policy-name E2AConvLambdaPolicy<br /><br />aws iam delete-role \<br />--role-name E2AConvLambdaRole</pre> | General AWS |
| Delete the files generated in the Amazon S3 bucket. | From the CloudShell working folder, enter the following command to delete the files generated in the Amazon S3 bucket:<pre>aws s3 rm s3://$bucket/layout --recursive<br />aws s3 rm s3://$bucket/input --recursive<br />aws s3 rm s3://$bucket/CLIENT.ASCII.txt</pre> | General AWS |
| Delete the working folder. | From the CloudShell working folder, enter the following command to remove `workdir` and its contents:<pre>cd ..; rm -Rf workdir</pre> | General AWS |

## Related resources
<a name="convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda-resources"></a>
+ [Mainframe Data Utilities README](https://github.com/aws-samples/mainframe-data-utilities/blob/main/README.md) (GitHub)
+ [The EBCDIC character set](https://www.ibm.com/docs/en/zos-basic-skills?topic=mainframe-ebcdic-character-set) (IBM documentation)
+ [EBCDIC to ASCII](https://www.ibm.com/docs/en/iis/11.7.0?topic=tables-ebcdic-ascii) (IBM documentation)
+ [COBOL](https://www.ibm.com/docs/en/i/7.6.0?topic=languages-cobol) (IBM documentation)
+ [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) (AWS Lambda documentation)

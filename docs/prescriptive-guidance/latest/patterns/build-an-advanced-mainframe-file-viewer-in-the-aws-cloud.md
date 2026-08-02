---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html
---

# Build an advanced mainframe file viewer in the AWS Cloud
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud"></a>

*Boopathy GOPALSAMY and Jeremiah O'Connor, Amazon Web Services*

## Summary
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-summary"></a>

This pattern provides code samples and steps to help you build an advanced tool for browsing and reviewing your mainframe fixed-format files by using AWS serverless services. The pattern provides an example of how to convert a mainframe input file to an Amazon OpenSearch Service document for browsing and searching. The file viewer tool can help you achieve the following:
+ Retain the same mainframe file structure and layout for consistency in your AWS target migration environment (for example, you can maintain the same layout for files in a batch application that transmits files to external parties)
+ Speed up development and testing during your mainframe migration
+ Support maintenance activities after the migration

## Prerequisites and limitations
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC) with a subnet that’s reachable by your legacy platform
+
**Note**
An input file and its corresponding common business-oriented language (COBOL) copybook (: For input file and COBOL copybook examples, see [gfs-mainframe-solutions](https://github.com/aws-samples/gfs-mainframe-patterns.git) on the GitHub repository. For more information about COBOL copybooks, see the [Enterprise COBOL for z/OS 6.3](https://publibfp.boulder.ibm.com/epubs/pdf/igy6pg30.pdf) Programming Guide on the IBM website.)

**Limitations**
+ Copybook parsing is limited to no more than two nested levels (OCCURS)

## Architecture
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-architecture"></a>

**Source technology stack  **
+ Input files in [FB (Fixed Blocked)](https://www.ibm.com/docs/en/zos-basic-skills?topic=set-data-record-formats) format
+ COBOL copybook layout

**Target technology stack  **
+ Amazon Athena
+ Amazon OpenSearch Service
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Lambda
+ AWS Step Functions

**Target architecture**

The following diagram shows the process of parsing and converting a mainframe input file to an OpenSearch Service document for browsing and searching.

![Process to parse and convert mainframe input file to OpenSearch Service.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/36d72b00-d163-455f-9e59-e2c872e7c28a/images/cce68438-bcf2-48c1-b86b-01242235ec76.png)

The diagram shows the following workflow:

1. An admin user or application pushes input files to one S3 bucket and COBOL copybooks to another S3 bucket.

1.
**Note**
The S3 bucket with the input files invokes a Lambda function that kicks off a serverless Step Functions workflow. : The use of an S3 event trigger and Lambda function to drive the Step Functions workflow in this pattern is optional. The GitHub code samples in this pattern don’t include the use of these services, but you can use these services based on your requirements.

1. The Step Functions workflow coordinates all the batch processes from the following Lambda functions:
   + The `s3copybookparser.py` function parses the copybook layout and extracts field attributes, data types, and offsets (required for input data processing).
   + The `s3toathena.py` function creates an Athena table layout. Athena parses the input data that’s processed by the `s3toathena.py` function and converts the data to a CSV file.
   + The `s3toelasticsearch.py` function ingests the results file from the S3 bucket and pushes the file to OpenSearch Service.

1. Users access OpenSearch Dashboards with OpenSearch Service to retrieve the data in various table and column formats and then run queries against the indexed data.

## Tools
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use. In this pattern, you use Lambda to implement core logic, such as parsing files, converting data, and loading data into OpenSearch Service for interactive file access.
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a managed service that helps you deploy, operate, and scale OpenSearch Service clusters in the AWS Cloud. In this pattern, you use OpenSearch Service to index the converted files and provide interactive search capabilities for users.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine Lambda functions and other AWS services to build business-critical applications. In this pattern, you use Step Functions to orchestrate Lambda functions.

**Other tools**
+ [GitHub](https://github.com/) is a code-hosting service that provides collaboration tools and version control.
+ [Python](https://www.python.org/) is a high-level programming language.

**Code**

The code for this pattern is available in the GitHub [gfs-mainframe-patterns](https://github.com/aws-samples/gfs-mainframe-patterns.git) repository.

## Epics
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-epics"></a>

### Prepare the target environment
<a name="prepare-the-target-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the S3 bucket. | [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) for storing the copybooks, input files, and output files. We recommend the following folder structure for your S3 bucket:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Create the s3copybookparser function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Create the s3toathena function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Create the s3toelasticsearch function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Create the OpenSearch Service cluster. | **Create the cluster**[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html)<br />**Grant access to the IAM role**<br />To provide fine-grained access to the Lambda function’s IAM role (`arn:aws:iam::**:role/service-role/s3toelasticsearch-role-**`), do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Create Step Functions for orchestration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |

### Deploy and run
<a name="deploy-and-run"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the input files and copybooks to the S3 bucket. | Download sample files from the [GitHub ](https://github.com/aws-samples/gfs-mainframe-patterns.git)repository sample folder and upload the files to the S3 bucket that you created earlier.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |
| Invoke the Step Functions. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html)<pre>{<br />  "s3_copybook_bucket_name": "<BUCKET NAME>",<br />  "s3_copybook_bucket_key": "<COPYBOOK PATH>",<br />  "s3_source_bucket_name": "<BUCKET NAME",<br />  "s3_source_bucket_key": "INPUT FILE PATH"<br />}</pre>For example:<pre>{<br />  "s3_copybook_bucket_name": "fileaidtest",<br />  "s3_copybook_bucket_key": "copybook/acctix.cpy",<br />  "s3_source_bucket_name": "fileaidtest",<br />  "s3_source_bucket_key": "input/acctindex"<br />}</pre> | General AWS |
| Validate the workflow execution in Step Functions. | In the [Step Functions console](https://console.aws.amazon.com/states/home), review the workflow execution in the **Graph inspector**. The execution run states are color coded to represent execution status. For example, blue indicates **In Progress**, green indicates **Succeeded**, and red indicates **Failed**. You can also review the table in the **Execution event history** section for more detailed information about the execution events.<br />For an example of a graphical workflow execution, see *Step Functions graph* in the *Additional information* section of this pattern. | General AWS |
| Validate the delivery logs in Amazon CloudWatch. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html)For an example of successful delivery logs, see *CloudWatch delivery logs* in the *Additional information* section of this pattern. | General AWS |
| Validate the formatted file in OpenSearch Dashboards and perform file operations. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-advanced-mainframe-file-viewer-in-the-aws-cloud.html) | General AWS |

## Related resources
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-resources"></a>

**References **
+ [Example COBOL copybook](https://www.ibm.com/docs/en/record-generator/3.0?topic=SSMQ4D_3.0.0/documentation/cobol_rcg_examplecopybook.html) (IBM documentation)
+ [BMC Compuware File-AID](https://www.bmc.com/it-solutions/bmc-compuware-file-aid.html) (BMC documentation)

**Tutorials**
+ [Tutorial: Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) (AWS Lambda documentation)
+ [How do I create a serverless workflow with AWS Step Functions and AWS Lambda](https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/) (AWS documentation)
+ [Using OpenSearch Dashboards with Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html) (AWS documentation)

## Additional information
<a name="build-an-advanced-mainframe-file-viewer-in-the-aws-cloud-additional"></a>

**Step Functions graph**

The following example shows a Step Functions graph. The graph shows the execution run status for the Lambda functions used in this pattern.

![Step Functions graph shows execution run status for the Lambda functions used in this pattern.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/36d72b00-d163-455f-9e59-e2c872e7c28a/images/11093e5d-2f9e-4bbf-8abc-f3b2980dd550.png)

**CloudWatch delivery logs**

The following example shows successful delivery logs for the execution of the `s3toelasticsearch` execution.

|
|
| 2022-08-10T15:53:33.033-05:00 | Number of processing documents: 100 |  |
| --- |--- |--- |
|  | 2022-08-10T15:53:33.171-05:00 | [INFO] 2022-08-10T20:53:33.171Z a1b2c3d4-5678-90ab-cdef-EXAMPLE11111POST https://search-essearch-3h4uqclifeqaj2vg4mphe7ffle.us-east-2.es.amazonaws.com:443/\_bulk [status:200 request:0.100s] |
|  | 2022-08-10T15:53:33.172-05:00 | Bulk write succeed: 100 documents |

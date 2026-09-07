---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-resource-assessment.html
---

# Automate AWS resource assessment
<a name="automate-aws-resource-assessment"></a>

*Naveen Suthar, Arun Bagal, Manish Garg, and Sandeep Gawande, Amazon Web Services*

## Summary
<a name="automate-aws-resource-assessment-summary"></a>

This pattern describes an automated approach for setting up resource assessment capabilities by using the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). By using this pattern, operations teams gather resource auditing details in an automated manner and view the details of all resources deployed in an AWS account on a single dashboard. This is helpful in the following use cases:
+ Identifying infrastructure as code (IaC) tools and isolating resources created by different IaC solutions such as [HashiCorp Terraform](https://www.terraform.io/), [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), AWS CDK, and [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
+ Fetching resource-auditing information

This solution will also help the leadership team obtain insights about the resources and activities in an AWS account from a single dashboard.

|
|
| Note: [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a paid service. Before running it to analyze data and create a dashboard, review the [Amazon Quick Sight pricing](https://aws.amazon.com/quicksight/pricing/). |
| --- |

## Prerequisites and limitations
<a name="automate-aws-resource-assessment-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Identity and Access Management (IAM) roles and permissions with access to provision resources
+ An [Amazon Quick account](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) created with access to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
+ AWS CDK version 2.55.1 or later installed
+ [Python](https://www.python.org/downloads/release/python-390/) version 3.9 or later installed

**Limitations**
+ This solution is deployed to a single AWS account.
+ The solution will not track the events that happened before its deployment unless AWS CloudTrail was already set up and storing data in an S3 bucket.

**Product versions**
+ AWS CDK version 2.55.1 or later
+ Python version 3.9 or later

## Architecture
<a name="automate-aws-resource-assessment-architecture"></a>

**Target technology stack**
+ Amazon Athena
+ AWS CloudTrail
+ AWS Glue
+ AWS Lambda
+ Amazon Quick Sight
+ Amazon S3

**Target architecture**

The AWS CDK code will deploy all the resources that are required to set up resource-assessment capabilities in an AWS account. The following diagram shows the process of sending CloudTrail logs to AWS Glue, Amazon Athena, and Quick Sight.

![AWS resource assessment with AWS Glue, Amazon Athena, and Amazon QuickSight in a six-step process.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a504774e-db7a-4c36-a22c-ce56d252fb58/images/8f2b549d-33a8-4cbf-86fd-33244716b668.png)

1. CloudTrail sends logs to an S3 bucket for storage.

1. An event notification invokes a Lambda function that processes the logs and generates filtered data.

1. The filtered data is stored in another S3 bucket.

1. An AWS Glue crawler is set up on the filtered data that is in the S3 bucket to create a schema in the AWS Glue Data Catalog table.

1. The filtered data is ready to be queried by Amazon Athena.

1. The queried data is accessed by Quick Sight for visualization.

**Automation and scale**
+ This solution can be scaled from one AWS account to multiple AWS accounts if there is an organization-wide CloudTrail trail in AWS Organizations. By deploying CloudTrail at the organizational level, you can also use this solution to fetch resource-auditing details for all the required resources.
+ This pattern uses AWS serverless resources to deploy the solution.

## Tools
<a name="automate-aws-resource-assessment-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams. This pattern uses an AWS Glue crawler and an AWS Glue Data Catalog table.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The code for this pattern is available in the GitHub [infrastructure-assessment-iac-automation](https://github.com/aws-samples/infrastructure-assessment-iac-automation) repository.

The code repository contains the following files and folders:
+ `lib` folder – The AWS CDK construct Python files used to create AWS resources
+ `src/lambda_code` – The Python code that is run in the Lambda function
+ `requirements.txt` – The list of all Python dependencies that must be installed
+ `cdk.json` – The input file to provide values required to spin up resources

## Best practices
<a name="automate-aws-resource-assessment-best-practices"></a>

Set up monitoring and alerting for the Lambda function. For more information, see [Monitoring and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html). For general best practices when working with Lambda functions, see the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

## Epics
<a name="automate-aws-resource-assessment-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo on your local machine. | To clone the repository, run the command `git clone https://github.com/aws-samples/infrastructure-assessment-iac-automation.git`. | AWS DevOps, DevOps engineer |
| Set up the Python virtual environment and install required dependencies. | To set up the Python virtual environment, run the following commands.<pre>cd infrastructure-assessment-iac-automation<br />python3 -m venv .venv<br />source .venv/bin/activate</pre><br />To set up the required dependencies, run the command `pip install -r requirements.txt`. | AWS DevOps, DevOps engineer |
| Set up the AWS CDK environment and synthesize the AWS CDK code. | 1. To set up the AWS CDK environment in your AWS account, run the command `cdk bootstrap aws://ACCOUNT-NUMBER/REGION`.<br />2. To convert the code to an AWS CloudFormation stack configuration, run the command `cdk synth`. | AWS DevOps, DevOps engineer |

### Set up AWS credentials on your local machine
<a name="set-up-aws-credentials-on-your-local-machine"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export variables for the account and Region where the stack will be deployed. | To provide AWS credentials for AWS CDK by using environment variables, run the following commands.<pre>export CDK_DEFAULT_ACCOUNT=<12 Digit AWS Account Number><br />export CDK_DEFAULT_REGION=<region></pre> | AWS DevOps, DevOps engineer |
| Set up the AWS CLI profile. | To set up the AWS CLI profile for the account, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/keys-profiles-credentials.html). | AWS DevOps, DevOps engineer |

### Configure and deploy the resource-assessment tool
<a name="configure-and-deploy-the-resource-assessment-tool"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy resources in the account. | To deploy resources in the AWS account by using AWS CDK, do the following:1. In the root of the cloned repository, in the `cdk.json` file, provide inputs for the following parameters:`s3_context``ct_context``kms_context``lambda_context``glue_context``qs_context`<br />These values define resource configurations and nomenclature. Default values are set and can be changed if required.To avoid an error saying that the S3 bucket already exists, make sure to provide unique names for `s3_context` in the `ct `and `output` sections.<br />2. To deploy resources, run the command `cdk deploy`.<br />The `cdk deploy` command creates a CloudTrail resource to log events and save the log file in the input S3 bucket. The trail's log files will be processed by the Lambda function. The filtered results are stored in the output S3 bucket and are ready to be consumed by Amazon Athena and Amazon Quick Sight. | AWS DevOps |
| Run the AWS Glue crawler and create the Data Catalog table. | An [AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) is used to keep the data schema dynamic. The solution creates and updates partitions in the [AWS Glue Data Catalog table](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html) by running the crawler periodically as defined by the AWS Glue crawler scheduler. After the data is available in the output S3 bucket, use the following steps to run the AWS Glue crawler and create the Data Catalog table schema for testing:1. Sign in to the AWS Management Console and navigate to the AWS Glue console.<br />2. In the navigation pane, under **Data Catalog**, choose **Crawlers**.<br />3. Select the `iac-tool-qa-resource-iac-json-crawler` crawler.<br />4. Run the crawler.<br />5. After the crawler runs successfully, it creates an AWS Glue Data Catalog table. Quick Sight will use the table to visualize the data.The AWS CDK code configures the AWS Glue crawler to run at a particular time, but you can also run it on demand. | AWS DevOps, DevOps engineer |
| Deploy the Quick Sight construct. | 1. To deploy the Quick Sight construct, uncomment the code between `#QuickSight setup - start` and `#QuickSight setup – ends` in `resource_iac_tool_stack.py`.<br />2. After you uncomment, run the `cdk deploy` command to create `QuickSight DataSource` and `QuickSight DataSet` in the Quick Sight account. | AWS DevOps, DevOps engineer |
| Create the Quick Sight dashboard. | To create the example Quick Sight dashboard and analysis, do the following:1. Navigate to the Quick Sight console and select the AWS Region where resources are deployed.<br />2. In the navigation pane, choose **Datasets**, and validate that a dataset named `ct-operations-iac-ds` has been created in the Quick Sight dataset.<br />If you don't see the dataset, redeploy the Quick Sight construct.<br />3. Select the `ct-operations-iac-ds` dataset, and choose **USE IN ANALYSIS**.<br />4. Select the default sheet.<br />5. Select the respective columns from the field list on the left side.<br />6. After selecting the required columns, select the appropriate visual type to view the data.<br />For more information, see [Starting an analysis in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/creating-an-analysis.html) and [Visual types in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visual-types.html). | AWS DevOps, DevOps engineer |

### Clean up all AWS resources in the solution
<a name="clean-up-all-aws-resources-in-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the AWS resources. | 1. To remove AWS resources deployed by the solution, run the command `cdk destroy`.<br />2. Delete all objects from the two S3 buckets, and then remove the buckets.<br />For more information, see [Deleting a bucket.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) | AWS DevOps, DevOps engineer |

### Set up additional features on top of the AWS resource-assessment tool automation
<a name="set-up-additional-features-on-top-of-the-aws-resource-assessment-tool-automation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Monitor and clean up manually created resources. | (Optional) If your organization has compliance requirements to create resources using IaC tools, you can achieve compliance by using AWS resource-assessment tool automation to fetch manually provisioned resources. You can also use the tool to import the resources to an IaC tool or to re-create them. To monitor manually provisioned resources, perform the following high-level tasks:1. Deploy AWS resource-assessment tool automation.<br />2. Set up a Lambda function to query the Athena tables on a daily basis, find the relevant data about manually provisioned resources, and export it to a comma-separated values (CSV) file.<br />3. After the Lambda function runs, a notification with the required data can be sent to respective stakeholders.<br />4. For longer retention, the .csv file can be stored in the S3 bucket.<br />5. Based on the information in the .csv file, delete the manually created resources or import them to an existing IaC solution. | AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="automate-aws-resource-assessment-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS CDK returns errors. | For help with AWS CDK issues, see [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html). |

## Related resources
<a name="automate-aws-resource-assessment-resources"></a>
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ [Get started with AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
+ [Working with AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
+ [Creating a CloudTrail log trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [Get Started with Amazon Quick Sight](https://aws.amazon.com/quicksight/getting-started/)

## Additional information
<a name="automate-aws-resource-assessment-additional"></a>

**Multiple accounts**

To set up the AWS CLI credential for multiple accounts, use AWS profiles. For more information, see the *Configure multiple profiles* section in [Set up the AWS CLI](https://aws.amazon.com/getting-started/guides/setup-environment/module-three/).

**AWS CDK commands**

When working with AWS CDK, keep in mind the following useful commands:
+ Lists all stacks in the app

  ```
  cdk ls
  ```
+ Emits the synthesized AWS CloudFormation template

  ```
  cdk synth
  ```
+ Deploys the stack to your default AWS account and Region

  ```
  cdk deploy
  ```
+ Compares the deployed stack with the current state

  ```
  cdk diff
  ```
+ Opens the AWS CDK documentation

  ```
  cdk docs
  ```

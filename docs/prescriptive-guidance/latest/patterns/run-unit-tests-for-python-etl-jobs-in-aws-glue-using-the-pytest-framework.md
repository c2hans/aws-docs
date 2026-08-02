---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html
---

# Run unit tests for Python ETL jobs in AWS Glue using the pytest framework
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework"></a>

*Praveen Kumar Jeyarajan and Vaidy Sankaran, Amazon Web Services*

## Summary
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-summary"></a>

You can run unit tests for Python extract, transform, and load (ETL) jobs for AWS Glue in a [local development environment](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html), but replicating those tests in a DevOps pipeline can be difficult and time consuming. Unit testing can be especially challenging when you’re modernizing mainframe ETL process on AWS technology stacks. This pattern shows you how to simplify unit testing, while keeping existing functionality intact, avoiding disruptions to key application functionality when you release new features, and maintaining high-quality software. You can use the steps and code samples in this pattern to run unit tests for Python ETL jobs in AWS Glue by using the pytest framework in AWS CodePipeline. You can also use this pattern to test and deploy multiple AWS Glue jobs.

## Prerequisites and limitations
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon Elastic Container Registry (Amazon ECR) image URI for your AWS Glue library, downloaded from the [Amazon ECR Public Gallery](https://gallery.ecr.aws/glue/aws-glue-libs)
+ Bash terminal (on any operating system) with a profile for the target AWS account and AWS Region
+ [Python 3.10](https://www.python.org/downloads/) or later
+ [Pytest](https://github.com/pytest-dev/pytest)
+ [Moto](https://github.com/getmoto/moto) Python library for testing AWS services

## Architecture
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-architecture"></a>

The following diagram describes how to incorporate unit testing for AWS Glue ETL processes that are based on Python into a typical enterprise-scale AWS DevOps pipeline.

![Unit testing for AWS Glue ETL processes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82781ca8-4da0-4df0-bf23-32992fece231/images/6286dafc-f1e0-4967-beed-4dedc6047c10.png)

The diagram shows the following workflow:

1. In the source stage, AWS CodePipeline uses a versioned Amazon Simple Storage Service (Amazon S3) bucket to store and manage source code assets. These assets include a sample Python ETL job (`sample.py`), a unit test file (`test_sample.py`), and an AWS CloudFormation template. Then, CodePipeline transfers the most recent code from the main branch to the AWS CodeBuild project for further processing.

1. In the build and publish stage, the most recent code from the previous source stage is unit tested with the help of an AWS Glue public Amazon ECR image. Then, the test report is published to CodeBuild report groups. The container image in the public Amazon ECR repository for AWS Glue libraries includes all the binaries required to run and unit test [PySpark-based](https://spark.apache.org/docs/latest/api/python/) ETL tasks in AWS Glue locally. The public container repository has three image tags, one for each version supported by AWS Glue. For demonstration purposes, this pattern uses the `glue_libs_4.0.0_image_01` image tag. To use this container image as a runtime image in CodeBuild, copy the image URI that corresponds to the image tag that you intend to use, and then update the `pipeline.yml` file in the GitHub repository for the `TestBuild` resource.

1. In the deploy stage, the CodeBuild project is launched and it publishes the code to an Amazon S3 bucket if all the tests pass.

1. The user deploys the AWS Glue task by using the CloudFormation template in the `deploy` folder.

## Tools
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed ETL service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is an object storage service offering industry-leading scalability, data availability, security, and performance.

**Other tools**
+ [Python](https://www.python.org/) is a high-level, interpreted general purpose programming language.
+ [Moto](https://github.com/getmoto/moto) is a Python library for testing AWS services.
+ [Pytest](https://github.com/pytest-dev/pytest) is a framework for writing small unit tests that scale to support complex functional testing for applications and libraries.
+ [Python ETL library](https://github.com/awslabs/aws-glue-libs) for AWS Glue is a repository for Python libraries that are used in the local development of PySpark batch jobs for AWS Glue.

**Code repository**

The code for this pattern is available in the GitHub [aws-glue-jobs-unit-testing](https://github.com/aws-samples/aws-glue-jobs-unit-testing) repository. The repository includes the following resources:
+ A sample Python-based AWS Glue job in the `src` folder
+ Associated unit test cases (built using the pytest framework) in the `tests` folder
+ A CloudFormation template (written in YAML) in the `deploy` folder

## Best practices
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-best-practices"></a>

**Security for CodePipeline resources**

It’s a best practice to use encryption and authentication for the source repositories that connect to your pipelines in CodePipeline. For more information, see [Security best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html) in the CodePipeline documentation.

**Monitoring and logging for CodePipeline resources**

It’s a best practice to use AWS logging features to determine what actions users take in your account and what resources they use. The log files show the following:
+ Time and date of actions
+ Source IP address of actions
+ Which actions failed due to inadequate permissions

Logging features are available in AWS CloudTrail and Amazon CloudWatch Events. You can use CloudTrail to log AWS API calls and related events made by or on behalf of your AWS account. For more information, see [Logging CodePipeline API calls with AWS CloudTrail](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring-cloudtrail-logs.html) in the CodePipeline documentation.

You can use CloudWatch Events to monitor your AWS Cloud resources and applications running on AWS. You can also create alerts in CloudWatch Events. For more information, see [Monitoring CodePipeline events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html) in the CodePipeline documentation.

## Epics
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-epics"></a>

### Deploy the source code
<a name="deploy-the-source-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the code archive for deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html) | DevOps engineer |
| Create the CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html)The stack creates a CodePipeline view using Amazon S3 as the source. In the steps above, the pipeline is **aws-glue-unit-test-pipeline**. | AWS DevOps, DevOps engineer |

### Run the unit tests
<a name="run-the-unit-tests"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the unit tests in the pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html) | AWS DevOps, DevOps engineer |

### Clean up all AWS resources
<a name="clean-up-all-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the resources in your environment. | To avoid additional infrastructure costs, make sure that you delete the stack after experimenting with the examples provided in this pattern.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html) | AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The CodePipeline service role cannot access the Amazon S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework.html) |
| CodePipeline returns an error that the Amazon S3 bucket is not versioned. | CodePipeline requires that the source Amazon S3 bucket be versioned. Enable versioning on your Amazon S3 bucket. For instructions, see [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html). |

## Related resources
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-resources"></a>
+ [AWS Glue](https://aws.amazon.com/glue/)
+ [Developing and testing AWS Glue jobs locally](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html)
+ [AWS CloudFormation for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/populate-with-cloudformation-templates.html)

## Additional information
<a name="run-unit-tests-for-python-etl-jobs-in-aws-glue-using-the-pytest-framework-additional"></a>

Additionally, you can deploy the AWS CloudFormation templates by using the AWS Command Line Interface (AWS CLI). For more information, see [Quickly deploying templates with transforms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-deploy.html) in the CloudFormation documentation.

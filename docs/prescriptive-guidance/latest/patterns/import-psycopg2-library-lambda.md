---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/import-psycopg2-library-lambda.html
---

# Import the psycopg2 library to AWS Lambda to interact with your PostgreSQL database
<a name="import-psycopg2-library-lambda"></a>

*Louis Hourcade, Amazon Web Services*

## Summary
<a name="import-psycopg2-library-lambda-summary"></a>

[Psycopg](https://www.psycopg.org/docs/) is a PostgresSQL database adapter for Python. Developers use the `psycopg2` library to write Python applications that interact with PostgreSQL databases.

On Amazon Web Services (AWS), developers also use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to run code for applications or backend services. Lambda is a serverless, event-driven compute service runs code without the need to provision or manage servers.

By default, when you create a new function that uses a [Python runtime that’s supported by Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html), the Lambda runtime environment is created from a [base image for Lambda](https://github.com/aws/aws-lambda-base-images) provided by AWS. Libraries, such as `pandas` or `psycopg2`, aren't included in the base image. To use a library, you need to bundle it in a custom package and attach it to Lambda.

There are multiple ways to bundle and attach a library, including the following:
+ Deploy your Lambda function from a [.zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html).
+ Deploy your Lambda function from a custom container image.
+ Create a [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html#lambda-layer-versions), and attach it to your Lambda function.

This pattern demonstrates the first two options.

With a .zip deployment package, adding the `pandas` library to your Lambda function is relatively straightforward. Create a folder on your Linux machine, add the Lambda script together with the `pandas` library and the library's dependencies to the folder, zip the folder, and provide it as a source for your Lambda function.

Although using a .zip deployment package is a common practice, that approach doesn't work for the `psycopg2` library. This pattern first shows the error that you get if you use a .zip deployment package to add the `psycopg2` library to your Lambda function. The pattern then shows how to deploy Lambda from a Dockerfile and edit the Lambda image to make the `psycopg2` library work.

For information about the three resources that the pattern deploys, see the [Additional information](#import-psycopg2-library-lambda-additional) section.

## Prerequisites and limitations
<a name="import-psycopg2-library-lambda-prereqs"></a>

**Prerequisites **
+ An active AWS account with sufficient permissions to deploy the AWS resources used by this pattern
+ AWS Cloud Development Kit (AWS CDK) installed globally by running `npm install -g aws-cdk`
+ A Git client
+ Python
+ Docker

**Limitations **
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ Python runtime version that’s [supported by Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ Psycopg2 version 2.9.3
+ Pandas version 1.5.2

## Architecture
<a name="import-psycopg2-library-lambda-architecture"></a>

**Solution overview **

To illustrate the challenges that you might face when using the `psycopg2` library in Lambda, the pattern deploys two Lambda functions:
+ One Lambda function with the Python runtime created from a .zip file. The `psycopg2` and `pandas` libraries are installed in this .zip deployment package by using [pip](https://pypi.org/project/pip/).
+ One Lambda function with the Python runtime created from a Dockerfile. The Dockerfile installs the `psycopg2` and `pandas` libraries into the Lambda container image.

The first Lambda function installs the `pandas` library and its dependencies in a .zip file, and Lambda can use that library.

The second Lambda function demonstrates that by building a container image for your Lambda function, you can run the  `pandas` and `psycopg2` libraries in Lambda.

## Tools
<a name="import-psycopg2-library-lambda-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [pandas](https://pandas.pydata.org/) is a Python-based open source tool for data analysis and manipulation.
+ [Psycopg](https://www.psycopg.org/docs/) is a PostgreSQL database adapter for the Python language that is designed for multithreaded applications. This pattern uses Psycopg 2.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the [import-psycopg2-in-lambda-to-interact-with-postgres-database](https://github.com/aws-samples/import-psycopg2-in-lambda-to-interact-with-postgres-database) repository on GitHub.

## Best practices
<a name="import-psycopg2-library-lambda-best-practices"></a>

This pattern provides you with a working example of using AWS CDK to create a Lambda function from a Dockerfile. If you reuse this code in your application, make sure that the deployed resources meet all security requirements. Use tools such as [Checkov](https://www.checkov.io/), which scans cloud infrastructure configurations to find misconfiguration before the infrastructure is deployed.

## Epics
<a name="import-psycopg2-library-lambda-epics"></a>

### Clone the repository and configure the deployment
<a name="clone-the-repository-and-configure-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the GitHub repository on your local machine, run the following commands:<pre>git clone https://github.com/aws-samples/import-psycopg2-in-lambda-to-interact-with-postgres-database.git<br />cd AWS-lambda-psycopg2</pre> | General AWS |
| Configure your deployment. | Edit the `app.py` file with information about your AWS account:<pre>aws_acccount = "AWS_ACCOUNT_ID"<br />region = "AWS_REGION"<br /># Select the CPU architecture you are using to build the image (ARM or X86)<br />architecture = "ARM"</pre> | General AWS |

### Bootstrap your AWS account and deploy the application
<a name="bootstrap-your-aws-account-and-deploy-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bootstrap your AWS account. | If you haven't already [bootstrapped your AWS environment](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html), run the following commands with the AWS credentials of your AWS account:<pre>cdk bootstrap aws://<tooling-account-id>/<aws-region></pre> | General AWS |
| Deploy the code. | To deploy the AWS CDK application, run the following command:<pre>cdk deploy AWSLambdaPyscopg2</pre> | General AWS |

### Test the Lambda functions from the AWS Management Console
<a name="test-the-lambda-functions-from-the-aws-management-console"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the Lambda function created from the .zip file. | To test the Lambda function that was created from the .zip file, do the following:1. Sign in to the console, and open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).<br />2. Select the `lambda-from-zip` Lambda function.<br />3. Create a test event to invoke the function.<br />4. When invoked, the function should raise an error that includes the following message:<pre>"errorMessage": Unable to import module 'lambda_code': libpq.so.5: cannot open shared object,<br />"stackTrace": []<br />"errorType": Runtime.ImportModuleError",</pre><br />5. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/). The CloudWatch logs show that the `pandas` library has been imported successfully but that the `psycopg2` library import has failed.<br />Because Lambda doesn't find the required PostgreSQL libraries in the default image, it can't use the `psycopg2` library. | General AWS |
| Test the Lambda function created from the Dockerfile. | To use the `psycopg2` library within your Lambda function, you must edit the Lambda Amazon Machine Image (AMI).<br />To test the Lambda function that was created from the Dockerfile, do the following:1. Sign in to the console, and open the Lambda console.<br />2. Select the `lambda-from-docker` Lambda function.<br />3. Create a test event to invoke the function.<br />4. When invoked, the function should run successfully.<br />The following code shows the Dockerfile that the AWS CDK template creates:<pre># Start from lambda Python3.13 image<br />FROM public.ecr.aws/lambda/python:3.13<br /><br /># Copy the lambda code, together with its requirements<br />COPY lambda/requirements.txt ${LAMBDA_TASK_ROOT}<br />COPY lambda/lambda_code.py ${LAMBDA_TASK_ROOT}<br /><br /># Install postgresql-devel in your image<br />RUN yum install -y gcc postgresql-devel<br /><br /># install the requirements for the Lambda code<br />RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"<br /><br /># Command can be overwritten by providing a different command in the template directly.<br />CMD ["lambda_code.handler"]</pre><br />The Dockerfile takes the AWS provided Lambda image for the Python runtime and installs [postgresql-devel](https://yum-info.contradodigital.com/view-package/updates/postgresql-devel/), which contains the libraries needed to compile applications that directly interact with the PostgreSQL management server. The Dockerfile also installs the `pandas` and `psycopg2` libraries, which are indicated in the `requirements.txt` file. | General AWS |

## Related resources
<a name="import-psycopg2-library-lambda-resources"></a>
+ [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
+ [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

## Additional information
<a name="import-psycopg2-library-lambda-additional"></a>

In this pattern, the AWS CDK template provides an AWS stack with three resources:
+ An [AWS Identity and Access Management (IAM) role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for the Lambda functions.
+ A Lambda function with a Python runtime. The function is deployed from the `Constructs/lambda/lambda_deploy.zip` deployment package.
+ A Lambda function with a Python runtime. The function is deployed from the Dockerfile under the `Constructs` folder

The script for both Lambda functions checks whether the `pandas` and `psycopg2` libraries are successfully imported:

```
import pandas
print("pandas successfully imported")

import psycopg2
print("psycopg2 successfully imported")

def handler(event, context):
    """Function that checks whether psycopg2  and pandas are successfully imported or not"""
    return {"Status": "psycopg2 and pandas successfully imported"}
```

The `lambda_deploy.zip` deployment package is built with the `Constructs/lambda/build.sh` bash script. This script creates a folder, copies the Lambda script, installs the `pandas` and `psycopg2` libraries, and generates the .zip file. To generate the .zip file yourself, run this bash script and redeploy the AWS CDK stack.

The Dockerfile starts with the AWS provided base image for Lambda with a Python runtime. The Dockerfile installs the `pandas` and `psycopg2` libraries on top of the default image.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

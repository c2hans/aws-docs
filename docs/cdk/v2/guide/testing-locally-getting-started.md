---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/testing-locally-getting-started.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Getting started with locally testing
<a name="testing-locally-getting-started"></a>

This topic describes what you need to use the AWS SAM CLI with AWS CDK applications, and it provides instructions for building and locally testing a simple AWS CDK application.

## Prerequisites
<a name="testing-locally-getting-started-prerequisites"></a>

To test locally, you must install the AWS SAM CLI. see [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/getting_started.html) for installation instructions.

## Creating and locally testing an AWS CDK application
<a name="testing-locally-getting-started-tutorial"></a>

To locally test an AWS CDK application using the AWS SAM CLI, you must have an AWS CDK application that contains a Lambda function. Use the following steps to create a basic AWS CDK application with a Lambda function. For more information, see [Creating a serverless application using the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/serverless_example.html) in the * AWS Cloud Development Kit (AWS CDK) Developer Guide*.<a name="testing-locally-getting-started-tutorial-init"></a>

 **Step 1: Create an AWS CDK application**
For this tutorial, initialize an AWS CDK application that uses TypeScript.
Command to run:

```
$ mkdir cdk-sam-example
$ cd cdk-sam-example
$ cdk init app --language typescript
```<a name="testing-locally-getting-started-tutorial-lambda"></a>

 **Step 2: Add a Lambda function to your application**
Replace the code in `lib/cdk-sam-example-stack.ts` with the following:

```
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class CdkSamExampleStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new lambda.Function(this, 'MyFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'app.lambda_handler',
      code: lambda.Code.fromAsset('./my_function'),
    });
  }
}
```<a name="testing-locally-getting-started-tutorial-code"></a>

 **Step 3: Add your Lambda function code**
Create a directory named `my_function`. In that directory, create a file named `app.py`.
Command to run:

**Example**

```
$ mkdir my_function
$ cd my_function
$ touch app.py
```

```
$ mkdir my_function
$ cd my_function
$ type nul > app.py
```

```
$ mkdir my_function
$ cd my_function
$ New-Item -Path "app.py”
```
Add the following code to `app.py`:

```
def lambda_handler(event, context):
    return "Hello from SAM and the CDK!"
```<a name="testing-locally-getting-started-tutorial-function"></a>

 **Step 4: Test your Lambda function**
You can use the AWS SAM CLI to locally invoke a Lambda function that you define in an AWS CDK application. To do this, you need the function construct identifier and the path to your synthesized AWS CloudFormation template.
Run the following command to go back to the `lib` directory:

```
$  cd ..
```
 **Command to run:**

```
$  cdk synth --no-staging
```

```
$  sam local invoke MyFunction --no-event -t ./cdk.out/CdkSamExampleStack.template.json
```
 **Example output:**

```
Invoking app.lambda_handler (python3.9)

START RequestId: 5434c093-7182-4012-9b06-635011cac4f2 Version: $LATEST
"Hello from SAM and the CDK!"
END RequestId: 5434c093-7182-4012-9b06-635011cac4f2
REPORT RequestId: 5434c093-7182-4012-9b06-635011cac4f2	Init Duration: 0.32 ms	Duration: 177.47 ms	Billed Duration: 178 ms	Memory Size: 128 MB	Max Memory Used: 128 MB
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

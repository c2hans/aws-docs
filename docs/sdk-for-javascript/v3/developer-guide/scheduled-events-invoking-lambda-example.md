---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/scheduled-events-invoking-lambda-example.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Creating scheduled events to execute AWS Lambda functions
<a name="scheduled-events-invoking-lambda-example"></a>

You can create a scheduled event that invokes an AWS Lambda function by using an Amazon CloudWatch Event. You can configure a CloudWatch Event to use a cron expression to schedule when a Lambda function is invoked. For example, you can schedule a CloudWatch Event to invoke an Lambda function every weekday.

AWS Lambda is a compute service that enables you to run code without provisioning or managing servers. You can create Lambda functions in various programming languages. For more information about AWS Lambda, see [What is AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

In this tutorial, you create a Lambda function by using the Lambda JavaScript runtime API. This example invokes different AWS services to perform a specific use case. For example, assume that an organization sends a mobile text message to its employees that congratulates them at the one year anniversary date, as shown in this illustration.

![DynamoDB table](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/apigateway_example/picPhone.png)

The tutorial should take about 20 minutes to complete.

This tutorial shows you how to use JavaScript logic to create a solution that performs this use case. For example, you'll learn how to read a database to determine which employees have reached the one year anniversary date, how to process the data, and send out a text message all by using a Lambda function. Then you’ll learn how to use a cron expression to invoke the Lambda function every weekday.

This AWS tutorial uses an Amazon DynamoDB table named Employee that contains these fields.
+ **id** - the primary key for the table.
+ **firstName** - employee’s first name.
+ **phone** - employee’s phone number.
+ **startDate** - employee’s start date.

![DynamoDB table](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/apigateway_example/pic00.png)

**Important**
Cost to complete: The AWS services included in this document are included in the AWS Free Tier. However, be sure to terminate all of the resources after you have completed this tutorial to ensure that you are not charged.

**To build the app:**

1. [Complete prerequisites ](#scheduled-events-invoking-lambda-provision-resources)

1. [Create the AWS resources ](#scheduled-events-invoking-lambda-provision-resources)

1. [Prepare the browser script ](#scheduled-events-invoking-lambda-browser-script)

1. [Create and upload Lambda function ](#scheduled-events-invoking-lambda-browser-script)

1. [Deploy the Lambda function ](#scheduled-events-invoking-lambda-deploy-function)

1. [Run the app](#scheduled-events-invoking-lambda-run)

1. [Delete the resources](#scheduled-events-invoking-lambda-destroy)

## Prerequisite tasks
<a name="scheduled-events-invoking-lambda-prerequisites"></a>

To set up and run this example, you must first complete these tasks:
+ Set up the project environment to run these Node.js TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on[ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lex-bot/README.md).
+ Create a shared configurations file with your user credentials. For more information about providing a shared credentials file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

## Create the AWS resources
<a name="scheduled-events-invoking-lambda-provision-resources"></a>

This tutorial requires the following resources.
+ An Amazon DynamoDB table named **Employee** with a key named **Id** and the fields shown in the previous illustration. Make sure you enter the correct data, including a valid mobile phone that you want to test this use case with. For more information, see [Create a Table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html).
+ An IAM role with attached permissions to execute Lambda functions.
+ An Amazon S3 bucket to host Lambda function.

You can create these resources manually, but we recommend provisioning these resources using the CloudFormation as described in this tutorial.

### Create the AWS resources using CloudFormation
<a name="scheduled-events-invoking-lambda-resources-cli"></a>

CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. For more information about CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

To create the CloudFormation stack using the AWS CLI:

1. Install and configure the AWS CLI following the instructions in the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

1. Create a file named `setup.yaml` in the root directory of your project folder, and copy the content [ here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lambda-scheduled-events/setup.yaml) into it.
**Note**
The CloudFormation template was generated using the AWS CDK available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/resources/cdk/lambda_using_scheduled_events). For more information about the AWS CDK, see the [AWS Cloud Development Kit (AWS CDK) Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/).

1. Run the following command from the command line, replacing {{STACK\_NAME}} with a unique name for the stack.
**Important**
The stack name must be unique within an AWS Region and AWS account. You can specify up to 128 characters, and numbers and hyphens are allowed.

   ```
   aws cloudformation create-stack --stack-name STACK_NAME --template-body file://setup.yaml --capabilities CAPABILITY_IAM
   ```

   For more information on the `create-stack` command parameters, see the [AWS CLI Command Reference guide](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html), and the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html).

   View a list of the resources in the console by opening the stack on the CloudFormation dashboard, and choosing the **Resources** tab. You require these for the tutorial.

1. When the stack is created, use the AWS SDK for JavaScript to populate the DynamoDB table, as described in [Populate the DynamoDB table](#scheduled-events-invoking-lambda-resources-create-table).

### Populate the DynamoDB table
<a name="scheduled-events-invoking-lambda-resources-create-table"></a>

To populate the table, first create a directory named `libs`, and in it create a file named `dynamoClient.js`, and paste the content below into it.

```
const { DynamoDBClient } = require( "@aws-sdk/client-dynamodb" );
// Set the AWS Region.
const REGION = "REGION"; // e.g. "us-east-1"
// Create an Amazon DynamoDB service client object.
const dynamoClient = new DynamoDBClient({region:REGION});
module.exports = { dynamoClient };
```

 This code is available [ here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lambda-scheduled-events/src/libs/dynamoClient.js).

Next, create a file named `populate-table.js` in the root directory of your project folder, and copy the content [ here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lambda-api-gateway/src/helper-functions/populate-table.js) into it. For one of the items, replace the value for the `phone` property with a valid mobile phone number in the E.164 format, and the value for the `startDate` with today's date.

Run the following command from the command line.

```
node populate-table.js
```

```
const {
BatchWriteItemCommand } = require( "aws-sdk/client-dynamodb" );
const {dynamoClient} = require(  "./libs/dynamoClient" );
// Set the parameters.
const params = {
  RequestItems: {
    Employees: [
      {
        PutRequest: {
          Item: {
            id: { N: "1" },
            firstName: { S: "Bob" },
            phone: { N: "155555555555654" },
            startDate: { S: "2019-12-20" },
          },
        },
      },
      {
        PutRequest: {
          Item: {
            id: { N: "2" },
            firstName: { S: "Xing" },
            phone: { N: "155555555555653" },
            startDate: { S: "2019-12-17" },
          },
        },
      },
      {
        PutRequest: {
          Item: {
            id: { N: "55" },
            firstName: { S: "Harriette" },
            phone: { N: "155555555555652" },
            startDate: { S: "2019-12-19" },
          },
        },
      },
    ],
  },
};

export const run = async () => {
  try {
    const data = await dbclient.send(new BatchWriteItemCommand(params));
    console.log("Success", data);
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

 This code is available [ here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lambda-scheduled-events/src/helper-functions/populate-table.js).

## Creating the AWS Lambda function
<a name="scheduled-events-invoking-lambda-browser-script"></a>

### Configuring the SDK
<a name="scheduled-events-invoking-lambda-configure-sdk"></a>

First import the required AWS SDK for JavaScript (v3) modules and commands: `DynamoDBClient` and the DynamoDB `ScanCommand`, and `SNSClient` and the Amazon SNS `PublishCommand` command. Replace {{REGION}} with the AWS Region. Then calculate today's date and assign it to a parameter. Then create the parameters for the `ScanCommand`.Replace {{TABLE\_NAME}} with the name of the table you created in the [Create the AWS resources](#scheduled-events-invoking-lambda-provision-resources) section of this example.

The following code snippet shows this step. (See [Bundling the Lambda function](#scheduled-events-invoking-lambda-full) for the full example.)

```
"use strict";
// Load the required clients and commands.
const { DynamoDBClient, ScanCommand } = require("@aws-sdk/client-dynamodb");
const { SNSClient, PublishCommand } = require("@aws-sdk/client-sns");

//Set the AWS Region.
const REGION = "REGION"; //e.g. "us-east-1"

// Get today's date.
const today = new Date();
const dd = String(today.getDate()).padStart(2, "0");
const mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
const yyyy = today.getFullYear();
const date = yyyy + "-" + mm + "-" + dd;

// Set the parameters for the ScanCommand method.
const params = {
  // Specify which items in the results are returned.
  FilterExpression: "startDate = :topic",
  // Define the expression attribute value, which are substitutes for the values you want to compare.
  ExpressionAttributeValues: {
    ":topic": { S: date },
  },
  // Set the projection expression, which the the attributes that you want.
  ProjectionExpression: "firstName, phone",
  TableName: "TABLE_NAME",
};
```

### Scanning the DynamoDB table
<a name="scheduled-events-invoking-lambda-scan-table"></a>

First create an async/await function called `sendText` to publish a text message using the Amazon SNS `PublishCommand`. Then, add a `try` block pattern that scans the DynamoDB table for employees with their work anniversary today, and then calls the `sendText` function to send these employees a text message. If an error occurs the `catch` block is called.

The following code snippet shows this step. (See [Bundling the Lambda function](#scheduled-events-invoking-lambda-full) for the full example.)

```
exports.handler = async (event, context, callback) => {
  // Helper function to send message using Amazon SNS.
  async function sendText(textParams) {
    try {
      const data = await snsclient.send(new PublishCommand(textParams));
      console.log("Message sent");
    } catch (err) {
      console.log("Error, message not sent ", err);
    }
  }
  try {
    // Scan the table to check identify employees with work anniversary today.
    const data = await dbclient.send(new ScanCommand(params));
    data.Items.forEach(function (element, index, array) {
      const textParams = {
        PhoneNumber: element.phone.N,
        Message:
          "Hi " +
          element.firstName.S +
          "; congratulations on your work anniversary!",
      };
      // Send message using Amazon SNS.
      sendText(textParams);
    });
  } catch (err) {
    console.log("Error, could not scan table ", err);
  }
};
```

### Bundling the Lambda function
<a name="scheduled-events-invoking-lambda-full"></a>

This topic describes how to bundle the `mylambdafunction.js` and the required AWS SDK for JavaScript modules for this example into a bundled file called `index.js`.

1. If you haven't already, follow the [Prerequisite tasks](#scheduled-events-invoking-lambda-prerequisites) for this example to install webpack.
**Note**
For information about*webpack*, see [Bundle applications with webpack](webpack.md).

1. Run the the following in the command line to bundle the JavaScript for this example into a file called `<index.js>` :

   ```
   webpack mylamdbafunction.js --mode development --target node --devtool false --output-library-target umd -o index.js
   ```
**Important**
Notice the output is named `index.js`. This is because Lambda functions must have an `index.js` handler to work.

1. Compress the bundled output file, `index.js`, into a ZIP file named `my-lambda-function.zip`.

1. Upload `mylambdafunction.zip` to the Amazon S3 bucket you created in the [Create the AWS resources](#scheduled-events-invoking-lambda-provision-resources) topic of this tutorial.

Here is the complete browser script code for `mylambdafunction.js`.

```
"use strict";
// Load the required clients and commands.
const { DynamoDBClient, ScanCommand } = require("@aws-sdk/client-dynamodb");
const { SNSClient, PublishCommand } = require("@aws-sdk/client-sns");

//Set the AWS Region.
const REGION = "REGION"; //e.g. "us-east-1"

// Get today's date.
const today = new Date();
const dd = String(today.getDate()).padStart(2, "0");
const mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
const yyyy = today.getFullYear();
const date = yyyy + "-" + mm + "-" + dd;

// Set the parameters for the ScanCommand method.
const params = {
  // Specify which items in the results are returned.
  FilterExpression: "startDate = :topic",
  // Define the expression attribute value, which are substitutes for the values you want to compare.
  ExpressionAttributeValues: {
    ":topic": { S: date },
  },
  // Set the projection expression, which the the attributes that you want.
  ProjectionExpression: "firstName, phone",
  TableName: "TABLE_NAME",
};

// Create the client service objects.
const dbclient = new DynamoDBClient({ region: REGION });
const snsclient = new SNSClient({ region: REGION });

exports.handler = async (event, context, callback) => {
  // Helper function to send message using Amazon SNS.
  async function sendText(textParams) {
    try {
      const data = await snsclient.send(new PublishCommand(textParams));
      console.log("Message sent");
    } catch (err) {
      console.log("Error, message not sent ", err);
    }
  }
  try {
    // Scan the table to check identify employees with work anniversary today.
    const data = await dbclient.send(new ScanCommand(params));
    data.Items.forEach(function (element, index, array) {
      const textParams = {
        PhoneNumber: element.phone.N,
        Message:
          "Hi " +
          element.firstName.S +
          "; congratulations on your work anniversary!",
      };
      // Send message using Amazon SNS.
      sendText(textParams);
    });
  } catch (err) {
    console.log("Error, could not scan table ", err);
  }
};
```

## Deploy the Lambda function
<a name="scheduled-events-invoking-lambda-deploy-function"></a>

In the root of your project, create a `lambda-function-setup.js` file, and paste the content below into it.

Replace {{BUCKET\_NAME}} with the name of the Amazon S3 bucket you uploaded the ZIP version of your Lambda function to. Replace {{ZIP\_FILE\_NAME}} with the name of name the ZIP version of your Lambda function. Replace {{IAM\_ROLE\_ARN}} with the Amazon Resource Number (ARN) of the IAM role you created in the [Create the AWS resources](#scheduled-events-invoking-lambda-provision-resources) topic of this tutorial. Replace {{LAMBDA\_FUNCTION\_NAME}} with a name for the Lambda function.

```
// Load the required Lambda client and commands.
const {
   CreateFunctionCommand,
} = require("@aws-sdk/client-lambda");
const {
   lambdaClient
} = require("..libs/lambdaClient.js");

// Instantiate an Lambda client service object.
const lambda = new LambdaClient({ region: REGION });

// Set the parameters.
const params = {
  Code: {
    S3Bucket: "BUCKET_NAME", // BUCKET_NAME
    S3Key: "ZIP_FILE_NAME", // ZIP_FILE_NAME
  },
  FunctionName: "LAMBDA_FUNCTION_NAME",
  Handler: "index.handler",
  Role: "IAM_ROLE_ARN", // IAM_ROLE_ARN; e.g., arn:aws:iam::650138640062:role/v3-lambda-tutorial-lambda-role
  Runtime: "nodejs12.x",
  Description:
    "Scans a DynamoDB table of employee details and using Amazon Simple Notification Services (Amazon SNS) to " +
    "send employees an email the each anniversary of their start-date.",
};

const run = async () => {
  try {
    const data = await lambda.send(new CreateFunctionCommand(params));
    console.log("Success", data); // successful response
  } catch (err) {
    console.log("Error", err); // an error occurred
  }
};
run();
```

Enter the following at the command line to deploy the Lambda function.

```
node lambda-function-setup.js
```

This code example is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lambda-scheduled-events/src/helper-functions/lambda-function-setup.js).

## Configure CloudWatch to invoke the Lambda functions
<a name="scheduled-events-invoking-lambda-run"></a>

To configure CloudWatch to invoke the Lambda functions:

1. Open the **Functions** page on the Lambda console.

1. Choose the Lambda function.

1. Under **Designer**, choose **Add trigger**.

1. Set the trigger type to **CloudWatch Events/EventBridge**.

1. For Rule, choose **Create a new rule**.

1.  Fill in the Rule name and Rule description.

1. For rule type, select **Schedule expression**.

1. In the **Schedule expression** field, enter a cron expression. For example, **cron(0 12 ? \* MON-FRI \*)**.

1. Choose **Add**.
**Note**
For more information, see [Using Lambda with CloudWatch Events](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html).

## Delete the resources
<a name="scheduled-events-invoking-lambda-destroy"></a>

Congratulations\! You have invoked a Lambda function through Amazon CloudWatch scheduled events using the AWS SDK for JavaScript. As stated at the beginning of this tutorial, be sure to terminate all of the resources you create while going through this tutorial to ensure that you’re not charged. You can do this by deleting the CloudFormation stack you created in the [Create the AWS resources](#scheduled-events-invoking-lambda-provision-resources) topic of this tutorial, as follows:

1. Open the [CloudFormation console]( https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select the stack.

1. Choose **Delete**.

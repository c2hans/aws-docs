---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-publishing-messages.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Publishing Messages in Amazon SNS
<a name="sns-examples-publishing-messages"></a>

![JavaScript code example that applies to Node.js execution](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/nodeicon.png)

**This Node.js code example shows:**
+ How to publish messages to an Amazon SNS topic.

## The Scenario
<a name="sns-examples-publishing-messages-scenario"></a>

In this example, you use a series of Node.js modules to publish messages from Amazon SNS to topic endpoints, emails, or phone numbers. The Node.js modules use the SDK for JavaScript to send messages using this method of the `SNS` client class:
+ [`PublishCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/PublishCommand/)

## Prerequisite Tasks
<a name="sns-examples-publishing-messages-prerequisites"></a>

To set up and run this example, you must first complete these tasks:
+ Set up the project environment to run these Node TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on[ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/README.md).
+ Create a shared configurations file with your user credentials. For more information about providing a shared credentials file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
These examples demonstrate how to import/export client service objects and command using ECMAScript6 (ES6).
This requires Node.js version 13.x or higher. To download and install the latest version of Node.js, see [Node.js downloads.](https://nodejs.org/en/download).
If you prefer to use CommonJS syntax, see [JavaScript ES6/CommonJS syntax](sdk-example-javascript-syntax.md).

## Publishing a Message to an SNS Topic
<a name="sns-examples-publishing-text-messages"></a>

In this example, use a Node.js module to publish a message to an Amazon SNS topic.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

 Create a Node.js module with the file name `publish-topic.js`. Configure the SDK as previously shown.

Create an object containing the parameters for publishing a message, including the message text and the Amazon Resource Name (ARN) of the Amazon SNStopic. For details on available SMS attributes, see [SetSMSAttributes](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SNS.html#setSMSAttributes-property).

Pass the parameters to the `PublishCommand` method of the `SNS` client class. create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**
Replace {{MESSAGE\_TEXT}} with the message text, and {{TOPIC\_ARN}} with the ARN of the SNS topic.

```
import { PublishCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string | Record<string, any>} message - The message to send. Can be a plain string or an object
 *                                                 if you are using the `json` `MessageStructure`.
 * @param {string} topicArn - The ARN of the topic to which you would like to publish.
 */
export const publish = async (
  message = "Hello from SNS!",
  topicArn = "TOPIC_ARN",
) => {
  const response = await snsClient.send(
    new PublishCommand({
      Message: message,
      TopicArn: topicArn,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: 'e7f77526-e295-5325-9ee4-281a43ad1f05',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   MessageId: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node publish-topic.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/publish-topic.js).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

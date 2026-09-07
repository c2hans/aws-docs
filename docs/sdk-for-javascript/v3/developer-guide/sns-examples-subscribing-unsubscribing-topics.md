---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-subscribing-unsubscribing-topics.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Managing Subscriptions in Amazon SNS
<a name="sns-examples-subscribing-unsubscribing-topics"></a>

![JavaScript code example that applies to Node.js execution](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/nodeicon.png)

**This Node.js code example shows:**
+ How to list all subscriptions to an Amazon SNS topic.
+ How to subscribe an email address, an application endpoint, or an AWS Lambda function to an Amazon SNS topic.
+ How to unsubscribe from Amazon SNS topics.

## The Scenario
<a name="sns-examples-subscribing-unsubscribing-topics-scenario"></a>

In this example, you use a series of Node.js modules to publish notification messages to Amazon SNS topics. The Node.js modules use the SDK for JavaScript to manage topics using these methods of the `SNS` client class:
+ [`ListSubscriptionsByTopicCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/ListSubscriptionsByTopicCommand/)
+ [`SubscribeCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/SubscribeCommand/)
+ [`ConfirmSubscriptionCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/ConfirmSubscriptionCommand/)
+ [`UnsubscribeCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/UnsubscribeCommand/)

## Prerequisite Tasks
<a name="sns-examples-subscribing-unsubscribing-topics-prerequisites"></a>

To set up and run this example, you must first complete these tasks:
+ Set up the project environment to run these Node TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on[ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/README.md).
+ Create a shared configurations file with your user credentials. For more information about providing a shared credentials file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
These examples demonstrate how to import/export client service objects and command using ECMAScript6 (ES6).
This requires Node.js version 13.x or higher. To download and install the latest version of Node.js, see [Node.js downloads.](https://nodejs.org/en/download).
If you prefer to use CommonJS syntax, see [JavaScript ES6/CommonJS syntax](sdk-example-javascript-syntax.md).

## Listing Subscriptions to a Topic
<a name="sns-examples-list-subscriptions-email"></a>

In this example, use a Node.js module to list all subscriptions to an Amazon SNS topic.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

 Create a Node.js module with the file name `list-subscriptions-by-topic.js`. Configure the SDK as previously shown.

Create an object containing the `TopicArn` parameter for the topic whose subscriptions you want to list. Pass the parameters to the `ListSubscriptionsByTopicCommand` method of the `SNS` client class. To call the `ListSubscriptionsByTopicCommand` method, create an asynchronous function invoking an Amazon SNS client service object, and passing the parameters object.

**Note**
Replace {{TOPIC\_ARN}} with the Amazon Resource Name (ARN) for the topic whose subscriptions you want to list .

```
import { ListSubscriptionsByTopicCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicArn - The ARN of the topic for which you wish to list subscriptions.
 */
export const listSubscriptionsByTopic = async (topicArn = "TOPIC_ARN") => {
  const response = await snsClient.send(
    new ListSubscriptionsByTopicCommand({ TopicArn: topicArn }),
  );

  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '0934fedf-0c4b-572e-9ed2-a3e38fadb0c8',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   Subscriptions: [
  //     {
  //       SubscriptionArn: 'PendingConfirmation',
  //       Owner: '901487484989',
  //       Protocol: 'email',
  //       Endpoint: 'corepyle@amazon.com',
  //       TopicArn: 'arn:aws:sns:us-east-1:901487484989:mytopic'
  //     }
  //   ]
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node list-subscriptions-by-topic.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/list-subscriptions-by-topic.js).

## Subscribing an Email Address to a Topic
<a name="sns-examples-subscribing-email"></a>

In this example, use a Node.js module to subscribe an email address so that it receives SMTP email messages from an Amazon SNS topic.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `subscribe-email.js`. Configure the SDK as previously shown.

Create an object containing the `Protocol` parameter to specify the `email` protocol, the `TopicArn` for the topic to subscribe to, and an email address as the message `Endpoint`. Pass the parameters to the `SubscribeCommand` method of the `SNS` client class. You can use the `subscribe` method to subscribe several different endpoints to an Amazon SNS topic, depending on the values used for parameters passed, as other examples in this topic will show.

To call the `SubscribeCommand` method, create an asynchronous function invoking an Amazon SNS client service object, and passing the parameters object.

**Note**
Replace {{TOPIC\_ARN}} with the Amazon Resource Name (ARN) for the topic, and {{EMAIL\_ADDRESS}} with the email address to subscribe to.

```
import { SubscribeCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicArn - The ARN of the topic for which you wish to confirm a subscription.
 * @param {string} emailAddress - The email address that is subscribed to the topic.
 */
export const subscribeEmail = async (
  topicArn = "TOPIC_ARN",
  emailAddress = "usern@me.com",
) => {
  const response = await snsClient.send(
    new SubscribeCommand({
      Protocol: "email",
      TopicArn: topicArn,
      Endpoint: emailAddress,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: 'c8e35bcd-b3c0-5940-9f66-06f6fcc108f0',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   SubscriptionArn: 'pending confirmation'
  // }
};
```

To run the example, enter the following at the command prompt.

```
node subscribe-email.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/subscribe-email.js).

### Confirming Subscriptions
<a name="sns-confirm-subscription-email"></a>

In this example, use a Node.js module to verify an endpoint owner's intent to receive emails by validating the token sent to the endpoint by a previous subscribe action.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `confirm-subscription.js`. Configure the SDK as previously shown, including installing the required clients and packages.

Define the parameters, including the `TOPIC_ARN` and `TOKEN`, and define a value of `TRUE` or `FALSE` for `AuthenticateOnUnsubscribe`.

The token is a short-lived token sent to the owner of an endpoint during a previous `SUBSCRIBE` action. For example, for an email endpoint the `TOKEN` is in the URL of the Confirm Subscription email sent to the email owner. For example, `abc123` is the token in the following URL.

![Subscription confirmed message showing an email address subscribed to an SNS topic.](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/token.png)

To call the `ConfirmSubscriptionCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**
Replace {{TOPIC\_ARN}} with the Amazon Resource Name (ARN) for the topic, {{TOKEN}} with the token value from the URL sent to the endpoint owner in a previous `Subscribe` action, and define {{AuthenticateOnUnsubscribe}}. with a value of `TRUE` or `FALSE`.

```
import { ConfirmSubscriptionCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} token - This token is sent the subscriber. Only subscribers
 *                         that are not AWS services (HTTP/S, email) need to be confirmed.
 * @param {string} topicArn - The ARN of the topic for which you wish to confirm a subscription.
 */
export const confirmSubscription = async (
  token = "TOKEN",
  topicArn = "TOPIC_ARN",
) => {
  const response = await snsClient.send(
    // A subscription only needs to be confirmed if the endpoint type is
    // HTTP/S, email, or in another AWS account.
    new ConfirmSubscriptionCommand({
      Token: token,
      TopicArn: topicArn,
      // If this is true, the subscriber cannot unsubscribe while unauthenticated.
      AuthenticateOnUnsubscribe: "false",
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '4bb5bce9-805a-5517-8333-e1d2cface90b',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   SubscriptionArn: 'arn:aws:sns:us-east-1:xxxxxxxxxxxx:TOPIC_NAME:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node confirm-subscription.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/confirm-subscription.js).

## Subscribing an Application Endpoint to a Topic
<a name="sns-examples-subscribing-apps"></a>

In this example, use a Node.js module to subscribe a mobile application endpoint so it receives notifications from an Amazon SNS topic.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `subscribe-app.js`. Configure the SDK as previously shown, including installing the required modules and packages.

Create an object containing the `Protocol` parameter to specify the `application` protocol, the `TopicArn` for the topic to subscribe to, and the Amazon Resource Name (ARN) of a mobile application endpoint for the `Endpoint` parameter. Pass the parameters to the `SubscribeCommand` method of the `SNS` client class.

To call the `SubscribeCommand` method, create an asynchronous function invoking an Amazon SNS service object, passing the parameters object.

**Note**
Replace {{TOPIC\_ARN}} with the Amazon Resource Name (ARN) for the topic, and {{MOBILE\_ENDPOINT\_ARN}} with the endpoint you are subscribing to the topic.

```
import { SubscribeCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicArn - The ARN of the topic the subscriber is subscribing to.
 * @param {string} endpoint - The Endpoint ARN of an application. This endpoint is created
 *                            when an application registers for notifications.
 */
export const subscribeApp = async (
  topicArn = "TOPIC_ARN",
  endpoint = "ENDPOINT",
) => {
  const response = await snsClient.send(
    new SubscribeCommand({
      Protocol: "application",
      TopicArn: topicArn,
      Endpoint: endpoint,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: 'c8e35bcd-b3c0-5940-9f66-06f6fcc108f0',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   SubscriptionArn: 'pending confirmation'
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node subscribe-app.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/subscribe-app.js).

## Subscribing a Lambda Function to a Topic
<a name="sns-examples-subscribing-lambda"></a>

In this example, use a Node.js module to subscribe an AWS Lambda function so it receives notifications from an Amazon SNS topic.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `subscribe-lambda.js`. Configure the SDK as previously shown.

Create an object containing the `Protocol` parameter, specifying the `lambda` protocol, the `TopicArn` for the topic to subscribe to, and the Amazon Resource Name (ARN) of an AWS Lambda function as the `Endpoint` parameter. Pass the parameters to the `SubscribeCommand` method of the `SNS` client class.

To call the `SubscribeCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**
Replace {{TOPIC\_ARN}} with the Amazon Resource Name (ARN) for the topic, and {{LAMBDA\_FUNCTION\_ARN}} with the Amazon Resource Name (ARN) of the Lambda function.

```
import { SubscribeCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} topicArn - The ARN of the topic the subscriber is subscribing to.
 * @param {string} endpoint - The Endpoint ARN of and AWS Lambda function.
 */
export const subscribeLambda = async (
  topicArn = "TOPIC_ARN",
  endpoint = "ENDPOINT",
) => {
  const response = await snsClient.send(
    new SubscribeCommand({
      Protocol: "lambda",
      TopicArn: topicArn,
      Endpoint: endpoint,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: 'c8e35bcd-b3c0-5940-9f66-06f6fcc108f0',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   SubscriptionArn: 'pending confirmation'
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node subscribe-lambda.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/subscribe-lambda.js).

## Unsubscribing from a Topic
<a name="sns-examples-unsubscribing"></a>

In this example, use a Node.js module to unsubscribe an Amazon SNS topic subscription.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `unsubscribe.js`. Configure the SDK as previously shown, including installing the required clients and packages.

Create an object containing the `SubscriptionArn` parameter, specifying the Amazon Resource Name (ARN) of the subscription to unsubscribe. Pass the parameters to the `UnsubscribeCommand` method of the `SNS` client class.

To call the `UnsubscribeCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**
Replace {{TOPIC\_SUBSCRIPTION\_ARN}} with the Amazon Resource Name (ARN) of the subscription to unsubscribe.

```
import { UnsubscribeCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string} subscriptionArn - The ARN of the subscription to cancel.
 */
const unsubscribe = async (
  subscriptionArn = "arn:aws:sns:us-east-1:xxxxxxxxxxxx:mytopic:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
) => {
  const response = await snsClient.send(
    new UnsubscribeCommand({
      SubscriptionArn: subscriptionArn,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '0178259a-9204-507c-b620-78a7570a44c6',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   }
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node unsubscribe.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/unsubscribe.js).

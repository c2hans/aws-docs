---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-sending-sms.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Sending SMS Messages with Amazon SNS
<a name="sns-examples-sending-sms"></a>

![JavaScript code example that applies to Node.js execution](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/nodeicon.png)

**This Node.js code example shows:**
+ How to get and set SMS messaging preferences for Amazon SNS.
+ How to check a phone number to see if it has opted out of receiving SMS messages.
+ How to get a list of phone numbers that have opted out of receiving SMS messages.
+ How to send an SMS message.

## The Scenario
<a name="sns-examples-sending-sms-scenario"></a>

You can use Amazon SNS to send text messages, or SMS messages, to SMS-enabled devices. You can send a message directly to a phone number, or you can send a message to multiple phone numbers at once by subscribing those phone numbers to a topic and sending your message to the topic.

In this example, you use a series of Node.js modules to publish SMS text messages from Amazon SNS to SMS-enabled devices. The Node.js modules use the SDK for JavaScript to publish SMS messages using these methods of the `SNS` client class:
+ [`GetSMSAttributesCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/GetSMSAttributesCommand/)
+ [`SetSMSAttributesCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/SetSMSAttributesCommand/)
+ [`CheckIfPhoneNumberIsOptedOutCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/CheckIfPhoneNumberIsOptedOutCommand/)
+ [`ListPhoneNumbersOptedOutCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/ListPhoneNumbersOptedOutCommand/)
+ [`PublishCommand`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-sns/Class/PublishCommand/)

## Prerequisite Tasks
<a name="sns-examples-sending-sms-prerequisites"></a>

To set up and run this example, you must first complete these tasks:
+ Set up the project environment to run these Node TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/README.md).
+ Create a shared configurations file with your user credentials. For more information about providing a shared credentials file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
These examples demonstrate how to import/export client service objects and command using ECMAScript6 (ES6).
This requires Node.js version 13.x or higher. To download and install the latest version of Node.js, see [Node.js downloads.](https://nodejs.org/en/download).
If you prefer to use CommonJS syntax, see [JavaScript ES6/CommonJS syntax](sdk-example-javascript-syntax.md).

## Getting SMS Attributes
<a name="sending-sms-getattributes"></a>

Use Amazon SNS to specify preferences for SMS messaging, such as how your deliveries are optimized (for cost or for reliable delivery), your monthly spending limit, how message deliveries are logged, and whether to subscribe to daily SMS usage reports. These preferences are retrieved and set as SMS attributes for Amazon SNS.

In this example, use a Node.js module to get the current SMS attributes in Amazon SNS.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

 Create a Node.js module with the file name `get-sms-attributes.js`.

Configure the SDK as previously shown, including downloading the required clients and packages. Create an object containing the parameters for getting SMS attributes, including the names of the individual attributes to get. For details on available SMS attributes, see [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html) in the Amazon Simple Notification Service API Reference.

This example gets the `DefaultSMSType` attribute, which controls whether SMS messages are sent as `Promotional`, which optimizes message delivery to incur the lowest cost, or as `Transactional`, which optimizes message delivery to achieve the highest reliability. Pass the parameters to the `SetTopicAttributesCommand` method of the `SNS` client class. To call the `SetSMSAttributesCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**
Replace {{ATTRIBUTE\_NAME}} with the name of the attribute.

```
import { GetSMSAttributesCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

export const getSmsAttributes = async () => {
  const response = await snsClient.send(
    // If you have not modified the account-level mobile settings of SNS,
    // the DefaultSMSType is undefined. For this example, it was set to
    // Transactional.
    new GetSMSAttributesCommand({ attributes: ["DefaultSMSType"] }),
  );

  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '67ad8386-4169-58f1-bdb9-debd281d48d5',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   attributes: { DefaultSMSType: 'Transactional' }
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node get-sms-attributes.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/get-sms-attributes.js).

## Setting SMS Attributes
<a name="sending-sms-setattributes"></a>

In this example, use a Node.js module to get the current SMS attributes in Amazon SNS.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

 Create a Node.js module with the file name `set-sms-attribute-type.js`. Configure the SDK as previously shown, including installing the required clients and packages. Create an object containing the parameters for setting SMS attributes, including the names of the individual attributes to set and the values to set for each. For details on available SMS attributes, see [ SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html) in the Amazon Simple Notification Service API Reference.

This example sets the `DefaultSMSType` attribute to `Transactional`, which optimizes message delivery to achieve the highest reliability. Pass the parameters to the `SetTopicAttributesCommand` method of the `SNS` client class. To call the `SetSMSAttributesCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

```
import { SetSMSAttributesCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {"Transactional" | "Promotional"} defaultSmsType
 */
export const setSmsType = async (defaultSmsType = "Transactional") => {
  const response = await snsClient.send(
    new SetSMSAttributesCommand({
      attributes: {
        // Promotional – (Default) Noncritical messages, such as marketing messages.
        // Transactional – Critical messages that support customer transactions,
        // such as one-time passcodes for multi-factor authentication.
        DefaultSMSType: defaultSmsType,
      },
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '1885b977-2d7e-535e-8214-e44be727e265',
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
node set-sms-attribute-type.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/set-sms-attribute-type.js).

## Checking If a Phone Number Has Opted Out
<a name="sending-sms-checkifphonenumberisoptedout"></a>

In this example, use a Node.js module to check a phone number to see if it has opted out from receiving SMS messages.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `check-if-phone-number-is-opted-out.js`. Configure the SDK as previously shown. Create an object containing the phone number to check as a parameter.

This example sets the `PhoneNumber` parameter to specify the phone number to check. Pass the object to the `CheckIfPhoneNumberIsOptedOutCommand` method of the `SNS` client class. To call the `CheckIfPhoneNumberIsOptedOutCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

**Note**

Replace {{PHONE\_NUMBER}} with the phone number.

```
import { CheckIfPhoneNumberIsOptedOutCommand } from "@aws-sdk/client-sns";

import { snsClient } from "../libs/snsClient.js";

export const checkIfPhoneNumberIsOptedOut = async (
  phoneNumber = "5555555555",
) => {
  const command = new CheckIfPhoneNumberIsOptedOutCommand({
    phoneNumber,
  });

  const response = await snsClient.send(command);
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '3341c28a-cdc8-5b39-a3ee-9fb0ee125732',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   isOptedOut: false
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node check-if-phone-number-is-opted-out.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/check-if-phone-number-is-opted-out.js).

## Listing Opted-Out Phone Numbers
<a name="sending-sms-listphonenumbersoptedout"></a>

In this example, use a Node.js module to get a list of phone numbers that have opted out from receiving SMS messages.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `list-phone-numbers-opted-out.js`. Configure the SDK as previously shown. Create an empty object as a parameter.

Pass the object to the `ListPhoneNumbersOptedOutCommand` method of the `SNS` client class. To call the `ListPhoneNumbersOptedOutCommand` method, create an asynchronous function invoking an Amazon SNS client service object, passing the parameters object.

```
import { ListPhoneNumbersOptedOutCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

export const listPhoneNumbersOptedOut = async () => {
  const response = await snsClient.send(
    new ListPhoneNumbersOptedOutCommand({}),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '44ff72fd-1037-5042-ad96-2fc16601df42',
  //     extendedRequestId: undefined,
  //     cfId: undefined,
  //     attempts: 1,
  //     totalRetryDelay: 0
  //   },
  //   phoneNumbers: ['+15555550100']
  // }
  return response;
};
```

To run the example, enter the following at the command prompt.

```
node list-phone-numbers-opted-out.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/list-phone-numbers-opted-out.js).

## Publishing an SMS Message
<a name="sending-sms-publishsms"></a>

In this example, use a Node.js module to send an SMS message to a phone number.

Create a `libs` directory, and create a Node.js module with the file name `snsClient.js`. Copy and paste the code below into it, which creates the Amazon SNS client object. Replace {{REGION}} with your AWS Region.

```
import { SNSClient } from "@aws-sdk/client-sns";

// The AWS Region can be provided here using the `region` property. If you leave it blank
// the SDK will default to the region set in your AWS config.
export const snsClient = new SNSClient({});
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/libs/snsClient.js).

Create a Node.js module with the file name `publish-sms.js`. Configure the SDK as previously shown, including installing the required clients and packages. Create an object containing the `Message` and `PhoneNumber` parameters.

When you send an SMS message, specify the phone number using the E.164 format. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (\+) and the country code. For example, a US phone number in E.164 format would appear as \+1001XXX5550100.

This example sets the `PhoneNumber` parameter to specify the phone number to send the message. Pass the object to the `PublishCommand` method of the `SNS` client class. To call the `PublishCommand` method, create an asynchronous function invoking an Amazon SNS service object, passing the parameters object.

**Note**
Replace {{TEXT\_MESSAGE}} with the text message, and {{PHONE\_NUMBER}} with the phone number.

```
import { PublishCommand } from "@aws-sdk/client-sns";
import { snsClient } from "../libs/snsClient.js";

/**
 * @param {string | Record<string, any>} message - The message to send. Can be a plain string or an object
 *                                                 if you are using the `json` `MessageStructure`.
 * @param {*} phoneNumber - The phone number to send the message to.
 */
export const publish = async (
  message = "Hello from SNS!",
  phoneNumber = "+15555555555",
) => {
  const response = await snsClient.send(
    new PublishCommand({
      Message: message,
      // One of PhoneNumber, TopicArn, or TargetArn must be specified.
      PhoneNumber: phoneNumber,
    }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //     httpStatusCode: 200,
  //     requestId: '7410094f-efc7-5f52-af03-54737569ab77',
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
node publish-sms.js
```

This example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/sns/actions/publish-sms.js).

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/javascript_2_eventbridge_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# EventBridge examples using SDK for JavaScript (v2)
<a name="javascript_2_eventbridge_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for JavaScript (v2) with EventBridge.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `PutEvents`
<a name="eventbridge_PutEvents_javascript_2_topic"></a>

The following code example shows how to use `PutEvents`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/eventbridge#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatchEvents service object
var ebevents = new AWS.EventBridge({ apiVersion: "2015-10-07" });

var params = {
  Entries: [
    {
      Detail: '{ "key1": "value1", "key2": "value2" }',
      DetailType: "appRequestSubmitted",
      Resources: ["RESOURCE_ARN"],
      Source: "com.company.app",
    },
  ],
};

ebevents.putEvents(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.Entries);
  }
});
```
+  For API details, see [PutEvents](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/eventbridge-2015-10-07/PutEvents) in *AWS SDK for JavaScript API Reference*.

### `PutRule`
<a name="eventbridge_PutRule_javascript_2_topic"></a>

The following code example shows how to use `PutRule`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/eventbridge#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatchEvents service object
var ebevents = new AWS.EventBridge({ apiVersion: "2015-10-07" });

var params = {
  Name: "DEMO_EVENT",
  RoleArn: "IAM_ROLE_ARN",
  ScheduleExpression: "rate(5 minutes)",
  State: "ENABLED",
};

ebevents.putRule(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.RuleArn);
  }
});
```
+  For API details, see [PutRule](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/eventbridge-2015-10-07/PutRule) in *AWS SDK for JavaScript API Reference*.

### `PutTargets`
<a name="eventbridge_PutTargets_javascript_2_topic"></a>

The following code example shows how to use `PutTargets`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/eventbridge#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatchEvents service object
var ebevents = new AWS.EventBridge({ apiVersion: "2015-10-07" });

var params = {
  Rule: "DEMO_EVENT",
  Targets: [
    {
      Arn: "LAMBDA_FUNCTION_ARN",
      Id: "myEventBridgeTarget",
    },
  ],
};

ebevents.putTargets(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});
```
+  For API details, see [PutTargets](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/eventbridge-2015-10-07/PutTargets) in *AWS SDK for JavaScript API Reference*.

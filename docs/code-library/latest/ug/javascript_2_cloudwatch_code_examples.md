---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/javascript_2_cloudwatch_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudWatch examples using SDK for JavaScript (v2)
<a name="javascript_2_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for JavaScript (v2) with CloudWatch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `DeleteAlarms`
<a name="cloudwatch_DeleteAlarms_javascript_2_topic"></a>

The following code example shows how to use `DeleteAlarms`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).
Import the SDK and client modules and call the API.

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

var params = {
  AlarmNames: ["Web_Server_CPU_Utilization"],
};

cw.deleteAlarms(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.html#cloudwatch-examples-creating-alarms-deleting).
+  For API details, see [DeleteAlarms](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/DeleteAlarms) in *AWS SDK for JavaScript API Reference*.

### `DescribeAlarmsForMetric`
<a name="cloudwatch_DescribeAlarmsForMetric_javascript_2_topic"></a>

The following code example shows how to use `DescribeAlarmsForMetric`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

cw.describeAlarms({ StateValue: "INSUFFICIENT_DATA" }, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    // List the names of all current alarms in the console
    data.MetricAlarms.forEach(function (item, index, array) {
      console.log(item.AlarmName);
    });
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.html#cloudwatch-examples-creating-alarms-describing).
+  For API details, see [DescribeAlarmsForMetric](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/DescribeAlarmsForMetric) in *AWS SDK for JavaScript API Reference*.

### `DisableAlarmActions`
<a name="cloudwatch_DisableAlarmActions_javascript_2_topic"></a>

The following code example shows how to use `DisableAlarmActions`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).
Import the SDK and client modules and call the API.

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

cw.disableAlarmActions(
  { AlarmNames: ["Web_Server_CPU_Utilization"] },
  function (err, data) {
    if (err) {
      console.log("Error", err);
    } else {
      console.log("Success", data);
    }
  }
);
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-using-alarm-actions.html#cloudwatch-examples-using-alarm-actions-disabling).
+  For API details, see [DisableAlarmActions](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/DisableAlarmActions) in *AWS SDK for JavaScript API Reference*.

### `EnableAlarmActions`
<a name="cloudwatch_EnableAlarmActions_javascript_2_topic"></a>

The following code example shows how to use `EnableAlarmActions`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).
Import the SDK and client modules and call the API.

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

var params = {
  AlarmName: "Web_Server_CPU_Utilization",
  ComparisonOperator: "GreaterThanThreshold",
  EvaluationPeriods: 1,
  MetricName: "CPUUtilization",
  Namespace: "AWS/EC2",
  Period: 60,
  Statistic: "Average",
  Threshold: 70.0,
  ActionsEnabled: true,
  AlarmActions: ["ACTION_ARN"],
  AlarmDescription: "Alarm when server CPU exceeds 70%",
  Dimensions: [
    {
      Name: "InstanceId",
      Value: "INSTANCE_ID",
    },
  ],
  Unit: "Percent",
};

cw.putMetricAlarm(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Alarm action added", data);
    var paramsEnableAlarmAction = {
      AlarmNames: [params.AlarmName],
    };
    cw.enableAlarmActions(paramsEnableAlarmAction, function (err, data) {
      if (err) {
        console.log("Error", err);
      } else {
        console.log("Alarm action enabled", data);
      }
    });
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-using-alarm-actions.html#cloudwatch-examples-using-alarm-actions-enabling).
+  For API details, see [EnableAlarmActions](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/EnableAlarmActions) in *AWS SDK for JavaScript API Reference*.

### `ListMetrics`
<a name="cloudwatch_ListMetrics_javascript_2_topic"></a>

The following code example shows how to use `ListMetrics`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

var params = {
  Dimensions: [
    {
      Name: "LogGroupName" /* required */,
    },
  ],
  MetricName: "IncomingLogEvents",
  Namespace: "AWS/Logs",
};

cw.listMetrics(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Metrics", JSON.stringify(data.Metrics));
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-getting-metrics.html#cloudwatch-examples-getting-metrics-listing).
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/ListMetrics) in *AWS SDK for JavaScript API Reference*.

### `PutMetricAlarm`
<a name="cloudwatch_PutMetricAlarm_javascript_2_topic"></a>

The following code example shows how to use `PutMetricAlarm`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

var params = {
  AlarmName: "Web_Server_CPU_Utilization",
  ComparisonOperator: "GreaterThanThreshold",
  EvaluationPeriods: 1,
  MetricName: "CPUUtilization",
  Namespace: "AWS/EC2",
  Period: 60,
  Statistic: "Average",
  Threshold: 70.0,
  ActionsEnabled: false,
  AlarmDescription: "Alarm when server CPU exceeds 70%",
  Dimensions: [
    {
      Name: "InstanceId",
      Value: "INSTANCE_ID",
    },
  ],
  Unit: "Percent",
};

cw.putMetricAlarm(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-creating-alarms.html#cloudwatch-examples-creating-alarms-putmetricalarm).
+  For API details, see [PutMetricAlarm](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/PutMetricAlarm) in *AWS SDK for JavaScript API Reference*.

### `PutMetricData`
<a name="cloudwatch_PutMetricData_javascript_2_topic"></a>

The following code example shows how to use `PutMetricData`.

**SDK for JavaScript (v2)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/cloudwatch#code-examples).

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: "2010-08-01" });

// Create parameters JSON for putMetricData
var params = {
  MetricData: [
    {
      MetricName: "PAGES_VISITED",
      Dimensions: [
        {
          Name: "UNIQUE_PAGES",
          Value: "URLS",
        },
      ],
      Unit: "None",
      Value: 1.0,
    },
  ],
  Namespace: "SITE/TRAFFIC",
};

cw.putMetricData(params, function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", JSON.stringify(data));
  }
});
```
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cloudwatch-examples-getting-metrics.html#cloudwatch-examples-getting-metrics-publishing-custom).
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/monitoring-2010-08-01/PutMetricData) in *AWS SDK for JavaScript API Reference*.

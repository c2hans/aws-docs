---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricDataQueryDefinition.html
---

# PutMetricDataQueryDefinition
<a name="API_PutMetricDataQueryDefinition"></a>

Creates or updates a metric data query definition.

A metric data query definition saves a metric query so that you can reuse it later. It includes the query expression, the query language, and a path that names the definition and can organize it into folders. When you save a definition, CloudWatch doesn't validate or run its expression.

To create a definition, omit `Id`. CloudWatch generates the ID and returns it. To update a definition, specify its `Id`. An update replaces the path, expression, and type, and keeps the creation time.

The path must be unique in your account and Region. If another definition already uses the path, the request fails with a `ConflictException`.

You can have up to 1,000 metric data query definitions in each Region of your account. A request that would create more fails with a `LimitExceededException`.

 **Permissions**

To create or update a definition, you need the `cloudwatch:PutMetricDataQueryDefinition` permission on the metric data query definition resource. The resource ARN has the format `arn:aws:cloudwatch:Region:account-id:metric-query-definition/Id`.

To add tags when you create a definition, you also need the `cloudwatch:TagResource` permission. You can use the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys to control which tags can be added.

## Request Syntax
<a name="API_PutMetricDataQueryDefinition_RequestSyntax"></a>

```
{
   "Expression": "{{string}}",
   "Id": "{{string}}",
   "Path": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_PutMetricDataQueryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Expression](#API_PutMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-request-Expression"></a>
The query expression, in the language that `Type` specifies. CloudWatch doesn't validate or run the expression when you save it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: Yes

 ** [Id](#API_PutMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-request-Id"></a>
The ID of the metric data query definition to update. Omit this parameter to create a definition. CloudWatch then generates the ID and returns it in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: No

 ** [Path](#API_PutMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-request-Path"></a>
The name of the metric data query definition. Use slashes (`/`) to organize definitions into folders, for example `team/web/latency`. The path must meet the following requirements:
+ It must be unique in your account and Region.
+ It can't start or end with a slash.
+ It can't contain an empty folder name (`//`).
+ It can be at most 1,015 bytes when encoded as UTF-8.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{N}\p{P}\p{S}\p{Zs}]+`
Required: Yes

 ** [Tags](#API_PutMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-request-Tags"></a>
A list of key-value pairs to associate with the metric data query definition. You can use tags to categorize definitions and to control access to them. Tags are applied only when the request creates a definition, that is, when you omit `Id`. To change the tags of an existing definition, use `TagResource` and `UntagResource`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Type](#API_PutMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-request-Type"></a>
The language of the expression. Valid values are the following:
+  `PROMQL` – A PromQL query.
+  `SQL` – A CloudWatch Metrics Insights query.
+  `METRIC_MATH` – A metric math expression.
Type: String
Valid Values: `PROMQL | SQL | METRIC_MATH`
Required: Yes

## Response Syntax
<a name="API_PutMetricDataQueryDefinition_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreatedAt": number,
   "Expression": "string",
   "Id": "string",
   "Path": "string",
   "Type": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_PutMetricDataQueryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-Arn"></a>
The Amazon Resource Name (ARN) of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [CreatedAt](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-CreatedAt"></a>
The date and time when you created the metric data query definition.
Type: Timestamp

 ** [Expression](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-Expression"></a>
The query expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [Id](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-Id"></a>
The ID of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`

 ** [Path](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-Path"></a>
The path of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{N}\p{P}\p{S}\p{Zs}]+`

 ** [Type](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-Type"></a>
The language of the expression.
Type: String
Valid Values: `PROMQL | SQL | METRIC_MATH`

 ** [UpdatedAt](#API_PutMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-PutMetricDataQueryDefinition-response-UpdatedAt"></a>
The date and time when you last updated the metric data query definition.
Type: Timestamp

## Errors
<a name="API_PutMetricDataQueryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** LimitExceededException **
The operation exceeded one or more limits.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_PutMetricDataQueryDefinition_Examples"></a>

### Example – Create a metric data query definition
<a name="API_PutMetricDataQueryDefinition_Example_1"></a>

The following AWS CLI command saves a CloudWatch Metrics Insights query that finds the 10 EC2 instances with the highest average CPU utilization. Replace the path and the expression with your own values. The JSON response follows the command.

#### Sample Request
<a name="API_PutMetricDataQueryDefinition_Example_1_Request"></a>

```
PROMPT> aws cloudwatch put-metric-data-query-definition \
    --path "ec2/top-cpu-instances" \
    --type SQL \
    --expression 'SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2", InstanceId) GROUP BY InstanceId ORDER BY AVG() DESC LIMIT 10'
```

#### Sample Response
<a name="API_PutMetricDataQueryDefinition_Example_1_Response"></a>

```
{
    "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Arn": "arn:aws:cloudwatch:us-east-1:111122223333:metric-query-definition/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Path": "ec2/top-cpu-instances",
    "Expression": "SELECT AVG(CPUUtilization) FROM SCHEMA(\"AWS/EC2\", InstanceId) GROUP BY InstanceId ORDER BY AVG() DESC LIMIT 10",
    "Type": "SQL",
    "CreatedAt": "2026-11-09T10:30:00Z",
    "UpdatedAt": "2026-11-09T10:30:00Z"
}
```

### Example – Create a metric data query definition with tags
<a name="API_PutMetricDataQueryDefinition_Example_2"></a>

The following AWS CLI command saves a metric math expression that finds the CPU utilization of every EC2 instance, and tags the new definition. Replace the path, the expression, and the tag with your own values. The JSON response follows the command.

#### Sample Request
<a name="API_PutMetricDataQueryDefinition_Example_2_Request"></a>

```
PROMPT> aws cloudwatch put-metric-data-query-definition \
    --path "ec2/cpu-all-instances" \
    --type METRIC_MATH \
    --expression "SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)" \
    --tags Key=Team,Value=Platform
```

#### Sample Response
<a name="API_PutMetricDataQueryDefinition_Example_2_Response"></a>

```
{
    "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Arn": "arn:aws:cloudwatch:us-east-1:111122223333:metric-query-definition/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Path": "ec2/cpu-all-instances",
    "Expression": "SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)",
    "Type": "METRIC_MATH",
    "CreatedAt": "2026-11-08T16:45:00Z",
    "UpdatedAt": "2026-11-08T16:45:00Z"
}
```

### Example – Update a metric data query definition
<a name="API_PutMetricDataQueryDefinition_Example_3"></a>

The following AWS CLI command replaces the expression of an existing definition. Replace the ID, the path, and the expression with your own values. The JSON response follows the command.

#### Sample Request
<a name="API_PutMetricDataQueryDefinition_Example_3_Request"></a>

```
PROMPT> aws cloudwatch put-metric-data-query-definition \
    --id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --path "ec2/top-cpu-instances" \
    --type SQL \
    --expression 'SELECT MAX(CPUUtilization) FROM SCHEMA("AWS/EC2", InstanceId) GROUP BY InstanceId ORDER BY MAX() DESC LIMIT 10'
```

#### Sample Response
<a name="API_PutMetricDataQueryDefinition_Example_3_Response"></a>

```
{
    "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Arn": "arn:aws:cloudwatch:us-east-1:111122223333:metric-query-definition/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Path": "ec2/top-cpu-instances",
    "Expression": "SELECT MAX(CPUUtilization) FROM SCHEMA(\"AWS/EC2\", InstanceId) GROUP BY InstanceId ORDER BY MAX() DESC LIMIT 10",
    "Type": "SQL",
    "CreatedAt": "2026-11-09T10:30:00Z",
    "UpdatedAt": "2026-11-10T08:15:00Z"
}
```

## See Also
<a name="API_PutMetricDataQueryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricDataQueryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricDataQueryDefinition)

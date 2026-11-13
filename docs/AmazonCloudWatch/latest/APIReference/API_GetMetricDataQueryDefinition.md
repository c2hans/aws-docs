---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricDataQueryDefinition.html
---

# GetMetricDataQueryDefinition
<a name="API_GetMetricDataQueryDefinition"></a>

Returns a metric data query definition, including its expression.

 **Permissions**

To get a definition, you need the `cloudwatch:GetMetricDataQueryDefinition` permission on the metric data query definition resource. You can use the `aws:ResourceTag/${TagKey}` condition key to control access based on the tags of the definition.

## Request Syntax
<a name="API_GetMetricDataQueryDefinition_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMetricDataQueryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_GetMetricDataQueryDefinition_RequestSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-request-Id"></a>
The ID of the metric data query definition to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

## Response Syntax
<a name="API_GetMetricDataQueryDefinition_ResponseSyntax"></a>

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
<a name="API_GetMetricDataQueryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-Arn"></a>
The Amazon Resource Name (ARN) of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [CreatedAt](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-CreatedAt"></a>
The date and time when you created the metric data query definition.
Type: Timestamp

 ** [Expression](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-Expression"></a>
The query expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [Id](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-Id"></a>
The ID of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`

 ** [Path](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-Path"></a>
The path of the metric data query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{N}\p{P}\p{S}\p{Zs}]+`

 ** [Type](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-Type"></a>
The language of the expression. Valid values are the following:
+  `PROMQL` – A PromQL query.
+  `SQL` – A CloudWatch Metrics Insights query.
+  `METRIC_MATH` – A metric math expression.
Type: String
Valid Values: `PROMQL | SQL | METRIC_MATH`

 ** [UpdatedAt](#API_GetMetricDataQueryDefinition_ResponseSyntax) **   <a name="ACW-GetMetricDataQueryDefinition-response-UpdatedAt"></a>
The date and time when you last updated the metric data query definition.
Type: Timestamp

## Errors
<a name="API_GetMetricDataQueryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_GetMetricDataQueryDefinition_Examples"></a>

### Example – Get a metric data query definition
<a name="API_GetMetricDataQueryDefinition_Example_1"></a>

The following AWS CLI command retrieves a saved definition by its ID. Replace the ID with your definition ID. The JSON response follows the command.

#### Sample Request
<a name="API_GetMetricDataQueryDefinition_Example_1_Request"></a>

```
PROMPT> aws cloudwatch get-metric-data-query-definition \
    --id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

#### Sample Response
<a name="API_GetMetricDataQueryDefinition_Example_1_Response"></a>

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

## See Also
<a name="API_GetMetricDataQueryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricDataQueryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricDataQueryDefinition)

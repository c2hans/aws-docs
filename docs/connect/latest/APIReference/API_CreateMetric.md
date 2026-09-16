---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateMetric.html
---

# CreateMetric
<a name="API_CreateMetric"></a>

Creates a new metric definition for the specified Connect Customer instance. You can create custom metrics that use formulas referencing existing AWS-managed metrics, optionally with filters applied.

## Request Syntax
<a name="API_CreateMetric_RequestSyntax"></a>

```
PUT /metrics/definitions/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "MetricCalculation": {
      "Calculation": "{{string}}",
      "CalculationComponents": [
         {
            "Alias": "{{string}}",
            "MetricFilters": [
               {
                  "BooleanCondition": {
                     "Comparison": "{{string}}"
                  },
                  "MetricFilterKey": "{{string}}",
                  "Negate": {{boolean}},
                  "NumberCondition": {
                     "Comparison": "{{string}}",
                     "Values": [ {{number}} ]
                  },
                  "StringCondition": {
                     "Comparison": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               }
            ],
            "MetricId": "{{string}}",
            "MetricName": "{{string}}"
         }
      ]
   },
   "Name": "{{string}}",
   "PositiveTrendIndicator": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Unit": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateMetric_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-Description"></a>
The description of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [MetricCalculation](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-MetricCalculation"></a>
The calculation definition for the metric, including the formula expression and the component metrics it references.
Type: [MetricCalculation](API_MetricCalculation.md) object
Required: Yes

 ** [Name](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-Name"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [PositiveTrendIndicator](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-PositiveTrendIndicator"></a>
How an increase in the metric value should be interpreted. Valid values: `POSITIVE`, `NEUTRAL`, `NEGATIVE`.
Type: String
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL`
Required: No

 ** [Status](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-Status"></a>
The publish status of the metric. Set to `PUBLISHED` to make the metric available for use in dashboards and reports, or `SAVED` to keep it in draft state.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** [Tags](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Unit](#API_CreateMetric_RequestSyntax) **   <a name="connect-CreateMetric-request-Unit"></a>
The display unit for the metric's data.
Type: String
Valid Values: `INTEGER | DOUBLE | PERCENT | SECONDS`
Required: Yes

## Response Syntax
<a name="API_CreateMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricArn": "string",
   "MetricId": "string"
}
```

## Response Elements
<a name="API_CreateMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricArn](#API_CreateMetric_ResponseSyntax) **   <a name="connect-CreateMetric-response-MetricArn"></a>
The Amazon Resource Name (ARN) of the metric.
Type: String

 ** [MetricId](#API_CreateMetric_ResponseSyntax) **   <a name="connect-CreateMetric-response-MetricId"></a>
The identifier of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.

## Errors
<a name="API_CreateMetric_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_CreateMetric_Examples"></a>

### Example
<a name="API_CreateMetric_Example_1"></a>

The following example creates a custom metric that calculates the percentage of contacts handled within 60 seconds of being queued.

#### Sample Request
<a name="API_CreateMetric_Example_1_Request"></a>

```
{
    "Name": "example-metric",
    "MetricCalculation": {
        "CalculationComponents": [
            {
                "Alias": "M1",
                "MetricName": "CONTACTS_HANDLED",
                "MetricFilters": [
                    {
                        "MetricFilterKey": "QUEUE_TIME_MS",
                        "NumberCondition": {"Comparison": "LESSER_OR_EQUAL", "Values": [60.0]}
                    }
                ]
            },
            {
                "Alias": "M2",
                "MetricName": "CONTACTS_QUEUED"
            }
        ],
        "Calculation": "100 * SUM(M1) / SUM(M2)"
    },
    "Unit": "PERCENT",
    "Status": "PUBLISHED",
    "Description": "Percentage of contacts handled within 60 seconds.",
    "PositiveTrendIndicator": "POSITIVE"
}
```

#### Sample Response
<a name="API_CreateMetric_Example_1_Response"></a>

```
{
    "MetricArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/metric/87654321-4321-4321-4321-210987654321",
    "MetricId": "87654321-4321-4321-4321-210987654321"
}
```

## See Also
<a name="API_CreateMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateMetric)

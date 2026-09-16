---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeMetric.html
---

# DescribeMetric
<a name="API_DescribeMetric"></a>

Retrieves the full definition of an existing metric from the specified Connect Customer instance.

## Request Syntax
<a name="API_DescribeMetric_RequestSyntax"></a>

```
GET /metrics/definitions/{{InstanceId}}/{{MetricId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeMetric_RequestSyntax) **   <a name="connect-DescribeMetric-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MetricId](#API_DescribeMetric_RequestSyntax) **   <a name="connect-DescribeMetric-request-uri-MetricId"></a>
The identifier of the metric to describe. Adding the `$SAVED` qualifier will describe the saved version of the metric. Adding `$LATEST` or omitting a qualifier will describe the published version.
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## Request Body
<a name="API_DescribeMetric_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Metric": {
      "Arn": "string",
      "Category": "string",
      "CreatedTime": number,
      "CreatedUser": { ... },
      "CreationMethod": "string",
      "DefaultStat": "string",
      "Description": "string",
      "EffectiveTime": number,
      "Filters": [
         {
            "Id": "string",
            "Type": "string"
         }
      ],
      "Groupings": [ "string" ],
      "Id": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "LastModifiedUser": { ... },
      "MetricCalculation": {
         "Calculation": "string",
         "CalculationComponents": [
            {
               "Alias": "string",
               "MetricFilters": [
                  {
                     "BooleanCondition": {
                        "Comparison": "string"
                     },
                     "MetricFilterKey": "string",
                     "Negate": boolean,
                     "NumberCondition": {
                        "Comparison": "string",
                        "Values": [ number ]
                     },
                     "StringCondition": {
                        "Comparison": "string",
                        "Values": [ "string" ]
                     }
                  }
               ],
               "MetricId": "string",
               "MetricName": "string"
            }
         ]
      },
      "Name": "string",
      "PositiveTrendIndicator": "string",
      "PrimaryEventSource": "string",
      "PrimaryEventSourceEffectiveTimestampType": "string",
      "RefreshRate": number,
      "Status": "string",
      "SupportedStats": [ "string" ],
      "SupportsCustomCalculation": boolean,
      "SupportsPreaggregateCalculation": boolean,
      "Tags": {
         "string" : "string"
      },
      "Type": "string",
      "Unit": "string"
   }
}
```

## Response Elements
<a name="API_DescribeMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metric](#API_DescribeMetric_ResponseSyntax) **   <a name="connect-DescribeMetric-response-Metric"></a>
The metric definition.
Type: [MetricDefinition](API_MetricDefinition.md) object

## Errors
<a name="API_DescribeMetric_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_DescribeMetric_Examples"></a>

### Example
<a name="API_DescribeMetric_Example_1"></a>

The following example retrieves the saved version of a metric.

#### Sample Request
<a name="API_DescribeMetric_Example_1_Request"></a>

```
GET /metrics/definitions/12345678-1234-1234-1234-123456789012/87654321-4321-4321-4321-210987654321:$SAVED
```

#### Sample Response
<a name="API_DescribeMetric_Example_1_Response"></a>

```
{
    "Metric": {
        "Arn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/metric/87654321-4321-4321-4321-210987654321:$SAVED",
        "Id": "87654321-4321-4321-4321-210987654321",
        "Name": "example-metric",
        "Status": "SAVED",
        "Type": "CUSTOMER_MANAGED",
        "Unit": "PERCENT",
        "MetricCalculation": {
            "Calculation": "100 * SUM(M1) / SUM(M2)",
            "CalculationComponents": [
                {"Alias": "M1", "MetricName": "CONTACTS_HANDLED"},
                {"Alias": "M2", "MetricName": "CONTACTS_QUEUED"}
            ]
        }
    }
}
```

## See Also
<a name="API_DescribeMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeMetric)

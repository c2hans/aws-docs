---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateMetricContent.html
---

# UpdateMetricContent
<a name="API_UpdateMetricContent"></a>

Updates the calculation, unit, and/or trend indicator of an existing metric in the specified Connect Customer instance.

## Request Syntax
<a name="API_UpdateMetricContent_RequestSyntax"></a>

```
POST /metrics/definitions/{{InstanceId}}/{{MetricId}}/content HTTP/1.1
Content-type: application/json

{
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
   "PositiveTrendIndicator": "{{string}}",
   "Unit": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMetricContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateMetricContent_RequestSyntax) **   <a name="connect-UpdateMetricContent-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MetricId](#API_UpdateMetricContent_RequestSyntax) **   <a name="connect-UpdateMetricContent-request-uri-MetricId"></a>
The identifier of the metric to update. Adding the `$SAVED` qualifier will update the saved version of the metric. Adding `$LATEST` or omitting a qualifier will update the published version.
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## Request Body
<a name="API_UpdateMetricContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MetricCalculation](#API_UpdateMetricContent_RequestSyntax) **   <a name="connect-UpdateMetricContent-request-MetricCalculation"></a>
The updated calculation definition for the metric.
Type: [MetricCalculation](API_MetricCalculation.md) object
Required: No

 ** [PositiveTrendIndicator](#API_UpdateMetricContent_RequestSyntax) **   <a name="connect-UpdateMetricContent-request-PositiveTrendIndicator"></a>
How an increase in the metric value should be interpreted. Valid values: `POSITIVE`, `NEUTRAL`, `NEGATIVE`.
Type: String
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL`
Required: No

 ** [Unit](#API_UpdateMetricContent_RequestSyntax) **   <a name="connect-UpdateMetricContent-request-Unit"></a>
The updated display unit for the metric.
Type: String
Valid Values: `INTEGER | DOUBLE | PERCENT | SECONDS`
Required: No

## Response Syntax
<a name="API_UpdateMetricContent_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateMetricContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateMetricContent_Errors"></a>

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
<a name="API_UpdateMetricContent_Examples"></a>

### Example
<a name="API_UpdateMetricContent_Example_1"></a>

The following example updates a metric's calculation to use a 30-second filter threshold.

#### Sample Request
<a name="API_UpdateMetricContent_Example_1_Request"></a>

```
{
    "MetricCalculation": {
        "CalculationComponents": [
            {
                "Alias": "M1",
                "MetricName": "CONTACTS_HANDLED",
                "MetricFilters": [
                    {
                        "MetricFilterKey": "QUEUE_TIME_MS",
                        "NumberCondition": {"Comparison": "LESSER_OR_EQUAL", "Values": [30.0]}
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
    "PositiveTrendIndicator": "POSITIVE"
}
```

#### Sample Response
<a name="API_UpdateMetricContent_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateMetricContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateMetricContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateMetricContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

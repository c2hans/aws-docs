---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeHoursOfOperationOverride.html
---

# DescribeHoursOfOperationOverride
<a name="API_DescribeHoursOfOperationOverride"></a>

Describes the hours of operation override.

## Request Syntax
<a name="API_DescribeHoursOfOperationOverride_RequestSyntax"></a>

```
GET /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}/overrides/{{HoursOfOperationOverrideId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeHoursOfOperationOverride_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_DescribeHoursOfOperationOverride_RequestSyntax) **   <a name="connect-DescribeHoursOfOperationOverride-request-uri-HoursOfOperationId"></a>
The identifier for the hours of operation.
Required: Yes

 ** [HoursOfOperationOverrideId](#API_DescribeHoursOfOperationOverride_RequestSyntax) **   <a name="connect-DescribeHoursOfOperationOverride-request-uri-HoursOfOperationOverrideId"></a>
The identifier for the hours of operation override.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [InstanceId](#API_DescribeHoursOfOperationOverride_RequestSyntax) **   <a name="connect-DescribeHoursOfOperationOverride-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeHoursOfOperationOverride_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeHoursOfOperationOverride_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HoursOfOperationOverride": {
      "Config": [
         {
            "Day": "string",
            "EndTime": {
               "Hours": number,
               "Minutes": number
            },
            "StartTime": {
               "Hours": number,
               "Minutes": number
            }
         }
      ],
      "Description": "string",
      "EffectiveFrom": "string",
      "EffectiveTill": "string",
      "HoursOfOperationArn": "string",
      "HoursOfOperationId": "string",
      "HoursOfOperationOverrideId": "string",
      "Name": "string",
      "OverrideType": "string",
      "RecurrenceConfig": {
         "RecurrencePattern": {
            "ByMonth": [ number ],
            "ByMonthDay": [ number ],
            "ByWeekdayOccurrence": [ number ],
            "Frequency": "string",
            "Interval": number
         }
      }
   }
}
```

## Response Elements
<a name="API_DescribeHoursOfOperationOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HoursOfOperationOverride](#API_DescribeHoursOfOperationOverride_ResponseSyntax) **   <a name="connect-DescribeHoursOfOperationOverride-response-HoursOfOperationOverride"></a>
Information about the hours of operations override.
Type: [HoursOfOperationOverride](API_HoursOfOperationOverride.md) object

## Errors
<a name="API_DescribeHoursOfOperationOverride_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_DescribeHoursOfOperationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeHoursOfOperationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeHoursOfOperationOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

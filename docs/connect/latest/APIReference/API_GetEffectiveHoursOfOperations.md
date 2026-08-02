---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetEffectiveHoursOfOperations.html
---

# GetEffectiveHoursOfOperations
<a name="API_GetEffectiveHoursOfOperations"></a>

Get the hours of operations with the effective override applied.

## Request Syntax
<a name="API_GetEffectiveHoursOfOperations_RequestSyntax"></a>

```
GET /effective-hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}?fromDate={{FromDate}}&toDate={{ToDate}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEffectiveHoursOfOperations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FromDate](#API_GetEffectiveHoursOfOperations_RequestSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-request-uri-FromDate"></a>
The date from when the hours of operation are listed.
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: Yes

 ** [HoursOfOperationId](#API_GetEffectiveHoursOfOperations_RequestSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-request-uri-HoursOfOperationId"></a>
The identifier for the hours of operation.
Required: Yes

 ** [InstanceId](#API_GetEffectiveHoursOfOperations_RequestSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ToDate](#API_GetEffectiveHoursOfOperations_RequestSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-request-uri-ToDate"></a>
The date until when the hours of operation are listed.
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: Yes

## Request Body
<a name="API_GetEffectiveHoursOfOperations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEffectiveHoursOfOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EffectiveHoursOfOperationList": [
      {
         "Date": "string",
         "OperationalHours": [
            {
               "End": {
                  "Hours": number,
                  "Minutes": number
               },
               "Start": {
                  "Hours": number,
                  "Minutes": number
               }
            }
         ]
      }
   ],
   "EffectiveOverrideHoursList": [
      {
         "Date": "string",
         "OverrideHours": [
            {
               "End": {
                  "Hours": number,
                  "Minutes": number
               },
               "OperationalStatus": "string",
               "OverrideName": "string",
               "Start": {
                  "Hours": number,
                  "Minutes": number
               }
            }
         ]
      }
   ],
   "TimeZone": "string"
}
```

## Response Elements
<a name="API_GetEffectiveHoursOfOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EffectiveHoursOfOperationList](#API_GetEffectiveHoursOfOperations_ResponseSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-response-EffectiveHoursOfOperationList"></a>
Information about the effective hours of operations.
Type: Array of [EffectiveHoursOfOperations](API_EffectiveHoursOfOperations.md) objects

 ** [EffectiveOverrideHoursList](#API_GetEffectiveHoursOfOperations_ResponseSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-response-EffectiveOverrideHoursList"></a>
Information about override configurations applied to the base hours of operation to calculate the effective hours.
For more information about how override types are applied, see [Build your list of overrides](https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html) in the * Administrator Guide*.
Type: Array of [EffectiveOverrideHours](API_EffectiveOverrideHours.md) objects

 ** [TimeZone](#API_GetEffectiveHoursOfOperations_ResponseSyntax) **   <a name="connect-GetEffectiveHoursOfOperations-response-TimeZone"></a>
The time zone for the hours of operation.
Type: String

## Errors
<a name="API_GetEffectiveHoursOfOperations_Errors"></a>

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
<a name="API_GetEffectiveHoursOfOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetEffectiveHoursOfOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetEffectiveHoursOfOperations)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListHoursOfOperationOverrides.html
---

# ListHoursOfOperationOverrides
<a name="API_ListHoursOfOperationOverrides"></a>

List the hours of operation overrides.

## Request Syntax
<a name="API_ListHoursOfOperationOverrides_RequestSyntax"></a>

```
GET /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}/overrides?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHoursOfOperationOverrides_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_ListHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-ListHoursOfOperationOverrides-request-uri-HoursOfOperationId"></a>
The identifier for the hours of operation.
Required: Yes

 ** [InstanceId](#API_ListHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-ListHoursOfOperationOverrides-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-ListHoursOfOperationOverrides-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-ListHoursOfOperationOverrides-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListHoursOfOperationOverrides_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHoursOfOperationOverrides_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HoursOfOperationOverrideList": [
      {
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
   ],
   "LastModifiedRegion": "string",
   "LastModifiedTime": number,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHoursOfOperationOverrides_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HoursOfOperationOverrideList](#API_ListHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-ListHoursOfOperationOverrides-response-HoursOfOperationOverrideList"></a>
Information about the hours of operation override.
Type: Array of [HoursOfOperationOverride](API_HoursOfOperationOverride.md) objects

 ** [LastModifiedRegion](#API_ListHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-ListHoursOfOperationOverrides-response-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_ListHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-ListHoursOfOperationOverrides-response-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp

 ** [NextToken](#API_ListHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-ListHoursOfOperationOverrides-response-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListHoursOfOperationOverrides_Errors"></a>

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
<a name="API_ListHoursOfOperationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListHoursOfOperationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListHoursOfOperationOverrides)

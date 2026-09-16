---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.html
---

# BatchUpdateExclusionWindows
<a name="API_BatchUpdateExclusionWindows"></a>

Add or remove time window exclusions for one or more Service Level Objectives (SLOs).

## Request Syntax
<a name="API_BatchUpdateExclusionWindows_RequestSyntax"></a>

```
PATCH /exclusion-windows HTTP/1.1
Content-type: application/json

{
   "AddExclusionWindows": [
      {
         "Reason": "{{string}}",
         "RecurrenceRule": {
            "Expression": "{{string}}"
         },
         "StartTime": {{number}},
         "Window": {
            "Duration": {{number}},
            "DurationUnit": "{{string}}"
         }
      }
   ],
   "RemoveExclusionWindows": [
      {
         "Reason": "{{string}}",
         "RecurrenceRule": {
            "Expression": "{{string}}"
         },
         "StartTime": {{number}},
         "Window": {
            "Duration": {{number}},
            "DurationUnit": "{{string}}"
         }
      }
   ],
   "SloIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateExclusionWindows_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateExclusionWindows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AddExclusionWindows](#API_BatchUpdateExclusionWindows_RequestSyntax) **   <a name="applicationsignals-BatchUpdateExclusionWindows-request-AddExclusionWindows"></a>
A list of exclusion windows to add to the specified SLOs. You can add up to 10 exclusion windows per SLO.
Type: Array of [ExclusionWindow](API_ExclusionWindow.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [RemoveExclusionWindows](#API_BatchUpdateExclusionWindows_RequestSyntax) **   <a name="applicationsignals-BatchUpdateExclusionWindows-request-RemoveExclusionWindows"></a>
A list of exclusion windows to remove from the specified SLOs. The window configuration must match an existing exclusion window.
Type: Array of [ExclusionWindow](API_ExclusionWindow.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [SloIds](#API_BatchUpdateExclusionWindows_RequestSyntax) **   <a name="applicationsignals-BatchUpdateExclusionWindows-request-SloIds"></a>
The list of SLO IDs to add or remove exclusion windows from.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateExclusionWindows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "SloId": "string"
      }
   ],
   "SloIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchUpdateExclusionWindows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchUpdateExclusionWindows_ResponseSyntax) **   <a name="applicationsignals-BatchUpdateExclusionWindows-response-Errors"></a>
A list of errors that occurred while processing the request.
Type: Array of [BatchUpdateExclusionWindowsError](API_BatchUpdateExclusionWindowsError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [SloIds](#API_BatchUpdateExclusionWindows_ResponseSyntax) **   <a name="applicationsignals-BatchUpdateExclusionWindows-response-SloIds"></a>
The list of SLO IDs that were successfully processed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_BatchUpdateExclusionWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchUpdateExclusionWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/BatchUpdateExclusionWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchUpdateExclusionWindows)

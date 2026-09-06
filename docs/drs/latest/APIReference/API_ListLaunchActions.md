---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ListLaunchActions.html
---

# ListLaunchActions
<a name="API_ListLaunchActions"></a>

Lists resource launch actions.

## Request Syntax
<a name="API_ListLaunchActions_RequestSyntax"></a>

```
POST /ListLaunchActions HTTP/1.1
Content-type: application/json

{
   "filters": {
      "actionIds": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLaunchActions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLaunchActions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListLaunchActions_RequestSyntax) **   <a name="drs-ListLaunchActions-request-filters"></a>
Filters to apply when listing resource launch actions.
Type: [LaunchActionsRequestFilters](API_LaunchActionsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListLaunchActions_RequestSyntax) **   <a name="drs-ListLaunchActions-request-maxResults"></a>
Maximum amount of items to return when listing resource launch actions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListLaunchActions_RequestSyntax) **   <a name="drs-ListLaunchActions-request-nextToken"></a>
Next token to use when listing resource launch actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [resourceId](#API_ListLaunchActions_RequestSyntax) **   <a name="drs-ListLaunchActions-request-resourceId"></a>
Launch configuration template Id or Source Server Id
Type: String
Pattern: `(s-[0-9a-zA-Z]{17}$|lct-[0-9a-zA-Z]{17})`
Required: Yes

## Response Syntax
<a name="API_ListLaunchActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "actionCode": "string",
         "actionId": "string",
         "actionVersion": "string",
         "active": boolean,
         "category": "string",
         "description": "string",
         "name": "string",
         "optional": boolean,
         "order": number,
         "parameters": {
            "string" : {
               "type": "string",
               "value": "string"
            }
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLaunchActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListLaunchActions_ResponseSyntax) **   <a name="drs-ListLaunchActions-response-items"></a>
List of resource launch actions.
Type: Array of [LaunchAction](API_LaunchAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [nextToken](#API_ListLaunchActions_ResponseSyntax) **   <a name="drs-ListLaunchActions-response-nextToken"></a>
Next token returned when listing resource launch actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListLaunchActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

## See Also
<a name="API_ListLaunchActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/ListLaunchActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ListLaunchActions)

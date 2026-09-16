---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledControls.html
---

# ListEnabledControls
<a name="API_ListEnabledControls"></a>

Lists the controls enabled by AWS Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the [*Controls Reference Guide*](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html).

## Request Syntax
<a name="API_ListEnabledControls_RequestSyntax"></a>

```
POST /list-enabled-controls HTTP/1.1
Content-type: application/json

{
   "filter": {
      "controlIdentifiers": [ "{{string}}" ],
      "driftStatuses": [ "{{string}}" ],
      "inheritanceDriftStatuses": [ "{{string}}" ],
      "parentIdentifiers": [ "{{string}}" ],
      "resourceDriftStatuses": [ "{{string}}" ],
      "statuses": [ "{{string}}" ]
   },
   "includeChildren": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "targetIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEnabledControls_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEnabledControls_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListEnabledControls_RequestSyntax) **   <a name="controltower-ListEnabledControls-request-filter"></a>
An input filter for the `ListEnabledControls` API that lets you select the types of control operations to view.
Type: [EnabledControlFilter](API_EnabledControlFilter.md) object
Required: No

 ** [includeChildren](#API_ListEnabledControls_RequestSyntax) **   <a name="controltower-ListEnabledControls-request-includeChildren"></a>
A boolean value that determines whether to include enabled controls from child organizational units in the response.
Type: Boolean
Required: No

 ** [maxResults](#API_ListEnabledControls_RequestSyntax) **   <a name="controltower-ListEnabledControls-request-maxResults"></a>
How many results to return per API call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListEnabledControls_RequestSyntax) **   <a name="controltower-ListEnabledControls-request-nextToken"></a>
The token to continue the list from a previous API call with the same parameters.
Type: String
Required: No

 ** [targetIdentifier](#API_ListEnabledControls_RequestSyntax) **   <a name="controltower-ListEnabledControls-request-targetIdentifier"></a>
The ARN of the organizational unit. For information on how to find the `targetIdentifier`, see [the overview page](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## Response Syntax
<a name="API_ListEnabledControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "enabledControls": [
      {
         "arn": "string",
         "controlIdentifier": "string",
         "driftStatusSummary": {
            "driftStatus": "string",
            "types": {
               "inheritance": {
                  "status": "string"
               },
               "resource": {
                  "status": "string"
               }
            }
         },
         "parentIdentifier": "string",
         "statusSummary": {
            "lastOperationIdentifier": "string",
            "status": "string"
         },
         "targetIdentifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnabledControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [enabledControls](#API_ListEnabledControls_ResponseSyntax) **   <a name="controltower-ListEnabledControls-response-enabledControls"></a>
Lists the controls enabled by AWS Control Tower on the specified organizational unit and the accounts it contains.
Type: Array of [EnabledControlSummary](API_EnabledControlSummary.md) objects

 ** [nextToken](#API_ListEnabledControls_ResponseSyntax) **   <a name="controltower-ListEnabledControls-response-nextToken"></a>
Retrieves the next page of results. If the string is empty, the response is the end of the results.
Type: String

## Errors
<a name="API_ListEnabledControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEnabledControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListEnabledControls)

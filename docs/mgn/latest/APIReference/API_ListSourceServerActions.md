---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListSourceServerActions.html
---

# ListSourceServerActions
<a name="API_ListSourceServerActions"></a>

List source server post migration custom actions.

## Request Syntax
<a name="API_ListSourceServerActions_RequestSyntax"></a>

```
POST /ListSourceServerActions HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "filters": {
      "actionIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSourceServerActions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSourceServerActions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_ListSourceServerActions_RequestSyntax) **   <a name="mgn-ListSourceServerActions-request-accountID"></a>
Account ID to return when listing source server post migration custom actions.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [filters](#API_ListSourceServerActions_RequestSyntax) **   <a name="mgn-ListSourceServerActions-request-filters"></a>
Filters to apply when listing source server post migration custom actions.
Type: [SourceServerActionsRequestFilters](API_SourceServerActionsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListSourceServerActions_RequestSyntax) **   <a name="mgn-ListSourceServerActions-request-maxResults"></a>
Maximum amount of items to return when listing source server post migration custom actions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListSourceServerActions_RequestSyntax) **   <a name="mgn-ListSourceServerActions-request-nextToken"></a>
Next token to use when listing source server post migration custom actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [sourceServerID](#API_ListSourceServerActions_RequestSyntax) **   <a name="mgn-ListSourceServerActions-request-sourceServerID"></a>
Source server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_ListSourceServerActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "actionID": "string",
         "actionName": "string",
         "active": boolean,
         "category": "string",
         "description": "string",
         "documentIdentifier": "string",
         "documentVersion": "string",
         "externalParameters": {
            "string" : { ... }
         },
         "mustSucceedForCutover": boolean,
         "order": number,
         "parameters": {
            "string" : [
               {
                  "parameterName": "string",
                  "parameterType": "string"
               }
            ]
         },
         "timeoutSeconds": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSourceServerActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSourceServerActions_ResponseSyntax) **   <a name="mgn-ListSourceServerActions-response-items"></a>
List of source server post migration custom actions.
Type: Array of [SourceServerActionDocument](API_SourceServerActionDocument.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListSourceServerActions_ResponseSyntax) **   <a name="mgn-ListSourceServerActions-response-nextToken"></a>
Next token returned when listing source server post migration custom actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListSourceServerActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSourceServerActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListSourceServerActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListSourceServerActions)

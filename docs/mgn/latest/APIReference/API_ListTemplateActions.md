---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListTemplateActions.html
---

# ListTemplateActions
<a name="API_ListTemplateActions"></a>

List template post migration custom actions.

## Request Syntax
<a name="API_ListTemplateActions_RequestSyntax"></a>

```
POST /ListTemplateActions HTTP/1.1
Content-type: application/json

{
   "filters": {
      "actionIDs": [ "{{string}}" ]
   },
   "launchConfigurationTemplateID": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTemplateActions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTemplateActions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListTemplateActions_RequestSyntax) **   <a name="mgn-ListTemplateActions-request-filters"></a>
Filters to apply when listing template post migration custom actions.
Type: [TemplateActionsRequestFilters](API_TemplateActionsRequestFilters.md) object
Required: No

 ** [launchConfigurationTemplateID](#API_ListTemplateActions_RequestSyntax) **   <a name="mgn-ListTemplateActions-request-launchConfigurationTemplateID"></a>
Launch configuration template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [maxResults](#API_ListTemplateActions_RequestSyntax) **   <a name="mgn-ListTemplateActions-request-maxResults"></a>
Maximum amount of items to return when listing template post migration custom actions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTemplateActions_RequestSyntax) **   <a name="mgn-ListTemplateActions-request-nextToken"></a>
Next token to use when listing template post migration custom actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListTemplateActions_ResponseSyntax"></a>

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
         "operatingSystem": "string",
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
<a name="API_ListTemplateActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListTemplateActions_ResponseSyntax) **   <a name="mgn-ListTemplateActions-response-items"></a>
List of template post migration custom actions.
Type: Array of [TemplateActionDocument](API_TemplateActionDocument.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListTemplateActions_ResponseSyntax) **   <a name="mgn-ListTemplateActions-response-nextToken"></a>
Next token returned when listing template post migration custom actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListTemplateActions_Errors"></a>

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
<a name="API_ListTemplateActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListTemplateActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListTemplateActions)

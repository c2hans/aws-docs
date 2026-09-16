---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListComponentTypes.html
---

# ListComponentTypes
<a name="API_ListComponentTypes"></a>

Lists all component types in a workspace.

## Request Syntax
<a name="API_ListComponentTypes_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/component-types-list HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListComponentTypes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_ListComponentTypes_RequestSyntax) **   <a name="tm-ListComponentTypes-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_ListComponentTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListComponentTypes_RequestSyntax) **   <a name="tm-ListComponentTypes-request-filters"></a>
A list of objects that filter the request.
Type: Array of [ListComponentTypesFilter](API_ListComponentTypesFilter.md) objects
Required: No

 ** [maxResults](#API_ListComponentTypes_RequestSyntax) **   <a name="tm-ListComponentTypes-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListComponentTypes_RequestSyntax) **   <a name="tm-ListComponentTypes-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListComponentTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentTypeSummaries": [
      {
         "arn": "string",
         "componentTypeId": "string",
         "componentTypeName": "string",
         "creationDateTime": number,
         "description": "string",
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "state": "string"
         },
         "updateDateTime": number
      }
   ],
   "maxResults": number,
   "nextToken": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_ListComponentTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentTypeSummaries](#API_ListComponentTypes_ResponseSyntax) **   <a name="tm-ListComponentTypes-response-componentTypeSummaries"></a>
A list of objects that contain information about the component types.
Type: Array of [ComponentTypeSummary](API_ComponentTypeSummary.md) objects

 ** [maxResults](#API_ListComponentTypes_ResponseSyntax) **   <a name="tm-ListComponentTypes-response-maxResults"></a>
Specifies the maximum number of results to display.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.

 ** [nextToken](#API_ListComponentTypes_ResponseSyntax) **   <a name="tm-ListComponentTypes-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [workspaceId](#API_ListComponentTypes_ResponseSyntax) **   <a name="tm-ListComponentTypes-response-workspaceId"></a>
The ID of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_ListComponentTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListComponentTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListComponentTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListComponentTypes)

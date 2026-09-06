---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListComponents.html
---

# ListComponents
<a name="API_ListComponents"></a>

This API lists the components of an entity.

## Request Syntax
<a name="API_ListComponents_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/entities/{{entityId}}/components-list HTTP/1.1
Content-type: application/json

{
   "componentPath": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListComponents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entityId](#API_ListComponents_RequestSyntax) **   <a name="tm-ListComponents-request-uri-entityId"></a>
The ID for the entity whose metadata (component/properties) is returned by the operation.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: Yes

 ** [workspaceId](#API_ListComponents_RequestSyntax) **   <a name="tm-ListComponents-request-uri-workspaceId"></a>
The workspace ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_ListComponents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentPath](#API_ListComponents_RequestSyntax) **   <a name="tm-ListComponents-request-componentPath"></a>
This string specifies the path to the composite component, starting from the top-level component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** [maxResults](#API_ListComponents_RequestSyntax) **   <a name="tm-ListComponents-request-maxResults"></a>
The maximum number of results returned at one time. The default is 25.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListComponents_RequestSyntax) **   <a name="tm-ListComponents-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListComponents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentSummaries": [
      {
         "componentName": "string",
         "componentPath": "string",
         "componentTypeId": "string",
         "definedIn": "string",
         "description": "string",
         "propertyGroups": {
            "string" : {
               "groupType": "string",
               "isInherited": boolean,
               "propertyNames": [ "string" ]
            }
         },
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "state": "string"
         },
         "syncSource": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentSummaries](#API_ListComponents_ResponseSyntax) **   <a name="tm-ListComponents-response-componentSummaries"></a>
A list of objects that contain information about the components.
Type: Array of [ComponentSummary](API_ComponentSummary.md) objects

 ** [nextToken](#API_ListComponents_ResponseSyntax) **   <a name="tm-ListComponents-response-nextToken"></a>
The string that specifies the next page of component results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

## Errors
<a name="API_ListComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListComponents)

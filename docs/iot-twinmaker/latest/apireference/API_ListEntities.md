---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListEntities.html
---

# ListEntities
<a name="API_ListEntities"></a>

Lists all entities in a workspace.

## Request Syntax
<a name="API_ListEntities_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/entities-list HTTP/1.1
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
<a name="API_ListEntities_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_ListEntities_RequestSyntax) **   <a name="tm-ListEntities-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_ListEntities_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListEntities_RequestSyntax) **   <a name="tm-ListEntities-request-filters"></a>
A list of objects that filter the request.
Only one object is accepted as a valid input.
Type: Array of [ListEntitiesFilter](API_ListEntitiesFilter.md) objects
Required: No

 ** [maxResults](#API_ListEntities_RequestSyntax) **   <a name="tm-ListEntities-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListEntities_RequestSyntax) **   <a name="tm-ListEntities-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListEntities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entitySummaries": [
      {
         "arn": "string",
         "creationDateTime": number,
         "description": "string",
         "entityId": "string",
         "entityName": "string",
         "hasChildEntities": boolean,
         "parentEntityId": "string",
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
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitySummaries](#API_ListEntities_ResponseSyntax) **   <a name="tm-ListEntities-response-entitySummaries"></a>
A list of objects that contain information about the entities.
Type: Array of [EntitySummary](API_EntitySummary.md) objects

 ** [nextToken](#API_ListEntities_ResponseSyntax) **   <a name="tm-ListEntities-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

## Errors
<a name="API_ListEntities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListEntities)

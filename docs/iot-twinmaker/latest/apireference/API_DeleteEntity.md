---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DeleteEntity.html
---

# DeleteEntity
<a name="API_DeleteEntity"></a>

Deletes an entity.

## Request Syntax
<a name="API_DeleteEntity_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/entities/{{entityId}}?isRecursive={{isRecursive}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entityId](#API_DeleteEntity_RequestSyntax) **   <a name="tm-DeleteEntity-request-uri-entityId"></a>
The ID of the entity to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: Yes

 ** [isRecursive](#API_DeleteEntity_RequestSyntax) **   <a name="tm-DeleteEntity-request-uri-isRecursive"></a>
A Boolean value that specifies whether the operation deletes child entities.

 ** [workspaceId](#API_DeleteEntity_RequestSyntax) **   <a name="tm-DeleteEntity-request-uri-workspaceId"></a>
The ID of the workspace that contains the entity to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteEntity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "state": "string"
}
```

## Response Elements
<a name="API_DeleteEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [state](#API_DeleteEntity_ResponseSyntax) **   <a name="tm-DeleteEntity-response-state"></a>
The current state of the deleted entity.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`

## Errors
<a name="API_DeleteEntity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

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
<a name="API_DeleteEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/DeleteEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/DeleteEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

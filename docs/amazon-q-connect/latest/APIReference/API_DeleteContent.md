---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteContent.html
---

# DeleteContent
<a name="API_amazon-q-connect_DeleteContent"></a>

Deletes the content.

## Request Syntax
<a name="API_amazon-q-connect_DeleteContent_RequestSyntax"></a>

```
DELETE /knowledgeBases/{{knowledgeBaseId}}/contents/{{contentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_DeleteContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentId](#API_amazon-q-connect_DeleteContent_RequestSyntax) **   <a name="connect-amazon-q-connect_DeleteContent-request-uri-contentId"></a>
The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [knowledgeBaseId](#API_amazon-q-connect_DeleteContent_RequestSyntax) **   <a name="connect-amazon-q-connect_DeleteContent-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_DeleteContent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_DeleteContent_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_amazon-q-connect_DeleteContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_amazon-q-connect_DeleteContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_DeleteContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/DeleteContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/DeleteContent)

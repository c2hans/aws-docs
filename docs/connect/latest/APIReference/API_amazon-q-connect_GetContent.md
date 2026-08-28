---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GetContent.html
---

# GetContent
<a name="API_amazon-q-connect_GetContent"></a>

Retrieves content, including a pre-signed URL to download the content.

## Request Syntax
<a name="API_amazon-q-connect_GetContent_RequestSyntax"></a>

```
GET /knowledgeBases/{{knowledgeBaseId}}/contents/{{contentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentId](#API_amazon-q-connect_GetContent_RequestSyntax) **   <a name="connect-amazon-q-connect_GetContent-request-uri-contentId"></a>
The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [knowledgeBaseId](#API_amazon-q-connect_GetContent_RequestSyntax) **   <a name="connect-amazon-q-connect_GetContent-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetContent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "content": {
      "contentArn": "string",
      "contentId": "string",
      "contentType": "string",
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "linkOutUri": "string",
      "metadata": {
         "string" : "string"
      },
      "name": "string",
      "revisionId": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "title": "string",
      "url": "string",
      "urlExpiry": number
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_GetContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [content](#API_amazon-q-connect_GetContent_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetContent-response-content"></a>
The content.
Type: [ContentData](API_amazon-q-connect_ContentData.md) object

## Errors
<a name="API_amazon-q-connect_GetContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_amazon-q-connect_GetContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_DeactivateMessageTemplate.html
---

# DeactivateMessageTemplate
<a name="API_amazon-q-connect_DeactivateMessageTemplate"></a>

Deactivates a specific version of the Amazon Q in Connect message template . After the version is deactivated, you can no longer use the `$ACTIVE_VERSION` qualifier to reference the version in active status.

## Request Syntax
<a name="API_amazon-q-connect_DeactivateMessageTemplate_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}}/deactivate HTTP/1.1
Content-type: application/json

{
   "versionNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_DeactivateMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_DeactivateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_DeactivateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_DeactivateMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [versionNumber](#API_amazon-q-connect_DeactivateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-request-versionNumber"></a>
The version number of the message template version to deactivate.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_DeactivateMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageTemplateArn": "string",
   "messageTemplateId": "string",
   "versionNumber": number
}
```

## Response Elements
<a name="API_amazon-q-connect_DeactivateMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplateArn](#API_amazon-q-connect_DeactivateMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-response-messageTemplateArn"></a>
The Amazon Resource Name (ARN) of the message template.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`

 ** [messageTemplateId](#API_amazon-q-connect_DeactivateMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-response-messageTemplateId"></a>
The identifier of the message template.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [versionNumber](#API_amazon-q-connect_DeactivateMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_DeactivateMessageTemplate-response-versionNumber"></a>
The version number of the message template version that has been deactivated.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_amazon-q-connect_DeactivateMessageTemplate_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_DeactivateMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/DeactivateMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/DeactivateMessageTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

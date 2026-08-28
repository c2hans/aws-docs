---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetAssistantAssociation.html
---

# GetAssistantAssociation
<a name="API_amazon-q-connect_GetAssistantAssociation"></a>

Retrieves information about an assistant association.

## Request Syntax
<a name="API_amazon-q-connect_GetAssistantAssociation_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/associations/{{assistantAssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetAssistantAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantAssociationId](#API_amazon-q-connect_GetAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_GetAssistantAssociation-request-uri-assistantAssociationId"></a>
The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [assistantId](#API_amazon-q-connect_GetAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_GetAssistantAssociation-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetAssistantAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetAssistantAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assistantAssociation": {
      "assistantArn": "string",
      "assistantAssociationArn": "string",
      "assistantAssociationId": "string",
      "assistantId": "string",
      "associationData": { ... },
      "associationType": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_GetAssistantAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistantAssociation](#API_amazon-q-connect_GetAssistantAssociation_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetAssistantAssociation-response-assistantAssociation"></a>
The assistant association.
Type: [AssistantAssociationData](API_amazon-q-connect_AssistantAssociationData.md) object

## Errors
<a name="API_amazon-q-connect_GetAssistantAssociation_Errors"></a>

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
<a name="API_amazon-q-connect_GetAssistantAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetAssistantAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetAssistantAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

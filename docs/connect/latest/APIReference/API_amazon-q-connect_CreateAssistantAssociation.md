---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateAssistantAssociation.html
---

# CreateAssistantAssociation
<a name="API_amazon-q-connect_CreateAssistantAssociation"></a>

Creates an association between an Amazon Q in Connect assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

## Request Syntax
<a name="API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/associations HTTP/1.1
Content-type: application/json

{
   "association": { ... },
   "associationType": "{{string}}",
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateAssistantAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateAssistantAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [association](#API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-request-association"></a>
The identifier of the associated resource.
Type: [AssistantAssociationInputData](API_amazon-q-connect_AssistantAssociationInputData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [associationType](#API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-request-associationType"></a>
The type of association.
Type: String
Valid Values: `KNOWLEDGE_BASE | EXTERNAL_BEDROCK_KNOWLEDGE_BASE`
Required: Yes

 ** [clientToken](#API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [tags](#API_amazon-q-connect_CreateAssistantAssociation_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateAssistantAssociation_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_CreateAssistantAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistantAssociation](#API_amazon-q-connect_CreateAssistantAssociation_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateAssistantAssociation-response-assistantAssociation"></a>
The assistant association.
Type: [AssistantAssociationData](API_amazon-q-connect_AssistantAssociationData.md) object

## Errors
<a name="API_amazon-q-connect_CreateAssistantAssociation_Errors"></a>

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

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateAssistantAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateAssistantAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateAssistantAssociation)

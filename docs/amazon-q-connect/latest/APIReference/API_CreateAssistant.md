---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateAssistant.html
---

# CreateAssistant
<a name="API_amazon-q-connect_CreateAssistant"></a>

Creates an Amazon Q in Connect assistant.

## Request Syntax
<a name="API_amazon-q-connect_CreateAssistant_RequestSyntax"></a>

```
POST /assistants HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "serverSideEncryptionConfiguration": {
      "kmsKeyId": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateAssistant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_amazon-q-connect_CreateAssistant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [description](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-description"></a>
The description of the assistant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [name](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-name"></a>
The name of the assistant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [serverSideEncryptionConfiguration](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-serverSideEncryptionConfiguration"></a>
The configuration information for the customer managed key used for encryption.
The customer managed key must have a policy that allows `kms:CreateGrant`, ` kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow `kms:Decrypt`, `kms:GenerateDataKey*`, and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal.
For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html).
Type: [ServerSideEncryptionConfiguration](API_amazon-q-connect_ServerSideEncryptionConfiguration.md) object
Required: No

 ** [tags](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [type](#API_amazon-q-connect_CreateAssistant_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-request-type"></a>
The type of assistant.
Type: String
Valid Values: `AGENT`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_CreateAssistant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assistant": {
      "aiAgentConfiguration": {
         "string" : {
            "aiAgentId": "string"
         }
      },
      "assistantArn": "string",
      "assistantId": "string",
      "capabilityConfiguration": {
         "type": "string"
      },
      "description": "string",
      "integrationConfiguration": {
         "topicIntegrationArn": "string"
      },
      "name": "string",
      "orchestratorConfigurationList": [
         {
            "aiAgentId": "string",
            "orchestratorUseCase": "string"
         }
      ],
      "serverSideEncryptionConfiguration": {
         "kmsKeyId": "string"
      },
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateAssistant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assistant](#API_amazon-q-connect_CreateAssistant_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateAssistant-response-assistant"></a>
Information about the assistant.
Type: [AssistantData](API_amazon-q-connect_AssistantData.md) object

## Errors
<a name="API_amazon-q-connect_CreateAssistant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateAssistant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateAssistant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateAssistant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

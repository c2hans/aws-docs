---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateInstanceStorageConfig.html
---

# DisassociateInstanceStorageConfig
<a name="API_DisassociateInstanceStorageConfig"></a>

This API is in preview release for Connect Customer and is subject to change.

Removes the storage type configurations for the specified resource type and association ID.

## Request Syntax
<a name="API_DisassociateInstanceStorageConfig_RequestSyntax"></a>

```
DELETE /instance/{{InstanceId}}/storage-config/{{AssociationId}}?clientToken={{ClientToken}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateInstanceStorageConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationId](#API_DisassociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-DisassociateInstanceStorageConfig-request-uri-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ClientToken](#API_DisassociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-DisassociateInstanceStorageConfig-request-uri-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Length Constraints: Maximum length of 500.

 ** [InstanceId](#API_DisassociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-DisassociateInstanceStorageConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceType](#API_DisassociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-DisassociateInstanceStorageConfig-request-uri-ResourceType"></a>
A valid resource type.
Valid Values: `CHAT_TRANSCRIPTS | CALL_RECORDINGS | SCHEDULED_REPORTS | MEDIA_STREAMS | CONTACT_TRACE_RECORDS | AGENT_EVENTS | REAL_TIME_CONTACT_ANALYSIS_SEGMENTS | ATTACHMENTS | CONTACT_EVALUATIONS | SCREEN_RECORDINGS | REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS | REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS | EMAIL_MESSAGES`
Required: Yes

## Request Body
<a name="API_DisassociateInstanceStorageConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateInstanceStorageConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateInstanceStorageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateInstanceStorageConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DisassociateInstanceStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateInstanceStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateInstanceStorageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

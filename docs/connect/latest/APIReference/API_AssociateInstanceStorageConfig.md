---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateInstanceStorageConfig.html
---

# AssociateInstanceStorageConfig
<a name="API_AssociateInstanceStorageConfig"></a>

This API is in preview release for Connect Customer and is subject to change.

Associates a storage resource type for the first time. You can only associate one type of storage configuration in a single call. This means, for example, that you can't define an instance with multiple S3 buckets for storing chat transcripts.

This API does not create a resource that doesn't exist. It only associates it to the instance. Ensure that the resource being specified in the storage configuration, like an S3 bucket, exists when being used for association.

## Request Syntax
<a name="API_AssociateInstanceStorageConfig_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/storage-config HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ResourceType": "{{string}}",
   "StorageConfig": {
      "AssociationId": "{{string}}",
      "KinesisFirehoseConfig": {
         "FirehoseArn": "{{string}}"
      },
      "KinesisStreamConfig": {
         "StreamArn": "{{string}}"
      },
      "KinesisVideoStreamConfig": {
         "EncryptionConfig": {
            "EncryptionType": "{{string}}",
            "KeyId": "{{string}}"
         },
         "Prefix": "{{string}}",
         "RetentionPeriodHours": {{number}}
      },
      "S3Config": {
         "BucketName": "{{string}}",
         "BucketPrefix": "{{string}}",
         "EncryptionConfig": {
            "EncryptionType": "{{string}}",
            "KeyId": "{{string}}"
         }
      },
      "StorageType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_AssociateInstanceStorageConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-AssociateInstanceStorageConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateInstanceStorageConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AssociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-AssociateInstanceStorageConfig-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ResourceType](#API_AssociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-AssociateInstanceStorageConfig-request-ResourceType"></a>
A valid resource type. To [enable streaming for real-time analysis of contacts](https://docs.aws.amazon.com/connect/latest/adminguide/enable-contact-analysis-segment-streams.html), use the following types:
+ For chat contacts, use `REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS`.
+ For voice contacts, use `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS`.
 `REAL_TIME_CONTACT_ANALYSIS_SEGMENTS` is deprecated, but it is still supported and will apply only to VOICE channel contacts. Use `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS` for voice contacts moving forward.
If you have previously associated a stream with `REAL_TIME_CONTACT_ANALYSIS_SEGMENTS`, no action is needed to update the stream to `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS`.
Type: String
Valid Values: `CHAT_TRANSCRIPTS | CALL_RECORDINGS | SCHEDULED_REPORTS | MEDIA_STREAMS | CONTACT_TRACE_RECORDS | AGENT_EVENTS | REAL_TIME_CONTACT_ANALYSIS_SEGMENTS | ATTACHMENTS | CONTACT_EVALUATIONS | SCREEN_RECORDINGS | REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS | REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS | EMAIL_MESSAGES`
Required: Yes

 ** [StorageConfig](#API_AssociateInstanceStorageConfig_RequestSyntax) **   <a name="connect-AssociateInstanceStorageConfig-request-StorageConfig"></a>
A valid storage type.
Type: [InstanceStorageConfig](API_InstanceStorageConfig.md) object
Required: Yes

## Response Syntax
<a name="API_AssociateInstanceStorageConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociationId": "string"
}
```

## Response Elements
<a name="API_AssociateInstanceStorageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationId](#API_AssociateInstanceStorageConfig_ResponseSyntax) **   <a name="connect-AssociateInstanceStorageConfig-response-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_AssociateInstanceStorageConfig_Errors"></a>

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

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateInstanceStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateInstanceStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateInstanceStorageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeInstanceStorageConfig.html
---

# DescribeInstanceStorageConfig
<a name="API_DescribeInstanceStorageConfig"></a>

This API is in preview release for Connect Customer and is subject to change.

Retrieves the current storage configurations for the specified resource type, association ID, and instance ID.

## Request Syntax
<a name="API_DescribeInstanceStorageConfig_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/storage-config/{{AssociationId}}?resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInstanceStorageConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationId](#API_DescribeInstanceStorageConfig_RequestSyntax) **   <a name="connect-DescribeInstanceStorageConfig-request-uri-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [InstanceId](#API_DescribeInstanceStorageConfig_RequestSyntax) **   <a name="connect-DescribeInstanceStorageConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceType](#API_DescribeInstanceStorageConfig_RequestSyntax) **   <a name="connect-DescribeInstanceStorageConfig-request-uri-ResourceType"></a>
A valid resource type.
Valid Values: `CHAT_TRANSCRIPTS | CALL_RECORDINGS | SCHEDULED_REPORTS | MEDIA_STREAMS | CONTACT_TRACE_RECORDS | AGENT_EVENTS | REAL_TIME_CONTACT_ANALYSIS_SEGMENTS | ATTACHMENTS | CONTACT_EVALUATIONS | SCREEN_RECORDINGS | REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS | REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS | EMAIL_MESSAGES`
Required: Yes

## Request Body
<a name="API_DescribeInstanceStorageConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInstanceStorageConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StorageConfig": {
      "AssociationId": "string",
      "KinesisFirehoseConfig": {
         "FirehoseArn": "string"
      },
      "KinesisStreamConfig": {
         "StreamArn": "string"
      },
      "KinesisVideoStreamConfig": {
         "EncryptionConfig": {
            "EncryptionType": "string",
            "KeyId": "string"
         },
         "Prefix": "string",
         "RetentionPeriodHours": number
      },
      "S3Config": {
         "BucketName": "string",
         "BucketPrefix": "string",
         "EncryptionConfig": {
            "EncryptionType": "string",
            "KeyId": "string"
         }
      },
      "StorageType": "string"
   }
}
```

## Response Elements
<a name="API_DescribeInstanceStorageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageConfig](#API_DescribeInstanceStorageConfig_ResponseSyntax) **   <a name="connect-DescribeInstanceStorageConfig-response-StorageConfig"></a>
A valid storage type.
Type: [InstanceStorageConfig](API_InstanceStorageConfig.md) object

## Errors
<a name="API_DescribeInstanceStorageConfig_Errors"></a>

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
<a name="API_DescribeInstanceStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeInstanceStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeInstanceStorageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

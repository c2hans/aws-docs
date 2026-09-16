---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListInstanceStorageConfigs.html
---

# ListInstanceStorageConfigs
<a name="API_ListInstanceStorageConfigs"></a>

This API is in preview release for Connect Customer and is subject to change.

Returns a paginated list of storage configs for the identified instance and resource type.

## Request Syntax
<a name="API_ListInstanceStorageConfigs_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/storage-configs?maxResults={{MaxResults}}&nextToken={{NextToken}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInstanceStorageConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListInstanceStorageConfigs_RequestSyntax) **   <a name="connect-ListInstanceStorageConfigs-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListInstanceStorageConfigs_RequestSyntax) **   <a name="connect-ListInstanceStorageConfigs-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListInstanceStorageConfigs_RequestSyntax) **   <a name="connect-ListInstanceStorageConfigs-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [ResourceType](#API_ListInstanceStorageConfigs_RequestSyntax) **   <a name="connect-ListInstanceStorageConfigs-request-uri-ResourceType"></a>
A valid resource type.
Valid Values: `CHAT_TRANSCRIPTS | CALL_RECORDINGS | SCHEDULED_REPORTS | MEDIA_STREAMS | CONTACT_TRACE_RECORDS | AGENT_EVENTS | REAL_TIME_CONTACT_ANALYSIS_SEGMENTS | ATTACHMENTS | CONTACT_EVALUATIONS | SCREEN_RECORDINGS | REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS | REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS | EMAIL_MESSAGES`
Required: Yes

## Request Body
<a name="API_ListInstanceStorageConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInstanceStorageConfigs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StorageConfigs": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListInstanceStorageConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListInstanceStorageConfigs_ResponseSyntax) **   <a name="connect-ListInstanceStorageConfigs-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [StorageConfigs](#API_ListInstanceStorageConfigs_ResponseSyntax) **   <a name="connect-ListInstanceStorageConfigs-response-StorageConfigs"></a>
A valid storage type.
Type: Array of [InstanceStorageConfig](API_InstanceStorageConfig.md) objects

## Errors
<a name="API_ListInstanceStorageConfigs_Errors"></a>

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
<a name="API_ListInstanceStorageConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListInstanceStorageConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListInstanceStorageConfigs)

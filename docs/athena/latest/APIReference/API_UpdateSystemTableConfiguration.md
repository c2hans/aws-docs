---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateSystemTableConfiguration.html
---

# UpdateSystemTableConfiguration
<a name="API_UpdateSystemTableConfiguration"></a>

Updates the account-level system tables configuration. If no configuration exists, use [CreateSystemTableConfiguration](API_CreateSystemTableConfiguration.md) to create one. Fields that you omit retain their current values.

## Request Syntax
<a name="API_UpdateSystemTableConfiguration_RequestSyntax"></a>

```
{
   "KmsKeyArn": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSystemTableConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [KmsKeyArn](#API_UpdateSystemTableConfiguration_RequestSyntax) **   <a name="athena-UpdateSystemTableConfiguration-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key to use for encrypting the system table data. The encryption key is immutable while the system table exists, so a change takes effect only after the table has been deleted.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:[a-z0-9\-]+:\d{12}:(key/(mrk-)?[0-9a-f\-]+|alias/[a-zA-Z0-9/_\-]+)$`
Required: No

 ** [TableName](#API_UpdateSystemTableConfiguration_RequestSyntax) **   <a name="athena-UpdateSystemTableConfiguration-request-TableName"></a>
The system table configuration to update. The only accepted value is `ALL`.
Type: String
Valid Values: `ALL`
Required: Yes

## Response Syntax
<a name="API_UpdateSystemTableConfiguration_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "KmsKeyArn": "string",
   "LastModifiedAt": number,
   "TableName": "string"
}
```

## Response Elements
<a name="API_UpdateSystemTableConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_UpdateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-UpdateSystemTableConfiguration-response-CreatedAt"></a>
The date and time the system table configuration was created.
Type: Timestamp

 ** [KmsKeyArn](#API_UpdateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-UpdateSystemTableConfiguration-response-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used for encrypting the system table data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:[a-z0-9\-]+:\d{12}:(key/(mrk-)?[0-9a-f\-]+|alias/[a-zA-Z0-9/_\-]+)$`

 ** [LastModifiedAt](#API_UpdateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-UpdateSystemTableConfiguration-response-LastModifiedAt"></a>
The date and time the system table configuration was last modified.
Type: Timestamp

 ** [TableName](#API_UpdateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-UpdateSystemTableConfiguration-response-TableName"></a>
The system table configuration. Always `ALL`.
Type: String
Valid Values: `ALL`

## Errors
<a name="API_UpdateSystemTableConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSystemTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateSystemTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateSystemTableConfiguration)

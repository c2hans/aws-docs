---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateSystemTableConfiguration.html
---

# CreateSystemTableConfiguration
<a name="API_CreateSystemTableConfiguration"></a>

Enables system tables for the current account. System tables are enabled or disabled for the entire account: creating this configuration enables them. If a configuration already exists, use [UpdateSystemTableConfiguration](API_UpdateSystemTableConfiguration.md) to update it.

## Request Syntax
<a name="API_CreateSystemTableConfiguration_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "TableName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSystemTableConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateSystemTableConfiguration_RequestSyntax) **   <a name="athena-CreateSystemTableConfiguration-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the system table configuration is idempotent (executes only once). If another `CreateSystemTableConfiguration` request is received with the same client token but different parameters, the request fails with an `InvalidRequestException`.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [KmsKeyArn](#API_CreateSystemTableConfiguration_RequestSyntax) **   <a name="athena-CreateSystemTableConfiguration-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key to use for encrypting the system table data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:[a-z0-9\-]+:\d{12}:(key/(mrk-)?[0-9a-f\-]+|alias/[a-zA-Z0-9/_\-]+)$`
Required: No

 ** [TableName](#API_CreateSystemTableConfiguration_RequestSyntax) **   <a name="athena-CreateSystemTableConfiguration-request-TableName"></a>
The system table configuration to create. The only accepted value is `ALL`, the reserved keyword that enables all system tables for the account.
Type: String
Valid Values: `ALL`
Required: Yes

 ** [Tags](#API_CreateSystemTableConfiguration_RequestSyntax) **   <a name="athena-CreateSystemTableConfiguration-request-Tags"></a>
The tags to add to the system table configuration.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateSystemTableConfiguration_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "KmsKeyArn": "string",
   "LastModifiedAt": number,
   "TableName": "string"
}
```

## Response Elements
<a name="API_CreateSystemTableConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_CreateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-CreateSystemTableConfiguration-response-CreatedAt"></a>
The date and time the system table configuration was created.
Type: Timestamp

 ** [KmsKeyArn](#API_CreateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-CreateSystemTableConfiguration-response-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used for encrypting the system table data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:[a-z0-9\-]+:\d{12}:(key/(mrk-)?[0-9a-f\-]+|alias/[a-zA-Z0-9/_\-]+)$`

 ** [LastModifiedAt](#API_CreateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-CreateSystemTableConfiguration-response-LastModifiedAt"></a>
The date and time the system table configuration was last modified.
Type: Timestamp

 ** [TableName](#API_CreateSystemTableConfiguration_ResponseSyntax) **   <a name="athena-CreateSystemTableConfiguration-response-TableName"></a>
The system table configuration that was created. Always `ALL`.
Type: String
Valid Values: `ALL`

## Errors
<a name="API_CreateSystemTableConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_CreateSystemTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateSystemTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CreateSystemTableConfiguration)

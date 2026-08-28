---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_CreateDatabase.html
---

# CreateDatabase
<a name="API_CreateDatabase"></a>

Creates a new Timestream database. If the AWS KMS key is not specified, the database will be encrypted with a Timestream managed AWS KMS key located in your account. For more information, see [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk). [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html). For details, see [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-db.html).

## Request Syntax
<a name="API_CreateDatabase_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "KmsKeyId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_CreateDatabase_RequestSyntax) **   <a name="timestream-CreateDatabase-request-DatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [KmsKeyId](#API_CreateDatabase_RequestSyntax) **   <a name="timestream-CreateDatabase-request-KmsKeyId"></a>
The AWS KMS key for the database. If the AWS KMS key is not specified, the database will be encrypted with a Timestream managed AWS KMS key located in your account. For more information, see [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Tags](#API_CreateDatabase_RequestSyntax) **   <a name="timestream-CreateDatabase-request-Tags"></a>
 A list of key-value pairs to label the table.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDatabase_ResponseSyntax"></a>

```
{
   "Database": {
      "Arn": "string",
      "CreationTime": number,
      "DatabaseName": "string",
      "KmsKeyId": "string",
      "LastUpdatedTime": number,
      "TableCount": number
   }
}
```

## Response Elements
<a name="API_CreateDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Database](#API_CreateDatabase_ResponseSyntax) **   <a name="timestream-CreateDatabase-response-Database"></a>
The newly created Timestream database.
Type: [Database](API_Database.md) object

## Errors
<a name="API_CreateDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** ConflictException **
Timestream was unable to process this request because it contains resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 The instance quota of resource exceeded for this account.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

 ** ValidationException **
 An invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/CreateDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/CreateDatabase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_UpdateLanguageModel.html
---

# UpdateLanguageModel
<a name="API_UpdateLanguageModel"></a>

Updates the encryption configuration for an existing custom language model. You can use this operation to change the AWS KMS key used to encrypt your model artifacts. The model artifacts are re-encrypted in place. No model training is required.

Your custom language model must not be in the `IN_PROGRESS` state when you call this operation. You cannot submit another update while a previous update is in progress. Use [DescribeLanguageModel](API_DescribeLanguageModel.md) to check the current state of your model.

Your custom language model remains available for transcription jobs while the update is being processed.

## Request Syntax
<a name="API_UpdateLanguageModel_RequestSyntax"></a>

```
{
   "DataAccessRoleArn": "{{string}}",
   "EncryptionConfiguration": {
      "KMSEncryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "KMSKey": "{{string}}"
   },
   "ModelName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLanguageModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataAccessRoleArn](#API_UpdateLanguageModel_RequestSyntax) **   <a name="transcribe-UpdateLanguageModel-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role. If you include `EncryptionConfiguration` in your request, this role must have permissions to access the specified AWS KMS key. If the role that you specify doesn't have the appropriate permissions, your request fails.
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`.
For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`
Required: No

 ** [EncryptionConfiguration](#API_UpdateLanguageModel_RequestSyntax) **   <a name="transcribe-UpdateLanguageModel-request-EncryptionConfiguration"></a>
Specifies the new encryption configuration for your custom language model. The model artifacts are re-encrypted in place using the specified AWS KMS key or with an AWS owned key if a key is not supplied.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [ModelName](#API_UpdateLanguageModel_RequestSyntax) **   <a name="transcribe-UpdateLanguageModel-request-ModelName"></a>
The name of the custom language model you want to update. Model names are case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateLanguageModel_ResponseSyntax"></a>

```
{
   "LastModifiedTime": number,
   "ModelName": "string",
   "ModelStatus": "string"
}
```

## Response Elements
<a name="API_UpdateLanguageModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastModifiedTime](#API_UpdateLanguageModel_ResponseSyntax) **   <a name="transcribe-UpdateLanguageModel-response-LastModifiedTime"></a>
The date and time the specified custom language model was last modified.
Type: Timestamp

 ** [ModelName](#API_UpdateLanguageModel_ResponseSyntax) **   <a name="transcribe-UpdateLanguageModel-response-ModelName"></a>
The name of the custom language model that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`

 ** [ModelStatus](#API_UpdateLanguageModel_ResponseSyntax) **   <a name="transcribe-UpdateLanguageModel-response-ModelStatus"></a>
The status of the specified custom language model.
Type: String
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`

## Errors
<a name="API_UpdateLanguageModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.
HTTP Status Code: 400

 ** ConflictException **
A resource already exists with this name. Resource names must be unique within an AWS account.
HTTP Status Code: 400

 ** InternalFailureException **
There was an internal error. Check the error message, correct the issue, and try your request again.
HTTP Status Code: 500

 ** LimitExceededException **
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.
HTTP Status Code: 400

 ** NotFoundException **
We can't find the requested resource. Check that the specified name is correct and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLanguageModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/UpdateLanguageModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/UpdateLanguageModel)

---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccessKey.html
---

# UpdateAccessKey
<a name="API_UpdateAccessKey"></a>

Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotation workflow.

If the `UserName` is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request. If a temporary access key is used, then `UserName` is required. If a long-term key is assigned to the user, then `UserName` is not required. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.

For information about rotating keys, see [Managing keys and certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_UpdateAccessKey_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccessKeyId **
The access key ID of the secret access key you want to update.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters that can consist of any upper or lowercased letter or digit.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** Status **
 The status you want to assign to the secret access key. `Active` means that the key can be used for programmatic calls to AWS, while `Inactive` means that the key cannot be used.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: Yes

 ** UserName **
The name of the user whose key you want to update.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## Errors
<a name="API_UpdateAccessKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_UpdateAccessKey_Examples"></a>

### Example
<a name="API_UpdateAccessKey_Example_1"></a>

This example illustrates one usage of UpdateAccessKey.

#### Sample Request
<a name="API_UpdateAccessKey_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateAccessKey
&UserName=Bob
&AccessKeyId=AKIAIOSFODNN7EXAMPLE
&Status=Inactive
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateAccessKey_Example_1_Response"></a>

```
<UpdateAccessKeyResponse>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</UpdateAccessKeyResponse>
```

## See Also
<a name="API_UpdateAccessKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateAccessKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateAccessKey)

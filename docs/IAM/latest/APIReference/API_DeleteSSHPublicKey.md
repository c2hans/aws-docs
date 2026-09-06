---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSSHPublicKey.html
---

# DeleteSSHPublicKey
<a name="API_DeleteSSHPublicKey"></a>

Deletes the specified SSH public key.

The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see [Set up CodeCommit for SSH connections](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html) in the *CodeCommit User Guide*.

## Request Parameters
<a name="API_DeleteSSHPublicKey_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SSHPublicKeyId **
The unique identifier for the SSH public key.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters that can consist of any upper or lowercased letter or digit.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** UserName **
The name of the IAM user associated with the SSH public key.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_DeleteSSHPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

## Examples
<a name="API_DeleteSSHPublicKey_Examples"></a>

### Example
<a name="API_DeleteSSHPublicKey_Example_1"></a>

This example illustrates one usage of DeleteSSHPublicKey.

#### Sample Request
<a name="API_DeleteSSHPublicKey_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=DeleteSSHPublicKey
&SSHPublicKeyId=APKAEIVFHP46CEXAMPLE
&UserName=Jane
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteSSHPublicKey_Example_1_Response"></a>

```
<DeleteSSHPublicKeyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>1a21282e-f36e-11e4-a53b-6b544EXAMPLE</RequestId>
  </ResponseMetadata>
</DeleteSSHPublicKeyResponse>
```

## See Also
<a name="API_DeleteSSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/DeleteSSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DeleteSSHPublicKey)

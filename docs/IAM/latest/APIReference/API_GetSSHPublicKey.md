---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSSHPublicKey.html
---

# GetSSHPublicKey
<a name="API_GetSSHPublicKey"></a>

Retrieves the specified SSH public key, including metadata about the key.

The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see [Set up CodeCommit for SSH connections](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html) in the *CodeCommit User Guide*.

## Request Parameters
<a name="API_GetSSHPublicKey_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Encoding **
Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
Type: String
Valid Values: `SSH | PEM`
Required: Yes

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

## Response Elements
<a name="API_GetSSHPublicKey_ResponseElements"></a>

The following element is returned by the service.

 ** SSHPublicKey **
A structure containing details about the SSH public key.
Type: [SSHPublicKey](API_SSHPublicKey.md) object

## Errors
<a name="API_GetSSHPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** UnrecognizedPublicKeyEncoding **
The request was rejected because the public key encoding format is unsupported or unrecognized.
HTTP Status Code: 400

## Examples
<a name="API_GetSSHPublicKey_Examples"></a>

### Example
<a name="API_GetSSHPublicKey_Example_1"></a>

This example illustrates one usage of GetSSHPublicKey.

#### Sample Request
<a name="API_GetSSHPublicKey_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetSSHPublicKey
&Encoding=PEM
&SSHPublicKeyId=APKAEIVFHP46CEXAMPLE
&UserName=Jane
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetSSHPublicKey_Example_1_Response"></a>

```
<GetSSHPublicKeyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetSSHPublicKeyResult>
    <SSHPublicKey>
      <UploadDate>2015-06-05T20:56:46Z</UploadDate>
      <Fingerprint>7a:1d:ea:9e:b0:80:ac:f8:ec:d8:dc:e6:a7:2c:fc:51</Fingerprint>
      <UserName>Jane</UserName>
      <SSHPublicKeyId>APKAEIVFHP46CEXAMPLE</SSHPublicKeyId>
      <Status>Active</Status>
      <SSHPublicKeyBody>
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsu+WpO9hhmqGTctHI1BE
        SJ/pq4GtAt9JJpIsDnjeB+mLbwnVJLFaaYzzoZuPOVhUc7yHMWjBLmfSEgJKfAH3
        n8m8R9D3UFoRC0rtKR2jJwAwFO3Tp9wgnqzvPtLMnG7uBEuD/nHStanrd6bbBv83
        kDSy5jiuc4yEWtTAEtyp8C8BxFTxHuCQ/sX4IbjtJ8M1IKZ3hjcJO5u6ooWCxZzQ
        hXXlPDniK/RZnO+YOaJR5umaAv23HAB7qx5H3A6WpyUyzXy0eTo9eAmUrET+JDXZ
        vqHufiDzO/MOCfb+KV1OJos2AxNtRuIFA1cTq7NF+upTIoV+gK1YJhCvjSuRkIJ/
        cwIDAQAB
        -----END PUBLIC KEY-----
      </SSHPublicKeyBody>
    </SSHPublicKey>
  </GetSSHPublicKeyResult>
  <ResponseMetadata>
    <RequestId>4817ee13-f36d-11e4-97db-33c4eEXAMPLE</RequestId>
  </ResponseMetadata>
</GetSSHPublicKeyResponse>
```

## See Also
<a name="API_GetSSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetSSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetSSHPublicKey)

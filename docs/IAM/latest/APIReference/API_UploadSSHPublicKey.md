---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSSHPublicKey.html
---

# UploadSSHPublicKey
<a name="API_UploadSSHPublicKey"></a>

Uploads an SSH public key and associates it with the specified IAM user.

The SSH public key uploaded by this operation can be used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see [Set up CodeCommit for SSH connections](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html) in the *CodeCommit User Guide*.

## Request Parameters
<a name="API_UploadSSHPublicKey_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SSHPublicKeyBody **
The SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public key is 2048 bits. For example, you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes long.
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** UserName **
The name of the IAM user to associate the SSH public key with.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Response Elements
<a name="API_UploadSSHPublicKey_ResponseElements"></a>

The following element is returned by the service.

 ** SSHPublicKey **
Contains information about the SSH public key.
Type: [SSHPublicKey](API_SSHPublicKey.md) object

## Errors
<a name="API_UploadSSHPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateSSHPublicKey **
The request was rejected because the SSH public key is already associated with the specified IAM user.
HTTP Status Code: 400

 ** InvalidPublicKey **
The request was rejected because the public key is malformed or otherwise invalid.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** UnrecognizedPublicKeyEncoding **
The request was rejected because the public key encoding format is unsupported or unrecognized.
HTTP Status Code: 400

## Examples
<a name="API_UploadSSHPublicKey_Examples"></a>

### Example
<a name="API_UploadSSHPublicKey_Example_1"></a>

This example illustrates one usage of UploadSSHPublicKey.

#### Sample Request
<a name="API_UploadSSHPublicKey_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UploadSSHPublicKey
&SSHPublicKeyBody=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCy75ak72GGaoZNy0cjUERIn
+mrga0C30kmkiwOeN4H6YtvCdUksVppjPOhm485WFRzvIcxaMEuZ9ISAkp8AfefybxH0PdQWhELSu0p
HaMnADAU7dOn3CCerO8+0sycbu4ES4P+cdK1qet3ptsG/zeQNLLmOK5zjIRa1MAS3KnwLwHEVPEe4JD
+xfghuO0nwzUgpneGNwk7m7qihYLFnNCFdeU8OeIr9Fmc75g5olHm6ZoC/bccAHurHkfcDpanJTLNfL
R5Oj14CZSsRP4kNdm+oe5+IPM78w4J9v4pXU4mizYDE21G4gUDVxOrs0X66lMihX6ArVgmEK+NK5GQg
n9z jane@example.com
&UserName=Jane
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UploadSSHPublicKey_Example_1_Response"></a>

```
<UploadSSHPublicKeyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <UploadSSHPublicKeyResult>
    <PublicKey>
      <UploadDate>2015-06-05T20:56:46.012Z</UploadDate>
      <Fingerprint>7a:1d:ea:9e:b0:80:ac:f8:ec:d8:dc:e6:a7:2c:fc:51</Fingerprint>
      <UserName>Jane</UserName>
      <SSHPublicKeyId>APKAEIVFHP46CEXAMPLE</SSHPublicKeyId>
      <Status>Active</Status>
      <SSHPublicKeyBody>
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCy75ak72GGaoZNy0cjUERIn+mrga0C30k
        mkiwOeN4H6YtvCdUksVppjPOhm485WFRzvIcxaMEuZ9ISAkp8AfefybxH0PdQWhELSu0pHa
        MnADAU7dOn3CCerO8+0sycbu4ES4P+cdK1qet3ptsG/zeQNLLmOK5zjIRa1MAS3KnwLwHEV
        PEe4JD+xfghuO0nwzUgpneGNwk7m7qihYLFnNCFdeU8OeIr9Fmc75g5olHm6ZoC/bccAHur
        HkfcDpanJTLNfLR5Oj14CZSsRP4kNdm+oe5+IPM78w4J9v4pXU4mizYDE21G4gUDVxOrs0X
        66lMihX6ArVgmEK+NK5GQgn9z jane@example.com
      </SSHPublicKeyBody>
    </PublicKey>
  </UploadSSHPublicKeyResult>
  <ResponseMetadata>
    <RequestId>3da97a2f-f369-11e4-97ab-c53b2EXAMPLE</RequestId>
  </ResponseMetadata>
</UploadSSHPublicKeyResponse>
```

## See Also
<a name="API_UploadSSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UploadSSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UploadSSHPublicKey)

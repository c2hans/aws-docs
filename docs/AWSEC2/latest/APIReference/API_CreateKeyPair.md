---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html
---

# CreateKeyPair
<a name="API_CreateKeyPair"></a>

Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the specified format. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS\#1 private key or an unencrypted PPK formatted private key for use with PuTTY. If a key with the specified name already exists, Amazon EC2 returns an error.

The key pair returned to you is available only in the AWS Region in which you create it. If you prefer, you can create your own key pair using a third-party tool and upload it to any Region using [ImportKeyPair](API_ImportKeyPair.md).

You can have up to 5,000 key pairs per AWS Region.

For more information, see [Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateKeyPair_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **KeyFormat**
The format of the key pair.
Default: `pem`
Type: String
Valid Values: `pem | ppk`
Required: No

 **KeyName**
A unique name for the key pair.
Constraints: Up to 255 ASCII characters
Type: String
Required: Yes

 **KeyType**
The type of key pair. Note that ED25519 keys are not supported for Windows instances.
Default: `rsa`
Type: String
Valid Values: `rsa | ed25519`
Required: No

 **TagSpecification.N**
The tags to apply to the new key pair.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateKeyPair_ResponseElements"></a>

The following elements are returned by the service.

 **keyFingerprint**
+ For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.
+ For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with OpenSSH 6.8.
Type: String

 **keyMaterial**
An unencrypted PEM encoded RSA or ED25519 private key.
Type: String

 **keyName**
The name of the key pair.
Type: String

 **keyPairId**
The ID of the key pair.
Type: String

 **requestId**
The ID of the request.
Type: String

 **tagSet**
Any tags applied to the key pair.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateKeyPair_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateKeyPair_Examples"></a>

### Example
<a name="API_CreateKeyPair_Example_1"></a>

This example request creates a key pair named `my-key-pair`, and applies a tag with a key of `purpose` and a value of `production`.

#### Sample Request
<a name="API_CreateKeyPair_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateKeyPair
&KeyName=my-key-pair
&TagSpecification.1.ResourceType=key-pair
&TagSpecification.1.Tag.1.Key=purpose
&TagSpecification.1.Tag.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateKeyPair_Example_1_Response"></a>

```
<CreateKeyPairResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>1b5b5bcf-3670-4c16-83d7-c2c9example</requestId>
  <keyName>my-key-pair</keyName>
  <keyPairId>key-abcd12345eEXAMPLE</keyPairId>
  <keyFingerprint>1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f</keyFingerprint>
  <keyMaterial>---- BEGIN RSA PRIVATE KEY ----
MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE
-----END RSA PRIVATE KEY-----</keyMaterial>
  <tagSet>
    <item>
      <key>purpose</key>
      <value>production</value>
    </item>
  </tagSet>
</CreateKeyPairResponse>
```

### Saving the file
<a name="API_CreateKeyPair_Example_2"></a>

Create a file named `my-key-pair.pem` and paste the entire key from the response into this file. Keep this file in a safe place; it is required to decrypt login information when you connect to an instance that you launched using this key pair. If you're using an SSH client on a Linux computer to connect to your instance, use the following command to set the permissions of your private key file so that only you can read it.

#### Sample Request
<a name="API_CreateKeyPair_Example_2_Request"></a>

```
chmod 400 my-key-pair.pem
```

## See Also
<a name="API_CreateKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateKeyPair)

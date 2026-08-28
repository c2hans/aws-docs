---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html
---

# ImportKeyPair
<a name="API_ImportKeyPair"></a>

Imports the public key from an RSA or ED25519 key pair that you created using a third-party tool. You give AWS only the public key. The private key is never transferred between you and AWS.

For more information about the requirements for importing a key pair, see [Create a key pair and import the public key to Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ImportKeyPair_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **KeyName**
A unique name for the key pair.
Type: String
Required: Yes

 **PublicKeyMaterial**
The public key.
Type: Base64-encoded binary data object
Required: Yes

 **TagSpecification.N**
The tags to apply to the imported key pair.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_ImportKeyPair_ResponseElements"></a>

The following elements are returned by the service.

 **keyFingerprint**
+ For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC 4716.
+ For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with [OpenSSH 6.8](http://www.openssh.com/txt/release-6.8).
Type: String

 **keyName**
The key pair name that you provided.
Type: String

 **keyPairId**
The ID of the resulting key pair.
Type: String

 **requestId**
The ID of the request.
Type: String

 **tagSet**
The tags applied to the imported key pair.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ImportKeyPair_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ImportKeyPair_Examples"></a>

### Example
<a name="API_ImportKeyPair_Example_1"></a>

This example imports the public key named `my-key-pair`, and applies a tag with a key of `purpose` and a value of `production`.

#### Sample Request
<a name="API_ImportKeyPair_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ImportKeyPair
&KeyName=my-key-pair
&PublicKeyMaterial=MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
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
&TagSpecification.1.ResourceType=key-pair
&TagSpecification.1.Tag.1.Key=purpose
&TagSpecification.1.Tag.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_ImportKeyPair_Example_1_Response"></a>

```
<ImportKeyPairResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <keyName>my-key-pair</keyName>
    <keyPairId>key-abced1234eEXAMPLE</keyPairId>
    <keyFingerprint>1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f</keyFingerprint>
    <tagSet>
        <item>
            <key>purpose</key>
            <value>production</value>
        </item>
    </tagSet>
</ImportKeyPairResponse>
```

## See Also
<a name="API_ImportKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ImportKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportKeyPair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

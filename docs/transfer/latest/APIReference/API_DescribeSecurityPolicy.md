---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribeSecurityPolicy.html
---

# DescribeSecurityPolicy
<a name="API_DescribeSecurityPolicy"></a>

Describes the security policy that is attached to your server or SFTP connector. The response contains a description of the security policy's properties. For more information about security policies, see [Working with security policies for servers](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html) or [Working with security policies for SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html).

## Request Syntax
<a name="API_DescribeSecurityPolicy_RequestSyntax"></a>

```
{
   "SecurityPolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSecurityPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecurityPolicyName](#API_DescribeSecurityPolicy_RequestSyntax) **   <a name="TransferFamily-DescribeSecurityPolicy-request-SecurityPolicyName"></a>
Specify the text name of the security policy for which you want the details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `Transfer[A-Za-z0-9]*SecurityPolicy-[A-Za-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeSecurityPolicy_ResponseSyntax"></a>

```
{
   "SecurityPolicy": {
      "Fips": boolean,
      "Protocols": [ "string" ],
      "SecurityPolicyName": "string",
      "SshCiphers": [ "string" ],
      "SshHostKeyAlgorithms": [ "string" ],
      "SshKexs": [ "string" ],
      "SshMacs": [ "string" ],
      "TlsCiphers": [ "string" ],
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeSecurityPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecurityPolicy](#API_DescribeSecurityPolicy_ResponseSyntax) **   <a name="TransferFamily-DescribeSecurityPolicy-response-SecurityPolicy"></a>
An array containing the properties of the security policy.
Type: [DescribedSecurityPolicy](API_DescribedSecurityPolicy.md) object

## Errors
<a name="API_DescribeSecurityPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

## Examples
<a name="API_DescribeSecurityPolicy_Examples"></a>

### Example
<a name="API_DescribeSecurityPolicy_Example_1"></a>

The following example command takes the security policy name as an argument, and returns the algorithms for the specified security policy.

#### Sample Request
<a name="API_DescribeSecurityPolicy_Example_1_Request"></a>

```
aws transfer describe-security-policy --security-policy-name "TransferSecurityPolicy-FIPS-2023-05"
```

#### Sample Response
<a name="API_DescribeSecurityPolicy_Example_1_Response"></a>

```
{
    "SecurityPolicy": {
        "Fips": true,
        "SecurityPolicyName": "TransferSecurityPolicy-FIPS-2023-05",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ]
    }
}
```

## See Also
<a name="API_DescribeSecurityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/DescribeSecurityPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribeSecurityPolicy)

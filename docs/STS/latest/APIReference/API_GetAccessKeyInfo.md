---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html
---

# GetAccessKeyInfo
<a name="API_GetAccessKeyInfo"></a>

Returns the account identifier for the specified access key ID.

Access keys consist of two parts: an access key ID (for example, `AKIAIOSFODNN7EXAMPLE`) and a secret access key (for example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). For more information about access keys, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.

When you pass an access key ID to this operation, it returns the ID of the AWS account to which the keys belong. Access key IDs beginning with `AKIA` are long-term credentials for an IAM user or the AWS account root user. Access key IDs beginning with `ASIA` are temporary credentials that are created using AWS STS operations. If the account in the response belongs to you, you can sign in as the root user and review your root user access keys. Then, you can pull a [credentials report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) to learn which IAM user owns the keys. To learn who requested the temporary credentials for an `ASIA` access key, view the AWS STS events in your [CloudTrail logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html) in the *IAM User Guide*.

This operation does not indicate the state of the access key. The key might be active, inactive, or deleted. Active keys might not have permissions to perform an operation. Providing a deleted access key might return an error that the key doesn't exist.

## Request Parameters
<a name="API_GetAccessKeyInfo_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccessKeyId **
The identifier of an access key.
This parameter allows (through its regex pattern) a string of characters that can consist of any upper- or lowercase letter or digit.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]*`
Required: Yes

## Response Elements
<a name="API_GetAccessKeyInfo_ResponseElements"></a>

The following element is returned by the service.

 ** Account **
The number used to identify the AWS account.
Type: String

## Errors
<a name="API_GetAccessKeyInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetAccessKeyInfo_Examples"></a>

### Example
<a name="API_GetAccessKeyInfo_Example_1"></a>

This example illustrates one usage of GetAccessKeyInfo.

#### Sample Request
<a name="API_GetAccessKeyInfo_Example_1_Request"></a>

```
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=GetAccessKeyInfo
&AccessKeyId=AKIAI44QH8DHBEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccessKeyInfo_Example_1_Response"></a>

```
<GetAccessKeyInfoResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <GetAccessKeyInfoResult>
    <Account>111122223333</Account>
  </GetAccessKeyInfoResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</GetAccessKeyInfoResponse>
```

## See Also
<a name="API_GetAccessKeyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/GetAccessKeyInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/GetAccessKeyInfo)

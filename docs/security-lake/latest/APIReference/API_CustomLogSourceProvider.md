---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceProvider.html
---

# CustomLogSourceProvider
<a name="API_CustomLogSourceProvider"></a>

The details of the log provider for a third-party custom source.

## Contents
<a name="API_CustomLogSourceProvider_Contents"></a>

 ** location **   <a name="securitylake-Type-CustomLogSourceProvider-location"></a>
The location of the partition in the Amazon S3 bucket for Security Lake.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3[an]?://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^/].*)+`
Required: No

 ** roleArn **   <a name="securitylake-Type-CustomLogSourceProvider-roleArn"></a>
The ARN of the IAM role to be used by the entity putting logs into your custom source partition. Security Lake will apply the correct access policies to this role, but you must first manually create the trust policy for this role. The IAM role name must start with the text 'Security Lake'. The IAM role must trust the `logProviderAccountId` to assume the role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_CustomLogSourceProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CustomLogSourceProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CustomLogSourceProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CustomLogSourceProvider)

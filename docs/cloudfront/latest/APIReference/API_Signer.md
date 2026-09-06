---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Signer.html
---

# Signer
<a name="API_Signer"></a>

A list of AWS accounts and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs and signed cookies.

## Contents
<a name="API_Signer_Contents"></a>

 ** AwsAccountNumber **   <a name="cloudfront-Type-Signer-AwsAccountNumber"></a>
An AWS account number that contains active CloudFront key pairs that CloudFront can use to verify the signatures of signed URLs and signed cookies. If the AWS account that owns the key pairs is the same account that owns the CloudFront distribution, the value of this field is `self`.
Type: String
Required: No

 ** KeyPairIds **   <a name="cloudfront-Type-Signer-KeyPairIds"></a>
A list of CloudFront key pair identifiers.
Type: [KeyPairIds](API_KeyPairIds.md) object
Required: No

## See Also
<a name="API_Signer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Signer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Signer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Signer)

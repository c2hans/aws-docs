---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_PolicyDescriptorType.html
---

# PolicyDescriptorType
<a name="API_PolicyDescriptorType"></a>

A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.

## Contents
<a name="API_PolicyDescriptorType_Contents"></a>

 ** arn **
The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`
Required: No

## See Also
<a name="API_PolicyDescriptorType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/PolicyDescriptorType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/PolicyDescriptorType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/PolicyDescriptorType)

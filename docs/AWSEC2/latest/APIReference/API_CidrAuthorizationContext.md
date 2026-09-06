---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CidrAuthorizationContext.html
---

# CidrAuthorizationContext
<a name="API_CidrAuthorizationContext"></a>

Provides authorization for Amazon to bring a specific IP address range to a specific AWS account using bring your own IP addresses (BYOIP). For more information, see [Configuring your BYOIP address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#prepare-for-byoip) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_CidrAuthorizationContext_Contents"></a>

 ** Message **
The plain-text authorization message for the prefix and account.
Type: String
Required: Yes

 ** Signature **
The signed authorization message for the prefix and account.
Type: String
Required: Yes

## See Also
<a name="API_CidrAuthorizationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CidrAuthorizationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CidrAuthorizationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CidrAuthorizationContext)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClassicLinkInstance.html
---

# ClassicLinkInstance
<a name="API_ClassicLinkInstance"></a>

**Note**
Deprecated.

Describes a linked EC2-Classic instance.

## Contents
<a name="API_ClassicLinkInstance_Contents"></a>

 ** GroupSet.N **
The security groups.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_ClassicLinkInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClassicLinkInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClassicLinkInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClassicLinkInstance)

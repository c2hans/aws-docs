---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceEventWindowAssociationTarget.html
---

# InstanceEventWindowAssociationTarget
<a name="API_InstanceEventWindowAssociationTarget"></a>

One or more targets associated with the event window.

## Contents
<a name="API_InstanceEventWindowAssociationTarget_Contents"></a>

 ** DedicatedHostIdSet.N **
The IDs of the Dedicated Hosts associated with the event window.
Type: Array of strings
Required: No

 ** InstanceIdSet.N **
The IDs of the instances associated with the event window.
Type: Array of strings
Required: No

 ** TagSet.N **
The instance tags associated with the event window. Any instances associated with the tags will be associated with the event window.
Note that while you can't create tag keys beginning with `aws:`, you can specify existing AWS managed tag keys (with the `aws:` prefix) when specifying them as targets to associate with the event window.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceEventWindowAssociationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceEventWindowAssociationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceEventWindowAssociationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceEventWindowAssociationTarget)

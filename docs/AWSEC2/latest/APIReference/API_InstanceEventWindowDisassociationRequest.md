---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceEventWindowDisassociationRequest.html
---

# InstanceEventWindowDisassociationRequest
<a name="API_InstanceEventWindowDisassociationRequest"></a>

The targets to disassociate from the specified event window.

## Contents
<a name="API_InstanceEventWindowDisassociationRequest_Contents"></a>

 ** DedicatedHostId.N **
The IDs of the Dedicated Hosts to disassociate from the event window.
Type: Array of strings
Required: No

 ** InstanceId.N **
The IDs of the instances to disassociate from the event window.
Type: Array of strings
Required: No

 ** InstanceTag.N **
The instance tags to disassociate from the event window. Any instances associated with the tags will be disassociated from the event window.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceEventWindowDisassociationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceEventWindowDisassociationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceEventWindowDisassociationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceEventWindowDisassociationRequest)

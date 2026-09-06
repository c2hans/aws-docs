---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamResourceDiscoveryAssociation.html
---

# IpamResourceDiscoveryAssociation
<a name="API_IpamResourceDiscoveryAssociation"></a>

An IPAM resource discovery association. An associated resource discovery is a resource discovery that has been associated with an IPAM. IPAM aggregates the resource CIDRs discovered by the associated resource discovery.

## Contents
<a name="API_IpamResourceDiscoveryAssociation_Contents"></a>

 ** ipamArn **
The IPAM ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamId **
The IPAM ID.
Type: String
Required: No

 ** ipamRegion **
The IPAM home Region.
Type: String
Required: No

 ** ipamResourceDiscoveryAssociationArn **
The resource discovery association Amazon Resource Name (ARN).
Type: String
Required: No

 ** ipamResourceDiscoveryAssociationId **
The resource discovery association ID.
Type: String
Required: No

 ** ipamResourceDiscoveryId **
The resource discovery ID.
Type: String
Required: No

 ** isDefault **
Defines if the resource discovery is the default. When you create an IPAM, a default resource discovery is created for your IPAM and it's associated with your IPAM.
Type: Boolean
Required: No

 ** ownerId **
The AWS account ID of the resource discovery owner.
Type: String
Required: No

 ** resourceDiscoveryStatus **
The resource discovery status.
+  `active` - Connection or permissions required to read the results of the resource discovery are intact.
+  `not-found` - Connection or permissions required to read the results of the resource discovery are broken. This may happen if the owner of the resource discovery stopped sharing it or deleted the resource discovery. Verify the resource discovery still exists and the AWS RAM resource share is still intact.
Type: String
Valid Values: `active | not-found`
Required: No

 ** state **
The lifecycle state of the association when you associate or disassociate a resource discovery.
+  `associate-in-progress` - Resource discovery is being associated.
+  `associate-complete` - Resource discovery association is complete.
+  `associate-failed` - Resource discovery association has failed.
+  `disassociate-in-progress` - Resource discovery is being disassociated.
+  `disassociate-complete` - Resource discovery disassociation is complete.
+  `disassociate-failed ` - Resource discovery disassociation has failed.
+  `isolate-in-progress` - AWS account that created the resource discovery association has been removed and the resource discovery association is being isolated.
+  `isolate-complete` - Resource discovery isolation is complete.
+  `restore-in-progress` - Resource discovery is being restored.
Type: String
Valid Values: `associate-in-progress | associate-complete | associate-failed | disassociate-in-progress | disassociate-complete | disassociate-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** TagSet.N **
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamResourceDiscoveryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamResourceDiscoveryAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamResourceDiscoveryAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamResourceDiscoveryAssociation)

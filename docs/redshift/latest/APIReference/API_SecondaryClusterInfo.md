---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_SecondaryClusterInfo.html
---

# SecondaryClusterInfo
<a name="API_SecondaryClusterInfo"></a>

The AvailabilityZone and ClusterNodes information of the secondary compute unit.

## Contents
<a name="API_SecondaryClusterInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityZone **
The name of the Availability Zone in which the secondary compute unit of the cluster is located.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ClusterNodes.member.N **
The nodes in the secondary compute unit.
Type: Array of [ClusterNode](API_ClusterNode.md) objects
Required: No

## See Also
<a name="API_SecondaryClusterInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/SecondaryClusterInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/SecondaryClusterInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/SecondaryClusterInfo)

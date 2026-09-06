---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageEksClusterDetails.html
---

# CoverageEksClusterDetails
<a name="API_CoverageEksClusterDetails"></a>

Information about the EKS cluster that has a coverage status.

## Contents
<a name="API_CoverageEksClusterDetails_Contents"></a>

 ** addonDetails **   <a name="guardduty-Type-CoverageEksClusterDetails-addonDetails"></a>
Information about the installed EKS add-on.
Type: [AddonDetails](API_AddonDetails.md) object
Required: No

 ** clusterName **   <a name="guardduty-Type-CoverageEksClusterDetails-clusterName"></a>
Name of the EKS cluster.
Type: String
Required: No

 ** compatibleNodes **   <a name="guardduty-Type-CoverageEksClusterDetails-compatibleNodes"></a>
Represents all the nodes within the EKS cluster in your account.
Type: Long
Required: No

 ** coveredNodes **   <a name="guardduty-Type-CoverageEksClusterDetails-coveredNodes"></a>
Represents the nodes within the EKS cluster that have a `HEALTHY` coverage status.
Type: Long
Required: No

 ** managementType **   <a name="guardduty-Type-CoverageEksClusterDetails-managementType"></a>
Indicates how the Amazon EKS add-on GuardDuty agent is managed for this EKS cluster.
 `AUTO_MANAGED` indicates GuardDuty deploys and manages updates for this resource.
 `MANUAL` indicates that you are responsible to deploy, update, and manage the Amazon EKS add-on GuardDuty agent for this resource.
Type: String
Valid Values: `AUTO_MANAGED | MANUAL | DISABLED`
Required: No

## See Also
<a name="API_CoverageEksClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageEksClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageEksClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageEksClusterDetails)

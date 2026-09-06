---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FargateDetails.html
---

# FargateDetails
<a name="API_FargateDetails"></a>

Contains information about AWS Fargate details associated with an Amazon ECS cluster.

## Contents
<a name="API_FargateDetails_Contents"></a>

 ** issues **   <a name="guardduty-Type-FargateDetails-issues"></a>
Runtime coverage issues identified for the resource running on AWS Fargate.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** managementType **   <a name="guardduty-Type-FargateDetails-managementType"></a>
Indicates how the GuardDuty security agent is managed for this resource.
+  `AUTO_MANAGED` indicates that GuardDuty deploys and manages updates for this resource.
+  `DISABLED` indicates that the deployment of the GuardDuty security agent is disabled for this resource.
The `MANUAL` status doesn't apply to the AWS Fargate (Amazon ECS only) woprkloads.
Type: String
Valid Values: `AUTO_MANAGED | MANUAL | DISABLED`
Required: No

## See Also
<a name="API_FargateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FargateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FargateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FargateDetails)

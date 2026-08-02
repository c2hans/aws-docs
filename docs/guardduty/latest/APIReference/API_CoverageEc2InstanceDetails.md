---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageEc2InstanceDetails.html
---

# CoverageEc2InstanceDetails
<a name="API_CoverageEc2InstanceDetails"></a>

Contains information about the Amazon EC2 instance runtime coverage details.

## Contents
<a name="API_CoverageEc2InstanceDetails_Contents"></a>

 ** agentDetails **   <a name="guardduty-Type-CoverageEc2InstanceDetails-agentDetails"></a>
Information about the installed security agent.
Type: [AgentDetails](API_AgentDetails.md) object
Required: No

 ** clusterArn **   <a name="guardduty-Type-CoverageEc2InstanceDetails-clusterArn"></a>
The cluster ARN of the Amazon ECS cluster running on the Amazon EC2 instance.
Type: String
Required: No

 ** instanceId **   <a name="guardduty-Type-CoverageEc2InstanceDetails-instanceId"></a>
The Amazon EC2 instance ID.
Type: String
Required: No

 ** instanceType **   <a name="guardduty-Type-CoverageEc2InstanceDetails-instanceType"></a>
The instance type of the Amazon EC2 instance.
Type: String
Required: No

 ** managementType **   <a name="guardduty-Type-CoverageEc2InstanceDetails-managementType"></a>
Indicates how the GuardDuty security agent is managed for this resource.
+  `AUTO_MANAGED` indicates that GuardDuty deploys and manages updates for this resource.
+  `MANUAL` indicates that you are responsible to deploy, update, and manage the GuardDuty security agent updates for this resource.
The `DISABLED` status doesn't apply to Amazon EC2 instances and Amazon EKS clusters.
Type: String
Valid Values: `AUTO_MANAGED | MANUAL | DISABLED`
Required: No

## See Also
<a name="API_CoverageEc2InstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageEc2InstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageEc2InstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageEc2InstanceDetails)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceStatus.html
---

# InstanceStatus
<a name="API_InstanceStatus"></a>

Describes the status of an instance, including system status, instance status, attached EBS status, and application status.

## Contents
<a name="API_InstanceStatus_Contents"></a>

 ** applicationStatus **
Reports the application-level health status for the instance.
Type: [ApplicationStatusSummary](API_ApplicationStatusSummary.md) object
Required: No

 ** attachedEbsStatus **
Reports impaired functionality that stems from an attached Amazon EBS volume that is unreachable and unable to complete I/O operations.
Type: [EbsStatusSummary](API_EbsStatusSummary.md) object
Required: No

 ** availabilityZone **
The Availability Zone of the instance.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone of the instance.
Type: String
Required: No

 ** EventsSet.N **
Any scheduled events associated with the instance.
Type: Array of [InstanceStatusEvent](API_InstanceStatusEvent.md) objects
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** instanceState **
The intended state of the instance. [DescribeInstanceStatus](API_DescribeInstanceStatus.md) requires that an instance be in the `running` state.
Type: [InstanceState](API_InstanceState.md) object
Required: No

 ** instanceStatus **
Reports impaired functionality that stems from issues internal to the instance, such as impaired reachability.
Type: [InstanceStatusSummary](API_InstanceStatusSummary.md) object
Required: No

 ** operator **
The service provider that manages the instance.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** systemStatus **
Reports impaired functionality that stems from issues related to the systems that support an instance, such as hardware failures and network connectivity problems.
Type: [InstanceStatusSummary](API_InstanceStatusSummary.md) object
Required: No

## See Also
<a name="API_InstanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

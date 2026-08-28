---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ContainerInstanceDetails.html
---

# ContainerInstanceDetails
<a name="API_ContainerInstanceDetails"></a>

Contains information about the Amazon EC2 instance that is running the Amazon ECS container.

## Contents
<a name="API_ContainerInstanceDetails_Contents"></a>

 ** compatibleContainerInstances **   <a name="guardduty-Type-ContainerInstanceDetails-compatibleContainerInstances"></a>
Represents total number of nodes in the Amazon ECS cluster.
Type: Long
Required: No

 ** coveredContainerInstances **   <a name="guardduty-Type-ContainerInstanceDetails-coveredContainerInstances"></a>
Represents the nodes in the Amazon ECS cluster that has a `HEALTHY` coverage status.
Type: Long
Required: No

## See Also
<a name="API_ContainerInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ContainerInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ContainerInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ContainerInstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

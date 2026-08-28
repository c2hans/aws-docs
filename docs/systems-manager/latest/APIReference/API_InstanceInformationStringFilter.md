---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceInformationStringFilter.html
---

# InstanceInformationStringFilter
<a name="API_InstanceInformationStringFilter"></a>

The filters to describe or get information about your managed nodes.

## Contents
<a name="API_InstanceInformationStringFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-InstanceInformationStringFilter-Key"></a>
The filter key name to describe your managed nodes.
Valid filter key values: ActivationIds \| AgentVersion \| AssociationStatus \| IamRole \| InstanceIds \| PingStatus \| PlatformTypes \| ResourceType \| SourceIds \| SourceTypes \| "tag-key" \| "tag:`{keyname}`
+ Valid values for the `AssociationStatus` filter key: Success \| Pending \| Failed
+ Valid values for the `PingStatus` filter key: Online \| ConnectionLost \| Inactive (deprecated)
+ Valid values for the `PlatformTypes` filter key: Windows \| Linux \| MacOS
+ Valid values for the `ResourceType` filter key: EC2Instance \| ManagedInstance
+ Valid values for the `SourceType` filter key: AWS::EC2::Instance \| AWS::SSM::ManagedInstance \| AWS::IoT::Thing \| Microsoft.Compute/virtualMachines
+ Valid tag examples: `Key=tag-key,Values=Purpose` \| `Key=tag:Purpose,Values=Test`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Values **   <a name="systemsmanager-Type-InstanceInformationStringFilter-Values"></a>
The filter values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_InstanceInformationStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceInformationStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceInformationStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceInformationStringFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

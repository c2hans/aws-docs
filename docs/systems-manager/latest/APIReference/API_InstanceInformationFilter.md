---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceInformationFilter.html
---

# InstanceInformationFilter
<a name="API_InstanceInformationFilter"></a>

Describes a filter for a specific list of managed nodes. You can filter node information by using tags. You specify tags by using a key-value mapping.

Use this operation instead of the [DescribeInstanceInformation:InstanceInformationFilterList](API_DescribeInstanceInformation.md#systemsmanager-DescribeInstanceInformation-request-InstanceInformationFilterList) method. The `InstanceInformationFilterList` method is a legacy method and doesn't support tags.

## Contents
<a name="API_InstanceInformationFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-InstanceInformationFilter-key"></a>
The name of the filter.
Type: String
Valid Values: `InstanceIds | AgentVersion | PingStatus | PlatformTypes | ActivationIds | IamRole | ResourceType | AssociationStatus`
Required: Yes

 ** valueSet **   <a name="systemsmanager-Type-InstanceInformationFilter-valueSet"></a>
The filter values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_InstanceInformationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceInformationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceInformationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceInformationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

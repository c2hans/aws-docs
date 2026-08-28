---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfigurationItem.html
---

# GroupConfigurationItem
<a name="API_GroupConfigurationItem"></a>

An item in a group configuration. A group service configuration can have one or more items. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).

## Contents
<a name="API_GroupConfigurationItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="ARG-Type-GroupConfigurationItem-Type"></a>
Specifies the type of group configuration item. Each item must have a unique value for `type`. For the list of types that you can specify for a configuration item, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types).
Type: String
Length Constraints: Maximum length of 40.
Pattern: `AWS::[a-zA-Z0-9]+::[a-zA-Z0-9]+`
Required: Yes

 ** Parameters **   <a name="ARG-Type-GroupConfigurationItem-Parameters"></a>
A collection of parameters for this group configuration item. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types).
Type: Array of [GroupConfigurationParameter](API_GroupConfigurationParameter.md) objects
Required: No

## See Also
<a name="API_GroupConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupConfigurationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

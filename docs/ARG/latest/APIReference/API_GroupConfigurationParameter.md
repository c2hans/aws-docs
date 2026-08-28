---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfigurationParameter.html
---

# GroupConfigurationParameter
<a name="API_GroupConfigurationParameter"></a>

A parameter for a group configuration item. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).

## Contents
<a name="API_GroupConfigurationParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="ARG-Type-GroupConfigurationParameter-Name"></a>
The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-z-]+`
Required: Yes

 ** Values **   <a name="ARG-Type-GroupConfigurationParameter-Values"></a>
The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9:\/\._-]+`
Required: No

## See Also
<a name="API_GroupConfigurationParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupConfigurationParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupConfigurationParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupConfigurationParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

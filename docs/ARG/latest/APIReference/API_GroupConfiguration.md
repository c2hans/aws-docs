---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfiguration.html
---

# GroupConfiguration
<a name="API_GroupConfiguration"></a>

A service configuration associated with a resource group. The configuration options are determined by the AWS service that defines the `Type`, and specifies which resources can be included in the group. You can add a service configuration when you create the group by using [CreateGroup](API_CreateGroup.md), or later by using the [PutGroupConfiguration](API_PutGroupConfiguration.md) operation. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).

## Contents
<a name="API_GroupConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Configuration **   <a name="ARG-Type-GroupConfiguration-Configuration"></a>
The configuration currently associated with the group and in effect.
Type: Array of [GroupConfigurationItem](API_GroupConfigurationItem.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** FailureReason **   <a name="ARG-Type-GroupConfiguration-FailureReason"></a>
If present, the reason why a request to update the group configuration failed.
Type: String
Required: No

 ** ProposedConfiguration **   <a name="ARG-Type-GroupConfiguration-ProposedConfiguration"></a>
If present, the new configuration that is in the process of being applied to the group.
Type: Array of [GroupConfigurationItem](API_GroupConfigurationItem.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** Status **   <a name="ARG-Type-GroupConfiguration-Status"></a>
The current status of an attempt to update the group configuration.
Type: String
Valid Values: `UPDATING | UPDATE_COMPLETE | UPDATE_FAILED`
Required: No

## See Also
<a name="API_GroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

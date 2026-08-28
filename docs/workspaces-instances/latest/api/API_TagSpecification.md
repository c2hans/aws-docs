---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_TagSpecification.html
---

# TagSpecification
<a name="API_TagSpecification"></a>

Defines tagging configuration for a resource.

## Contents
<a name="API_TagSpecification_Contents"></a>

 ** ResourceType **   <a name="workspacesinstances-Type-TagSpecification-ResourceType"></a>
Type of resource being tagged.
Type: String
Valid Values: `instance | volume | spot-instances-request | network-interface`
Required: No

 ** Tags **   <a name="workspacesinstances-Type-TagSpecification-Tags"></a>
Collection of tags for the specified resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_TagSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/TagSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/TagSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/TagSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

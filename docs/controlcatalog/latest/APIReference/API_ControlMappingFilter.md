---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlMappingFilter.html
---

# ControlMappingFilter
<a name="API_ControlMappingFilter"></a>

A structure that defines filtering criteria for the ListControlMappings operation. You can use this filter to narrow down the list of control mappings based on control ARNs, common control ARNs, or mapping types.

## Contents
<a name="API_ControlMappingFilter_Contents"></a>

 ** CommonControlArns **   <a name="controlcatalog-Type-ControlMappingFilter-CommonControlArns"></a>
A list of common control ARNs to filter the mappings. When specified, only mappings associated with these common controls are returned.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 41. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):controlcatalog:::common-control/[0-9a-z]+`
Required: No

 ** ControlArns **   <a name="controlcatalog-Type-ControlMappingFilter-ControlArns"></a>
A list of control ARNs to filter the mappings. When specified, only mappings associated with these controls are returned.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
Required: No

 ** MappingTypes **   <a name="controlcatalog-Type-ControlMappingFilter-MappingTypes"></a>
A list of mapping types to filter the mappings. When specified, only mappings of these types are returned.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `FRAMEWORK | COMMON_CONTROL | RELATED_CONTROL`
Required: No

## See Also
<a name="API_ControlMappingFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ControlMappingFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ControlMappingFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ControlMappingFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

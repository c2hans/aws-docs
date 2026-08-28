---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlMapping.html
---

# ControlMapping
<a name="API_ControlMapping"></a>

A structure that contains information about a control mapping, including the control ARN, mapping type, and mapping details.

## Contents
<a name="API_ControlMapping_Contents"></a>

 ** ControlArn **   <a name="controlcatalog-Type-ControlMapping-ControlArn"></a>
The Amazon Resource Name (ARN) that identifies the control in the mapping.
Type: String
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
Required: Yes

 ** Mapping **   <a name="controlcatalog-Type-ControlMapping-Mapping"></a>
The details of the mapping relationship, for example, containing framework, common control, or related control information.
Type: [Mapping](API_Mapping.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** MappingType **   <a name="controlcatalog-Type-ControlMapping-MappingType"></a>
The type of mapping relationship between the control and other entities.
Type: String
Valid Values: `FRAMEWORK | COMMON_CONTROL | RELATED_CONTROL`
Required: Yes

## See Also
<a name="API_ControlMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ControlMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ControlMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ControlMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

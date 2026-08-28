---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualCustomizationFieldsConfiguration.html
---

# VisualCustomizationFieldsConfiguration
<a name="API_VisualCustomizationFieldsConfiguration"></a>

The configuration that controls field customization options available to dashboard readers for a visual.

## Contents
<a name="API_VisualCustomizationFieldsConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalFields **   <a name="QS-Type-VisualCustomizationFieldsConfiguration-AdditionalFields"></a>
The additional dataset fields available for dashboard readers to customize the visual with, beyond the fields already configured on the visual.
Type: Array of [ColumnIdentifier](API_ColumnIdentifier.md) objects
Array Members: Maximum number of 2500 items.
Required: No

 ** Status **   <a name="QS-Type-VisualCustomizationFieldsConfiguration-Status"></a>
Specifies whether dashboard readers can customize fields for this visual. This option is `ENABLED` by default.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_VisualCustomizationFieldsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VisualCustomizationFieldsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VisualCustomizationFieldsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VisualCustomizationFieldsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

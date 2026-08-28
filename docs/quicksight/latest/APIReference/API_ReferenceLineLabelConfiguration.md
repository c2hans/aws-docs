---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReferenceLineLabelConfiguration.html
---

# ReferenceLineLabelConfiguration
<a name="API_ReferenceLineLabelConfiguration"></a>

The label configuration of a reference line.

## Contents
<a name="API_ReferenceLineLabelConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomLabelConfiguration **   <a name="QS-Type-ReferenceLineLabelConfiguration-CustomLabelConfiguration"></a>
The custom label configuration of the label in a reference line.
Type: [ReferenceLineCustomLabelConfiguration](API_ReferenceLineCustomLabelConfiguration.md) object
Required: No

 ** FontColor **   <a name="QS-Type-ReferenceLineLabelConfiguration-FontColor"></a>
The font color configuration of the label in a reference line.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** FontConfiguration **   <a name="QS-Type-ReferenceLineLabelConfiguration-FontConfiguration"></a>
The font configuration of the label in a reference line.
Type: [FontConfiguration](API_FontConfiguration.md) object
Required: No

 ** HorizontalPosition **   <a name="QS-Type-ReferenceLineLabelConfiguration-HorizontalPosition"></a>
The horizontal position configuration of the label in a reference line. Choose one of the following options:
+  `LEFT`
+  `CENTER`
+  `RIGHT`
Type: String
Valid Values: `LEFT | CENTER | RIGHT`
Required: No

 ** ValueLabelConfiguration **   <a name="QS-Type-ReferenceLineLabelConfiguration-ValueLabelConfiguration"></a>
The value label configuration of the label in a reference line.
Type: [ReferenceLineValueLabelConfiguration](API_ReferenceLineValueLabelConfiguration.md) object
Required: No

 ** VerticalPosition **   <a name="QS-Type-ReferenceLineLabelConfiguration-VerticalPosition"></a>
The vertical position configuration of the label in a reference line. Choose one of the following options:
+  `ABOVE`
+  `BELOW`
Type: String
Valid Values: `ABOVE | BELOW`
Required: No

## See Also
<a name="API_ReferenceLineLabelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReferenceLineLabelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReferenceLineLabelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReferenceLineLabelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

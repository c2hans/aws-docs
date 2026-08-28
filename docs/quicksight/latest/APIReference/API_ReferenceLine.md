---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReferenceLine.html
---

# ReferenceLine
<a name="API_ReferenceLine"></a>

The reference line visual display options.

## Contents
<a name="API_ReferenceLine_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataConfiguration **   <a name="QS-Type-ReferenceLine-DataConfiguration"></a>
The data configuration of the reference line.
Type: [ReferenceLineDataConfiguration](API_ReferenceLineDataConfiguration.md) object
Required: Yes

 ** LabelConfiguration **   <a name="QS-Type-ReferenceLine-LabelConfiguration"></a>
The label configuration of the reference line.
Type: [ReferenceLineLabelConfiguration](API_ReferenceLineLabelConfiguration.md) object
Required: No

 ** Status **   <a name="QS-Type-ReferenceLine-Status"></a>
The status of the reference line. Choose one of the following options:
+  `ENABLE`
+  `DISABLE`
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** StyleConfiguration **   <a name="QS-Type-ReferenceLine-StyleConfiguration"></a>
The style configuration of the reference line.
Type: [ReferenceLineStyleConfiguration](API_ReferenceLineStyleConfiguration.md) object
Required: No

## See Also
<a name="API_ReferenceLine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReferenceLine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReferenceLine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReferenceLine)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

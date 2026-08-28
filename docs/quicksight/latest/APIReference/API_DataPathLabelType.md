---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPathLabelType.html
---

# DataPathLabelType
<a name="API_DataPathLabelType"></a>

The option that specifies individual data values for labels.

## Contents
<a name="API_DataPathLabelType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-DataPathLabelType-FieldId"></a>
The field ID of the field that the data label needs to be applied to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** FieldValue **   <a name="QS-Type-DataPathLabelType-FieldValue"></a>
The actual value of the field that is labeled.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** Visibility **   <a name="QS-Type-DataPathLabelType-Visibility"></a>
The visibility of the data label.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_DataPathLabelType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPathLabelType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPathLabelType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPathLabelType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

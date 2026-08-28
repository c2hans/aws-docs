---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataLabelType.html
---

# DataLabelType
<a name="API_DataLabelType"></a>

The option that determines the data label type.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_DataLabelType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataPathLabelType **   <a name="QS-Type-DataLabelType-DataPathLabelType"></a>
The option that specifies individual data values for labels.
Type: [DataPathLabelType](API_DataPathLabelType.md) object
Required: No

 ** FieldLabelType **   <a name="QS-Type-DataLabelType-FieldLabelType"></a>
Determines the label configuration for the entire field.
Type: [FieldLabelType](API_FieldLabelType.md) object
Required: No

 ** MaximumLabelType **   <a name="QS-Type-DataLabelType-MaximumLabelType"></a>
Determines the label configuration for the maximum value in a visual.
Type: [MaximumLabelType](API_MaximumLabelType.md) object
Required: No

 ** MinimumLabelType **   <a name="QS-Type-DataLabelType-MinimumLabelType"></a>
Determines the label configuration for the minimum value in a visual.
Type: [MinimumLabelType](API_MinimumLabelType.md) object
Required: No

 ** RangeEndsLabelType **   <a name="QS-Type-DataLabelType-RangeEndsLabelType"></a>
Determines the label configuration for range end value in a visual.
Type: [RangeEndsLabelType](API_RangeEndsLabelType.md) object
Required: No

## See Also
<a name="API_DataLabelType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataLabelType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataLabelType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataLabelType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FieldTooltipItem.html
---

# FieldTooltipItem
<a name="API_FieldTooltipItem"></a>

The tooltip item for the fields.

## Contents
<a name="API_FieldTooltipItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldId **   <a name="QS-Type-FieldTooltipItem-FieldId"></a>
The unique ID of the field that is targeted by the tooltip.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Label **   <a name="QS-Type-FieldTooltipItem-Label"></a>
The label of the tooltip item.
Type: String
Required: No

 ** TooltipTarget **   <a name="QS-Type-FieldTooltipItem-TooltipTarget"></a>
Determines the target of the field tooltip item in a combo chart visual.
Type: String
Valid Values: `BOTH | BAR | LINE`
Required: No

 ** Visibility **   <a name="QS-Type-FieldTooltipItem-Visibility"></a>
The visibility of the tooltip item.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_FieldTooltipItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FieldTooltipItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FieldTooltipItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FieldTooltipItem)

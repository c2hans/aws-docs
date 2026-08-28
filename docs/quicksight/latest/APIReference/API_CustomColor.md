---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomColor.html
---

# CustomColor
<a name="API_CustomColor"></a>

Determines the color that's applied to a particular data value in a column.

## Contents
<a name="API_CustomColor_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Color **   <a name="QS-Type-CustomColor-Color"></a>
The color that is applied to the data value.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: Yes

 ** FieldValue **   <a name="QS-Type-CustomColor-FieldValue"></a>
The data value that the color is applied to.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** SpecialValue **   <a name="QS-Type-CustomColor-SpecialValue"></a>
The value of a special data value.
Type: String
Valid Values: `EMPTY | NULL | OTHER`
Required: No

## See Also
<a name="API_CustomColor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomColor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomColor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomColor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

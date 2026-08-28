---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataPathColor.html
---

# DataPathColor
<a name="API_DataPathColor"></a>

The color map that determines the color options for a particular element.

## Contents
<a name="API_DataPathColor_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Color **   <a name="QS-Type-DataPathColor-Color"></a>
The color that needs to be applied to the element.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: Yes

 ** Element **   <a name="QS-Type-DataPathColor-Element"></a>
The element that the color needs to be applied to.
Type: [DataPathValue](API_DataPathValue.md) object
Required: Yes

 ** TimeGranularity **   <a name="QS-Type-DataPathColor-TimeGranularity"></a>
The time granularity of the field that the color needs to be applied to.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

## See Also
<a name="API_DataPathColor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataPathColor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataPathColor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataPathColor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

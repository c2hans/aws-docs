---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ProfileLimitValue.html
---

# ProfileLimitValue
<a name="API_ProfileLimitValue"></a>

A value that defines a resource usage limit, consisting of a maximum value and a unit of measurement.

## Contents
<a name="API_ProfileLimitValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** maxValue **   <a name="QS-Type-ProfileLimitValue-maxValue"></a>
The maximum allowed value for the resource.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** unit **   <a name="QS-Type-ProfileLimitValue-unit"></a>
The unit of measurement for the limit value.
Type: String
Valid Values: `MB | GB | HOURS | DAYS`
Required: Yes

## See Also
<a name="API_ProfileLimitValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ProfileLimitValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ProfileLimitValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ProfileLimitValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

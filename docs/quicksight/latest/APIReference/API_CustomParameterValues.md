---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomParameterValues.html
---

# CustomParameterValues
<a name="API_CustomParameterValues"></a>

The customized parameter values.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_CustomParameterValues_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimeValues **   <a name="QS-Type-CustomParameterValues-DateTimeValues"></a>
A list of datetime-type parameter values.
Type: Array of timestamps
Array Members: Maximum number of 50000 items.
Required: No

 ** DecimalValues **   <a name="QS-Type-CustomParameterValues-DecimalValues"></a>
A list of decimal-type parameter values.
Type: Array of doubles
Array Members: Maximum number of 50000 items.
Required: No

 ** IntegerValues **   <a name="QS-Type-CustomParameterValues-IntegerValues"></a>
A list of integer-type parameter values.
Type: Array of longs
Array Members: Maximum number of 50000 items.
Required: No

 ** StringValues **   <a name="QS-Type-CustomParameterValues-StringValues"></a>
A list of string-type parameter values.
Type: Array of strings
Array Members: Maximum number of 50000 items.
Required: No

## See Also
<a name="API_CustomParameterValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomParameterValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomParameterValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomParameterValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

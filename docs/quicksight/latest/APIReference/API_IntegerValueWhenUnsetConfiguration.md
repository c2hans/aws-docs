---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IntegerValueWhenUnsetConfiguration.html
---

# IntegerValueWhenUnsetConfiguration
<a name="API_IntegerValueWhenUnsetConfiguration"></a>

A parameter declaration for the `Integer` data type.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_IntegerValueWhenUnsetConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomValue **   <a name="QS-Type-IntegerValueWhenUnsetConfiguration-CustomValue"></a>
A custom value that's used when the value of a parameter isn't set.
Type: Long
Required: No

 ** ValueWhenUnsetOption **   <a name="QS-Type-IntegerValueWhenUnsetConfiguration-ValueWhenUnsetOption"></a>
The built-in options for default values. The value can be one of the following:
+  `RECOMMENDED`: The recommended value.
+  `NULL`: The `NULL` value.
Type: String
Valid Values: `RECOMMENDED_VALUE | NULL`
Required: No

## See Also
<a name="API_IntegerValueWhenUnsetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IntegerValueWhenUnsetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IntegerValueWhenUnsetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IntegerValueWhenUnsetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

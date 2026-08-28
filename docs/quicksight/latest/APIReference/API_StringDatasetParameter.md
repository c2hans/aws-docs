---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StringDatasetParameter.html
---

# StringDatasetParameter
<a name="API_StringDatasetParameter"></a>

A string parameter for a dataset.

## Contents
<a name="API_StringDatasetParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="QS-Type-StringDatasetParameter-Id"></a>
An identifier for the string parameter that is created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** Name **   <a name="QS-Type-StringDatasetParameter-Name"></a>
The name of the string parameter that is created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ValueType **   <a name="QS-Type-StringDatasetParameter-ValueType"></a>
The value type of the dataset parameter. Valid values are `single value` or `multi value`.
Type: String
Valid Values: `MULTI_VALUED | SINGLE_VALUED`
Required: Yes

 ** DefaultValues **   <a name="QS-Type-StringDatasetParameter-DefaultValues"></a>
A list of default values for a given string dataset parameter type. This structure only accepts static values.
Type: [StringDatasetParameterDefaultValues](API_StringDatasetParameterDefaultValues.md) object
Required: No

## See Also
<a name="API_StringDatasetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StringDatasetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StringDatasetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StringDatasetParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

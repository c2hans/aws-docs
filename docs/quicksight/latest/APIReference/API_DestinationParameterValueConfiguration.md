---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DestinationParameterValueConfiguration.html
---

# DestinationParameterValueConfiguration
<a name="API_DestinationParameterValueConfiguration"></a>

The configuration of destination parameter values.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_DestinationParameterValueConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomValuesConfiguration **   <a name="QS-Type-DestinationParameterValueConfiguration-CustomValuesConfiguration"></a>
The configuration of custom values for destination parameter in `DestinationParameterValueConfiguration`.
Type: [CustomValuesConfiguration](API_CustomValuesConfiguration.md) object
Required: No

 ** SelectAllValueOptions **   <a name="QS-Type-DestinationParameterValueConfiguration-SelectAllValueOptions"></a>
The configuration that selects all options.
Type: String
Valid Values: `ALL_VALUES`
Required: No

 ** SourceColumn **   <a name="QS-Type-DestinationParameterValueConfiguration-SourceColumn"></a>
A column of a data set.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: No

 ** SourceField **   <a name="QS-Type-DestinationParameterValueConfiguration-SourceField"></a>
The source field ID of the destination parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** SourceParameterName **   <a name="QS-Type-DestinationParameterValueConfiguration-SourceParameterName"></a>
The source parameter name of the destination parameter.
Type: String
Required: No

## See Also
<a name="API_DestinationParameterValueConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DestinationParameterValueConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DestinationParameterValueConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DestinationParameterValueConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

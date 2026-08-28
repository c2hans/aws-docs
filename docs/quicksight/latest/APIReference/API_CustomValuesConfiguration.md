---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomValuesConfiguration.html
---

# CustomValuesConfiguration
<a name="API_CustomValuesConfiguration"></a>

The configuration of custom values for the destination parameter in `DestinationParameterValueConfiguration`.

## Contents
<a name="API_CustomValuesConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomValues **   <a name="QS-Type-CustomValuesConfiguration-CustomValues"></a>
The customized parameter values.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [CustomParameterValues](API_CustomParameterValues.md) object
Required: Yes

 ** IncludeNullValue **   <a name="QS-Type-CustomValuesConfiguration-IncludeNullValue"></a>
Includes the null value in custom action parameter values.
Type: Boolean
Required: No

## See Also
<a name="API_CustomValuesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomValuesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomValuesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomValuesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

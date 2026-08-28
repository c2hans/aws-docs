---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ExtractionDefinitionNotFoundBehavior.html
---

# ExtractionDefinitionNotFoundBehavior
<a name="API_ExtractionDefinitionNotFoundBehavior"></a>

The behavior configuration when an extraction definition cannot find the target value.

## Contents
<a name="API_ExtractionDefinitionNotFoundBehavior_Contents"></a>

 ** Behavior **   <a name="connect-Type-ExtractionDefinitionNotFoundBehavior-Behavior"></a>
The behavior type. `USE_DEFAULT_VALUE` returns the specified default value. `OMIT` excludes the field from the output.
Type: String
Valid Values: `USE_DEFAULT_VALUE | OMIT`
Required: Yes

 ** DefaultValue **   <a name="connect-Type-ExtractionDefinitionNotFoundBehavior-DefaultValue"></a>
The default value to use when the behavior is `USE_DEFAULT_VALUE`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_ExtractionDefinitionNotFoundBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ExtractionDefinitionNotFoundBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ExtractionDefinitionNotFoundBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ExtractionDefinitionNotFoundBehavior)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

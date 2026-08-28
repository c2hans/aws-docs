---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_FilterExpression.html
---

# FilterExpression
<a name="API_FilterExpression"></a>

Represents a structure for defining parameter conditions. Supported conditions are described here: [Supported conditions for dynamic datasets](https://docs.aws.amazon.com/databrew/latest/dg/datasets.multiple-files.html#conditions.for.dynamic.datasets) in the * AWS Glue DataBrew Developer Guide*.

## Contents
<a name="API_FilterExpression_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Expression **   <a name="databrew-Type-FilterExpression-Expression"></a>
The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, "(starts\_with :prefix1 or starts\_with :prefix2) and (ends\_with :suffix1 or ends\_with :suffix2)". Substitution variables should start with ':' symbol.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `^[<>0-9A-Za-z_.,:)(!= ]+$`
Required: Yes

 ** ValuesMap **   <a name="databrew-Type-FilterExpression-ValuesMap"></a>
The map of substitution variable names to their values used in this filter expression.
Type: String to string map
Key Length Constraints: Minimum length of 2. Maximum length of 128.
Key Pattern: `^:[A-Za-z0-9_]+$`
Value Length Constraints: Maximum length of 1024.
Required: Yes

## See Also
<a name="API_FilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/FilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/FilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/FilterExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

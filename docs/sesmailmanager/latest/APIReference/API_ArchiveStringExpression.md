---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveStringExpression.html
---

# ArchiveStringExpression
<a name="API_ArchiveStringExpression"></a>

A string expression to evaluate an email attribute value against one or more string values.

## Contents
<a name="API_ArchiveStringExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-ArchiveStringExpression-Evaluate"></a>
The attribute of the email to evaluate.
Type: [ArchiveStringToEvaluate](API_ArchiveStringToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-ArchiveStringExpression-Operator"></a>
The operator to use when evaluating the string values.
Type: String
Valid Values: `CONTAINS`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-ArchiveStringExpression-Values"></a>
The list of string values to evaluate the email attribute against.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_ArchiveStringExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveStringExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveStringExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveStringExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

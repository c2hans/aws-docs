---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressStringToEvaluate.html
---

# IngressStringToEvaluate
<a name="API_IngressStringToEvaluate"></a>

The union type representing the allowed types for the left hand side of a string condition.

## Contents
<a name="API_IngressStringToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Analysis **   <a name="sesmailmanager-Type-IngressStringToEvaluate-Analysis"></a>
The structure type for a string condition stating the Add On ARN and its returned value.
Type: [IngressAnalysis](API_IngressAnalysis.md) object
Required: No

 ** Attribute **   <a name="sesmailmanager-Type-IngressStringToEvaluate-Attribute"></a>
The enum type representing the allowed attribute types for a string condition.
Type: String
Valid Values: `RECIPIENT`
Required: No

## See Also
<a name="API_IngressStringToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressStringToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressStringToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressStringToEvaluate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressBooleanToEvaluate.html
---

# IngressBooleanToEvaluate
<a name="API_IngressBooleanToEvaluate"></a>

The union type representing the allowed types of operands for a boolean condition.

## Contents
<a name="API_IngressBooleanToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Analysis **   <a name="sesmailmanager-Type-IngressBooleanToEvaluate-Analysis"></a>
The structure type for a boolean condition stating the Add On ARN and its returned value.
Type: [IngressAnalysis](API_IngressAnalysis.md) object
Required: No

 ** IsInAddressList **   <a name="sesmailmanager-Type-IngressBooleanToEvaluate-IsInAddressList"></a>
The structure type for a boolean condition that provides the address lists to evaluate incoming traffic on.
Type: [IngressIsInAddressList](API_IngressIsInAddressList.md) object
Required: No

## See Also
<a name="API_IngressBooleanToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressBooleanToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressBooleanToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressBooleanToEvaluate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

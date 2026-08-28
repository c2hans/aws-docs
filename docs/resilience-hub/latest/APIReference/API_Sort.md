---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_Sort.html
---

# Sort
<a name="API_Sort"></a>

Indicates the sorting order of the fields in the metrics.

## Contents
<a name="API_Sort_Contents"></a>

 ** field **   <a name="resiliencehub-Type-Sort-field"></a>
Indicates the order in which you want to sort the metrics. By default, the list is sorted in ascending order. To sort the list in descending order, set this field to False.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** ascending **   <a name="resiliencehub-Type-Sort-ascending"></a>
Indicates the name or identifier of the field or attribute that should be used as the basis for sorting the metrics.
Type: Boolean
Required: No

## See Also
<a name="API_Sort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/Sort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/Sort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/Sort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

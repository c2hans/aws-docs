---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GroupByValue.html
---

# GroupByValue
<a name="API_GroupByValue"></a>

Represents individual aggregated results when grouping security findings for each `GroupByField`.

## Contents
<a name="API_GroupByValue_Contents"></a>

 ** Count **   <a name="securityhub-Type-GroupByValue-Count"></a>
The number of findings for a specific `FieldValue` and `GroupByField`.
Type: Integer
Required: No

 ** FieldValue **   <a name="securityhub-Type-GroupByValue-FieldValue"></a>
The value of the field by which findings are grouped.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_GroupByValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GroupByValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GroupByValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GroupByValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_MetricConfiguration.html
---

# MetricConfiguration
<a name="API_MetricConfiguration"></a>

This structure contains the `Filter` parameter which you can use to specify which metric namespaces are to be shared from this source account to the monitoring account.

## Contents
<a name="API_MetricConfiguration_Contents"></a>

 ** Filter **   <a name="OAM-Type-MetricConfiguration-Filter"></a>
Use this field to specify which metrics are to be shared with the monitoring account. Use the term `Namespace` and one or more of the following operands. Use single quotation marks (') around namespace names. The matching of namespace names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR`.
+  `=` and `!=`
+  `AND`
+  `OR`
+  `LIKE` and `NOT LIKE`. These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
+  `IN` and `NOT IN`, using parentheses `( )`
Examples:
+  `Namespace NOT LIKE 'AWS/%'` includes only namespaces that don't start with `AWS/`, such as custom namespaces.
+  `Namespace IN ('AWS/EC2', 'AWS/ELB', 'AWS/S3')` includes only the metrics in the EC2, Elastic Load Balancing, and Amazon S3 namespaces.
+  `Namespace = 'AWS/EC2' OR Namespace NOT LIKE 'AWS/%'` includes only the EC2 namespace and your custom namespaces.
If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all metric namespaces with the monitoring account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_MetricConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/MetricConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/MetricConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/MetricConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Observability Access Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query OAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

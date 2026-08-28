---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationSummary.html
---

# ImplementationSummary
<a name="API_ImplementationSummary"></a>

A summary of how the control is implemented, including the AWS service that enforces the control and its service-specific identifier. For example, the value of this field could indicate that the control is implemented as an AWS Config Rule or an AWS Security Hub control.

## Contents
<a name="API_ImplementationSummary_Contents"></a>

 ** Type **   <a name="controlcatalog-Type-ImplementationSummary-Type"></a>
A string that represents the AWS service that implements this control. For example, a value of `AWS::Config::ConfigRule` indicates that the control is implemented by AWS Config, and `AWS::SecurityHub::SecurityControl` indicates implementation by AWS Security Hub.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `[A-Za-z0-9]+(::[A-Za-z0-9_]+){2,3}`
Required: Yes

 ** Identifier **   <a name="controlcatalog-Type-ImplementationSummary-Identifier"></a>
The identifier originally assigned by the AWS service that implements the control. For example, `CODEPIPELINE_DEPLOYMENT_COUNT_CHECK`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\.-]+`
Required: No

## See Also
<a name="API_ImplementationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ImplementationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ImplementationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ImplementationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

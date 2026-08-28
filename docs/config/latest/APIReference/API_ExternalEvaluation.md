---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ExternalEvaluation.html
---

# ExternalEvaluation
<a name="API_ExternalEvaluation"></a>

Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.

## Contents
<a name="API_ExternalEvaluation_Contents"></a>

 ** ComplianceResourceId **   <a name="config-Type-ExternalEvaluation-ComplianceResourceId"></a>
The evaluated compliance resource ID. AWS Config accepts only AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: Yes

 ** ComplianceResourceType **   <a name="config-Type-ExternalEvaluation-ComplianceResourceType"></a>
The evaluated compliance resource type. AWS Config accepts `AWS::::Account` resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ComplianceType **   <a name="config-Type-ExternalEvaluation-ComplianceType"></a>
The compliance of the AWS resource. The valid values are `COMPLIANT, NON_COMPLIANT, ` and `NOT_APPLICABLE`.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: Yes

 ** OrderingTimestamp **   <a name="config-Type-ExternalEvaluation-OrderingTimestamp"></a>
The time when the compliance was recorded.
Type: Timestamp
Required: Yes

 ** Annotation **   <a name="config-Type-ExternalEvaluation-Annotation"></a>
Supplementary information about the reason of compliance. For example, this task was completed on a specific date.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ExternalEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ExternalEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ExternalEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ExternalEvaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

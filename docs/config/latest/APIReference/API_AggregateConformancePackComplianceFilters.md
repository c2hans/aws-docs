---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateConformancePackComplianceFilters.html
---

# AggregateConformancePackComplianceFilters
<a name="API_AggregateConformancePackComplianceFilters"></a>

Filters the conformance packs based on an account ID, region, compliance type, and the name of the conformance pack.

## Contents
<a name="API_AggregateConformancePackComplianceFilters_Contents"></a>

 ** AccountId **   <a name="config-Type-AggregateConformancePackComplianceFilters-AccountId"></a>
The 12-digit AWS account ID of the source account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AwsRegion **   <a name="config-Type-AggregateConformancePackComplianceFilters-AwsRegion"></a>
The source AWS Region from where the data is aggregated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ComplianceType **   <a name="config-Type-AggregateConformancePackComplianceFilters-ComplianceType"></a>
The compliance status of the conformance pack.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: No

 ** ConformancePackName **   <a name="config-Type-AggregateConformancePackComplianceFilters-ConformancePackName"></a>
The name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_AggregateConformancePackComplianceFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateConformancePackComplianceFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateConformancePackComplianceFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateConformancePackComplianceFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

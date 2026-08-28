---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateComplianceByConformancePack.html
---

# AggregateComplianceByConformancePack
<a name="API_AggregateComplianceByConformancePack"></a>

Provides aggregate compliance of the conformance pack. Indicates whether a conformance pack is compliant based on the name of the conformance pack, account ID, and region.

A conformance pack is compliant if all of the rules in a conformance packs are compliant. It is noncompliant if any of the rules are not compliant. The compliance status of a conformance pack is INSUFFICIENT\_DATA only if all rules within a conformance pack cannot be evaluated due to insufficient data. If some of the rules in a conformance pack are compliant but the compliance status of other rules in that same conformance pack is INSUFFICIENT\_DATA, the conformance pack shows compliant.

## Contents
<a name="API_AggregateComplianceByConformancePack_Contents"></a>

 ** AccountId **   <a name="config-Type-AggregateComplianceByConformancePack-AccountId"></a>
The 12-digit AWS account ID of the source account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AwsRegion **   <a name="config-Type-AggregateComplianceByConformancePack-AwsRegion"></a>
The source AWS Region from where the data is aggregated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Compliance **   <a name="config-Type-AggregateComplianceByConformancePack-Compliance"></a>
The compliance status of the conformance pack.
Type: [AggregateConformancePackCompliance](API_AggregateConformancePackCompliance.md) object
Required: No

 ** ConformancePackName **   <a name="config-Type-AggregateComplianceByConformancePack-ConformancePackName"></a>
The name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_AggregateComplianceByConformancePack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateComplianceByConformancePack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateComplianceByConformancePack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateComplianceByConformancePack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

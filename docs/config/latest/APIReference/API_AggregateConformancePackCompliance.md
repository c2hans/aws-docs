---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateConformancePackCompliance.html
---

# AggregateConformancePackCompliance
<a name="API_AggregateConformancePackCompliance"></a>

Provides the number of compliant and noncompliant rules within a conformance pack. Also provides the compliance status of the conformance pack and the total rule count which includes compliant rules, noncompliant rules, and rules that cannot be evaluated due to insufficient data.

A conformance pack is compliant if all of the rules in a conformance packs are compliant. It is noncompliant if any of the rules are not compliant. The compliance status of a conformance pack is INSUFFICIENT\_DATA only if all rules within a conformance pack cannot be evaluated due to insufficient data. If some of the rules in a conformance pack are compliant but the compliance status of other rules in that same conformance pack is INSUFFICIENT\_DATA, the conformance pack shows compliant.

## Contents
<a name="API_AggregateConformancePackCompliance_Contents"></a>

 ** ComplianceType **   <a name="config-Type-AggregateConformancePackCompliance-ComplianceType"></a>
The compliance status of the conformance pack.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: No

 ** CompliantRuleCount **   <a name="config-Type-AggregateConformancePackCompliance-CompliantRuleCount"></a>
The number of compliant AWS Config Rules.
Type: Integer
Required: No

 ** NonCompliantRuleCount **   <a name="config-Type-AggregateConformancePackCompliance-NonCompliantRuleCount"></a>
The number of noncompliant AWS Config Rules.
Type: Integer
Required: No

 ** TotalRuleCount **   <a name="config-Type-AggregateConformancePackCompliance-TotalRuleCount"></a>
Total number of compliant rules, noncompliant rules, and the rules that do not have any applicable resources to evaluate upon resulting in insufficient data.
Type: Integer
Required: No

## See Also
<a name="API_AggregateConformancePackCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateConformancePackCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateConformancePackCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateConformancePackCompliance)

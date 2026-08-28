---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SubResourceSummary.html
---

# SubResourceSummary
<a name="API_SubResourceSummary"></a>

The attack information for the specified SubResource.

## Contents
<a name="API_SubResourceSummary_Contents"></a>

 ** AttackVectors **   <a name="AWSShield-Type-SubResourceSummary-AttackVectors"></a>
The list of attack types and associated counters.
Type: Array of [SummarizedAttackVector](API_SummarizedAttackVector.md) objects
Required: No

 ** Counters **   <a name="AWSShield-Type-SubResourceSummary-Counters"></a>
The counters that describe the details of the attack.
Type: Array of [SummarizedCounter](API_SummarizedCounter.md) objects
Required: No

 ** Id **   <a name="AWSShield-Type-SubResourceSummary-Id"></a>
The unique identifier (ID) of the `SubResource`.
Type: String
Required: No

 ** Type **   <a name="AWSShield-Type-SubResourceSummary-Type"></a>
The `SubResource` type.
Type: String
Valid Values: `IP | URL`
Required: No

## See Also
<a name="API_SubResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/SubResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/SubResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/SubResourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

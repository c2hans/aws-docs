---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SummarizedAttackVector.html
---

# SummarizedAttackVector
<a name="API_SummarizedAttackVector"></a>

A summary of information about the attack.

## Contents
<a name="API_SummarizedAttackVector_Contents"></a>

 ** VectorType **   <a name="AWSShield-Type-SummarizedAttackVector-VectorType"></a>
The attack type, for example, SNMP reflection or SYN flood.
Type: String
Required: Yes

 ** VectorCounters **   <a name="AWSShield-Type-SummarizedAttackVector-VectorCounters"></a>
The list of counters that describe the details of the attack.
Type: Array of [SummarizedCounter](API_SummarizedCounter.md) objects
Required: No

## See Also
<a name="API_SummarizedAttackVector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/SummarizedAttackVector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/SummarizedAttackVector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/SummarizedAttackVector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

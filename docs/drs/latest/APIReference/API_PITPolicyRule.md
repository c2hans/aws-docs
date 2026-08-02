---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_PITPolicyRule.html
---

# PITPolicyRule
<a name="API_PITPolicyRule"></a>

A rule in the Point in Time (PIT) policy representing when to take snapshots and how long to retain them for.

## Contents
<a name="API_PITPolicyRule_Contents"></a>

 ** interval **   <a name="drs-Type-PITPolicyRule-interval"></a>
How often, in the chosen units, a snapshot should be taken.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** retentionDuration **   <a name="drs-Type-PITPolicyRule-retentionDuration"></a>
The duration to retain a snapshot for, in the chosen units.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** units **   <a name="drs-Type-PITPolicyRule-units"></a>
The units used to measure the interval and retentionDuration.
Type: String
Valid Values: `MINUTE | HOUR | DAY`
Required: Yes

 ** enabled **   <a name="drs-Type-PITPolicyRule-enabled"></a>
Whether this rule is enabled or not.
Type: Boolean
Required: No

 ** ruleID **   <a name="drs-Type-PITPolicyRule-ruleID"></a>
The ID of the rule.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_PITPolicyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/PITPolicyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/PITPolicyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/PITPolicyRule)

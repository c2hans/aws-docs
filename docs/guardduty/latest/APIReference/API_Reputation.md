---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Reputation.html
---

# Reputation
<a name="API_Reputation"></a>

Contains reputation information about a threat indicator.

## Contents
<a name="API_Reputation_Contents"></a>

 ** currentDisposition **   <a name="guardduty-Type-Reputation-currentDisposition"></a>
The current reputation of the indicator.
Type: String
Required: No

 ** findingTimeDisposition **   <a name="guardduty-Type-Reputation-findingTimeDisposition"></a>
The reputation of the indicator at the time of the finding.
Type: String
Required: No

 ** reputationComparison **   <a name="guardduty-Type-Reputation-reputationComparison"></a>
A comparison of the reputation at the time of the finding with the current reputation.
Type: String
Required: No

## See Also
<a name="API_Reputation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Reputation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Reputation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Reputation)

---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AccountStatistics.html
---

# AccountStatistics
<a name="API_AccountStatistics"></a>

Represents a list of map of accounts with the number of findings associated with each account.

## Contents
<a name="API_AccountStatistics_Contents"></a>

 ** accountId **   <a name="guardduty-Type-AccountStatistics-accountId"></a>
The ID of the AWS account.
Type: String
Required: No

 ** lastGeneratedAt **   <a name="guardduty-Type-AccountStatistics-lastGeneratedAt"></a>
The timestamp at which the finding for this account was last generated.
Type: Timestamp
Required: No

 ** totalFindings **   <a name="guardduty-Type-AccountStatistics-totalFindings"></a>
The total number of findings associated with an account.
Type: Integer
Required: No

## See Also
<a name="API_AccountStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AccountStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AccountStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AccountStatistics)

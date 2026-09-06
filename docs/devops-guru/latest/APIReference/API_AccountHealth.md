---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AccountHealth.html
---

# AccountHealth
<a name="API_AccountHealth"></a>

 Returns the number of open reactive insights, the number of open proactive insights, and the number of metrics analyzed in your AWS account. Use these numbers to gauge the health of operations in your AWS account.

## Contents
<a name="API_AccountHealth_Contents"></a>

 ** AccountId **   <a name="DevOpsGuru-Type-AccountHealth-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** Insight **   <a name="DevOpsGuru-Type-AccountHealth-Insight"></a>
 Information about the health of the AWS resources in your account, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights.
Type: [AccountInsightHealth](API_AccountInsightHealth.md) object
Required: No

## See Also
<a name="API_AccountHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AccountHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AccountHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AccountHealth)

---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UnprocessedAccount.html
---

# UnprocessedAccount
<a name="API_UnprocessedAccount"></a>

Contains information about the accounts that weren't processed.

## Contents
<a name="API_UnprocessedAccount_Contents"></a>

 ** accountId **   <a name="guardduty-Type-UnprocessedAccount-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** result **   <a name="guardduty-Type-UnprocessedAccount-result"></a>
A reason why the account hasn't been processed.
Type: String
Required: Yes

## See Also
<a name="API_UnprocessedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UnprocessedAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UnprocessedAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UnprocessedAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

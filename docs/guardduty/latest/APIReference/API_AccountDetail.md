---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AccountDetail.html
---

# AccountDetail
<a name="API_AccountDetail"></a>

Contains information about the account.

## Contents
<a name="API_AccountDetail_Contents"></a>

 ** accountId **   <a name="guardduty-Type-AccountDetail-accountId"></a>
The member account ID.
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** email **   <a name="guardduty-Type-AccountDetail-email"></a>
The email address of the member account. The following list includes the rules for a valid email address:
+ The email address must be a minimum of 6 and a maximum of 64 characters long.
+ All characters must be 7-bit ASCII characters.
+ There must be one and only one @ symbol, which separates the local name from the domain name.
+ The local name can't contain any of the following characters:

  whitespace, " ' ( ) < > [ ] : ' , \\ \| % &
+ The local name can't begin with a dot (.).
+ The domain name can consist of only the characters [a-z], [A-Z], [0-9], hyphen (-), or dot (.).
+ The domain name can't begin or end with a dot (.) or hyphen (-).
+ The domain name must contain at least one dot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_AccountDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AccountDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AccountDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AccountDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

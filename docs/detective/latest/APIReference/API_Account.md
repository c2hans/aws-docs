---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_Account.html
---

# Account
<a name="API_Account"></a>

An AWS account that is the administrator account of or a member of a behavior graph.

## Contents
<a name="API_Account_Contents"></a>

 ** AccountId **   <a name="detective-Type-Account-AccountId"></a>
The account identifier of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: Yes

 ** EmailAddress **   <a name="detective-Type-Account-EmailAddress"></a>
The AWS account root user email address for the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.+@(?:(?:(?!-)[A-Za-z0-9-]{1,62})?[A-Za-z0-9]{1}\.)+[A-Za-z]{2,63}$`
Required: Yes

## See Also
<a name="API_Account_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/Account)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/Account)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/Account)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

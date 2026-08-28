---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Account.html
---

# Account
<a name="API_Account"></a>

Contains information about an AWS account that is a member of an organization.

## Contents
<a name="API_Account_Contents"></a>

 ** Arn **   <a name="organizations-Type-Account-Arn"></a>
The Amazon Resource Name (ARN) of the account.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}`
Required: No

 ** Email **   <a name="organizations-Type-Account-Email"></a>
The email address associated with the AWS account.
The [regex pattern](http://wikipedia.org/wiki/regex) for this parameter is a string of characters that represents a standard internet email address.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: No

 ** Id **   <a name="organizations-Type-Account-Id"></a>
The unique identifier (ID) of the account.
The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

 ** JoinedMethod **   <a name="organizations-Type-Account-JoinedMethod"></a>
The method by which the account joined the organization.
Type: String
Valid Values: `INVITED | CREATED`
Required: No

 ** JoinedTimestamp **   <a name="organizations-Type-Account-JoinedTimestamp"></a>
The date the account became a part of the organization.
Type: Timestamp
Required: No

 ** Name **   <a name="organizations-Type-Account-Name"></a>
The friendly name of the account.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** Paths **   <a name="organizations-Type-Account-Paths"></a>
The paths in the organization where the account exists.
Type: Array of strings
Pattern: `^(o-[a-z0-9]{10,32}\/r-[0-9a-z]{4,32}(\/ou\-[0-9a-z]{4,32}-[a-z0-9]{8,32})*(\/\d{12})*)\/`
Required: No

 ** State **   <a name="organizations-Type-Account-State"></a>
Each state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.
For more information about account states and their implications, see [Monitor the state of your AWS accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html) in the * AWS Organizations User Guide*.
Type: String
Valid Values: `PENDING_ACTIVATION | ACTIVE | SUSPENDED | PENDING_CLOSURE | CLOSED`
Required: No

 ** Status **   <a name="organizations-Type-Account-Status"></a>
The status of the account in the organization.
The `Status` parameter in the `Account` object will be retired on September 9, 2026. Although both the account `State` and account `Status` parameters are currently available in the AWS Organizations APIs (`DescribeAccount`, `ListAccounts`, `ListAccountsForParent`), we recommend that you update your scripts or other code to use the `State` parameter instead of `Status` before September 9, 2026.
Type: String
Valid Values: `ACTIVE | SUSPENDED | PENDING_CLOSURE`
Required: No

## See Also
<a name="API_Account_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Account)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Account)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Account)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

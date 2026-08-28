---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_DelegatedAdministrator.html
---

# DelegatedAdministrator
<a name="API_DelegatedAdministrator"></a>

Contains information about the delegated administrator.

## Contents
<a name="API_DelegatedAdministrator_Contents"></a>

 ** Arn **   <a name="organizations-Type-DelegatedAdministrator-Arn"></a>
The Amazon Resource Name (ARN) of the delegated administrator's account.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}`
Required: No

 ** DelegationEnabledDate **   <a name="organizations-Type-DelegatedAdministrator-DelegationEnabledDate"></a>
The date when the account was made a delegated administrator.
Type: Timestamp
Required: No

 ** Email **   <a name="organizations-Type-DelegatedAdministrator-Email"></a>
The email address that is associated with the delegated administrator's AWS account.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: No

 ** Id **   <a name="organizations-Type-DelegatedAdministrator-Id"></a>
The unique identifier (ID) of the delegated administrator's account.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

 ** JoinedMethod **   <a name="organizations-Type-DelegatedAdministrator-JoinedMethod"></a>
The method by which the delegated administrator's account joined the organization.
Type: String
Valid Values: `INVITED | CREATED`
Required: No

 ** JoinedTimestamp **   <a name="organizations-Type-DelegatedAdministrator-JoinedTimestamp"></a>
The date when the delegated administrator's account became a part of the organization.
Type: Timestamp
Required: No

 ** Name **   <a name="organizations-Type-DelegatedAdministrator-Name"></a>
The friendly name of the delegated administrator's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="organizations-Type-DelegatedAdministrator-State"></a>
Each state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.
For more information about account states and their implications, see [Monitor the state of your AWS accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html) in the * AWS Organizations User Guide*.
Type: String
Valid Values: `PENDING_ACTIVATION | ACTIVE | SUSPENDED | PENDING_CLOSURE | CLOSED`
Required: No

 ** Status **   <a name="organizations-Type-DelegatedAdministrator-Status"></a>
The status of the delegated administrator's account in the organization.
Type: String
Valid Values: `ACTIVE | SUSPENDED | PENDING_CLOSURE`
Required: No

## See Also
<a name="API_DelegatedAdministrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/DelegatedAdministrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/DelegatedAdministrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/DelegatedAdministrator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

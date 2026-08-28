---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Contains information about the user involved in the attack sequence.

## Contents
<a name="API_User_Contents"></a>

 ** name **   <a name="guardduty-Type-User-name"></a>
The name of the user.
Type: String
Required: Yes

 ** type **   <a name="guardduty-Type-User-type"></a>
The type of the user.
Type: String
Required: Yes

 ** uid **   <a name="guardduty-Type-User-uid"></a>
The unique identifier of the user.
Type: String
Required: Yes

 ** account **   <a name="guardduty-Type-User-account"></a>
Contains information about the AWS account within which the activity took place. This is not necessarily the account that owns the user identity.
Type: [Account](API_Account.md) object
Required: No

 ** credentialUid **   <a name="guardduty-Type-User-credentialUid"></a>
The credentials of the user ID.
Type: String
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/User)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountSettings.html
---

# AccountSettings
<a name="API_AccountSettings"></a>

The Quick Sight settings associated with your AWS account.

## Contents
<a name="API_AccountSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountName **   <a name="QS-Type-AccountSettings-AccountName"></a>
The "account name" you provided for the Quick Sight subscription in your AWS account. You create this name when you sign up for Quick Sight. It is unique in all of AWS and it appears only when users sign in.
Type: String
Required: No

 ** DefaultNamespace **   <a name="QS-Type-AccountSettings-DefaultNamespace"></a>
The default Quick Sight namespace for your AWS account.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** Edition **   <a name="QS-Type-AccountSettings-Edition"></a>
The edition of Quick Sight that you're currently subscribed to: Enterprise edition or Standard edition.
Type: String
Valid Values: `STANDARD | ENTERPRISE | ENTERPRISE_AND_Q`
Required: No

 ** NotificationEmail **   <a name="QS-Type-AccountSettings-NotificationEmail"></a>
The main notification email for your Quick Sight subscription.
Type: String
Required: No

 ** PublicSharingEnabled **   <a name="QS-Type-AccountSettings-PublicSharingEnabled"></a>
A Boolean value that indicates whether public sharing is turned on for an Quick account. For more information about turning on public sharing, see [UpdatePublicSharingSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdatePublicSharingSettings.html).
Type: Boolean
Required: No

 ** TerminationProtectionEnabled **   <a name="QS-Type-AccountSettings-TerminationProtectionEnabled"></a>
A boolean value that determines whether or not an Quick Sight account can be deleted. A `True` value doesn't allow the account to be deleted and results in an error message if a user tries to make a `DeleteAccountSubsctiption` request. A `False` value will allow the ccount to be deleted.
Type: Boolean
Required: No

## See Also
<a name="API_AccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

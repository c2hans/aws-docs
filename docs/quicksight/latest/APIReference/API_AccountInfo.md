---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountInfo.html
---

# AccountInfo
<a name="API_AccountInfo"></a>

A structure that contains the following account information elements:
+ Your Quick Sight account name.
+ The edition of Quick Sight that your account is using.
+ The notification email address that is associated with the Quick Sight account.
+ The authentication type of the Quick Sight account.
+ The status of the Quick Sight account's subscription.

## Contents
<a name="API_AccountInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountName **   <a name="QS-Type-AccountInfo-AccountName"></a>
The account name that you provided for the Amazon Quick Sight subscription in your AWS account. You create this name when you sign up for Quick. It's unique over all of AWS, and it appears only when users sign in.
Type: String
Required: No

 ** AccountSubscriptionStatus **   <a name="QS-Type-AccountInfo-AccountSubscriptionStatus"></a>
The status of your account subscription.
Type: String
Required: No

 ** AuthenticationType **   <a name="QS-Type-AccountInfo-AuthenticationType"></a>
The way that your Amazon Quick Sight account is authenticated.
Type: String
Required: No

 ** Edition **   <a name="QS-Type-AccountInfo-Edition"></a>
The edition of your Quick Sight account.
Type: String
Valid Values: `STANDARD | ENTERPRISE | ENTERPRISE_AND_Q`
Required: No

 ** IAMIdentityCenterInstanceArn **   <a name="QS-Type-AccountInfo-IAMIdentityCenterInstanceArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center instance.
Type: String
Required: No

 ** NotificationEmail **   <a name="QS-Type-AccountInfo-NotificationEmail"></a>
The email address that will be used for Quick Sight to send notifications regarding your AWS account or Quick Sight subscription.
Type: String
Required: No

## See Also
<a name="API_AccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AccountInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

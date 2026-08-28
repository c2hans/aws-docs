---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_EmailContact.html
---

# EmailContact
<a name="API_EmailContact"></a>

An email contact.

## Contents
<a name="API_EmailContact_Contents"></a>

 ** address **   <a name="notificationscontacts-Type-EmailContact-address"></a>
The email address this email contact points to. The activation email and any subscribed emails are sent here.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 254.
Pattern: `(.+)@(.+)`
Required: Yes

 ** arn **   <a name="notificationscontacts-Type-EmailContact-arn"></a>
The Amazon Resource Name (ARN) of the email contact.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`
Required: Yes

 ** creationTime **   <a name="notificationscontacts-Type-EmailContact-creationTime"></a>
The creation time of the resource.
Type: Timestamp
Required: Yes

 ** name **   <a name="notificationscontacts-Type-EmailContact-name"></a>
The name of the email contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[\w-.~]+.*`
Required: Yes

 ** status **   <a name="notificationscontacts-Type-EmailContact-status"></a>
The status of the email contact. Only activated email contacts receive emails.
Type: String
Valid Values: `inactive | active`
Required: Yes

 ** updateTime **   <a name="notificationscontacts-Type-EmailContact-updateTime"></a>
The time the resource was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_EmailContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/EmailContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/EmailContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/EmailContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications Contacts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notificationscontacts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

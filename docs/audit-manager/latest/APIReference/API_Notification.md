---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Notification.html
---

# Notification
<a name="API_Notification"></a>

 The notification that informs a user of an update in AWS Audit Manager. For example, this includes the notification that's sent when a control set is delegated for review.

## Contents
<a name="API_Notification_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-Notification-assessmentId"></a>
 The identifier for the assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentName **   <a name="auditmanager-Type-Notification-assessmentName"></a>
 The name of the related assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** controlSetId **   <a name="auditmanager-Type-Notification-controlSetId"></a>
 The identifier for the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** controlSetName **   <a name="auditmanager-Type-Notification-controlSetName"></a>
 Specifies the name of the control set that the notification is about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** description **   <a name="auditmanager-Type-Notification-description"></a>
 The description of the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** eventTime **   <a name="auditmanager-Type-Notification-eventTime"></a>
 The time when the notification was sent.
Type: Timestamp
Required: No

 ** id **   <a name="auditmanager-Type-Notification-id"></a>
 The unique identifier for the notification.
Type: String
Length Constraints: Minimum length of 47. Maximum length of 50.
Pattern: `^[0-9]{10,13}_[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** source **   <a name="auditmanager-Type-Notification-source"></a>
 The sender of the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Notification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Notification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Notification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Notification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

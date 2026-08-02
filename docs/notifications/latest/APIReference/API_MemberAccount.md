---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_MemberAccount.html
---

# MemberAccount
<a name="API_MemberAccount"></a>

Contains information about a member account.

## Contents
<a name="API_MemberAccount_Contents"></a>

 ** accountId **   <a name="Notifications-Type-MemberAccount-accountId"></a>
The AWS account ID of the member account.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** organizationalUnitId **   <a name="Notifications-Type-MemberAccount-organizationalUnitId"></a>
The unique identifier of the organizational unit containing the member account.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: Yes

 ** status **   <a name="Notifications-Type-MemberAccount-status"></a>
The current status of the member account.
Type: String
Valid Values: `ACTIVE | PENDING | INACTIVE | CREATING | DELETING`
Required: Yes

 ** statusReason **   <a name="Notifications-Type-MemberAccount-statusReason"></a>
The reason for the current status of the member account.
Type: String
Required: Yes

 ** notificationConfigurationArn **   <a name="Notifications-Type-MemberAccount-notificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the notification configuration associated with the member account.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: No

## See Also
<a name="API_MemberAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/MemberAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/MemberAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/MemberAccount)

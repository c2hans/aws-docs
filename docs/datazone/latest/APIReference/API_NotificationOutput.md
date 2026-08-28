---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_NotificationOutput.html
---

# NotificationOutput
<a name="API_NotificationOutput"></a>

The details of a notification generated in Amazon DataZone.

## Contents
<a name="API_NotificationOutput_Contents"></a>

 ** actionLink **   <a name="datazone-Type-NotificationOutput-actionLink"></a>
The action link included in the notification.
Type: String
Required: Yes

 ** creationTimestamp **   <a name="datazone-Type-NotificationOutput-creationTimestamp"></a>
The timestamp of when a notification was created.
Type: Timestamp
Required: Yes

 ** domainIdentifier **   <a name="datazone-Type-NotificationOutput-domainIdentifier"></a>
The identifier of a Amazon DataZone domain in which the notification exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** identifier **   <a name="datazone-Type-NotificationOutput-identifier"></a>
The identifier of the notification.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** lastUpdatedTimestamp **   <a name="datazone-Type-NotificationOutput-lastUpdatedTimestamp"></a>
The timestamp of when the notification was last updated.
Type: Timestamp
Required: Yes

 ** message **   <a name="datazone-Type-NotificationOutput-message"></a>
The message included in the notification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: Yes

 ** title **   <a name="datazone-Type-NotificationOutput-title"></a>
The title of the notification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** topic **   <a name="datazone-Type-NotificationOutput-topic"></a>
The topic of the notification.
Type: [Topic](API_Topic.md) object
Required: Yes

 ** type **   <a name="datazone-Type-NotificationOutput-type"></a>
The type of the notification.
Type: String
Valid Values: `TASK | EVENT`
Required: Yes

 ** metadata **   <a name="datazone-Type-NotificationOutput-metadata"></a>
The metadata included in the notification.
Type: String to string map
Required: No

 ** status **   <a name="datazone-Type-NotificationOutput-status"></a>
The status included in the notification.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_NotificationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/NotificationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/NotificationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/NotificationOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

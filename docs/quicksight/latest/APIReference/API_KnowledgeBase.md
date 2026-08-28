---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBase.html
---

# KnowledgeBase
<a name="API_KnowledgeBase"></a>

A knowledge base resource that provides data from connected sources for AI-powered experiences in Amazon QuickSight.

## Contents
<a name="API_KnowledgeBase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-KnowledgeBase-DataSourceArn"></a>
The ARN of the data source associated with the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** KnowledgeBaseArn **   <a name="QS-Type-KnowledgeBase-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** KnowledgeBaseConfiguration **   <a name="QS-Type-KnowledgeBase-KnowledgeBaseConfiguration"></a>
The configuration settings for the knowledge base.
Type: [KnowledgeBaseConfiguration](API_KnowledgeBaseConfiguration.md) object
Required: Yes

 ** KnowledgeBaseId **   <a name="QS-Type-KnowledgeBase-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** Name **   <a name="QS-Type-KnowledgeBase-Name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[\p{L}\p{N}][\p{L}\p{N} _\-\.]*`
Required: Yes

 ** Status **   <a name="QS-Type-KnowledgeBase-Status"></a>
The status of the knowledge base.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | FAILED | DELETING`
Required: Yes

 ** AccessControlConfiguration **   <a name="QS-Type-KnowledgeBase-AccessControlConfiguration"></a>
The access control configuration for the knowledge base.
Type: [AccessControlConfiguration](API_AccessControlConfiguration.md) object
Required: No

 ** CreatedAt **   <a name="QS-Type-KnowledgeBase-CreatedAt"></a>
The date and time that the knowledge base was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-KnowledgeBase-Description"></a>
The description of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** DocumentCount **   <a name="QS-Type-KnowledgeBase-DocumentCount"></a>
The number of documents in the knowledge base.
Type: Long
Required: No

 ** FirstCompletedIngestionSummary **   <a name="QS-Type-KnowledgeBase-FirstCompletedIngestionSummary"></a>
A summary of the first completed ingestion for the knowledge base.
Type: [KnowledgeBaseIngestionSummary](API_KnowledgeBaseIngestionSummary.md) object
Required: No

 ** FirstIncompleteIngestionSummary **   <a name="QS-Type-KnowledgeBase-FirstIncompleteIngestionSummary"></a>
A summary of the first incomplete ingestion for the knowledge base.
Type: [KnowledgeBaseIngestionSummary](API_KnowledgeBaseIngestionSummary.md) object
Required: No

 ** IsEmailNotificationOptedForIngestionFailures **   <a name="QS-Type-KnowledgeBase-IsEmailNotificationOptedForIngestionFailures"></a>
Specifies whether email notifications are enabled for ingestion failures.
Type: Boolean
Required: No

 ** KnowledgeBaseSizeBytes **   <a name="QS-Type-KnowledgeBase-KnowledgeBaseSizeBytes"></a>
The size of the knowledge base in bytes.
Type: Long
Required: No

 ** LatestIngestionSummary **   <a name="QS-Type-KnowledgeBase-LatestIngestionSummary"></a>
A summary of the most recent ingestion for the knowledge base.
Type: [KnowledgeBaseIngestionSummary](API_KnowledgeBaseIngestionSummary.md) object
Required: No

 ** MediaExtractionConfiguration **   <a name="QS-Type-KnowledgeBase-MediaExtractionConfiguration"></a>
The media extraction configuration for the knowledge base.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** PrimaryOwnerArn **   <a name="QS-Type-KnowledgeBase-PrimaryOwnerArn"></a>
The ARN of the primary owner of the knowledge base.
Type: String
Required: No

 ** PrimaryOwnerUsername **   <a name="QS-Type-KnowledgeBase-PrimaryOwnerUsername"></a>
The username of the primary owner of the knowledge base.
Type: String
Required: No

 ** Type **   <a name="QS-Type-KnowledgeBase-Type"></a>
The type of the knowledge base.
Type: String
Required: No

 ** UpdatedAt **   <a name="QS-Type-KnowledgeBase-UpdatedAt"></a>
The date and time that the knowledge base was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_KnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

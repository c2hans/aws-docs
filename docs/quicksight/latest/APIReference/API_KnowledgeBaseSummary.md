---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseSummary.html
---

# KnowledgeBaseSummary
<a name="API_KnowledgeBaseSummary"></a>

A summary of a knowledge base, including its identifier, name, status, and metadata.

## Contents
<a name="API_KnowledgeBaseSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-KnowledgeBaseSummary-DataSourceArn"></a>
The ARN of the data source associated with the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** KnowledgeBaseArn **   <a name="QS-Type-KnowledgeBaseSummary-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** KnowledgeBaseId **   <a name="QS-Type-KnowledgeBaseSummary-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** Name **   <a name="QS-Type-KnowledgeBaseSummary-Name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[\p{L}\p{N}][\p{L}\p{N} _\-\.]*`
Required: Yes

 ** Status **   <a name="QS-Type-KnowledgeBaseSummary-Status"></a>
The status of the knowledge base.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | FAILED | DELETING`
Required: Yes

 ** CreatedAt **   <a name="QS-Type-KnowledgeBaseSummary-CreatedAt"></a>
The date and time that the knowledge base was created.
Type: Timestamp
Required: No

 ** DocumentCount **   <a name="QS-Type-KnowledgeBaseSummary-DocumentCount"></a>
The number of documents in the knowledge base.
Type: Long
Required: No

 ** KnowledgeBaseSizeBytes **   <a name="QS-Type-KnowledgeBaseSummary-KnowledgeBaseSizeBytes"></a>
The size of the knowledge base in bytes.
Type: Long
Required: No

 ** PrimaryOwnerArn **   <a name="QS-Type-KnowledgeBaseSummary-PrimaryOwnerArn"></a>
The ARN of the primary owner of the knowledge base.
Type: String
Required: No

 ** PrimaryOwnerUsername **   <a name="QS-Type-KnowledgeBaseSummary-PrimaryOwnerUsername"></a>
The username of the primary owner of the knowledge base.
Type: String
Required: No

 ** Type **   <a name="QS-Type-KnowledgeBaseSummary-Type"></a>
The type of the knowledge base.
Type: String
Required: No

 ** UpdatedAt **   <a name="QS-Type-KnowledgeBaseSummary-UpdatedAt"></a>
The date and time that the knowledge base was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_KnowledgeBaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

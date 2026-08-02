---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_JournalRecord.html
---

# JournalRecord
<a name="API_JournalRecord"></a>

Represents a journal record containing execution details and content

## Contents
<a name="API_JournalRecord_Contents"></a>

 ** agentSpaceId **   <a name="devopsagent-Type-JournalRecord-agentSpaceId"></a>
The unique identifier for the agent space containing this record
Type: String
Required: Yes

 ** content **   <a name="devopsagent-Type-JournalRecord-content"></a>
The content of this journal record
Type: JSON value
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-JournalRecord-createdAt"></a>
Timestamp when this journal record was created
Type: Timestamp
Required: Yes

 ** executionId **   <a name="devopsagent-Type-JournalRecord-executionId"></a>
The execution ID associated with this journal record
Type: String
Required: Yes

 ** recordId **   <a name="devopsagent-Type-JournalRecord-recordId"></a>
The unique identifier for this journal record
Type: String
Required: Yes

 ** recordType **   <a name="devopsagent-Type-JournalRecord-recordType"></a>
The type of this journal record
Type: String
Required: Yes

 ** userReference **   <a name="devopsagent-Type-JournalRecord-userReference"></a>
Reference to the user associated with this journal record
Type: [UserReference](API_UserReference.md) object
Required: No

## See Also
<a name="API_JournalRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/JournalRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/JournalRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/JournalRecord)

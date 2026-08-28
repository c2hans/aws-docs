---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/sample-appsync-api-to-query-forensic-details.html
---

# Sample AppSync API to query forensic details
<a name="sample-appsync-api-to-query-forensic-details"></a>

To query forensic information, [AppSync](https://aws.amazon.com/appsync/) provides the following queries.

| Query | Description |
| --- | --- |
|  `allForensicRecords`  | Gets all the forensic records. It can be filtered by:<br />\* `awsAccountId` \* `awsRegion` \* `completionTime` \* `creationTime` \* `diskAnalysisStatus` \* `diskAnalysisStatusDescription` \* `id` \* `lastUpdatedTime` \* `memoryAnalysisStatus` \* `memoryAnalysisStatusDescription` \* `resourceId` \* `resourceInfo` \* `resourceType` \* `triageStatus` \* `triageStatusDescription`  |
|  `getForensicRecord`  | Gets all forensic records based on ForensicID |
|  `listForensicRecordsForAccount`  | Lists forensic records by account. |
|  `listForensicRecordsForRegion`  | Lists forensic records by account and Region. |
|  `listForensicRecordsForResource`  | Lists forensic records by account, Region and ResourceType. |
|  `timelineEventsForRecord`  | Gets timeline of events by ForensicID. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

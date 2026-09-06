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

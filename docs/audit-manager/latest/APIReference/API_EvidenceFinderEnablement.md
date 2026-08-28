---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceFinderEnablement.html
---

# EvidenceFinderEnablement
<a name="API_EvidenceFinderEnablement"></a>

The settings object that specifies whether evidence finder is enabled. This object also describes the related event data store, and the backfill status for populating the event data store with evidence data.

## Contents
<a name="API_EvidenceFinderEnablement_Contents"></a>

 ** backfillStatus **   <a name="auditmanager-Type-EvidenceFinderEnablement-backfillStatus"></a>
The current status of the evidence data backfill process.
The backfill starts after you enable evidence finder. During this task, Audit Manager populates an event data store with your past two years’ worth of evidence data so that your evidence can be queried.
+  `NOT_STARTED` means that the backfill hasn’t started yet.
+  `IN_PROGRESS` means that the backfill is in progress. This can take up to 7 days to complete, depending on the amount of evidence data.
+  `COMPLETED` means that the backfill is complete. All of your past evidence is now queryable.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED`
Required: No

 ** enablementStatus **   <a name="auditmanager-Type-EvidenceFinderEnablement-enablementStatus"></a>
The current status of the evidence finder feature and the related event data store.
+  `ENABLE_IN_PROGRESS` means that you requested to enable evidence finder. An event data store is currently being created to support evidence finder queries.
+  `ENABLED` means that an event data store was successfully created and evidence finder is enabled. We recommend that you wait 7 days until the event data store is backfilled with your past two years’ worth of evidence data. You can use evidence finder in the meantime, but not all data might be available until the backfill is complete.
+  `DISABLE_IN_PROGRESS` means that you requested to disable evidence finder, and your request is pending the deletion of the event data store.
+  `DISABLED` means that you have permanently disabled evidence finder and the event data store has been deleted. You can't re-enable evidence finder after this point.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLE_IN_PROGRESS | DISABLE_IN_PROGRESS`
Required: No

 ** error **   <a name="auditmanager-Type-EvidenceFinderEnablement-error"></a>
Represents any errors that occurred when enabling or disabling evidence finder.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** eventDataStoreArn **   <a name="auditmanager-Type-EvidenceFinderEnablement-eventDataStoreArn"></a>
The Amazon Resource Name (ARN) of the CloudTrail Lake event data store that’s used by evidence finder. The event data store is the lake of evidence data that evidence finder runs queries against.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:cloudtrail:.*`
Required: No

## See Also
<a name="API_EvidenceFinderEnablement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/EvidenceFinderEnablement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/EvidenceFinderEnablement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/EvidenceFinderEnablement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

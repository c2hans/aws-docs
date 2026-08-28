---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/changing-configuration-and-risks.html
---

# Changing configuration and associated risks
<a name="changing-configuration-and-risks"></a>

 Changing beacon configuration after data has been written can have significant correctness and security implications. Some configuration parameters directly affect how beacons are derived and queried, and incorrect changes might result in incomplete query results or ambiguous semantics. Misconfiguration does not cause data loss—data remains accessible via Scan—but it might prevent Query operations from returning complete results.

**Warning**
 Some configuration changes are effectively irreversible without rewriting data.

## Irreversible changes
<a name="changing-configuration-irreversible-changes"></a>
+  After the first item is written, the truncation length and beacon key must be treated as immutable.
+  Partition configuration must be monotonic; decreases are not supported.
+  Correcting these issues requires recomputing all affected beacons.

## What can go wrong
<a name="changing-configuration-what-can-go-wrong"></a>
+  Decreasing partition configuration (for example, `maximumNumberOfPartitions, defaultNumberOfPartitions, numberOfPartitions`) can cause queries to miss items and make existing `PartitionNumber` values ambiguous.
+  Changing the truncation length after writes might cause queries to return incomplete results.
+  Changing the beacon key invalidates all existing beacons.

## Recommended guidance
<a name="changing-configuration-recommended-guidance"></a>
+  Choose conservative truncation lengths and treat them as fixed.
+  Plan for partition growth up front and allow only increases over time.
+  Never change beacon keys without a full migration plan.

## Pre-flight checklist
<a name="changing-configuration-pre-flight-checklist"></a>

Before deployment, confirm:
+ The dataset is suitable for beacons.
+ Truncation length and partition growth are planned and documented.
+ Monitoring and alerting are in place for configuration changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

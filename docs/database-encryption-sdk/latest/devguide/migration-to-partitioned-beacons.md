---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/migration-to-partitioned-beacons.html
---

# Migration to partitioned beacons
<a name="migration-to-partitioned-beacons"></a>

 A non-partitioned table is equivalent to a table configured with `maximumNumberOfPartitions = 1`. From a configuration perspective, migrating from a non-partitioned setup to a partitioned one is therefore treated as an increase in `maximumNumberOfPartitions`.

Each individual beacon definition may be either unconstrained or constrained to a single `PartitionNumber`. These constraints are part of the beacon configuration and must remain unchanged over time.

Migration from non-partitioned to partitioned beacons follows the same rules as any other change to partition configuration:
+  `maximumNumberOfPartitions` may only be increased and cannot be decreased.
+  Increasing `maximumNumberOfPartitions` does not retroactively improve the anonymity of existing items.
+  Newly written items will use the updated partition configuration and be assigned a `PartitionNumber` accordingly.
+  Queries that include all partitions will continue to return both existing (non-partitioned) items and newly written partitioned items.

To improve the anonymity of existing items or the efficiency of the system, you might choose to re-encrypt some items in the table using an updated partitioning scheme. Re-encryption requires removing the existing item, regenerating its beacons under the new configuration, and writing the item back to the table. This process applies only to items that are explicitly rewritten; items that are not re-encrypted continue to use their original beacon configuration. Re-encrypting items might temporarily increase write traffic and affect application availability. Perform re-encryption in a controlled manner, such as through a staged or background migration.

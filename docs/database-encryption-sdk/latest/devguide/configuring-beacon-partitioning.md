---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configuring-beacon-partitioning.html
---

# Configuring Beacon Partitioning
<a name="configuring-beacon-partitioning"></a>

This section describes how beacon partitioning is configured and how it affects beacon derivation, query behavior, and security guarantees. Partitioning applies to all beacons and provides a consistent model for distributing values, limiting frequency leakage, and controlling query fan-out. Understanding how partition counts and partition assignment work together helps you choose configurations that balance privacy, performance, and operational safety.

## Overview of partition configuration
<a name="configuring-beacon-partitioning.overview"></a>

 Partitioning is configured at the logical table level and applies uniformly to all standard beacons. Each logical table defines a single partitioning scheme, which is controlled by two parameters: **maximumNumberOfPartitions** and **defaultNumberOfPartitions**.

## maximumNumberOfPartitions
<a name="configuring-beacon-partitioning.maximumNumberOfPartitions"></a>

 The `maximumNumberOfPartitions` field defines the upper bound on the number of partitions the table may use over its lifetime. This value:
+ Determines the maximum possible query fan-out.
+ Can be increased as data volume or security requirements evolve.
+ Must not be decreased after data exists.

## defaultNumberOfPartitions
<a name="configuring-beacon-partitioning.defaultNumberOfPartitions"></a>

 The `defaultNumberOfPartitions` field specifies how many partitions are used by standard beacons that do not explicitly declare their own partition count. This value:
+  Must satisfy `1 ≤ defaultNumberOfPartitions ≤ maximumNumberOfPartitions ≤ 255`.
+  Can be increased, but must never be decreased after items have been written.
+  Set this value to the same value as `maximumNumberOfPartitions` unless you intentionally want to constrain how many partitions an individual beacon can use. Limiting the number of partitions for a beacon can be useful when an attribute has a small or well-understood value space, when the attribute is queried very frequently, or when you want to reduce query fan-out and query cost. Constraining partitions trades some randomness and distribution benefits for improved query efficiency and predictability. For most attributes, using the full set of available partitions provides the best balance between privacy protection and flexibility.

## Partition assignment using a PartitionSelector
<a name="configuring-beacon-partitioning.partition-selector"></a>

 A user-provided function called `PartitionSelector` assigns each item to a partition at write time. It determines the partition number:

```
GetPartitionNumber(item, numberOfPartitions, logicalTableName) -> PartitionNumber
```

 You can encode domain knowledge in the selector to:
+ Distribute high-frequency values across multiple partitions.
+ Assign rare values consistently to a single partition.
+ Use the default random selector for general-purpose workloads.

 Beacon derivation incorporates the selected partition number, which is never exposed directly in the encrypted item or beacon value.

## Configuring partition counts on standard beacons
<a name="configuring-beacon-partitioning.standard-beacons"></a>

 By default, all standard beacons use `defaultNumberOfPartitions`. You can optionally constrain an individual beacon by setting `numberOfPartitions`. This is useful when:
+ The underlying data is already approximately uniformly distributed.
+ Query workloads are expected to return very small result sets.
+ Reducing query fan-out significantly improves performance.

 For constrained beacons, the effective partition used during beacon derivation is computed as:

```
effectivePartition = itemPartition % numberOfPartitions
```

 Apply beacon-level constraints only when necessary and with appropriate security review. Incorrect constraints can weaken anonymity guarantees or make existing items unreachable during queries.

### Example configuration syntax
<a name="w2aac15c27c17c13c15"></a>

------
#### [ Java ]

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beaconName}}")
    .length(beaconLengthInBits)
    .numberOfPartitions({{number}})
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

------
#### [ C\# / .NET ]

```
var standardBeaconList = new List<StandardBeacon>();
StandardBeacon exampleStandardBeacon = new StandardBeacon
  {
    Name = "{{beaconName}}",
    Length = 10,
    NumberOfPartitions = {{number}}
  };
standardBeaconList.Add(exampleStandardBeacon);
```

------
#### [ Rust ]

```
let standard_beacon_list = vec![
    StandardBeacon::builder()
        .name("{{beacon_name}}")
        .length({{beacon_length_in_bits}})
        .number_of_partitions({{number}})
        .build()?,
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

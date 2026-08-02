---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-partitions.html
---

# Determine whether you need more than one partition
<a name="choosing-beacon-partitions"></a>

All beacons are derived using partitions by default. In the simplest configuration, a beacon uses a single partition. Using additional partitions is a tuning decision that helps address skew, hot values, and frequency leakage, but it can also increase query fan-out because queries must be issued once per partition. This section explains when a single partition is sufficient and when you should configure multiple partitions.

## Start with population and uniformity
<a name="determine-partitioned-beacons.start"></a>

Begin by evaluating the attribute you plan to beaconize:
+  **Population size**: The beacon should be derived from a field with enough distinct values (for example, at least 32 unique values) for beaconization to be effective. If this requirement is not met, increasing the number of partitions can help distribute values more effectively.
+  **Frequency distribution**: Use uniformity analysis to assess whether the attribute has a mostly uniform distribution or shows noticeable skew.

  If an attribute has an approximately uniform distribution, a single partition is usually sufficient. If the distribution is skewed or contains clear hot values, configuring more than one partition is recommended.

## When multiple partitions are recommended
<a name="determine-partitioned-beacons.when-needed"></a>

Configuring more than one partition is recommended when one or more of the following conditions apply:
+  **Hot values or hot beacons**: A small number of values appear much more often than others (for example, a very common last name). These values create very large groups of identical beacons, making them easier to distinguish from other values.
+  **Uneven data distributions**: Some values appear very frequently, while many others appear only a few times. These rare values do not occur often enough to blend in with others, making it harder to protect them within sufficiently large groups.
+  **Longer beacon length is required**: Using a longer beacon length improves query accuracy but reduces the chance of collisions. Partitioning helps maintain collisions by spreading values across multiple partitions. Because each partition has its own beacon space, the same value can collide with different values in different partitions, helping balance privacy and precision.
+  **High-volume search on the attribute**: The attribute is queried frequently, and false positives are expensive. Partitioning allows you to increase beacon length to reduce false positives while still maintaining acceptable privacy protections.

## When a single partition is sufficient
<a name="determine-partitioned-beacons.when-not-needed"></a>

Using a single partition may be appropriate when:
+ The attribute’s distribution is approximately uniform and passes the uniformity checks.
+ The attribute is rarely used as a search predicate, or false positives and frequency leakage are not significant concerns.

In these cases, configuring the attribute with a single partition is simpler and avoids additional query fan-out.

In general, if an attribute is suitable for beaconization but exhibits skew, hot values, or anonymity constraints that cannot be met with a single partition, configuring multiple partitions provides a safer and more flexible solution.

---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-length.html
---

# Choosing a beacon length and partitions
<a name="choosing-beacon-length"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

When you write a new value to an encrypted field that is configured for searchable encryption, the AWS Database Encryption SDK calculates an HMAC over the plaintext value combined with a partition identifier. Within a given partition, the full HMAC uniquely represents the plaintext value. The SDK then truncates the HMAC output so that multiple distinct plaintext values can map to the same beacon. These collisions, also known as *false positives*, limit an unauthorized user’s ability to infer distinguishing information about the underlying plaintext.

The average number of false positives generated for each beacon is determined by the beacon length remaining after truncation and the number of partitions in use. You only need to define beacon length when configuring standard beacons. Compound beacons use the beacon lengths of the standard beacons they're constructed from. By distributing values across multiple partitions, collisions are maintained within each partition, which helps reduce frequency concentration while preserving correct query behavior.

The beacon does not alter the encrypted state of the field. However, when you use beacons, there is an inherent tradeoff between how efficient your queries are and how much information is revealed about the distribution of your data. Shorter beacon lengths and additional partitions increase collisions and reduce frequency leakage, while longer beacon lengths and fewer partitions improve query precision.

The goal of searchable encryption is to reduce the performance costs associated with client-side encrypted databases by using beacons to perform queries on encrypted data. Beacons are stored alongside the encrypted fields they are calculated from. This means that they can reveal distinguishing information about the distribution of your dataset. In extreme cases, an unauthorized user might be able to analyze the information revealed about your distribution and use it to identify a field's plaintext value. Choosing appropriate beacon lengths and partition counts helps mitigate these risks and preserve the confidentiality of your data.

Review your threat model to determine the level of security that you need. For example, the more individuals who have access to your database, but should not have access to the plaintext data, the more you might want to protect the confidentiality of your dataset distribution. Increasing confidentiality typically requires generating more false positives—through shorter beacon lengths, additional partitions, or both—which in turn can reduce query performance.

**Topics**
+ [Choosing a partitioning scheme](#choosing-partitioning-scheme)
+ [Calculating beacon length](#calculate-beacon-length)
+ [Advanced beacon length example](#beacon-length-example)

## Choosing a partitioning scheme
<a name="choosing-partitioning-scheme"></a>

 The partitioning scheme determines how items are distributed across partitions when beacons are derived. Choosing an appropriate scheme is important for balancing privacy, performance, and operational predictability.

When selecting a partitioning scheme, consider the following goals:
+  Distribute high-frequency values to reduce large beacon equivalence classes.
+  Avoid introducing predictable patterns that could leak sensitive information.
+  Maintain stable behavior across writes and queries.

### Default random distribution
<a name="w2aac15c25c29c17b9"></a>

 The recommended default is a random distribution scheme. In this model, each item is assigned to a partition using a cryptographically secure random value. Random distribution produces approximately equal partition sizes over time and ensures that frequent values are evenly spread.

Use random distribution when:
+  You do not have strong domain knowledge about value distributions.
+  The dataset contains unknown or evolving skew.
+  You want to minimize attribute-dependent leakage.

### Deterministic distribution
<a name="w2aac15c25c29c17c11"></a>

 In some cases, partition assignment must be deterministic. A deterministic scheme assigns partitions based on a stable function of item attributes. These schemes must be designed carefully, because skewed or sensitive inputs can result in uneven partitioning or unintended information leakage.

Use deterministic distribution when:
+  Operational workflows depend on consistent partition placement.
+  You have a set of unique values that are intentionally grouped into a single partition.

### Handling known hot values
<a name="w2aac15c25c29c17c13"></a>

 If your dataset contains well-known hot values, you can combine random and deterministic strategies. For example, you might randomly distribute a small set of high-frequency values while assigning all other values deterministically.

 This approach reduces concentration for hot values while preserving predictable behavior for the rest of the dataset. Because it introduces additional complexity, review it carefully to avoid unintended information leakage.

### Partitioning scheme examples
<a name="w2aac15c25c29c17c15"></a>

 The following examples illustrate common partitioning schemes and show how different data characteristics influence partition assignment. Each example demonstrates how to balance privacy, performance, and operational simplicity.

#### Example 1: Uniformly distributed data
<a name="w2aac15c25c29c17c15b5"></a>

 You are creating a beacon for phone numbers, and the values in your dataset are approximately uniformly distributed. No single phone number appears significantly more often than others.

 In this case, configuring a single partition is sufficient. Additional partitions provide little benefit and would only increase query fan-out.

#### Example 2: Binary outcomes with skewed frequency
<a name="w2aac15c25c29c17c15b7"></a>

 You have a database that stores medical test results with two possible values: NEGATIVE and POSITIVE. NEGATIVE results occur approximately five times more often than POSITIVE results.

 To reduce frequency leakage, use a mixed strategy:
+  Assign NEGATIVE results randomly across five partitions.
+  Assign POSITIVE results deterministically to a single partition.

 This approach spreads the overrepresented value while keeping the rarer value stable, reducing large equivalence classes without unnecessary fan-out.

#### Example 3: Known hot values in a large domain
<a name="w2aac15c25c29c17c15b9"></a>

 You have a database of first names in the United States. A relatively small set of common names (for example, the top 500 most frequent names) appears far more often than the rest.
+  Assign the top 500 most frequent names randomly across four partitions.
+  Assign all remaining names deterministically to a single partition.
+  Gradually increase the number of partitions until the data assigned to each partition exhibits an approximately uniform distribution.

 This hybrid approach targets known hot values while keeping partitioning simple and predictable for most names.

 These examples show how partitioning schemes can be adapted to different data characteristics. In most cases, random distribution is sufficient, but incorporating domain knowledge can further improve privacy and performance when applied carefully.

## Calculating beacon length
<a name="calculate-beacon-length"></a>

Beacon length is specified in bits and determines how many bits of the HMAC output are retained after truncation. The recommended length depends on how values are distributed within each partition, whether the data contains correlated values, and your security and performance requirements. When a dataset is approximately uniform after applying an appropriate partitioning scheme, you can use simple equations and tuning procedures to estimate an effective beacon length. These equations provide an estimate of the average number of false positives a beacon may produce, but they do not guarantee a specific number of false positives for every unique value in the dataset. The first step is to Estimate the population.

**Note**
The effectiveness of these equations is dependent on the distribution of your dataset within each partition. If your dataset is not uniformly distributed, see [Are beacons right for my dataset?](searchable-encryption.md#are-beacons-right-for-me).

### Estimate the population
<a name="estimate-population"></a>

The population is the expected number of unique values in the field that your standard beacon is constructed from, it is not the total expected number of values stored in the field. For example, consider an encrypted `Room` field that identifies the location of employee meetings. The `Room` field is expected to store 100,000 total values, but there are only 50 different rooms that employees can reserve for meetings. This means that the population is 50 because there only 50 possible unique values that can be stored in the `Room` field.

**Note**
If your standard beacon is constructed from a [virtual field](beacons.md#virtual-field), the population used to calculate beacon length is the number of unique combinations created by the virtual field.

When estimating your population, be sure to consider the projected growth of the dataset. After you have written new records with the beacon, you cannot update the beacon length. Review your threat model and any existing database solutions to create an estimate for the number of unique values you expect this field to store in the next five years.

Your population does not need to be precise. First, identify the number of unique values in your current database, or estimate the number of unique values that you expect to store in the first year. Next, use the following questions to help you determine the projected growth of unique values over the next five years.
+ Do you expect the unique values to multiply by 10?
+ Do you expect the unique values to multiply by 100?
+ Do you expect the unique values to multiply by 1000?

The difference between 50,000 and 60,000 unique values is not significant and they will both result in the same recommended beacon length. However, the difference between 50,000 and 500,000 unique values will significantly impact the recommended beacon length.

Consider reviewing public data on the frequency of common data types, such as ZIP codes or last names. For example, there are 41,707 ZIP codes in the United States. The population you use should be proportional to your own database. If the `ZIPCode` field in your database includes data from across the entire United States, then you might define your population as 41,707, even if the `ZIPCode` field does not *currently* have 41,707 unique values. If the `ZIPCode` field in your database only includes data from a single state, and will only ever include data from a single state, then you might define your population as the total number of ZIP codes in that state instead of 41,704.

### Calculating beacon length from population size
<a name="calculating-beacon-length"></a>

 When your data is approximately uniformly distributed within each partition and does not contain correlated values, you can estimate an appropriate beacon length using a simple population-based formula.

 Let *p* be the population size of the beacon—that is, the number of distinct plaintext values the beacon is constructed from within a single partition. A common starting point for the beacon length *b* (in bits) is:

```
b = log₂(p) − 1
```

 This formula preserves a non-negligible probability of collisions while keeping the number of false positives manageable. Subtracting one bit from the logarithm ensures that multiple distinct values are expected to map to the same beacon, which helps limit frequency leakage and supports anonymity.

 This calculation provides an estimate of the average collision behavior across the dataset. It does not guarantee that every value will produce the same number of false positives, nor does it account for skewed distributions, correlated values, or adversarial data patterns.

 Use this formula as an initial guideline rather than a strict requirement. Always validate the resulting configuration against your threat model, performance expectations, and observed data characteristics, and adjust the beacon length or number of partitions as needed.

### Advanced topic on beacon length
<a name="w2aac15c25c29c19c11"></a>

 As an advanced user, you have greater flexibility when selecting an appropriate beacon length for your solution. You must choose a length that adequately protects the confidentiality of your data while minimizing any unnecessary impact on query performance. The amount of security preserved by a beacon depends on the [distribution](searchable-encryption.md#searchable-encryption-distribution) of your dataset and the [correlation](searchable-encryption.md#searchable-encryption-correlated-values) of the fields that your beacons are constructed from.
+  A beacon length that is **too long** produces too few false positives and might reveal distinguishing information about the distribution of your dataset.
+  A beacon length that is **too short** produces too many false positives and increases the performance cost of queries because it requires broader scanning of the database.

If your dataset is approximately uniformly distributed, you can use the following equations and procedures to help estimate an appropriate beacon length for your implementation. These equations provide an estimate of the average number of false positives a beacon may produce, but they do not guarantee a specific number of false positives for every unique value in the dataset. The following topics assume that your beacons are uniformly distributed and do not contain correlated data.

1. **Calculate the recommended range for the expected number of collisions**

   To determine the appropriate beacon length for a given field, you must first identify an appropriate range for the expected number of collisions. The expected number of collisions represents the average expected number of unique plaintext values that map to a particular HMAC tag. The expected number of false positives for one unique plaintext value is one less than the expected number of collisions.

   We recommend that the expected number of collisions is greater than or equal to two, and less than the square root of your population. The following equations only work if your population has 16 or more unique values.

   ```
   2 ≤ number of collisions < √(Population)
   ```

   If the number of collisions is less than two, the beacon will produce too few false positives. We recommend two as the minimum number of expected collisions because it means, on average, every unique value in the field will generate at least one false positive by mapping to one other unique value.

1. **Calculate the recommended range for beacon lengths**

   After identifying the minimum and maximum number of expected collisions, use the following equation to identify a range of appropriate beacon lengths.

   ```
   number of collisions = Population * 2-(beacon length)
   ```

   First, solve for **beacon length** where the number of expected collisions equals two (the minimum recommended number of expected collisions).

   ```
   2 = Population * 2-(beacon length)
   ```

   Then, solve for **beacon length** where the expected number of collisions equals the square root of your population (the maximum recommended number of expected collisions).

   ```
   √(Population) = Population * 2-(beacon length)
   ```

   We recommend rounding the output produced by this equation down to the shorter beacon length. For example, if the equation produces a beacon length of 15.6, we recommend rounding that value down to 15 bits instead of rounding up to 16 bits.

1. **Choose a beacon length**

   These equations only identify a recommended range of beacon lengths for your field. We recommend using a shorter beacon length to preserve the security of your dataset whenever possible. However, the beacon length that you actually use is determined by your threat model. Consider your performance requirements as you review your threat model to determine the best beacon length for your field.

   Using a shorter beacon length reduces query performance, while using a longer beacon length decreases security. In general, if your dataset is unevenly [distributed](searchable-encryption.md#searchable-encryption-distribution), or if you construct distinct beacons from [correlated](searchable-encryption.md#searchable-encryption-correlated-values) fields, you need to use shorter beacon lengths to minimize the amount of information revealed about the distribution of your datasets.

   If you review your threat model and decide that any distinguishing information revealed about the distribution of a field does not present a threat to your overall security, you might choose to use a beacon length that is longer than the recommended range you calculated. For example, if you calculated the recommended range of beacon lengths for a field as 9—16 bits, you might choose to use a beacon length of 24 bits to avoid any performance loss.

   Choose your beacon length carefully. After you have written new records with the beacon, you cannot update the beacon length.

## Advanced beacon length example
<a name="beacon-length-example"></a>

Consider a database that marked the `unit` field as `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions). To configure a standard beacon for the `unit` field, we need to determine the expected number of false positives and beacon length for the `unit` field.

1. Estimate the population

   After reviewing our threat model and current database solution, we expect the `unit` field to eventually have 100,000 unique values.

   This means that **Population = 100,000**.

1. Calculate the recommended range for the expected number of collisions.

   For this example, the expected number of collisions should be between 2—316.

   ```
   2 ≤ number of collisions < √(Population)
   ```

   1.

      ```
      2 ≤ number of collisions < √({{100,000}})
      ```

   1.

      ```
      2 ≤ number of collisions < {{316}}
      ```

1. Calculate the recommended range for beacon length.

   For this example, the beacon length should be between 9—16 bits.

   ```
   number of collisions = Population * 2-(beacon length)
   ```

   1. Calculate the beacon length where the expected number of collisions equals the minimum identified in **Step 2**.

      ```
      2 = 100,000 * 2-(beacon length)
      ```

      Beacon length = 15.6, or 15 bits

   1. Calculate the beacon length where the expected number of collisions equals the maximum identified in **Step 2**.

      ```
      316 = 100,000 * 2-(beacon length)
      ```

      Beacon length = 8.3, or 8 bits

1. Determine the beacon length appropriate for your security and performance requirements.

   For every bit below 15, the performance cost and the security double.
   + 16 bits
     + On average, each unique value will map to 1.5 other units.
     + Security: two records with the same truncated HMAC tag are 66% likely to have the same plaintext value.
     + Performance: a query will retrieve 15 records for every 10 records that you actually requested.
   + 14 bits
     + On average, each unique value will map to 6.1 other units.
     + Security: two records with the same truncated HMAC tag are 33% likely to have the same plaintext value.
     + Performance: a query will retrieve 30 records for every 10 records that you actually requested.

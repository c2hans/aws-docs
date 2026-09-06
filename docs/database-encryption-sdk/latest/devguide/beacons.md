---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/beacons.html
---

# Beacons
<a name="beacons"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

A beacon is a truncated Hash-Based Message Authentication Code (HMAC) tag that maps a plaintext field value to an encrypted, searchable identifier stored alongside the encrypted data in your database. The beacon does not alter the encrypted state of the field. When you write a value to a field configured for searchable encryption, the AWS Database Encryption SDK computes an HMAC over the plaintext value and derives the beacon in the context of a partition. The full HMAC uniquely corresponds to the plaintext value, but the SDK intentionally truncates the output so that multiple distinct plaintext values can map to the same beacon. These collisions (false positives) limit an unauthorized user’s ability to infer distinguishing information about the underlying plaintext.

**Note**
 A *Hash-based Message Authentication Code (HMAC)* is a keyed cryptographic hash function commonly used to provide integrity and authenticity. In searchable encryption systems, HMAC is often used to deterministically derive *beacons* from plaintext values so they can be indexed and queried.

A full-length HMAC is deterministic: for a given key, the same plaintext value always produces the same beacon. This determinism results in a one-to-one mapping between plaintext values and beacons, preserving the original frequency distribution of the data. All records that share the same plaintext value map to the same beacon and therefore form an *equivalence class*. The size of each equivalence class directly reflects how frequently the corresponding plaintext value appears in the dataset.

 This frequency preservation enables *frequency-analysis attacks*, in which an observer infers likely plaintext values by correlating observed beacon frequencies with known or expected data distributions.

 To mitigate frequency-analysis attacks, the SDK derives beacons using *truncation* and *partitioning*. Truncating the HMAC introduces controlled collisions, so that not all records within an equivalence class necessarily share the same beacon value. In addition, incorporating a partition identifier into beacon derivation allows identical plaintext values to map to different beacons across partitions. Together, these techniques promote greater randomness for unevenly distributed datasets while preserving correct and efficient query behavior.

Beacons can only be constructed from fields that are marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in your [cryptographic actions](concepts.md#crypt-actions). The beacon itself is not signed or encrypted. You cannot construct a beacon with fields that are marked `DO_NOTHING`.

After you [configure your beacons](configure-beacons.md), you must configure a secondary index for each beacon before you can search on the encrypted fields. For more information, see [Configuring secondary indexes with beacons](ddb-searchable-encryption.md#ddb-beacon-indexes).

**Topics**
+ [Understanding beacon derivation across partitions](#partitioned-beacon-overview)
+ [Beacon types](#Beacon.Types)

## Understanding beacon derivation across partitions
<a name="partitioned-beacon-overview"></a>

Partitioning is a core part of beacon configuration and applies to all beacons, including those that use a single partition. This model ensures consistent and forward-compatible beacon derivation across all data, and allows you to increase the number of partitions over time as data volume or distribution changes. By doing so, you can reduce frequency leakage and strengthen protections for unevenly distributed datasets without rewriting existing items.

Partitions introduce controlled randomness by distributing items across multiple logical groups. This reduces frequency leakage, limits the size of beacon equivalence classes, and improves security and privacy for attributes with skewed distributions.

When an item is assigned to a partition, the partition number is incorporated into beacon derivation. Within the same partition, identical plaintext values produce the same beacon, preserving equality search semantics. Across different partitions, the same plaintext value produces different beacon values. This breaks large equivalence classes into smaller, per-partition groups and helps flatten the overall frequency distribution of beacons.

You have full control over how each database item is assigned to a partition. Items can be placed into specific partitions deterministically, or they can be distributed randomly to help smooth out uneven data distributions. Random assignment is especially useful for high-frequency values, because it spreads those values across multiple partitions and reduces visible concentration in any single partition. Deterministic assignment can be used when domain knowledge indicates that certain values should be constrained to fewer partitions.

The partition identifier is not exposed in the encrypted record. Instead, the partition number is incorporated into the beacon derivation process—hashed together with the plaintext value—so that it cannot be inferred by examining the encrypted data or the beacon itself. This design ensures that partition assignments remain confidential while still providing the distribution and privacy benefits of partitioned beacons.

 **Partitioning impact on querying**
Partitioning affects how `Query` operations are performed. Because DynamoDB queries require an exact match on the indexed beacon value, and beacon values differ across partitions, the caller must query each partition independently. If a table has `N` partitions:
+  Retrieving all matching items requires `N` separate queries.
+  Only `Query` is affected.
+  `Scan` and `Get` operations behave as before.
The reason is structural: `Scan` reads all items, and `Get` operates on a specific key; only `Query` depends on exact equality in the index, which becomes partition-specific.
**Fan-out **refers to the number of DynamoDB queries that must be issued to satisfy a single logical request when using partitioned beacons. The system provides **bounded fan-out**, meaning the maximum number of partition-level queries is fixed and predictable based on the configured number of partitions.
 ** Performance considerations**
Using partitions affects the number of DynamoDB queries required per logical request. The performance impact depends on the expected result size:
+  **Large result sets:** When queries return many pages, the extra partition-level queries add little overhead.
+  **Single-item lookups:** If a request normally returns one item and five partitions are configured, five queries are issued—four returning no results—resulting in a near-linear slowdown.
+  **Reduced locality:** Items may be spread across partitions, increasing retrieval time.
 Because each partition triggers an additional query, **fan-out** is an important factor in planning for performance and capacity.
 ** Performance advantages**
Despite the additional query overhead, partitions can improve performance in certain scenarios:
+  **Reducing large equivalence classes:** When a rare value shares a truncated beacon with a frequently occurring value, queries for the rare value must process many irrelevant matches. Partitioning limits the size of each equivalence class and reduces this overhead.
+  **Supporting longer beacon lengths:** Configuring more partitions can allow the use of longer beacon lengths, which lowers false-positive rates and reduces the amount of post-decryption filtering required.

## Beacon types
<a name="Beacon.Types"></a>

The type of beacon you configure determines the type of queries you are able to perform. There are two types of beacons that support searchable encryption. Standard beacons perform equality searches. Compound beacons combine literal plaintext strings and standard beacons to perform complex database operations.

### Standard beacons
<a name="standard-beacon-overview"></a>

Standard beacons are the simplest way to implement searchable encryption in your database. They can only perform equality searches for a single encrypted or virtual field. To learn how to configure standard beacons, see [Configuring standard beacons](configure-beacons.md#config-standard-beacons). You can also use [partitions](#partitioned-beacon-overview) with beacons to promote randomness when the underlying data has an uneven distribution.

The following are important concepts for standard beacons.

 **Beacon source**
The field that a standard beacon is constructed from is called the *beacon source*. It identifies the location of the data that the beacon needs to map. The beacon source can be either an encrypted field or a *virtual field*. The beacon source in each standard beacon must be unique. You cannot configure two beacons with the same beacon source.
Standard beacons can be used to perform equality searches for an encrypted or virtual field. Or, they can be used to construct compound beacons to perform more complex database operations. To help you organize and manage standard beacons, the AWS Database Encryption SDK provides the following optional *beacon styles* that define the intended use of a standard beacon. For more information see, [Defining beacon styles](configure-beacons.md#define-beacon-styles).
You can create a standard beacon that performs equality searches for a single encrypted field, or you can create a standard beacon that performs equality searches on the concatenation of multiple `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields by creating a virtual field.

**Virtual fields**
A virtual field is a conceptual field constructed from one or more source fields. Creating a virtual field does not write a new field to your record. The virtual field is not explicitly stored in your database. It is used in standard beacon configuration to give the beacon instructions on how to identify a specific segment of a field or concatenate multiple fields within a record to perform a specific query. A virtual field requires at least one encrypted field.
The following example demonstrates the types of transformations and queries you can perform with a virtual field. In application, the example fields used in this example might not meet the [distribution](searchable-encryption.md#searchable-encryption-distribution) and [correlation](searchable-encryption.md#searchable-encryption-correlated-values) uniqueness recommendations for beacons.
For example, if you want to perform equality searches on the concatenation of `FirstName` and `LastName` fields, you might create one of the following virtual fields.
+ A virtual `NameTag` field, constructed from the first letter of the `FirstName` field, followed by the `LastName` field, all in lowercase. This virtual field enables you to query `NameTag=mjones`.
+ A virtual `LastFirst` field, which is constructed from the `LastName` field, followed by the `FirstName` field. This virtual field enables you to query `LastFirst=JonesMary`.
Or, if you want to perform equality searches on a specific segment of an encrypted field, create a virtual field that identifies the segment you want to query.
For example, if you want to query an encrypted `IPAddress` field using the first three segments of the IP address, create the following virtual field.
+ A virtual `IPSegment` field, constructed from `Segments(‘.’, 0, 3)`. This virtual field enables you to query `IPSegment=192.0.2`. The query returns all records with an `IPAddress` value that starts with "192.0.2".
Virtual fields must be unique. Two virtual fields cannot be constructed from the exact same source fields.
For help configuring virtual fields and the beacons that use them, see [Creating a virtual field](configure-beacons.md#create-virtual-field).

### Compound beacons
<a name="compound-beacon-overview"></a>

Compound beacons create indexes that improve query performance and enable you to perform more complex database operations. You can use compound beacons to combine literal plaintext strings and standard beacons to perform complex queries on encrypted records, such as querying two different record types from a single index or querying a combination of fields with a sort key. For more compound beacon solution examples, see [Choose a beacon type](choosing-beacon-type.md).

Compound beacons can be constructed from standard beacons or a combination of standard beacons and signed fields. They are constructed from a list of parts. All compound beacons should include a list of [encrypted parts](configure-beacons.md#encrypted-parts) that identifies the `ENCRYPT_AND_SIGN` fields included in the beacon. Every `ENCRYPT_AND_SIGN` field must be identified by a standard beacon. More complex compound beacons might also include a list of [signed parts](configure-beacons.md#signed-parts) that identifies the plaintext `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields included in the beacon, and a list of [constructor parts](configure-beacons.md#constructor-parts) that identify all of the possible ways the compound beacon can assemble the fields.

**Note**
The AWS Database Encryption SDK also supports *signed beacons* that can be configured entirely from plaintext `SIGN_ONLY` and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields. Signed beacons are a type of compound beacon that index and perform complex queries on signed, but not encrypted, fields. For more information, see [Creating signed beacons](configure.md#signed-beacons).

For help configuring compound beacons, see [Configuring compound beacons](configure-beacons.md#config-compound-beacons).

The way you configure your compound beacon determines the types of queries it can perform. For example, you can make some encrypted and signed parts optional to allow for more flexibility in your queries. For more information on the types of queries compound beacons can perform, see [Querying beacons](using-beacons.md#querying-beacons).

---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/searchable-encryption.html
---

# Searchable encryption
<a name="searchable-encryption"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

Searchable encryption enables you to search encrypted records without decrypting the entire database. This is accomplished using *beacons*, which create a map between the plaintext value written to a field and the encrypted value that is actually stored in your database. The AWS Database Encryption SDK stores the beacon in a new field that it adds to the record. Depending on the type of beacon you use, you can perform exact match searches or more customized complex queries on your encrypted data.

**Note**
Searchable encryption in the AWS Database Encryption SDK differs from the searchable symmetric encryption defined in academic research, such as [searchable symmetric encryption](https://dl.acm.org/doi/10.1145/1180405.1180417).

A beacon is a truncated Hash-Based Message Authentication Code (HMAC) tag that maps a plaintext field value to an encrypted, searchable identifier. When you write a value to an encrypted field configured for searchable encryption, the AWS Database Encryption SDK computes an HMAC over the plaintext value. This HMAC output is a one‐to‐one (1:1) match for the plaintext value of that field. The SDK intentionally truncates the HMAC output so that multiple distinct plaintext values collide on the same beacon. These collisions (false positives) limit an unauthorized user’s ability to infer sensitive information from frequency patterns. When you query a beacon, the AWS Database Encryption SDK automatically filters out these false positives and returns the plaintext result of your query. To further address this problem of frequency leakage, beacons are partitioned, allowing identical plaintext values to produce different beacon values across partitions. When the table uses only a single partition, this behavior naturally matches traditional, non-partitioned beacons.

The average number of false positives for each beacon depends on the remaining beacon length after truncation and the number of partitions. For help determining the appropriate beacon length for your implementation, see [Determining beacon length](choosing-beacon-length.md).

**Note**
Searchable encryption is designed to be implemented in new, unpopulated databases. Any beacon configured in an existing database will only map new records uploaded to the database, there is no way for a beacon to map existing data.

**Topics**
+ [Are beacons right for my dataset?](#are-beacons-right-for-me)
+ [Searchable encryption scenario](#beacon-overview-example)

## Are beacons right for my dataset?
<a name="are-beacons-right-for-me"></a>

Using beacons to perform queries on encrypted data reduces the performance costs associated with client-side encrypted databases. When you use beacons, there is an inherent tradeoff between how efficient your queries are and how much information is revealed about the distribution of your data. The beacon does not alter the encrypted state of the field. When you encrypt and sign a field with the AWS Database Encryption SDK, the plaintext value of the field is never exposed to the database. The database stores the randomized, encrypted value of the field.

Beacons are stored alongside the [ encrypted fields they are calculated from](plan-searchable-encryption.md#plan-searchable-encryption.title). This means that even if an unauthorized user cannot view the plaintext values of an encrypted field, they might be able to perform statistical analysis on the beacons to learn more about the distribution of your dataset, and, in extreme cases, identify the plaintext values that a beacon maps to. Proper beacon configuration is essential for mitigating these risks. Selecting an appropriate beacon length and partitioning scheme preserves confidentiality by ensuring sufficient collisions and mitigating frequency-based attacks through limiting the concentration of values in any single beacon.

**Security vs. Performance**
+ Shorter beacon lengths and higher partition counts improve security by increasing collisions and reducing frequency leakage,
+ Longer beacon lengths and fewer partitions improve performance by reducing false positives and query fan-out.

In many practical scenarios, a well-chosen configuration can balance these competing goals. However, searchable encryption may not be able to deliver the desired levels of both security and performance for every dataset.

Before configuring any beacons, carefully review your threat model, security requirements, and performance needs, and consider the uniqueness characteristics of your dataset to determine whether searchable encryption is an appropriate choice.

**Distribution**
The security properties of a beacon depend on both the distribution of the underlying data and how the beacon is configured, including how many partitions are used. When you configure an encrypted field for searchable encryption, the AWS Database Encryption SDK computes an HMAC over each plaintext value written to that field and derives the beacon using a cryptographic key. Beacons are computed in the context of a partition, which allows identical plaintext values to produce different beacon values across partitions. When the table uses only a single partition, identical plaintext values always map to the same truncated HMAC tag, which can preserve frequency patterns from the original dataset.
Fields with highly skewed distributions require special care. For example, consider a database that stores the city of residence for all residents of Illinois. If you construct a beacon from the encrypted `City` field, the value “Chicago” will occur far more frequently than other cities. Even if an unauthorized user can only access encrypted items and beacon values, this imbalance may allow them to infer which records correspond to residents of Chicago by observing overrepresented beacons. Truncating the beacon can reduce this leakage by forcing more collisions, but the beacon length required to sufficiently hide severe skew can introduce significant performance overhead due to increased false positives.
To configure beacons safely, you should analyze the frequency distribution of your data and understand how truncation and partitioning interact. The number of bits retained in a beacon determines how much statistical information is exposed, while the number of partitions bounds how concentrated any single beacon value can become. Shorter beacon lengths and more partitions reduce frequency leakage but increase false positives and query fan-out. Longer beacon lengths and fewer partitions improve query efficiency but expose more information about the underlying distribution.
In some extreme cases, workloads are not viable when the table uses only a single partition. Attributes with very small populations or highly imbalanced binary outcomes—such as medical test results where NEGATIVE values dominate—cannot be protected using truncation alone. With one partition, a beacon short enough to hide the distribution collapses all values into a single tag, while a longer beacon makes rare values easy to identify. In these cases, partitioned beacons are required to make searchable encryption feasible. By distributing overrepresented values across multiple partitions, this approach reduces the size of equivalence classes and limits frequency leakage in ways that are not possible when using a single partition.

**Correlation**
We strongly recommend that you avoid constructing distinct beacons from fields with correlated values. Beacons constructed from correlated fields require shorter beacon lengths to sufficiently minimize the amount of information revealed about the distribution of each dataset to an unauthorized user. You must carefully analyze your dataset, including its entropy and the joint distribution of correlated values, to determine how much your beacons need to be truncated. If the resulting beacon length does not meet your performance needs, then beacons might not be a good fit for your dataset.
For example, you should not construct two separate beacons from `City` and `ZIPCode` fields because the ZIP code will likely be associated with just one city. Typically, the false positives generated by a beacon limit an unauthorized user's ability to identify distinguishing information about your dataset. But the correlation between the `City` and `ZIPCode` fields means that an unauthorized user can easily identify which results are false positives and distinguish the different ZIP codes.
You should also avoid constructing beacons from fields that contain the same plaintext values. For example, you should not construct a beacon from `mobilePhone` and `preferredPhone` fields because they likely hold the same values. If you construct distinct beacons from both fields, the AWS Database Encryption SDK creates the beacons for each field under different keys. This results in two different HMAC tags for the same plaintext value. The two distinct beacons are unlikely to have the same false positives and an unauthorized user might be able to distinguish different phone numbers.

Even if your dataset contains correlated fields or has an uneven distribution, you might be able to construct beacons that preserve the confidentiality of your dataset by using shorter beacon lengths. However, beacon length does not guarantee that every unique value in your dataset will produce a number of false positives that effectively minimizes the amount of distinguishing information revealed about your dataset. Beacon length only estimates the average number of false positives produced. The more unevenly distributed your dataset, the less effective beacon length is at determining the average number of false positives produced.

Carefully evaluate the distribution of the fields you choose to beaconize and determine how much truncation is required to meet your security requirements. The following topics in this chapter assume that, within each partition, beacon values are uniformly distributed and that the underlying data does not introduce correlations that would weaken these assumptions.

## Searchable encryption scenario
<a name="beacon-overview-example"></a>

The following example demonstrates a searchable encryption solution and illustrates the core concepts discussed in this chapter. In this scenario, certain field values occur very frequently, which would lead to large equivalence classes and increased frequency leakage if a single partition were used. To address this, the configuration uses multiple partitions so that highly frequent values are distributed more evenly, reducing leakage while preserving the ability to perform efficient equality searches.

Consider a database named `Employees` that tracks employee data for a company. Each record in the database contains fields called *EmployeeID*, *LastName*, *FirstName*, and *Address*. Each field in the `Employees` database is identified by the primary key `EmployeeID`.

The following is an example plaintext record in the database.

```
{
    "EmployeeID": 101,
    "LastName": "Jones",
    "FirstName": "Mary",
    "Address": {
                "Street": "123 Main",
                "City": "Anytown",
                "State": "OH",
                "ZIPCode": 12345
    }
}
```

If you marked the `LastName` and `FirstName` fields as `ENCRYPT_AND_SIGN` in your [cryptographic actions](concepts.md#crypt-actions), the values in these fields are encrypted locally before they're uploaded to the database. The encrypted data that is uploaded is fully randomized, the database doesn't recognize this data as being protected. It just detects typical data entries. This means that the record that is actually stored in the database might look like the following.

```
{
    "PersonID": 101,
    "LastName": "1d76e94a2063578637d51371b363c9682bad926cbd",
    "FirstName": "21d6d54b0aaabc411e9f9b34b6d53aa4ef3b0a35",
    "Address": {
                "Street": "123 Main",
                "City": "Anytown",
                "State": "OH",
                "ZIPCode": 12345
    }
}
```

If you need to query the database for exact matches in the `LastName` field, [configure a standard beacon](configure-beacons.md#config-standard-beacons) named *LastName* to map the plaintext values written to the `LastName` field to the encrypted values stored in the database.

This beacon calculates HMACs from the plaintext values in the `LastName` field. Each HMAC output is truncated so that it is no longer an exact match for the plaintext value. For example, the complete hash and the truncated hash for `Jones` might look like the following.

**Complete hash**

`2aa4e9b404c68182562b6ec761fcca5306de527826a69468885e59dc36d0c3f824bdd44cab45526f70a2a18322000264f5451acf75f9f817e2b35099d408c833`

**Truncated hash**

`b35099d408c833`

In a dataset with many employees, certain last names such as *Jones*, *Smith*, or *Johnson* may occur far more frequently than others. To reduce frequency leakage and limit the size of beacon equivalence classes, you should configure the **LastName** beacon to use more than one partition.

When partitions are enabled, each item is assigned to a partition at write time, and the partition number is incorporated into beacon derivation. As a result, employees with the same last name may map to different beacon values across partitions. This spreads highly frequent names across multiple partitions, reducing overrepresentation of any single beacon value.

After the standard beacon is configured, you can perform equality searches on the `LastName` field. For example, if you want to search for `Jones`, use the *LastName* beacon to perform the following query.

```
LastName = Jones
```

When querying for a specific high-frequency last name, such as **Jones**, the application should issue one query per partition using the **LastName** beacon. The AWS Database Encryption SDK then decrypts the results and automatically filters out any false positives, returning the correct plaintext records.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

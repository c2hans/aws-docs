---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-type.html
---

# Choosing a beacon type
<a name="choosing-beacon-type"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

With searchable encryption, you can search encrypted records by mapping the plaintext values in an encrypted field with a *beacon*. The type of beacon you configure determines the type of queries that you can perform.

We strongly recommend identifying and planning the types of queries that you need to perform before you configure your beacons. After you [configure your beacons](configure-beacons.md), you must configure a secondary index for each beacon before you can search on the encrypted fields. For more information, see [Configuring secondary indexes with beacons](ddb-searchable-encryption.md#ddb-beacon-indexes).

Beacons create a map between the plaintext value written to a field and the encrypted value that is actually stored in your database. You cannot compare the values of two standard beacons, even if they contain the same underlying plaintext. The two standard beacons will produce two different HMAC tags for the same plaintext values. As a result, standard beacons cannot perform the following queries.
+ `{{beacon1}} = {{beacon2}}`
+ `{{beacon1}} IN ({{beacon2}})`
+ `{{value}} IN ({{beacon1}}, {{beacon2}}, ...)`
+ `CONTAINS({{beacon1}}, {{beacon2}})`

You can only perform the above queries if you compare the [signed parts](configure-beacons.md#signed-parts) of compound beacons, with the exception of the `CONTAINS` operator, which you can use with compound beacons to identify the entire value of an encrypted or signed field that the assembled beacon contains. When you compare signed parts, you can optionally include the prefix of an [encrypted part](configure-beacons.md#encrypted-parts), but you cannot include the encrypted value of a field. For more information about the types of queries that standard and compound beacons can perform, see [Querying beacons](using-beacons.md#querying-beacons).

Consider the following searchable encryption solutions as you review your database access patterns. The following examples define which beacon to configure to satisfy different encryption and querying requirements.

## Standard beacons
<a name="plan-standard-beacon"></a>

[Standard beacons](beacons.md#standard-beacon-overview) can only perform equality searches. You can use standard beacons to perform the following queries.

### Query a single encrypted field
<a name="se-example1"></a>

If you want to identify records that contain a specific value for an encrypted field, create a standard beacon.

#### Examples
<a name="example1"></a>

For the following example, consider a database named `UnitInspection` that tracks inspection data for a production facility. Each record in the database contains fields called `work_id`, `inspection_date`, `inspector_id_last4`, and `unit`. The full inspector ID is a number between 0—99,999,999. However, to ensure that the dataset is uniformly distributed, the `inspector_id_last4` only stores the last four digits of the inspector's ID. Each field in the database is identified by the primary key `work_id`. The `inspector_id_last4` and `unit` fields are marked `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions).

The following is an example of a plaintext entry in the `UnitInspection` database.

```
{
    "work_id": "1c7fcff3-6e74-41a8-b7f7-925dc039830b",
    "inspection_date": 2023-06-07,
    "inspector_id_last4": 8744,
    "unit": 229304973450
}
```

**Query a single encrypted field in a record**
If the `inspector_id_last4` field needs to be encrypted, but you still need query it for exact matches, construct a standard beacon from the `inspector_id_last4` field. Then, use the standard beacon to create a secondary index. You can use this secondary index to query on the encrypted `inspector_id_last4` field.

For help configuring standard beacons, see [Configuring standard beacons](configure-beacons.md#config-standard-beacons).

### Query a virtual field
<a name="se-example2"></a>

A [virtual field](beacons.md#virtual-field) is a conceptual field constructed from one or more source fields. If you want to perform equality searches for a specific segment of an encrypted field, or perform equality searches on the concatenation of multiple fields, construct a standard beacon from a virtual field. All virtual fields must include at least one encrypted source field.

#### Examples
<a name="example2"></a>

The following examples create virtual fields for the `Employees` database. The following is an example plaintext record in the `Employees` database.

```
{
    "EmployeeID": 101,
    "SSN": 000-00-0000,
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

**Query a segment of an encrypted field**
For this example, the `SSN` field is encrypted.
If you want to query the `SSN` field using the last four digits of a social security number, create a virtual field that identifies the segment you plan to query.
A virtual `Last4SSN` field, constructed from `Suffix(4)` enables you to query `Last4SSN=0000`. Use this virtual field to construct a standard beacon. Then, use the standard beacon to create a secondary index. You can use this secondary index to query on the virtual field. This query returns all records with an `SSN` value that ends with the last four digits you specified.

**Query the concatenation of multiple fields**
The following example demonstrates the types of transformations and queries you can perform with a virtual field. In application, the example fields used in this example might not meet the [distribution](searchable-encryption.md#searchable-encryption-distribution) and [correlation](searchable-encryption.md#searchable-encryption-correlated-values) uniqueness recommendations for beacons.
If you want to perform equality searches on a concatenation of `FirstName` and `LastName` fields, you might create a virtual `NameTag` field, constructed from the first letter of the `FirstName` field, followed by the `LastName` field, all in lowercase. Use this virtual field to construct a standard beacon. Then, use the standard beacon to create a secondary index. You can use this secondary index to query `NameTag=mjones` on the virtual field.
At least one of the source fields must be encrypted. Either `FirstName` or `LastName` could be encrypted, or they could both be encrypted. Any plaintext source fields must be marked as `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in your [cryptographic actions](concepts.md#crypt-actions).

For help configuring virtual fields and the beacons that use them, see [Creating a virtual field](configure-beacons.md#create-virtual-field).

## Compound beacons
<a name="plan-compound-beacons"></a>

[Compound beacons](beacons.md#compound-beacon-overview) create an index from literal plaintext strings and standard beacons to perform complex database operations. You can use compound beacons to perform the following queries.

### Query a combination of encrypted fields on a single index
<a name="se-example3"></a>

If you need to query a combination of encrypted fields on a single index, create a compound beacon that combines the individual standard beacons constructed for each encrypted field to form a single index.

After you configure the compound beacon, you can create a secondary index that specifies the compound beacon as the partition key to perform exact match queries or with a sort key to perform more complex queries. Secondary indexes that specify the compound beacon as the sort key can perform exact match queries and more customized complex queries.

#### Examples
<a name="example3"></a>

For the following examples, consider a database named `UnitInspection` that tracks inspection data for a production facility. Each record in the database contains fields called `work_id`, `inspection_date`, `inspector_id_last4`, and `unit`. The full inspector ID is a number between 0—99,999,999. However, to ensure that the dataset is uniformly distributed, the `inspector_id_last4` only stores the last four digits of the inspector's ID. Each field in the database is identified by the primary key `work_id`. The `inspector_id_last4` and `unit` fields are marked `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions).

The following is an example of a plaintext entry in the `UnitInspection` database.

```
{
    "work_id": "1c7fcff3-6e74-41a8-b7f7-925dc039830b",
    "inspection_date": 2023-06-07,
    "inspector_id_last4": 8744,
    "unit": 229304973450
}
```

**Perform equality searches on a combination of encrypted fields**
If you want to query the `UnitInspection` database for exact matches on `inspector_id_last4.unit`, first create distinct standard beacons for the `inspector_id_last4` and `unit` fields. Then, create a compound beacon from the two standard beacons.
After you configure the compound beacon, create a secondary index that specifies the compound beacon as the partition key. Use this secondary index to query for exact matches on `inspector_id_last4.unit`. For example, you could query this beacon to find a list of inspections that an inspector performed for a given unit.

**Perform complex queries on a combination of encrypted fields**
If you want to query the `UnitInspection` database on `inspector_id_last4` and `inspector_id_last4.unit`, first create distinct standard beacons for the `inspector_id_last4` and `unit` fields. Then, create a compound beacon from the two standard beacons.
After you configure the compound beacon, create a secondary index that specifies the compound beacon as the sort key. Use this secondary index to query the `UnitInspection` database for entries that start with a certain inspector or query the database for a list of all of the units within a specific unit ID range that were inspected by a certain inspector. You can also perform exact match searches on `inspector_id_last4.unit`.

For help configuring compound beacons, see [Configuring compound beacons](configure-beacons.md#config-compound-beacons).

### Query a combination of encrypted and plaintext fields on a single index
<a name="se-example4"></a>

If you need to query a combination of encrypted and plaintext fields on a single index, create a compound beacon that combines individual standard beacons and plaintext fields to form a single index. The plaintext fields used to construct the compound beacon must be marked `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in your [cryptographic actions](concepts.md#crypt-actions).

After you configure the compound beacon, you can create a secondary index that specifies the compound beacon as the partition key to perform exact match queries or with a sort key to perform more complex queries. Secondary indexes that specify the compound beacon as the sort key can perform exact match queries and more customized complex queries.

#### Examples
<a name="example4"></a>

For the following examples, consider a database named `UnitInspection` that tracks inspection data for a production facility. Each record in the database contains fields called `work_id`, `inspection_date`, `inspector_id_last4`, and `unit`. The full inspector ID is a number between 0—99,999,999. However, to ensure that the dataset is uniformly distributed, the `inspector_id_last4` only stores the last four digits of the inspector's ID. Each field in the database is identified by the primary key `work_id`. The `inspector_id_last4` and `unit` fields are marked `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions).

The following is an example of a plaintext entry in the `UnitInspection` database.

```
{
    "work_id": "1c7fcff3-6e74-41a8-b7f7-925dc039830b",
    "inspection_date": 2023-06-07,
    "inspector_id_last4": 8744,
    "unit": 229304973450
}
```

**Perform equality searches on a combination of fields**
If you want to query the `UnitInspection` database for inspections conducted by a specific inspector on a specific date, first create a standard beacon for the `inspector_id_last4` field. The `inspector_id_last4` field is marked `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions). All encrypted parts require their own standard beacon. The `inspection_date` field is marked `SIGN_ONLY` and does not require a standard beacon. Next, create a compound beacon from the `inspection_date` field and the `inspector_id_last4` standard beacon.
After you configure the compound beacon, create a secondary index that specifies the compound beacon as the partition key. Use this secondary index to query the databases for records with exact matches to a certain inspector and inspection date. For example, you can query the database for a list of all inspections that the inspector whose ID ends with `8744` conducted on a specific date.

**Perform complex queries on a combination of fields**
If you want to query the database for inspections conducted within an `inspection_date` range, or query the database for inspections conducted on a particular `inspection_date` constrained by `inspector_id_last4` or `inspector_id_last4.unit`, first create distinct standard beacons for the `inspector_id_last4` and `unit` fields. Then, create a compound beacon from the plaintext `inspection_date` field and the two standard beacons.
After you configure the compound beacon, create a secondary index that specifies the compound beacon as the sort key. Use this secondary index to perform queries for inspections conducted on specific dates by a specific inspector. For example, you can query the database for a list of all units inspected on the same date. Or, you can query the database for a list of all inspections performed on a specific unit between a given range of inspection dates.

For help configuring compound beacons, see [Configuring compound beacons](configure-beacons.md#config-compound-beacons).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

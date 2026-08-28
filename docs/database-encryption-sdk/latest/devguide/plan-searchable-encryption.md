---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/plan-searchable-encryption.html
---

# Planning beacons
<a name="plan-searchable-encryption"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

Beacons are designed to be implemented in new, unpopulated databases. Any beacon configured in an existing database will only map new records written to the database. Beacons are calculated from the plaintext value of a field, once the field is encrypted there is no way for the beacon to map existing data. After you have written new records with a beacon, you cannot update the beacon's configuration. However, you can add new beacons for new fields that you add to your record.

To implement searchable encryption, you must use the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) to generate, encrypt, and decrypt the data keys used to protect your records. For more information, see [Using the Hierarchical keyring for searchable encryption](use-hierarchical-keyring.md#searchable-encryption-hierarchical-keyrings).

Before you can configure [beacons](searchable-encryption.md#beacon-definition) for searchable encryption, you need to review your encryption requirements, database access patterns, and threat model to determine the best solution for your database.

The [type of beacon](beacons.md) that you configure determines the type of queries that you can perform. The [beacon length](choosing-beacon-length.md) that you specify in standard beacon configuration determines the expected number of false positives produced for a given beacon. We strongly recommend identifying and planning the types of queries that you need to perform before you configure your beacons. Once you have used a beacon, the configuration cannot be updated.

We strongly recommend that you review and complete the following tasks before you configure any beacons.
+ [Determine if beacons are right for your dataset](searchable-encryption.md#are-beacons-right-for-me)
+ [Choose a beacon type](choosing-beacon-type.md)
+ [ Determine whether you need partitioned beacons ](choosing-beacon-partitions.md)
+ [Choose a beacon length](choosing-beacon-length.md)
+ [Choose a beacon name](choosing-beacon-name.md)

Remember the following beacon uniqueness requirements as you plan the searchable encryption solution for your database.
+ **Every standard beacon must have a unique [beacon source](beacons.md#beacon-source)**

  Multiple standard beacons cannot be constructed from the same encrypted or virtual field.

  However, a single standard beacon can be used to construct multiple compound beacons.
+ **Avoid creating a virtual field with source fields that overlap with existing standard beacons**

  Constructing a standard beacon from a virtual field that contains a source field that was used to create another standard beacon can reduce the security of both beacons.

  For more information, see [Security considerations for virtual fields](configure-beacons.md#virtual-field-considerations).

## Considerations for multitenant databases
<a name="planning-multitenant-beacons"></a>

To query beacons configured in a multitenant database, you must include the field that stores the `branch-key-id` associated with the tenant that encrypted the record in your query. You define this field when you [define the beacon key source](use-hierarchical-keyring.md#beacon-key-source). For the query to succeed, the value in this field must identify the appropriate beacon key materials required to recalculate the beacon.

Before you configure your beacons, you must decide how you plan to include the `branch-key-id` in your queries. For more information on the different ways you can include the `branch-key-id` in your queries, see [Querying beacons in a multitenant database](searchable-encryption-multitenant.md#query-multitenant-beacons).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

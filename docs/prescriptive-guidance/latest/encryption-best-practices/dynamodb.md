---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/dynamodb.html
---

# Amazon DynamoDB
<a name="dynamodb"></a>

[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance. DynamoDB encryption at rest secures data in an encrypted table—including its primary key, local and global secondary indexes, streams, global tables, backups, and DynamoDB Accelerator (DAX) clusters whenever the data is stored in durable media.

In accordance with data classification requirements, data confidentiality and integrity can be maintained by implementing server-side or client-side encryption:

For server-side encryption, when you create a new table, you can use AWS KMS keys to encrypt the table. You can use AWS owned keys, AWS managed keys, or customer managed keys. We recommend using customer managed keys because your organization has full control of the key, and because when you use this key type, the table-level encryption key, the DynamoDB table, local and global secondary indexes, and streams are all encrypted with the same key. For more information about these key types, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).

|
|
| Note: You can switch between an AWS owned key, AWS managed key, and customer managed key at any given time. |
| --- |

For client-side encryption and end-to-end protection of data, both at rest and in transit, you can use the [Amazon DynamoDB Encryption Client](https://docs.aws.amazon.com/dynamodb-encryption-client/latest/devguide/what-is-ddb-encrypt.html). In addition to encryption, which protects the confidentiality of the item attribute value, DynamoDB Encryption Client signs the item. This provides integrity protection by enabling detection of unauthorized changes to the item, including adding or deleting attributes, or substituting one encrypted value for another.

Consider the following encryption best practices for this service:
+ Limit permissions to disable or schedule deletion of the key to only those who need to perform these tasks. These states prevent all users and the DynamoDB service from being able to encrypt or decrypt data and to perform read and write operations on the table.
+ While DynamoDB encrypts data in transit by using HTTPS by default, additional security controls are recommended. You can use any of the following options:
  + AWS Site-to-Site VPN connection using IPsec for encryption.
  + AWS Direct Connect connection to establish a private connection.
  + AWS Direct Connect connection with AWS Site-to-Site VPN connection for an IPsec-encrypted private connection.
  + If access to DynamoDB is required only from within a virtual private cloud (VPC), you can use a VPC gateway endpoint and allow only resources in the VPC to access it. This prevents the traffic from traversing the public internet.
+ If you are using VPC endpoints, restrict the endpoint policies and IAM policies associated with the endpoint to only authorized users, resources, and services. For more information, see [Control access to DynamoDB endpoints by using IAM policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html#iam-policies-ddb) and [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).
+ You can implement column-level data encryption at the application level for data that requires encryption, according to your encryption policy.
+ Configure DAX clusters to encrypt data at rest, such as data in cache, configuration data, and log files, at the time of setting up the cluster. You can't enable encryption at rest on an existing cluster. This server-side encryption helps protect data from unauthorized access through the underlying storage. DAX encryption at rest automatically integrates with AWS KMS for managing the single-service default key that is used to encrypt the clusters. If a service default key doesn't exist when an encrypted DAX cluster is created, AWS KMS automatically creates a new AWS managed key. For more information, see [DAX encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html).

<table>
<tbody>
</tbody>
</table>

+ Configure DAX clusters to encrypt data in transit at the time of setting up the cluster. You can't enable encryption in transit on an existing cluster. DAX uses TLS to encrypt requests and responses between the application and the cluster, and it uses the cluster's x509 certificate to authenticate the identity of the cluster. For more information, see [DAX encryption in transit](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html).
+ In AWS Config, implement the [dax-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dax-encryption-enabled.html) AWS managed rule to validate and maintain encryption of DAX clusters.

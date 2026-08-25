---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-beacons.html
---

# Using beacons
<a name="using-beacons"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

Beacons enable you to search encrypted records without decrypting the entire database being queried. Beacons are designed to be implemented in new, unpopulated databases. Any beacon configured in an existing database will only map new records written to the database. Beacons are calculated from the plaintext value of a field, once the field is encrypted there is no way for the beacon to map existing data. After you have written new records with a beacon, you cannot update the beacon's configuration. However, you can add add new beacons for new fields that you add to your record.

After you configure your beacons, you must complete the following steps before you begin populating your database and performing queries on your beacons.

1. **Create an AWS KMS Hierarchical keyring**

   To use searchable encryption, you must use the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) to generate, encrypt, and decrypt the [data keys](concepts.md#data-key) used to protect your records.

   After you configure your beacons, assemble the [Hierarchical keyring prerequisites](use-hierarchical-keyring.md#hierarchical-keyring-prereqs) and [create your Hierarchical keyring](use-hierarchical-keyring.md#initialize-hierarchical-keyring).

   For more details on why the Hierarchical keyring is required, see [Using the Hierarchical keyring for searchable encryption](use-hierarchical-keyring.md#searchable-encryption-hierarchical-keyrings).

1.

   **Define the beacon version **

   Specify your `keyStore`, `keySource`, a list of all standard beacons you configured, a list of all compound beacons you configured, a list of encrypted parts, a list of signed parts, and a beacon version. You must specify `1` for the beacon version. For guidance on defining your `keySource`, see [Defining your beacon key source](use-hierarchical-keyring.md#beacon-key-source).

   The following Java example defines the beacon version for a single tenant database. For help defining the beacon version for a multitenant database, see [Searchable encryption for multitenant databases](searchable-encryption-multitenant.md).

------
#### [ Java ]

   ```
    List<BeaconVersion> beaconVersions = new ArrayList<>();
   beaconVersions.add(
       BeaconVersion.builder()
           .standardBeacons(standardBeaconList)
           .compoundBeacons(compoundBeaconList)
           .encryptedParts(encryptedPartsList)
           .signedParts(signedPartsList)
           .version(1) // MUST be 1
           .keyStore(keyStore)
           .keySource(BeaconKeySource.builder()
               .single(SingleKeyStore.builder()
                   .keyId(branchKeyId)
                   .cacheTTL(6000)
                   .build())
               .build())
           .build()
   );
   ```

------
#### [ C\# / .NET ]

   ```
   var beaconVersions = new List<BeaconVersion>
   {
       new BeaconVersion
       {
           StandardBeacons = standardBeaconList,
           CompoundBeacons = compoundBeaconList,
           EncryptedParts = encryptedPartsList,
           SignedParts = signedPartsList,
           Version = 1, // MUST be 1
           KeyStore = {{branchKeyStoreName}},
           KeySource = new BeaconKeySource
           {
               Single = new SingleKeyStore
               {
                   KeyId = {{branch-key-id}},
                   CacheTTL = {{6000}}
               }
           }
       }
   };
   ```

------
#### [ Rust ]

   ```
   let beacon_version = BeaconVersion::builder()
       .standard_beacons(standard_beacon_list)
       .compound_beacons(compound_beacon_list)
       .version(1) // MUST be 1
       .key_store(key_store.clone())
       .key_source(BeaconKeySource::Single(
           SingleKeyStore::builder()
               // `keyId` references a beacon key.
               // For every branch key we create in the keystore,
               // we also create a beacon key.
               // This beacon key is not the same as the branch key,
               // but is created with the same ID as the branch key.
               .key_id(branch_key_id)
               .cache_ttl(6000)
               .build()?,
       ))
       .build()?;
   let beacon_versions = vec![beacon_version];
   ```

------

1. **Configure secondary indexes**

   After you [configure your beacons](configure-beacons.md), you must configure a secondary index that reflects each beacon before you can search on the encrypted fields. For more information, see [Configuring secondary indexes with beacons](ddb-searchable-encryption.md#ddb-beacon-indexes).

1. **Define your [cryptographic actions](concepts.md#crypt-actions)**

   All fields used to construct a standard beacon must be marked `ENCRYPT_AND_SIGN`. All other fields used to construct beacons must be marked `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

1. **Configure an AWS Database Encryption SDK client**

   To configure an AWS Database Encryption SDK client that protects the table items in your DynamoDB table, see [Java client-side encryption library for DynamoDB](ddb-java.md).

## Querying beacons
<a name="querying-beacons"></a>

The type of beacon you configure determines the type of queries you are able to perform. Standard beacons use filter expressions to perform equality searches. Compound beacons combine literal plaintext strings and standard beacons to perform complex queries. When you query encrypted data, you search on the beacon name.

You cannot compare the values of two standard beacons, even if they contain the same underlying plaintext. The two standard beacons will produce two different HMAC tags for the same plaintext values. As a result, standard beacons cannot perform the following queries.
+ `{{beacon1}} = {{beacon2}}`
+ `{{beacon1}} IN ({{beacon2}})`
+ `{{value}} IN ({{beacon1}}, {{beacon2}}, ...)`
+ `CONTAINS({{beacon1}}, {{beacon2}})`

Compound beacons can perform the following queries.
+ `BEGINS_WITH({{a}})`, where `{{a}}` reflects the entire value of the field that the assembled compound beacon begins with. You cannot use the `BEGINS_WITH` operator to identify a value that begins with a particular substring. However, you can use `BEGINS_WITH({{S_}})`, where `{{S_}}` reflects the prefix for a part that the assembled compound beacon begins with.
+ `CONTAINS({{a}})`, where `{{a}}` reflects the entire value of a field that the assembled compound beacon contains. You cannot use the `CONTAINS` operator to identify a record that contains a particular substring or a value within a set.

  For example, you cannot perform a query `CONTAINS({{path}}, "{{a}}"` where `{{a}}` reflects the value in a set.
+ You can compare [signed parts](configure-beacons.md#signed-parts) of compound beacons. When you compare signed parts, you can optionally append the prefix of an [encrypted part](configure-beacons.md#encrypted-parts) to one or more signed parts, but you cannot include the value of an encrypted field in any query.

  For example, you can compare signed parts and query on `{{signedField1}} = {{signedField2}}` or `{{value}} IN ({{signedField1}}, {{signedField2}}, ...)`.

  You can also compare signed parts and the prefix of an encrypted part by query on `{{signedField1.A_}} = {{signedField2.B_}}`.
+ `{{field}} BETWEEN {{a}} AND {{b}}`, where `{{a}}` and `{{b}}` are signed parts. You can optionally append the prefix of an encrypted part to one or more signed parts, but you cannot include the value of an encrypted field in any query.

You must include the prefix for each part you include in a query on a compound beacon. For example, if you constructed a compound beacon, `compoundBeacon`, from two fields, `encryptedField` and `signedField`, you must include the prefixes configured for those two parts when you query the beacon.

```
compoundBeacon = E_{{encryptedFieldValue}}.S_{{signedFieldValue}}
```

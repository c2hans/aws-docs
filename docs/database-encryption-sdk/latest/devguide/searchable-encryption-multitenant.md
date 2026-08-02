---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/searchable-encryption-multitenant.html
---

# Searchable encryption for multitenant databases
<a name="searchable-encryption-multitenant"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

To implement searchable encryption in your database, you must use an [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md). The AWS KMS Hierarchical keyring generates, encrypts, and decrypts the data keys used to protect your records. It also creates the beacon key used to generate beacons. When using the AWS KMS Hierarchical keyring with multitenant databases, there is a distinct branch key and beacon key for each tenant. To query encrypted data in a multitenant database, you must identify the beacon key materials used to generate the beacon you are querying. For more information, see [Using the Hierarchical keyring for searchable encryption](use-hierarchical-keyring.md#searchable-encryption-hierarchical-keyrings).

When you define the [beacon version](using-beacons.md#beacon-version) for a multitenant database, specify a list of all standard beacons you configured, a list of all compound beacons you configured, a beacon version, and a `keySource`. You must [define your beacon key source](use-hierarchical-keyring.md#beacon-key-source) as a `MultiKeyStore`, and include a `keyFieldName`, a cache time to live for the local beacon key cache, and maximum cache size for the local beacon key cache.

If you configured any [signed beacons](configure.md#signed-beacons), they must be included in your `compoundBeaconList`. Signed beacons are a type of compound beacon that index and perform complex queries on `SIGN_ONLY` and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`fields.

------
#### [ Java ]

```
List<BeaconVersion> beaconVersions = new ArrayList<>();
    beaconVersions.add(
        BeaconVersion.builder()
                .standardBeacons(standardBeaconList)
                .compoundBeacons(compoundBeaconList)
                .version(1) // MUST be 1
                .keyStore({{branchKeyStoreName}})
                .keySource(BeaconKeySource.builder()
                        .multi(MultiKeyStore.builder()
                                .keyFieldName({{keyField}})
                                .cacheTTL({{6000}})
                                .maxCacheSize({{10}})
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
            Multi = new MultiKeyStore
            {
                KeyId = {{branch-key-id}},
                CacheTTL = {{6000}},
                MaxCacheSize = {{10}}
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
    .key_source(BeaconKeySource::Multi(
        MultiKeyStore::builder()
            // `keyId` references a beacon key.
            // For every branch key we create in the keystore,
            // we also create a beacon key.
            // This beacon key is not the same as the branch key,
            // but is created with the same ID as the branch key.
            .key_id(branch_key_id)
            .cache_ttl(6000)
            .max_cache_size(10)
            .build()?,
    ))
    .build()?;
let beacon_versions = vec![beacon_version];
```

------

**keyFieldName**
The [`keyFieldName`](use-hierarchical-keyring.md#keyFieldName) defines the name of the field that stores the `branch-key-id` associated with the beacon key used to generated beacons for a given tenant.
When you write new records to your database, the `branch-key-id` that identifies the beacon key used to generate any beacons for that record is stored in this field.
By default, the `keyField` is a conceptual field that is not explicitly stored in your database. The AWS Database Encryption SDK identifies the `branch-key-id` from the encrypted [data key](concepts.md#data-key) in the [material description](concepts.md#material-description) and stores the value in the conceptual `keyField` for you to reference in your compound beacons and [signed beacons](configure.md#signed-beacons). Since the material description is signed, the conceptual `keyField` is considered a signed part.
You can also include the `keyField` in your cryptographic actions as a `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` field to explicitly store the field in your database. If you do this, you must manually include the `branch-key-id` in the `keyField` every time you write a record to your database.

## Querying beacons in a multitenant database
<a name="query-multitenant-beacons"></a>

To query a beacon, you must include the `keyField` in your query to identify the appropriate beacon key materials required to recalculate the beacon. You must specify the `branch-key-id` associated with the beacon key used to generate the beacons for a record. You cannot specify the [friendly name](use-hierarchical-keyring.md#branch-key-id-supplier) that identifies a tenant's `branch-key-id` in the branch key ID supplier. You can include the `keyField` in your queries in a following ways.

**Compound beacons**
Whether you explicitly store the `keyField` in your records or not, you can include the `keyField` directly in your compound beacons as a signed part. The `keyField` signed part must be required.
For example, if you want to construct a compound beacon, `compoundBeacon`, from two fields, `encryptedField` and `signedField`, you must also include the `keyField` as a signed part. This enables you to perform the following query on `compoundBeacon`.

```
compoundBeacon = E_encryptedFieldValue.S_signedFieldValue.K_{{branch-key-id}}
```

**Signed beacons**
The AWS Database Encryption SDK uses standard and compound beacons to provide searchable encryption solutions. These beacons must include at least one encrypted field. However, the AWS Database Encryption SDK also supports [signed beacons](configure.md#signed-beacons) that can be configured entirely from plaintext `SIGN_ONLY` and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields.
Signed beacons can be constructed from a single part. Whether you explicitly store the `keyField` in your records or not, you can construct a signed beacon from the `keyField` and use it to create compound queries that combine a query on the `keyField` signed beacon with a query on one of your other beacons. For example, you could perform the following query.

```
keyField = K_{{branch-key-id}} AND compoundBeacon = E_encryptedFieldValue.S_signedFieldValue
```
For help configuring signed beacons, see [Creating signed beacons](configure.md#signed-beacons)

**Query directly on the `keyField`**
If you specified the `keyField` in your cryptographic actions and explicitly store the field in your record, you can create a compound query that combines a query on your beacon with a query on the `keyField`. You might choose to query directly on the `keyField` if you want to query a standard beacon. For example, you could perform the following query.

```
keyField = {{branch-key-id}} AND standardBeacon = S_standardBeaconValue
```

---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure.html
---

# Configuring the AWS Database Encryption SDK
<a name="configure"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK is designed to be easy to use. Although the AWS Database Encryption SDK has several configuration options, the default values are carefully chosen to be practical and secure for most applications. However, you might need to adjust your configuration to improve performance or include a custom feature in your design.

**Topics**
+ [Selecting a programming language](#config-language)
+ [Selecting wrapping keys](#config-keys)
+ [Creating a discovery filter](#config-discovery)
+ [Working with multitenant databases](#config-multitenant-databases)
+ [Creating signed beacons](#signed-beacons)

## Selecting a programming language
<a name="config-language"></a>

The AWS Database Encryption SDK for DynamoDB is available in multiple [programming languages](ddb-programming-languages.md). The language implementations are designed to be fully interoperable and to offer the same features, although they might be implemented in different ways. Typically, you use the library that is compatible with your application.

## Selecting wrapping keys
<a name="config-keys"></a>

The AWS Database Encryption SDK generates a unique symmetric data key to encrypt each field. You don't need to configure, manage, or use the data keys. The AWS Database Encryption SDK does it for you.

However, you must select one or more wrapping keys to encrypt each data key. The AWS Database Encryption SDK supports [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS) symmetric encryption KMS keys and asymmetric RSA KMS keys. It also supports AES symmetric keys and RSA asymmetric keys that you provide in different sizes. You are responsible for the safety and durability of your wrapping keys, so we recommend that you use an encryption key in a hardware security module or a key infrastructure service, such as AWS KMS.

To specify your wrapping keys for encryption and decryption, you use a [keyring](concepts.md#keyring-concept). Depending on the [type of keyring](keyrings.md) you use, you can specify one wrapping key or multiple wrapping keys of the same or different types. If you use multiple wrapping keys to wrap a data key, each wrapping key will encrypt a copy of the same data key. The encrypted data keys (one per wrapping key) are stored in the [material description](concepts.md#material-description) stored alongside the encrypted field. To decrypt the data, the AWS Database Encryption SDK must first use one of your wrapping keys to decrypt an encrypted data key.

We recommend using one of the AWS KMS keyrings whenever possible. The AWS Database Encryption SDK provides the [AWS KMS keyring](use-kms-keyring.md) and the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), which reduces the number of calls made to AWS KMS. To specify an AWS KMS key in a keyring, use a supported AWS KMS key identifier. If you use the AWS KMS Hierarchical keyring, you must specify the key ARN. For details about the key identifiers for an AWS KMS key, see [Key Identifiers](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.
+ When you encrypt with an AWS KMS keyring, you can specify any valid key identifier (key ARN, alias name, alias ARN, or key ID) for a symmetric encryption KMS key. If you use an asymmetric RSA KMS key, you must specify the key ARN.

  If you specify an alias name or alias ARN for a KMS key when encrypting, the AWS Database Encryption SDK saves the key ARN currently associated with that alias; it does not save the alias. Changes to the alias don't affect the KMS key used to decrypt your data keys.
+ By default, the AWS KMS keyring decrypts records in strict mode (where you specify particular KMS keys). You must use a key ARN to identify AWS KMS keys for decryption.

  When you encrypt with an AWS KMS keyring, the AWS Database Encryption SDK stores the key ARN of the AWS KMS key in the material description with the encrypted data key. When decrypting in strict mode, the AWS Database Encryption SDK verifies that the same key ARN appears in the keyring before it attempts to use the wrapping key to decrypt the encrypted data key. If you use a different key identifier, the AWS Database Encryption SDK will not recognize or use the AWS KMS key, even if the identifiers refer to the same key.
+ When decrypting in [discovery mode](#config-discovery), you don't specify any wrapping keys. First, the AWS Database Encryption SDK attempts to decrypt the record with the key ARN stored in the material description. If that doesn't work, the AWS Database Encryption SDK asks AWS KMS to decrypt the record using the KMS key that encrypted it, regardless of who owns or has access to that KMS key.

To specify a [raw AES key](use-raw-aes-keyring.md) or a [raw RSA key pair](use-raw-rsa-keyring.md) as a wrapping key in a keyring, you must specify a namespace and a name. When decrypting, you must use the exact same namespace and name for each raw wrapping key as you used when encrypting. If you use a different namespace or name, the AWS Database Encryption SDK will not recognize or use the wrapping key, even if the key material is the same.

## Creating a discovery filter
<a name="config-discovery"></a>

When decrypting data encrypted with KMS keys, it's a best practice to decrypt in *strict mode*, that is, to limit the wrapping keys used to only those that you specify. However, if necessary, you can also decrypt in *discovery mode*, where you don't specify any wrapping keys. In this mode, AWS KMS can decrypt the encrypted data key using the KMS key that encrypted it, regardless of who owns or has access to that KMS key.

If you must decrypt in discovery mode, we recommend that you always use a *discovery filter*, which limits the KMS keys that can be used to those in a specified AWS account and [partition](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). The discovery filter is optional, but it's a best practice.

Use the following table to determine the partition value for your discovery filter.

| Region | Partition |
| --- | --- |
| AWS Regions | aws |
| China Regions | aws-cn |
| AWS GovCloud (US) Regions | aws-us-gov |

The following example shows how to create a discovery filter. Before using the code, replace the example values with valid values for your AWS account and partition.

------
#### [ Java ]

```
// Create the discovery filter
DiscoveryFilter discoveryFilter = DiscoveryFilter.builder()
        .partition("{{aws}}")
        .accountIds({{111122223333}})
        .build();
```

------
#### [ C\# / .NET ]

```
var discoveryFilter = new DiscoveryFilter
{
    Partition = "{{aws}}",
    AccountIds = {{111122223333}}
};
```

------
#### [ Rust ]

```
// Create discovery filter
let discovery_filter = DiscoveryFilter::builder()
    .partition("{{aws}}")
    .account_ids({{111122223333}})
    .build()?;
```

------

## Working with multitenant databases
<a name="config-multitenant-databases"></a>

With the AWS Database Encryption SDK, you can configure client-side encryption for databases with a shared schema by isolating each tenant with distinct encryption materials. When considering a multitenant database, take some time to review your security requirements and how multitenancy might impact them. For example, using a multitenant database might impact your ability to combine the AWS Database Encryption SDK with another server-side encryption solution.

If you have multiple users performing encrypt operations within your database, you can use one of the AWS KMS keyrings to provide each user with a distinct key to use in their cryptographic operations. Managing the data keys for a multitenant client-side encryption solution can be complicated. We recommend organizing your data by tenant whenever possible. If the tenant is identified by the primary key values (for example, the partition key in an Amazon DynamoDB table), then managing your keys is easier.

You can use the [AWS KMS keyring](use-kms-keyring.md) to isolate each tenant with a distinct AWS KMS keyring and AWS KMS keys. Based on the volume of AWS KMS calls made per tenant, you might want to use the AWS KMS Hierarchical keyring to minimize your calls to AWS KMS. The [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) is a cryptographic materials caching solution that reduces the number of AWS KMS calls by using AWS KMS protected *branch keys* persisted in an Amazon DynamoDB table, and then locally caching branch key materials used in encrypt and decrypt operations. You must use the AWS KMS Hierarchical keyring to implement [searchable encryption](searchable-encryption.md) in your database.

## Creating signed beacons
<a name="signed-beacons"></a>

The AWS Database Encryption SDK uses [standard beacons](beacons.md#standard-beacon-overview) and [compound beacons](beacons.md#compound-beacon-overview) to provide [searchable encryption](searchable-encryption.md) solutions that enable you to search encrypted records without decrypting the entire database queried. However, the AWS Database Encryption SDK also supports *signed beacons* that can be configured entirely from plaintext signed fields. Signed beacons are a type of compound beacon that index and perform complex queries on `SIGN_ONLY` and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields.

For example, if you have a multitenant database, you might want to create a signed beacon that enables you to query your database for records encrypted by a specific tenant's key. For more information, see [Querying beacons in a multitenant database](searchable-encryption-multitenant.md#query-multitenant-beacons).

You must use the AWS KMS Hierarchical keyring to create signed beacons.

To configure a signed beacon, provide the following values.

------
#### [ Java ]

**Compound beacon configuration**

The following example defines the signed parts lists locally within the signed beacon configuration.

```
List<CompoundBeacon> compoundBeaconList = new ArrayList<>();
CompoundBeacon exampleCompoundBeacon = CompoundBeacon.builder()
    .name("{{compoundBeaconName}}")
    .split("{{.}}")
    .signed(signedPartList)
    .constructors(constructorList)
    .build();
compoundBeaconList.add(exampleCompoundBeacon);
```

**Beacon version definition**

The following example defines the signed parts lists globally in the beacon version. For more information on defining the beacon version, see [Using beacons](using-beacons.md).

```
 List<BeaconVersion> beaconVersions = new ArrayList<>();
beaconVersions.add(
    BeaconVersion.builder()
        .standardBeacons(standardBeaconList)
        .compoundBeacons(compoundBeaconList)
        .signedParts(signedPartList)
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

**See the complete code sample**: [BeaconConfig.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/searchableencryption/complexexample/BeaconConfig.cs)

**Signed beacon configuration**

The following example defines the signed parts lists locally within the signed beacon configuration.

```
var compoundBeaconList = new List<CompoundBeacon>();
var exampleCompoundBeacon = new CompoundBeacon
 {
    Name = "{{compoundBeaconName}}",
    Split = "{{.}}",
    Signed = signedPartList,
    Constructors = constructorList
 };
compoundBeaconList.Add(exampleCompoundBeacon);
```

**Beacon version definition**

The following example defines the signed parts lists globally in the beacon version. For more information on defining the beacon version, see [Using beacons](using-beacons.md).

```
var beaconVersions = new List<BeaconVersion>
{
    new BeaconVersion
    {
        StandardBeacons = standardBeaconList,
        CompoundBeacons = compoundBeaconList,
        SignedParts = signedPartsList,
        Version = 1, // MUST be 1
        KeyStore = keyStore,
        KeySource = new BeaconKeySource
        {
            Single = new SingleKeyStore
            {
                KeyId = branchKeyId,
                CacheTTL = 6000
            }
        }
    }
};
```

------

You can define your signed parts in locally or globally defined lists. We recommend defining your signed parts in a global list in the [beacon version](using-beacons.md#beacon-version) whenever possible. By defining signed parts globally, you can define each part once and then reuse the parts in multiple compound beacon configurations. If you only intend to use a signed part once, you can define it in a local list in the signed beacon configuration. You can reference both local and global parts in your [constructor list](configure-beacons.md#constructor-parts).

If you define your signed parts lists globally, you must provide a list of constructor parts that identify all of the possible ways the signed beacon can assemble the fields in your beacon configuration.

**Note**
To define signed parts lists globally, you must use version 3.2 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before defining any new parts globally.
You cannot update existing beacon configurations to define signed parts lists globally.

**Beacon name**
The name you use when querying the beacon.
A signed beacon name cannot be the same name as an unencrypted field. No two beacons can have the same beacon name.

**Split character**
The character used to separate the parts that make up your signed beacon.
The split character cannot appear in the plaintext values of any of the fields that the signed beacon is constructed from.

**Signed parts list**
Identifies the signed fields included in the signed beacon.
Each part must include a name, source, and prefix. The source is the `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` field that the part identifies. The source must be a field name or an index referring to the value of a nested field. If your part name identifies the source, you can omit the source and the AWS Database Encryption SDK will automatically use the name as its source. We recommend specifying the source as the part name whenever possible. The prefix can be any string, but it must be unique. No two signed parts in a signed beacon can have the same prefix. We recommend using a short value that distinguishes the part from other parts served by the compound beacon.
We recommend defining your signed parts globally whenever possible. You might consider defining a signed part locally if you only intend on using it in one compound beacon. A locally defined part cannot have the same prefix or name as a globally defined part.

```
List<SignedPart> signedPartList = new ArrayList<>();
    SignedPart signedPartExample = SignedPart.builder()
        .name("{{signedFieldName}}")
        .prefix("{{S}}-")
        .build();
    signedPartList.add(signedPartExample);
```

```
var signedPartsList = new List<SignedPart>
{
    new SignedPart { Name = "{{signedFieldName1}}", Prefix = "S-" },
    new SignedPart { Name = "{{signedFieldName2}}", Prefix = "SF-" }
};
```

**Constructor list (Optional)**
Identifies the *constructors* that define the different ways that the signed parts can be assembled by the signed beacon.
If you do not specify a constructor list, the AWS Database Encryption SDK assembles the signed beacon with the following default constructor.
+ All signed parts in the order they were added to the signed parts list
+ All parts are required
**Constructors**
Each constructor is an ordered list of *constructor parts* that defines one way that the signed beacon can be assembled. The constructor parts are joined together in the order they are added to the list, with each part separated by the specified split character.
Each constructor part names a signed part, and defines whether that part is required or optional within the constructor. For example, if you want to query a signed beacon on `Field1`, `Field1.Field2`, and `Field1.Field2.Field3`, mark `Field2` and `Field3` as optional and create one constructor.
Each constructor must have at least one required part. We recommend making the first part in each constructor required so that you can use the `BEGINS_WITH` operator in your queries.
A constructor succeeds if all its required parts are present in the record. When you write a new record, the signed beacon uses the constructor list to determine if the beacon can be assembled from the values provided. It attempts to assemble the beacon in the order that the constructors were added to the constructor list, and it uses the first constructor that succeeds. If no constructors succeed, the beacon is not written to the record.
All readers and writers should specify the same order of constructors to ensure that their query results are correct.
Use the following procedures to specify your own constructor list.

1. Create a constructor part for each signed part to define whether or not that part is required.

   The constructor part name must be the name of the signed field.

   The following example demonstrates how to create constructor part for one signed field.

------
#### [ Java ]

   ```
   ConstructorPart field1ConstructorPart = ConstructorPart.builder()
           .name("{{Field1}}")
           .required({{true}})
           .build();
   ```

------
#### [ C\# / .NET ]

   ```
   var field1ConstructorPart = new ConstructorPart { Name = "{{Field1}}", Required = {{true}} };
   ```

------

1. Create a constructor for each possible way that the signed beacon can be assembled using the constructor parts you created in **Step 1**.

   For example, if you want to query on `Field1.Field2.Field3` and `Field4.Field2.Field3`, then you must create two constructors. `Field1` and `Field4` can both be required because they are defined in two separate constructors.

------
#### [ Java ]

   ```
   // Create a list for Field1.Field2.Field3 queries
   List<ConstructorPart> field123ConstructorPartList = new ArrayList<>();
   field123ConstructorPartList.add(field1ConstructorPart);
   field123ConstructorPartList.add(field2ConstructorPart);
   field123ConstructorPartList.add(field3ConstructorPart);
   Constructor field123Constructor = Constructor.builder()
           .parts(field123ConstructorPartList)
           .build();
   // Create a list for Field4.Field2.Field1 queries
   List<ConstructorPart> field421ConstructorPartList = new ArrayList<>();
   field421ConstructorPartList.add(field4ConstructorPart);
   field421ConstructorPartList.add(field2ConstructorPart);
   field421ConstructorPartList.add(field1ConstructorPart);
   Constructor field421Constructor = Constructor.builder()
           .parts(field421ConstructorPartList)
           .build();
   ```

------
#### [ C\# / .NET ]

   ```
   // Create a list for Field1.Field2.Field3 queries
    var field123ConstructorPartList = new Constructor
   {
       Parts = new List<ConstructorPart> { field1ConstructorPart, field2ConstructorPart, field3ConstructorPart }
   };
   // Create a list for Field4.Field2.Field1 queries
   var field421ConstructorPartList = new Constructor
   {
       Parts = new List<ConstructorPart> { field4ConstructorPart, field2ConstructorPart, field1ConstructorPart }
   };
   ```

------

1. Create a constructor list that includes all of the constructors that you created in **Step 2**.

------
#### [ Java ]

   ```
   List<Constructor> constructorList = new ArrayList<>();
   constructorList.add(field123Constructor);
   constructorList.add(field421Constructor);
   ```

------
#### [ C\# / .NET ]

   ```
   var constructorList = new List<Constructor>
   {
       field123Constructor,
       field421Constructor
   };
   ```

------

1. Specify the `constructorList` when you create your signed beacon.

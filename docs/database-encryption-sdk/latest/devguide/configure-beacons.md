---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure-beacons.html
---

# Configuring beacons
<a name="configure-beacons"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

There are two types of beacons that support searchable encryption. Standard beacons perform equality searches. They are the simplest way to implement searchable encryption in your database. Compound beacons combine literal plaintext strings and standard beacons to perform more complex queries.

Beacons are designed to be implemented in new, unpopulated databases. Any beacon configured in an existing database will only map new records written to the database. Beacons are calculated from the plaintext value of a field, once the field is encrypted there is no way for the beacon to map existing data. After you have written new records with a beacon, you cannot update the beacon's configuration. However, you can add new beacons for new fields that you add to your record.

After determining your access patterns, configuring beacons should be the second step in your database implementation. Then, after you configure all of your beacons, you need to create an [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), define the beacon version, [configure a secondary index for each beacon](ddb-searchable-encryption.md#ddb-beacon-indexes), define your [cryptographic actions](concepts.md#crypt-actions), and configure your database and AWS Database Encryption SDK client. For more information, see [Using beacons](using-beacons.md).

To make it easier to define the beacon version, we recommend creating lists for standard and compound beacons. Add each beacon you create to the respective standard or compound beacon list as you configure them.

**Topics**
+ [Configuring standard beacons](#config-standard-beacons)
+ [Configuring Beacon Partitioning](configuring-beacon-partitioning.md)
+ [Configuring compound beacons](#config-compound-beacons)
+ [Example configurations](beacon-config-examples.md)
+ [Changing configuration and associated risks](changing-configuration-and-risks.md)

## Configuring standard beacons
<a name="config-standard-beacons"></a>

[Standard beacons](beacons.md#standard-beacon-overview) are the simplest way to implement searchable encryption in your database. They can only perform equality searches for a single encrypted or virtual field.

### Example configuration syntax
<a name="standard-config-syntax"></a>

------
#### [ Java ]

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beaconName}}")
    .length(beaconLengthInBits)
    .numberOfPartitions(2)
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

------
#### [ C\# / .NET ]

```
var standardBeaconList = new List<StandardBeacon>();
StandardBeacon exampleStandardBeacon = new StandardBeacon
  {
    Name = "{{beaconName}}",
    Length = 10,
    NumberOfPartitions = 2
  };
standardBeaconList.Add(exampleStandardBeacon);
```

------
#### [ Rust ]

```
let standard_beacon_list = vec![
    StandardBeacon::builder().name("{{beacon_name}}").length({{beacon_length_in_bits}}).number_of_partitions(2).build()?,
```

------

To configure a standard beacon, provide the following values.

**Beacon name**
The name you use when querying an encrypted field.
A beacon name can be the same name as an encrypted field or virtual field, but it cannot be the same name as an unencrypted field. We strongly recommend using the name of the encrypted field or [virtual field](beacons.md#virtual-field) that your standard beacon is constructed from whenever possible. Two different beacons cannot have the same beacon name. For help determining the best beacon name for your implementation, see [Choosing a beacon name](choosing-beacon-name.md).

**Beacon length**
The number of bits of the beacon hash value that are kept after truncation.
The beacon length determines the average number of false positives produced by a given beacon. For more information and help determining the appropriate beacon length for your implementation, see [Determining beacon length](choosing-beacon-length.md).

**Beacon source (Optional)**
The field that a standard beacon is constructed from.
The beacon source must be a field name or an index referring to the value of a nested field. When your beacon name is the same as the beacon source, you can omit the the beacon source from your configuration and the AWS Database Encryption SDK will automatically use the beacon name as the beacon source.

### Creating a virtual field
<a name="create-virtual-field"></a>

To create a [virtual field](beacons.md#virtual-field), you must provide a name for the virtual field and a list of the source fields. The order that you add source fields to the virtual part list determines the order that they are concatenated to build the virtual field. The following example concatenates two source fields in their entirety to create a virtual field.

**Note**
We recommend verifying that your virtual fields produce the expected outcome before you populate your database. For more information, see [Testing beacon outputs](ddb-searchable-encryption.md#ddb-beacon-testing).

------
#### [ Java ]

**See the complete code example**: [VirtualBeaconSearchableEncryptionExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/searchableencryption/VirtualBeaconSearchableEncryptionExample.java)

```
List<VirtualPart> virtualPartList = new ArrayList<>();
    virtualPartList.add({{sourceField1}});
    virtualPartList.add({{sourceField2}});

VirtualField {{virtualFieldName}} = VirtualField.builder()
    .name("{{virtualFieldName}}")
    .parts(virtualPartList)
    .build();

List<VirtualField> virtualFieldList = new ArrayList<>();
    virtualFieldList.add({{virtualFieldName}});
```

------
#### [ C\# / .NET ]

**See the complete code example**: [VirtualBeaconSearchableEncryptionExample.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/searchableencryption/VirtualBeaconSearchableEncryptionExample.cs)

```
var virtualPartList = new List<VirtualPart> { {{sourceField1}}, {{sourceField2}} };

var {{virtualFieldName}} = new VirtualField
{
    Name = "{{virtualFieldName}}",
    Parts = virtualPartList
};

var virtualFieldList = new List<VirtualField> { {{virtualFieldName}} };
```

------
#### [ Rust ]

**See the complete code example**: [virtual\_beacon\_searchable\_encryption.rs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/searchableencryption/virtual_beacon_searchable_encryption.rs)

```
let virtual_part_list = vec![{{source_field_one}}, {{source_field_two}}];

let state_and_has_test_result_field = VirtualField::builder()
    .name("{{virtual_field_name}}")
    .parts(virtual_part_list)
    .build()?;

let virtual_field_list = vec![{{virtual_field_name}}];
```

------

To create a virtual field with a specific segment of a source field, you must define that transformation before adding the source field to your virtual part list.

#### Security considerations for virtual fields
<a name="virtual-field-considerations"></a>

Beacons do not alter the encrypted state of the field. However, when you use beacons, there is an inherent tradeoff between how efficient your queries are and how much information is revealed about the distribution of your data. The way that you configure your beacon determines the level of security that is preserved by that beacon.

Avoid creating a virtual field with source fields that overlap with existing standard beacons. Creating virtual fields that include a source field that has already been used to create a standard beacon can reduce the level of security for both beacons. The extent that security is reduced is dependent on the level of entropy added by the additional source fields. The level of entropy is determined by the distribution of unique values in the additional source field and the number of bits that the additional source field contributes to the overall size of the virtual field.

You can use population and [beacon length](choosing-beacon-length.md) to determine if the source fields for a virtual field preserve the security of your dataset. The population is the expected number of unique values in a field. Your population does not need to be precise. For help estimating the population of a field, see [Estimate the population](choosing-beacon-length.md#estimate-population).

Consider the following example as you review the security of your virtual fields.
+ Beacon1 is constructed from `FieldA`. `FieldA` has a population greater than **2(Beacon1 length)**.
+ Beacon2 is constructed from `VirtualField`, which is constructed from `FieldA`, `FieldB`, `FieldC`, and `FieldD`. Together, `FieldB`, `FieldC`, and `FieldD` have a population greater than **2N**

Beacon2 preserves the security of both Beacon1 and Beacon2 if the following statements are true:

```
N ≥ (Beacon1 length)/2
```

and

```
N ≥ (Beacon2 length)/2
```

### Defining beacon styles
<a name="define-beacon-styles"></a>

Standard beacons can be used to perform equality searches for an encrypted or virtual field. Or, they can be used to construct compound beacons to perform more complex database operations. To help you organize and manage standard beacons, the AWS Database Encryption SDK provides the following optional *beacon styles* that define the intended use of a standard beacon.

**Note**
To define beacon styles, you must use version 3.2 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before adding beacon styles to your beacon configurations.

------
#### [ PartOnly ]

A standard beacon defined as `PartOnly` can only be used to define an [encrypted part](#encrypted-parts) of a compound beacon. You cannot directly query a `PartOnly` standard beacon.

**Java**

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beaconName}}")
    .length(beaconLengthInBits)
    .style(
        BeaconStyle.builder()
           .partOnly(PartOnly.builder().build())
        .build()
    )
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

**C\# / .NET**

```
new StandardBeacon
{
    Name = "{{beaconName}}",
    Length = beaconLengthInBits,
    Style = new BeaconStyle
    {
        PartOnly = new PartOnly()
    }
}
```

**Rust**

```
StandardBeacon::builder()
    .name("{{beacon_name}}")
    .length({{beacon_length_in_bits}})
    .style(BeaconStyle::PartOnly(PartOnly::builder().build()?))
    .build()?
```

------
#### [ Shared ]

By default, every standard beacon generates a unique HMAC key for beacon calculation. As a result, you cannot perform an equality search on the encrypted fields from two separate standard beacons. A standard beacon defined as `Shared` uses the HMAC key from another standard beacon for its calculations.

For example, if you need to compare `beacon1` fields to `beacon2` fields, define `beacon2` as a `Shared` beacon that uses the HMAC key from `beacon1` for its calculations.

**Note**
Consider your security and performance needs before configuring any `Shared` beacons. `Shared` beacons might increase the amount of statistical information that can be identified about the distribution of your dataset. For example, they might reveal which shared fields contain the same plaintext value.

**Java**

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beacon2}}")
    .length(beaconLengthInBits)
    .style(
        BeaconStyle.builder()
           .shared(Shared.builder().other("{{beacon1}}").build())
        .build()
    )
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

**C\# / .NET**

```
new StandardBeacon
{
    Name = "{{beacon2}}",
    Length = beaconLengthInBits,
    Style = new BeaconStyle
    {
        Shared = new Shared { Other = "{{beacon1}}" }
    }
}
```

**Rust**

```
StandardBeacon::builder()
    .name("{{beacon2}}")
    .length({{beacon_length_in_bits}})
    .style(BeaconStyle::Shared(
       Shared::builder().other("{{beacon1}}").build()?,
    ))
    .build()?
```

------
#### [ AsSet ]

By default, if a field value is a set, the AWS Database Encryption SDK calculates a single standard beacon for the set. As a result, you cannot perform the query `CONTAINS({{a}}, :{{value}})` where `{{a}}` is an encrypted field. A standard beacon defined as `AsSet` calculates individual standard beacon values for each individual element of the set and stores the beacon value in the item as a set. This enables the AWS Database Encryption SDK to perform the query `CONTAINS({{a}}, :{{value}})`.

To define an `AsSet` standard beacon, the elements in the set must be from the same population so that they can all use the same [beacon length](choosing-beacon-length.md). The beacon set might have fewer elements than the plaintext set if there were collisions when calculating the beacon values.

**Note**
Consider your security and performance needs before configuring any `AsSet` beacons. `AsSet` beacons might increase the amount of statistical information that can be identified about the distribution of your dataset. For example, they might reveal the size of the plaintext set.

**Java**

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beaconName}}")
    .length(beaconLengthInBits)
    .style(
        BeaconStyle.builder()
           .asSet(AsSet.builder().build())
        .build()
    )
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

**C\# / .NET**

```
new StandardBeacon
{
    Name = "{{beaconName}}",
    Length = beaconLengthInBits,
    Style = new BeaconStyle
    {
        AsSet = new AsSet()
    }
}
```

**Rust**

```
StandardBeacon::builder()
    .name("{{beacon_name}}")
    .length({{beacon_length_in_bits}})
    .style(BeaconStyle::AsSet(AsSet::builder().build()?))
    .build()?
```

------
#### [ SharedSet ]

A standard beacon defined as `SharedSet` combines the `Shared` and `AsSet` functions so that you can perform equality searches on the encrypted values of a set and field. This enables the AWS Database Encryption SDK to perform the query `CONTAINS({{a}}, {{b}})` where `{{a}}` is an encrypted set and `{{b}}` is an encrypted field.

**Note**
Consider your security and performance needs before configuring any `Shared` beacons. `SharedSet` beacons might increase the amount of statistical information that can be identified about the distribution of your dataset. For example, they might reveal the size of the plaintext set or which shared fields contain the same plaintext value.

**Java**

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{beacon2}}")
    .length(beaconLengthInBits)
    .style(
        BeaconStyle.builder()
           .sharedSet(SharedSet.builder().other("{{beacon1}}").build())
        .build()
    )
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

**C\# / .NET**

```
new StandardBeacon
{
    Name = "{{beacon2}}",
    Length = beaconLengthInBits,
    Style = new BeaconStyle
    {
        SharedSet = new SharedSet { Other = "{{beacon1}}" }
    }
}
```

**Rust**

```
StandardBeacon::builder()
    .name("{{beacon2}}")
    .length({{beacon_length_in_bits}})
    .style(BeaconStyle::SharedSet(
        SharedSet::builder().other("{{beacon1}}").build()?,
    ))
    .build()?
```

------

## Configuring compound beacons
<a name="config-compound-beacons"></a>

Compound beacons combine literal plaintext strings and standard beacons to perform complex database operations, such as querying two different record types from a single index or querying a combination of fields with a sort key. Compound beacons can be constructed from `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` fields. You must create a standard beacon for every encrypted field included in the compound beacon.

**Note**
We recommend verifying that your compound beacons produce the expected outcome before you populate your database. For more information, see [Testing beacon outputs](ddb-searchable-encryption.md#ddb-beacon-testing).

### Example configuration syntax
<a name="compound-config-syntax"></a>

------
#### [ Java ]

**Compound beacon configuration**

The following example defines encrypted and signed parts lists locally within the compound beacon configuration.

```
List<CompoundBeacon> compoundBeaconList = new ArrayList<>();
CompoundBeacon exampleCompoundBeacon = CompoundBeacon.builder()
    .name("{{compoundBeaconName}}")
    .split("{{.}}")
    .encrypted(encryptedPartList)
    .signed(signedPartList)
    .constructors(constructorList)
    .build();
compoundBeaconList.add(exampleCompoundBeacon);
```

**Beacon version definition**

The following example defines encrypted and signed parts lists globally in the beacon version. For more information on defining the beacon version, see [Using beacons](using-beacons.md).

```
 List<BeaconVersion> beaconVersions = new ArrayList<>();
beaconVersions.add(
    BeaconVersion.builder()
        .standardBeacons(standardBeaconList)
        .compoundBeacons(compoundBeaconList)
        .encryptedParts(encryptedPartList)
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

**Compound beacon configuration**

The following example defines encrypted and signed parts lists locally within the compound beacon configuration.

```
var compoundBeaconList = new List<CompoundBeacon>();
var exampleCompoundBeacon = new CompoundBeacon
 {
    Name = "{{compoundBeaconName}}",
    Split = "{{.}}",
    Encrypted = encryptedPartList,
    Signed = signedPartList,
    Constructors = constructorList
 };
compoundBeaconList.Add(exampleCompoundBeacon);
```

**Beacon version definition**

The following example defines encrypted and signed parts lists globally in the beacon version. For more information on defining the beacon version, see [Using beacons](using-beacons.md).

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
#### [ Rust ]

**See the complete code sample**: [beacon\_config.rs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/searchableencryption/complexexample/beacon_config.rs)

**Compound beacon configuration**

The following example defines encrypted and signed parts lists locally within the compound beacon configuration.

```
let compound_beacon_list = vec![
    CompoundBeacon::builder()
        .name("{{compound_beacon_name}}")
        .split("{{.}}")
        .encrypted(encrypted_parts_list)
        .signed(signed_parts_list)
        .constructors(constructor_list)
        .build()?
```

**Beacon version definition**

The following example defines encrypted and signed parts lists globally in the beacon version. For more information on defining the beacon version, see [Using beacons](using-beacons.md).

```
let beacon_versions = BeaconVersion::builder()
    .standard_beacons(standard_beacon_list)
    .compound_beacons(compound_beacon_list)
    .encrypted_parts(encrypted_parts_list)
    .signed_parts(signed_parts_list)
    .version(1) // MUST be 1
    .key_store(key_store.clone())
    .key_source(BeaconKeySource::Single(
        SingleKeyStore::builder()
            .key_id(branch_key_id)
            .cache_ttl(6000)
            .build()?,
    ))
    .build()?;
let beacon_versions = vec![beacon_versions];
```

------

You can define your [encrypted parts](#encrypted-parts) and [signed parts](#signed-parts) in locally or globally defined lists. We recommend defining your encrypted and signed parts in a global list in the [beacon version](using-beacons.md#beacon-version) whenever possible. By defining encrypted and signed parts globally, you can define each part once and then reuse the parts in multiple compound beacon configurations. If you only intend to use an encrypted or signed part once, you can define it in a local list in the compound beacon configuration. You can reference both local and global parts in your [constructor list](#constructor-parts).

If you define your encrypted and signed parts lists globally, you must provide a list of constructor parts that identify all of the possible ways the compound beacon can assemble the fields in your compound beacon configuration.

**Note**
To define encrypted and signed parts lists globally, you must use version 3.2 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before defining any new parts globally.
You cannot update existing beacon configurations to define encrypted and signed parts lists globally.

To configure a compound beacon, provide the following values.

**Beacon name**
The name you use when querying an encrypted field.
A beacon name can be the same name as an encrypted field or virtual field, but it cannot be the same name as an unencrypted field. No two beacons can have the same beacon name. For help determining the best beacon name for your implementation, see [Choosing a beacon name](choosing-beacon-name.md).

**Split character**
The character used to separate the parts that make up your compound beacon.
The split character cannot appear in the plaintext values of any of the fields that the compound beacon is constructed from.

**Encrypted parts list**
Identifies the `ENCRYPT_AND_SIGN` fields included in the compound beacon.
Each part must include a name and prefix. The part name must be the name of the standard beacon constructed from the encrypted field. The prefix can be any string, but it must be unique. An encrypted part cannot have the same prefix as a signed part. We recommend using a short value that distinguishes the part from other parts served by the compound beacon.
We recommend defining your encrypted parts globally whenever possible. You might consider defining an encrypted part locally if you only intend on using it in one compound beacon. A locally defined encrypted part cannot have the same prefix or name as a globally defined encrypted part.

```
List<EncryptedPart> encryptedPartList = new ArrayList<>();
EncryptedPart encryptedPartExample = EncryptedPart.builder()
    .name("{{standardBeaconName}}")
    .prefix("E-")
    .build();
encryptedPartList.add(encryptedPartExample);
```

```
var encryptedPartList = new List<EncryptedPart>();
var encryptedPartExample = new EncryptedPart
 {
    Name = "{{compoundBeaconName}}",
    Prefix = "E-"
 };
encryptedPartList.Add(encryptedPartExample);
```

```
let encrypted_parts_list = vec![
    EncryptedPart::builder()
        .name("{{standard_beacon_name}}")
        .prefix("E-")
        .build()?
];
```

**Signed parts list**
Identifies the signed fields included in the compound beacon.
Signed parts are optional. You can configure a compound beacon that does not reference any signed parts.
Each part must include a name, source, and prefix. The source is the `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` field that the part identifies. The source must be a field name or an index referring to the value of a nested field. If your part name identifies the source, you can omit the source and the AWS Database Encryption SDK will automatically use the name as its source. We recommend specifying the source as the part name whenever possible. The prefix can be any string, but it must be unique. A signed part cannot have the same prefix as an encrypted part. We recommend using a short value that distinguishes the part from other parts served by the compound beacon.
We recommend defining your signed parts globally whenever possible. You might consider defining a signed part locally if you only intend on using it in one compound beacon. A locally defined signed part cannot have the same prefix or name as a globally defined signed part.

```
List<SignedPart> signedPartList = new ArrayList<>();
SignedPart signedPartExample = SignedPart.builder()
    .name("{{signedFieldName}}")
    .prefix("S-")
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

```
let signed_parts_list = vec![
    SignedPart::builder()
        .name("{{signed_field_name_1}}")
        .prefix("S-")
        .build()?,
   SignedPart::builder()
        .name("{{signed_field_name_2}}")
        .prefix("SF-")
        .build()?,
];
```

**Constructor list**
Identifies the *constructors* that define the different ways that the encrypted and signed parts can be assembled by the compound beacon. You can reference both local and global parts in your constructor list.
If you construct your compound beacon from globally defined encrypted and signed parts, you must provide a constructor list.
If you do not use any globally defined encrypted or signed parts to construct your compound beacon, the constructor list is optional. If you do not specify a constructor list, the AWS Database Encryption SDK assembles the compound beacon with the following default constructor.
+ All signed parts in the order they were added to the signed parts list
+ All encrypted parts in the order they were added to the encrypted parts list
+ All parts are required
**Constructors**
Each constructor is an ordered list of *constructor parts* that defines one way that the compound beacon can be assembled. The constructor parts are joined together in the order they are added to the list, with each part separated by the specified split character.
Each constructor part names an encrypted part or a signed part, and defines whether that part is required or optional within the constructor. For example, if you want to query a compound beacon on `Field1`, `Field1.Field2`, and `Field1.Field2.Field3`, mark `Field2` and `Field3` as optional and create one constructor.
Each constructor must have at least one required part. We recommend making the first part in each constructor required so that you can use the `BEGINS_WITH` operator in your queries.
A constructor succeeds if all its required parts are present in the record. When you write a new record, the compound beacon uses the constructor list to determine if the beacon can be assembled from the values provided. It attempts to assemble the beacon in the order that the constructors were added to the constructor list, and it uses the first constructor that succeeds. If no constructors succeed, the beacon is not written to the record.
All readers and writers should specify the same order of constructors to ensure that their query results are correct.
Use the following procedures to specify your own constructor list.

1. Create a constructor part for each encrypted part and signed part to define whether or not that part is required.

   The constructor part name must be the name of the standard beacon or signed field it represents.

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
#### [ Rust ]

   ```
   let field_1_constructor_part = ConstructorPart::builder()
       .name("{{field_1}}")
       .required({{true}})
       .build()?;
   ```

------

1. Create a constructor for each possible way that the compound beacon can be assembled using the constructor parts you created in **Step 1**.

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
#### [ Rust ]

   ```
   // Create a list for field1.field2.field3 queries
   let field1_field2_field3_constructor = Constructor::builder()
       .parts(vec![
           field1_constructor_part,
           field2_constroctor_part.clone(),
           field3_constructor_part,
       ])
       .build()?;

   // Create a list for field4.field2.field1 queries
   let field4_field2_field1_constructor = Constructor::builder()
       .parts(vec![
           field4_constructor_part,
           field2_constroctor_part.clone(),
           field1_constructor_part,
       ])
       .build()?;
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
#### [ Rust ]

   ```
   let constructor_list = vec![
       field1_field2_field3_constructor,
       field4_field2_field1_constructor,
   ];
   ```

------

1. Specify the `constructorList` when you create your compound beacon.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

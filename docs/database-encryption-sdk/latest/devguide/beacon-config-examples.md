---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/beacon-config-examples.html
---

# Example configurations
<a name="beacon-config-examples"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The following examples demonstrate how to configure standard and compound beacons. The following configurations do not provide beacon lengths. For help determining the appropriate beacon length for your configuration, see [Choose a beacon length](choosing-beacon-length.md).

To see complete code examples that demonstrate how to configure and use beacons, see the [Java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/searchableencryption), [.NET](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/searchableencryption/), and [Rust](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/searchableencryption/) searchable encryption examples in the aws-database-encryption-sdk-dynamodb repository on GitHub.

**Topics**
+ [Standard beacons](#standard-config-examples)
+ [Compound beacons](#compound-config-examples)

## Standard beacons
<a name="standard-config-examples"></a>

If you want to query the `inspector_id_last4` field for exact matches, create a standard beacon using the following configuration.

------
#### [ Java ]

```
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon exampleStandardBeacon = StandardBeacon.builder()
    .name("{{inspector_id_last4}}")
    .length(beaconLengthInBits)
    .numberOfPartitions({{2}})
    .build();
standardBeaconList.add(exampleStandardBeacon);
```

------
#### [ C\# / .NET ]

```
var standardBeaconList = new List<StandardBeacon>();
StandardBeacon exampleStandardBeacon = new StandardBeacon
  {
    Name = "{{inspector_id_last4}}",
    Length = 10,
    NumberOfPartitions = {{2}}
  };
standardBeaconList.Add(exampleStandardBeacon);
```

------
#### [ Rust ]

```
let last4_beacon = StandardBeacon::builder()
    .name("{{inspector_id_last4}}")
    .length(10)
    .number_of_partitions({{2}})
    .build()?;

let unit_beacon = StandardBeacon::builder().name("{{unit}}").length(30).build()?;

let standard_beacon_list = vec![last4_beacon, unit_beacon];
```

------

## Compound beacons
<a name="compound-config-examples"></a>

If you want to query the `UnitInspection` database on `inspector_id_last4` and `inspector_id_last4.unit`, create a compound beacon with the following configuration. This compound beacon only requires [encrypted parts](configure-beacons.md#encrypted-parts).

------
#### [ Java ]

```
// 1. Create standard beacons for the inspector_id_last4 and unit fields.
List<StandardBeacon> standardBeaconList = new ArrayList<>();
StandardBeacon inspectorBeacon = StandardBeacon.builder()
    .name("{{inspector_id_last4}}")
    .length(beaconLengthInBits)
    .build();
standardBeaconList.add(inspectorBeacon);

StandardBeacon unitBeacon = StandardBeacon.builder()
    .name("{{unit}}")
    .length(beaconLengthInBits)
    .build();
standardBeaconList.add(unitBeacon);

// 2. Define the encrypted parts.
List<EncryptedPart> encryptedPartList = new ArrayList<>();

// Each encrypted part needs a name and prefix
// The name must be the name of the standard beacon
// The prefix must be unique
// For this example we use the prefix "I-" for "inspector_id_last4"
// and "U-" for "unit"
EncryptedPart encryptedPartInspector = EncryptedPart.builder()
    .name("{{inspector_id_last4}}")
    .prefix("I-")
    .build();
encryptedPartList.add(encryptedPartInspector);

EncryptedPart encryptedPartUnit = EncryptedPart.builder()
    .name("{{unit}}")
    .prefix("U-")
    .build();
encryptedPartList.add(encryptedPartUnit);

// 3. Create the compound beacon.
// This compound beacon only requires a name, split character,
// and list of encrypted parts
CompoundBeacon inspectorUnitBeacon = CompoundBeacon.builder()
    .name("{{inspectorUnitBeacon}}")
    .split(".")
    .sensitive(encryptedPartList)
    .build();
```

------
#### [ C\# / .NET ]

```
// 1. Create standard beacons for the inspector_id_last4 and unit fields.
StandardBeacon inspectorBeacon = new StandardBeacon
 {
   Name = "{{inspector_id_last4}}",
   Length = 10
 };
standardBeaconList.Add(inspectorBeacon);
StandardBeacon unitBeacon = new StandardBeacon
 {
    Name = "{{unit}}",
    Length = 30
 };
standardBeaconList.Add(unitBeacon);

// 2. Define the encrypted parts.
var last4EncryptedPart = new EncryptedPart

// Each encrypted part needs a name and prefix
// The name must be the name of the standard beacon
// The prefix must be unique
// For this example we use the prefix "I-" for "inspector_id_last4"
// and "U-" for "unit"
var last4EncryptedPart = new EncryptedPart
 {
   Name = "{{inspector_id_last4}}",
   Prefix = "I-"
 };
encryptedPartList.Add(last4EncryptedPart);

var unitEncryptedPart = new EncryptedPart
 {
   Name = "{{unit}}",
   Prefix = "U-"
 };
encryptedPartList.Add(unitEncryptedPart);

// 3. Create the compound beacon.
// This compound beacon only requires a name, split character,
// and list of encrypted parts
var compoundBeaconList = new List<CompoundBeacon>();
var inspectorCompoundBeacon = new CompoundBeacon
  {
      Name = "{{inspector_id_last4}}",
      Split = ".",
      Encrypted = encryptedPartList
  };
compoundBeaconList.Add(inspectorCompoundBeacon);
```

------
#### [ Rust ]

```
// 1. Create standard beacons for the inspector_id_last4 and unit fields.
let last4_beacon = StandardBeacon::builder()
    .name("inspector_id_last4")
    .length(10)
    .build()?;

let unit_beacon = StandardBeacon::builder().name("unit").length(30).build()?;

let standard_beacon_list = vec![last4_beacon, unit_beacon];

// 2. Define the encrypted parts.
// The name must be the name of the standard beacon
// The prefix must be unique
// For this example we use the prefix "I-" for "inspector_id_last4"
// and "U-" for "unit"
let encrypted_parts_list = vec![
    EncryptedPart::builder()
        .name("inspector_id_last4")
        .prefix("I-")
        .build()?,
    EncryptedPart::builder().name("unit").prefix("U-").build()?,
];

// 3. Create the compound beacon
// This compound beacon only requires a name, split character,
// and list of encrypted parts
let compound_beacon_list = vec![CompoundBeacon::builder()
    .name("last4UnitCompound")
    .split(".")
    .encrypted(encrypted_parts_list)
    .build()?];
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

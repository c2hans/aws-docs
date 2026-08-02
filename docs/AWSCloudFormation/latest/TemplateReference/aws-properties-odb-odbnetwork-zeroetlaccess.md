---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-zeroetlaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork ZeroEtlAccess
<a name="aws-properties-odb-odbnetwork-zeroetlaccess"></a>

The configuration for Zero-ETL access from the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-zeroetlaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-zeroetlaccess-syntax.json"></a>

```
{
  "[Cidr](#cfn-odb-odbnetwork-zeroetlaccess-cidr)" : {{String}},
  "[Status](#cfn-odb-odbnetwork-zeroetlaccess-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-zeroetlaccess-syntax.yaml"></a>

```
  [Cidr](#cfn-odb-odbnetwork-zeroetlaccess-cidr): {{String}}
  [Status](#cfn-odb-odbnetwork-zeroetlaccess-status): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-zeroetlaccess-properties"></a>

`Cidr`  <a name="cfn-odb-odbnetwork-zeroetlaccess-cidr"></a>
The CIDR block for the Zero-ETL access.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-zeroetlaccess-status"></a>
The status of the Zero-ETL access.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

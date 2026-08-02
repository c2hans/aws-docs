---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-kmsaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork KmsAccess
<a name="aws-properties-odb-odbnetwork-kmsaccess"></a>

Configuration for AWS Key Management Service (KMS) access from the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-kmsaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-kmsaccess-syntax.json"></a>

```
{
  "[DomainName](#cfn-odb-odbnetwork-kmsaccess-domainname)" : {{String}},
  "[Ipv4Addresses](#cfn-odb-odbnetwork-kmsaccess-ipv4addresses)" : {{[ String, ... ]}},
  "[KmsPolicyDocument](#cfn-odb-odbnetwork-kmsaccess-kmspolicydocument)" : {{String}},
  "[Status](#cfn-odb-odbnetwork-kmsaccess-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-kmsaccess-syntax.yaml"></a>

```
  [DomainName](#cfn-odb-odbnetwork-kmsaccess-domainname): {{String}}
  [Ipv4Addresses](#cfn-odb-odbnetwork-kmsaccess-ipv4addresses): {{
    - String}}
  [KmsPolicyDocument](#cfn-odb-odbnetwork-kmsaccess-kmspolicydocument): {{String}}
  [Status](#cfn-odb-odbnetwork-kmsaccess-status): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-kmsaccess-properties"></a>

`DomainName`  <a name="cfn-odb-odbnetwork-kmsaccess-domainname"></a>
The domain name for AWS Key Management Service (KMS) access configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Addresses`  <a name="cfn-odb-odbnetwork-kmsaccess-ipv4addresses"></a>
The IPv4 addresses allowed for AWS Key Management Service (KMS) access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsPolicyDocument`  <a name="cfn-odb-odbnetwork-kmsaccess-kmspolicydocument"></a>
The AWS Key Management Service (KMS) policy document that defines permissions for key usage.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-kmsaccess-status"></a>
The current status of the AWS Key Management Service (KMS) access configuration.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

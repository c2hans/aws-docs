---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-s3access.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork S3Access
<a name="aws-properties-odb-odbnetwork-s3access"></a>

The configuration for Amazon S3 access from the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-s3access-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-s3access-syntax.json"></a>

```
{
  "[DomainName](#cfn-odb-odbnetwork-s3access-domainname)" : {{String}},
  "[Ipv4Addresses](#cfn-odb-odbnetwork-s3access-ipv4addresses)" : {{[ String, ... ]}},
  "[S3PolicyDocument](#cfn-odb-odbnetwork-s3access-s3policydocument)" : {{String}},
  "[Status](#cfn-odb-odbnetwork-s3access-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-s3access-syntax.yaml"></a>

```
  [DomainName](#cfn-odb-odbnetwork-s3access-domainname): {{String}}
  [Ipv4Addresses](#cfn-odb-odbnetwork-s3access-ipv4addresses): {{
    - String}}
  [S3PolicyDocument](#cfn-odb-odbnetwork-s3access-s3policydocument): {{String}}
  [Status](#cfn-odb-odbnetwork-s3access-status): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-s3access-properties"></a>

`DomainName`  <a name="cfn-odb-odbnetwork-s3access-domainname"></a>
The domain name for the Amazon S3 access.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Addresses`  <a name="cfn-odb-odbnetwork-s3access-ipv4addresses"></a>
The IPv4 addresses for the Amazon S3 access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3PolicyDocument`  <a name="cfn-odb-odbnetwork-s3access-s3policydocument"></a>
The endpoint policy for the Amazon S3 access.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-s3access-status"></a>
The status of the Amazon S3 access.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

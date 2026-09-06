---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-managedservices.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork ManagedServices
<a name="aws-properties-odb-odbnetwork-managedservices"></a>

The managed services configuration for the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-managedservices-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-managedservices-syntax.json"></a>

```
{
  "[CrossRegionS3RestoreSourcesAccess](#cfn-odb-odbnetwork-managedservices-crossregions3restoresourcesaccess)" : {{[ CrossRegionS3RestoreSourcesAccess, ... ]}},
  "[KmsAccess](#cfn-odb-odbnetwork-managedservices-kmsaccess)" : {{KmsAccess}},
  "[ManagedS3BackupAccess](#cfn-odb-odbnetwork-managedservices-manageds3backupaccess)" : {{ManagedS3BackupAccess}},
  "[ManagedServicesIpv4Cidrs](#cfn-odb-odbnetwork-managedservices-managedservicesipv4cidrs)" : {{[ String, ... ]}},
  "[ResourceGatewayArn](#cfn-odb-odbnetwork-managedservices-resourcegatewayarn)" : {{String}},
  "[S3Access](#cfn-odb-odbnetwork-managedservices-s3access)" : {{S3Access}},
  "[ServiceNetworkArn](#cfn-odb-odbnetwork-managedservices-servicenetworkarn)" : {{String}},
  "[ServiceNetworkEndpoint](#cfn-odb-odbnetwork-managedservices-servicenetworkendpoint)" : {{ServiceNetworkEndpoint}},
  "[StsAccess](#cfn-odb-odbnetwork-managedservices-stsaccess)" : {{StsAccess}},
  "[ZeroEtlAccess](#cfn-odb-odbnetwork-managedservices-zeroetlaccess)" : {{ZeroEtlAccess}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-managedservices-syntax.yaml"></a>

```
  [CrossRegionS3RestoreSourcesAccess](#cfn-odb-odbnetwork-managedservices-crossregions3restoresourcesaccess): {{
    - CrossRegionS3RestoreSourcesAccess}}
  [KmsAccess](#cfn-odb-odbnetwork-managedservices-kmsaccess): {{
    KmsAccess}}
  [ManagedS3BackupAccess](#cfn-odb-odbnetwork-managedservices-manageds3backupaccess): {{
    ManagedS3BackupAccess}}
  [ManagedServicesIpv4Cidrs](#cfn-odb-odbnetwork-managedservices-managedservicesipv4cidrs): {{
    - String}}
  [ResourceGatewayArn](#cfn-odb-odbnetwork-managedservices-resourcegatewayarn): {{String}}
  [S3Access](#cfn-odb-odbnetwork-managedservices-s3access): {{
    S3Access}}
  [ServiceNetworkArn](#cfn-odb-odbnetwork-managedservices-servicenetworkarn): {{String}}
  [ServiceNetworkEndpoint](#cfn-odb-odbnetwork-managedservices-servicenetworkendpoint): {{
    ServiceNetworkEndpoint}}
  [StsAccess](#cfn-odb-odbnetwork-managedservices-stsaccess): {{
    StsAccess}}
  [ZeroEtlAccess](#cfn-odb-odbnetwork-managedservices-zeroetlaccess): {{
    ZeroEtlAccess}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-managedservices-properties"></a>

`CrossRegionS3RestoreSourcesAccess`  <a name="cfn-odb-odbnetwork-managedservices-crossregions3restoresourcesaccess"></a>
The access configuration for the cross-Region Amazon S3 database restore source.
*Required*: No
*Type*: [Array](aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess.md) of [CrossRegionS3RestoreSourcesAccess](aws-properties-odb-odbnetwork-crossregions3restoresourcesaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsAccess`  <a name="cfn-odb-odbnetwork-managedservices-kmsaccess"></a>
The AWS Key Management Service (KMS) access configuration.
*Required*: No
*Type*: [KmsAccess](aws-properties-odb-odbnetwork-kmsaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedS3BackupAccess`  <a name="cfn-odb-odbnetwork-managedservices-manageds3backupaccess"></a>
The managed Amazon S3 backup access configuration.
*Required*: No
*Type*: [ManagedS3BackupAccess](aws-properties-odb-odbnetwork-manageds3backupaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedServicesIpv4Cidrs`  <a name="cfn-odb-odbnetwork-managedservices-managedservicesipv4cidrs"></a>
The IPv4 CIDR blocks for the managed services.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceGatewayArn`  <a name="cfn-odb-odbnetwork-managedservices-resourcegatewayarn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
*Required*: No
*Type*: String
*Pattern*: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Access`  <a name="cfn-odb-odbnetwork-managedservices-s3access"></a>
The Amazon S3 access configuration.
*Required*: No
*Type*: [S3Access](aws-properties-odb-odbnetwork-s3access.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNetworkArn`  <a name="cfn-odb-odbnetwork-managedservices-servicenetworkarn"></a>
The Amazon Resource Name (ARN) of the service network.
*Required*: No
*Type*: String
*Pattern*: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNetworkEndpoint`  <a name="cfn-odb-odbnetwork-managedservices-servicenetworkendpoint"></a>
The service network endpoint configuration.
*Required*: No
*Type*: [ServiceNetworkEndpoint](aws-properties-odb-odbnetwork-servicenetworkendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StsAccess`  <a name="cfn-odb-odbnetwork-managedservices-stsaccess"></a>
The AWS Security Token Service (STS) access configuration.
*Required*: No
*Type*: [StsAccess](aws-properties-odb-odbnetwork-stsaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZeroEtlAccess`  <a name="cfn-odb-odbnetwork-managedservices-zeroetlaccess"></a>
The Zero-ETL access configuration.
*Required*: No
*Type*: [ZeroEtlAccess](aws-properties-odb-odbnetwork-zeroetlaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

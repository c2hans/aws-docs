---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-customdbengineversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::CustomDBEngineVersion
<a name="aws-resource-rds-customdbengineversion"></a>

Creates a custom DB engine version (CEV).

## Syntax
<a name="aws-resource-rds-customdbengineversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-customdbengineversion-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::CustomDBEngineVersion",
  "Properties" : {
      "[DatabaseInstallationFiles](#cfn-rds-customdbengineversion-databaseinstallationfiles)" : {{[ String, ... ]}},
      "[DatabaseInstallationFilesS3BucketName](#cfn-rds-customdbengineversion-databaseinstallationfiless3bucketname)" : {{String}},
      "[DatabaseInstallationFilesS3Prefix](#cfn-rds-customdbengineversion-databaseinstallationfiless3prefix)" : {{String}},
      "[Description](#cfn-rds-customdbengineversion-description)" : {{String}},
      "[Engine](#cfn-rds-customdbengineversion-engine)" : {{String}},
      "[EngineVersion](#cfn-rds-customdbengineversion-engineversion)" : {{String}},
      "[ImageId](#cfn-rds-customdbengineversion-imageid)" : {{String}},
      "[KMSKeyId](#cfn-rds-customdbengineversion-kmskeyid)" : {{String}},
      "[Manifest](#cfn-rds-customdbengineversion-manifest)" : {{String}},
      "[SourceCustomDbEngineVersionIdentifier](#cfn-rds-customdbengineversion-sourcecustomdbengineversionidentifier)" : {{String}},
      "[Status](#cfn-rds-customdbengineversion-status)" : {{String}},
      "[Tags](#cfn-rds-customdbengineversion-tags)" : {{[ Tag, ... ]}},
      "[UseAwsProvidedLatestImage](#cfn-rds-customdbengineversion-useawsprovidedlatestimage)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-rds-customdbengineversion-syntax.yaml"></a>

```
Type: AWS::RDS::CustomDBEngineVersion
Properties:
  [DatabaseInstallationFiles](#cfn-rds-customdbengineversion-databaseinstallationfiles): {{
    - String}}
  [DatabaseInstallationFilesS3BucketName](#cfn-rds-customdbengineversion-databaseinstallationfiless3bucketname): {{String}}
  [DatabaseInstallationFilesS3Prefix](#cfn-rds-customdbengineversion-databaseinstallationfiless3prefix): {{String}}
  [Description](#cfn-rds-customdbengineversion-description): {{String}}
  [Engine](#cfn-rds-customdbengineversion-engine): {{String}}
  [EngineVersion](#cfn-rds-customdbengineversion-engineversion): {{String}}
  [ImageId](#cfn-rds-customdbengineversion-imageid): {{String}}
  [KMSKeyId](#cfn-rds-customdbengineversion-kmskeyid): {{String}}
  [Manifest](#cfn-rds-customdbengineversion-manifest): {{String}}
  [SourceCustomDbEngineVersionIdentifier](#cfn-rds-customdbengineversion-sourcecustomdbengineversionidentifier): {{String}}
  [Status](#cfn-rds-customdbengineversion-status): {{String}}
  [Tags](#cfn-rds-customdbengineversion-tags): {{
    - Tag}}
  [UseAwsProvidedLatestImage](#cfn-rds-customdbengineversion-useawsprovidedlatestimage): {{Boolean}}
```

## Properties
<a name="aws-resource-rds-customdbengineversion-properties"></a>

`DatabaseInstallationFiles`  <a name="cfn-rds-customdbengineversion-databaseinstallationfiles"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseInstallationFilesS3BucketName`  <a name="cfn-rds-customdbengineversion-databaseinstallationfiless3bucketname"></a>
The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseInstallationFilesS3Prefix`  <a name="cfn-rds-customdbengineversion-databaseinstallationfiless3prefix"></a>
The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-rds-customdbengineversion-description"></a>
An optional description of your CEV.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-rds-customdbengineversion-engine"></a>
The database engine to use for your custom engine version (CEV).
Valid values:
+  `custom-oracle-ee`
+  `custom-oracle-ee-cdb`
+  `sqlserver-dev-ee`
+  `sqlserver-ee`
+  `sqlserver-se`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `35`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineVersion`  <a name="cfn-rds-customdbengineversion-engineversion"></a>
The name of your CEV. The name format is `major version.customized_string`. For example, a valid CEV name is `19.my_cev1`. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of `Engine` and `EngineVersion` is unique per customer per Region.
*Constraints:* Minimum length is 1. Maximum length is 60.
*Pattern:*`^[a-z0-9_.-]{1,60$`}
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageId`  <a name="cfn-rds-customdbengineversion-imageid"></a>
A value that indicates the ID of the AMI.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KMSKeyId`  <a name="cfn-rds-customdbengineversion-kmskeyid"></a>
The AWS KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.
If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you don't already have a symmetric encryption KMS key in your account, follow the instructions in [ Creating a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.
You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Manifest`  <a name="cfn-rds-customdbengineversion-manifest"></a>
The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
The following JSON fields are valid:
MediaImportTemplateVersion
Version of the CEV manifest. The date is in the format `YYYY-MM-DD`.
databaseInstallationFileNames
Ordered list of installation files for the CEV.
opatchFileNames
Ordered list of OPatch installers used for the Oracle DB engine.
psuRuPatchFileNames
The PSU and RU patches for this CEV.
OtherPatchFileNames
The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches.
For more information, see [ Creating the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest) in the *Amazon RDS User Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `51000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceCustomDbEngineVersionIdentifier`  <a name="cfn-rds-customdbengineversion-sourcecustomdbengineversionidentifier"></a>
The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either `Source` or `UseAwsProvidedLatestImage`. You can't specify a different JSON manifest when you specify `SourceCustomDbEngineVersionIdentifier`.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-rds-customdbengineversion-status"></a>
A value that indicates the status of a custom engine version (CEV).
*Required*: No
*Type*: String
*Allowed values*: `available | inactive | inactive-except-restore | pending-validation`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-customdbengineversion-tags"></a>
A list of tags. For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide.*
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-customdbengineversion-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseAwsProvidedLatestImage`  <a name="cfn-rds-customdbengineversion-useawsprovidedlatestimage"></a>
Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify `UseAwsProvidedLatestImage`, you can't also specify `ImageId`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-customdbengineversion-return-values"></a>

### Ref
<a name="aws-resource-rds-customdbengineversion-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the resource name, such as `mystack-abc1d2efg3h4.` For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-customdbengineversion-return-values-fn--getatt"></a>

GetAtt returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following attributes are available.

####
<a name="aws-resource-rds-customdbengineversion-return-values-fn--getatt-fn--getatt"></a>

`DBEngineVersionArn`  <a name="DBEngineVersionArn-fn::getatt"></a>
The ARN of the custom engine version.

## Examples
<a name="aws-resource-rds-customdbengineversion--examples"></a>

The following example specifies a custom DB engine version.

### Authentication details
<a name="aws-resource-rds-customdbengineversion--examples--Authentication_details"></a>

#### JSON
<a name="aws-resource-rds-customdbengineversion--examples--Authentication_details--json"></a>

```
"RDSCustomDBEngineVersion":{
   "Type":"AWS::RDS::CustomDBEngineVersion",
   "Properties":{
      "DatabaseInstallationFilesS3BucketName": "1-custom-installation-files",
      "DatabaseInstallationFilesS3Prefix": "123456789012/cev1",
      "Description": "CEV description",
      "Engine": "custom-oracle-ee",
      "EngineVersion": "19.cev1",
      "KMSKeyId": "12ab3c4d-5678-90e1-2fg3-45h6ijklmnops",
      "Manifest": "%7B%22mediaImportTemplateVersion%22%3A%222020-08--14%22%2C%22databaseInstallationFileNames%22%3A%5B%22V982063-01.zip%22%5D%2C%22opatchFileNames%22%3A%5B%22p6880880_190000_Linux-x86-64.zip%22%5D%2C%22psuRuPatchFileNames%22%3A%5B%22p31720396_190000_Linux-x86-64.zip%22%2C%22p29213893_199000DBRU_Generic.zip%22%2C%22p28730253_190000_Linux-x86-64.zip%22%2C%22p29374604_199000DBRU_Linux-x86-64.zip%22%2C%22p28852325_190000_Linux-x86-64.zip%22%2C%22p29997937_190000_Linux-x86-64.zip%22%2C%22p31335037_190000_Linux-x86-64.zip%22%2C%22p31335142_190000_Generic.zip%22%5D%7D"
  }
}
```

#### YAML
<a name="aws-resource-rds-customdbengineversion--examples--Authentication_details--yaml"></a>

```
CustomDBEngineVersion:
  Type: AWS::RDS::CustomDBEngineVersion
  Properties:
      DatabaseInstallationFilesS3BucketName: 1-custom-installation-files
      DatabaseInstallationFilesS3Prefix: "123456789012/cev1
      Description: CEV description
      Engine: custom-oracle-ee
      EngineVersion: 19.cev1
      KMSKeyId: 12ab3c4d-5678-90e1-2fg3-45h6ijklmnops
      Manifest: "%7B%22mediaImportTemplateVersion%22%3A%222020-08--14%22%2C%22databaseInstallationFileNames%22%3A%5B%22V982063-01.zip%22%5D%2C%22opatchFileNames%22%3A%5B%22p6880880_190000_Linux-x86-64.zip%22%5D%2C%22psuRuPatchFileNames%22%3A%5B%22p31720396_190000_Linux-x86-64.zip%22%2C%22p29213893_199000DBRU_Generic.zip%22%2C%22p28730253_190000_Linux-x86-64.zip%22%2C%22p29374604_199000DBRU_Linux-x86-64.zip%22%2C%22p28852325_190000_Linux-x86-64.zip%22%2C%22p29997937_190000_Linux-x86-64.zip%22%2C%22p31335037_190000_Linux-x86-64.zip%22%2C%22p31335142_190000_Generic.zip%22%5D%7D
```

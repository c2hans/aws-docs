---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-s3exportingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain S3ExportingConfig
<a name="aws-properties-customerprofiles-domain-s3exportingconfig"></a>

The S3 location where Identity Resolution Jobs write result files.

## Syntax
<a name="aws-properties-customerprofiles-domain-s3exportingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-s3exportingconfig-syntax.json"></a>

```
{
  "[S3BucketName](#cfn-customerprofiles-domain-s3exportingconfig-s3bucketname)" : {{String}},
  "[S3KeyName](#cfn-customerprofiles-domain-s3exportingconfig-s3keyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-s3exportingconfig-syntax.yaml"></a>

```
  [S3BucketName](#cfn-customerprofiles-domain-s3exportingconfig-s3bucketname): {{String}}
  [S3KeyName](#cfn-customerprofiles-domain-s3exportingconfig-s3keyname): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-s3exportingconfig-properties"></a>

`S3BucketName`  <a name="cfn-customerprofiles-domain-s3exportingconfig-s3bucketname"></a>
The name of the S3 bucket where Identity Resolution Jobs write result files.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9.-]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KeyName`  <a name="cfn-customerprofiles-domain-s3exportingconfig-s3keyname"></a>
The S3 key name of the location where Identity Resolution Jobs write result files.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership ProtectedQueryS3OutputConfiguration
<a name="aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration"></a>

Contains the configuration to write the query results to S3.

## Syntax
<a name="aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration-syntax.json"></a>

```
{
  "[Bucket](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-bucket)" : {{String}},
  "[KeyPrefix](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-keyprefix)" : {{String}},
  "[ResultFormat](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-resultformat)" : {{String}},
  "[SingleFileOutput](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-singlefileoutput)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration-syntax.yaml"></a>

```
  [Bucket](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-bucket): {{String}}
  [KeyPrefix](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-keyprefix): {{String}}
  [ResultFormat](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-resultformat): {{String}}
  [SingleFileOutput](#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-singlefileoutput): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration-properties"></a>

`Bucket`  <a name="cfn-cleanrooms-membership-protectedquerys3outputconfiguration-bucket"></a>
The S3 bucket to unload the protected query results.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-cleanrooms-membership-protectedquerys3outputconfiguration-keyprefix"></a>
The S3 prefix to unload the protected query results.
*Required*: No
*Type*: String
*Pattern*: `[\w!.=*/-]*`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultFormat`  <a name="cfn-cleanrooms-membership-protectedquerys3outputconfiguration-resultformat"></a>
Intended file format of the result.
*Required*: Yes
*Type*: String
*Allowed values*: `CSV | PARQUET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleFileOutput`  <a name="cfn-cleanrooms-membership-protectedquerys3outputconfiguration-singlefileoutput"></a>
Indicates whether files should be output as a single file (`TRUE`) or output as multiple files (`FALSE`). This parameter is only supported for analyses with the Spark analytics engine.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

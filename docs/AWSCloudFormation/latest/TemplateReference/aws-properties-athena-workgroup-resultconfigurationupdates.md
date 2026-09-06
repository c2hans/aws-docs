---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-resultconfigurationupdates.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup ResultConfigurationUpdates
<a name="aws-properties-athena-workgroup-resultconfigurationupdates"></a>

The information about the updates in the query results, such as output location and encryption configuration for the query results.

## Syntax
<a name="aws-properties-athena-workgroup-resultconfigurationupdates-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-resultconfigurationupdates-syntax.json"></a>

```
{
  "[AclConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-aclconfiguration)" : {{AclConfiguration}},
  "[EncryptionConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration)" : {{EncryptionConfiguration}},
  "[ExpectedBucketOwner](#cfn-athena-workgroup-resultconfigurationupdates-expectedbucketowner)" : {{String}},
  "[OutputLocation](#cfn-athena-workgroup-resultconfigurationupdates-outputlocation)" : {{String}},
  "[RemoveAclConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-removeaclconfiguration)" : {{Boolean}},
  "[RemoveEncryptionConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration)" : {{Boolean}},
  "[RemoveExpectedBucketOwner](#cfn-athena-workgroup-resultconfigurationupdates-removeexpectedbucketowner)" : {{Boolean}},
  "[RemoveOutputLocation](#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-resultconfigurationupdates-syntax.yaml"></a>

```
  [AclConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-aclconfiguration): {{
    AclConfiguration}}
  [EncryptionConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [ExpectedBucketOwner](#cfn-athena-workgroup-resultconfigurationupdates-expectedbucketowner): {{String}}
  [OutputLocation](#cfn-athena-workgroup-resultconfigurationupdates-outputlocation): {{String}}
  [RemoveAclConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-removeaclconfiguration): {{Boolean}}
  [RemoveEncryptionConfiguration](#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration): {{Boolean}}
  [RemoveExpectedBucketOwner](#cfn-athena-workgroup-resultconfigurationupdates-removeexpectedbucketowner): {{Boolean}}
  [RemoveOutputLocation](#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation): {{Boolean}}
```

## Properties
<a name="aws-properties-athena-workgroup-resultconfigurationupdates-properties"></a>

`AclConfiguration`  <a name="cfn-athena-workgroup-resultconfigurationupdates-aclconfiguration"></a>
The ACL configuration for the query results.
*Required*: No
*Type*: [AclConfiguration](aws-properties-athena-workgroup-aclconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration"></a>
The encryption configuration for the query results.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-athena-workgroup-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpectedBucketOwner`  <a name="cfn-athena-workgroup-resultconfigurationupdates-expectedbucketowner"></a>
The AWS account ID that you expect to be the owner of the Amazon S3 bucket specified by [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation). If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner`AWS account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.
If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration) and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputLocation`  <a name="cfn-athena-workgroup-resultconfigurationupdates-outputlocation"></a>
The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Query Results](https://docs.aws.amazon.com/athena/latest/ug/querying.html) If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The "workgroup settings override" is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See [EnforceWorkGroupConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoveAclConfiguration`  <a name="cfn-athena-workgroup-resultconfigurationupdates-removeaclconfiguration"></a>
If set to `true`, indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null. If set to `false` or not set, and a value is present in the `AclConfiguration` of `ResultConfigurationUpdates`, the `AclConfiguration` in the workgroup's `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoveEncryptionConfiguration`  <a name="cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration"></a>
If set to "true", indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the EncryptionConfiguration in ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the workgroup's ResultConfiguration will be updated with the new value. For more information, see [Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoveExpectedBucketOwner`  <a name="cfn-athena-workgroup-resultconfigurationupdates-removeexpectedbucketowner"></a>
If set to "true", removes the AWS account ID previously specified for [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-expectedbucketowner](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-expectedbucketowner). If set to "false" or not set, and a value is present in the `ExpectedBucketOwner` in `ResultConfigurationUpdates` (the client-side setting), the `ExpectedBucketOwner` in the workgroup's `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoveOutputLocation`  <a name="cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation"></a>
If set to "true", indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the OutputLocation in ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup's ResultConfiguration will be updated with the new value. For more information, see [Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

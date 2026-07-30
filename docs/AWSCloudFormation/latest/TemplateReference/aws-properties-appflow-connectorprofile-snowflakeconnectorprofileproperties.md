---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile SnowflakeConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties"></a>

 The connector-specific profile properties required when using Snowflake.

## Syntax
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties-syntax.json"></a>

```
{
  "[AccountName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-accountname)" : {{String}},
  "[BucketName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketname)" : {{String}},
  "[BucketPrefix](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketprefix)" : {{String}},
  "[PrivateLinkServiceName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-privatelinkservicename)" : {{String}},
  "[Region](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-region)" : {{String}},
  "[Stage](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-stage)" : {{String}},
  "[Warehouse](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-warehouse)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties-syntax.yaml"></a>

```
  [AccountName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-accountname): {{String}}
  [BucketName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketname): {{String}}
  [BucketPrefix](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketprefix): {{String}}
  [PrivateLinkServiceName](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-privatelinkservicename): {{String}}
  [Region](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-region): {{String}}
  [Stage](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-stage): {{String}}
  [Warehouse](#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-warehouse): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties-properties"></a>

`AccountName`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-accountname"></a>
 The name of the account.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketName`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketname"></a>
 The name of the Amazon S3 bucket associated with Snowflake.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketPrefix`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketprefix"></a>
 The bucket path that refers to the Amazon S3 bucket associated with Snowflake.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateLinkServiceName`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-privatelinkservicename"></a>
 The Snowflake Private Link service name to be used for private data transfers.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-region"></a>
 The AWS Region of the Snowflake account.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-stage"></a>
 The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account. This is written in the following format: < Database>< Schema><Stage Name>.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Warehouse`  <a name="cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-warehouse"></a>
 The name of the Snowflake warehouse.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\w/!@#+=.-]*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties--seealso"></a>
+ [SnowflakeConnectorProfileProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SnowflakeConnectorProfileProperties.html) in the *Amazon AppFlow API Reference*.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile RedshiftConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties"></a>

 The connector-specific profile properties when using Amazon Redshift.

## Syntax
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties-syntax.json"></a>

```
{
  "[BucketName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketname)" : {{String}},
  "[BucketPrefix](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketprefix)" : {{String}},
  "[ClusterIdentifier](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-clusteridentifier)" : {{String}},
  "[DataApiRoleArn](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-dataapirolearn)" : {{String}},
  "[DatabaseName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databasename)" : {{String}},
  "[DatabaseUrl](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databaseurl)" : {{String}},
  "[IsRedshiftServerless](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-isredshiftserverless)" : {{Boolean}},
  "[RoleArn](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-rolearn)" : {{String}},
  "[WorkgroupName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties-syntax.yaml"></a>

```
  [BucketName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketname): {{String}}
  [BucketPrefix](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketprefix): {{String}}
  [ClusterIdentifier](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-clusteridentifier): {{String}}
  [DataApiRoleArn](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-dataapirolearn): {{String}}
  [DatabaseName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databasename): {{String}}
  [DatabaseUrl](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databaseurl): {{String}}
  [IsRedshiftServerless](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-isredshiftserverless): {{Boolean}}
  [RoleArn](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-rolearn): {{String}}
  [WorkgroupName](#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties-properties"></a>

`BucketName`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketname"></a>
 A name for the associated Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketPrefix`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketprefix"></a>
 The object key for the destination bucket in which Amazon AppFlow places the files.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterIdentifier`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-clusteridentifier"></a>
The unique ID that's assigned to an Amazon Redshift cluster.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataApiRoleArn`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-dataapirolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see [Allow Amazon AppFlow to access Amazon Redshift databases with the Data API](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift).
*Required*: No
*Type*: String
*Pattern*: `arn:aws:iam:.*:[0-9]+:.*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databasename"></a>
The name of an Amazon Redshift database.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseUrl`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databaseurl"></a>
 The JDBC URL of the Amazon Redshift cluster.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsRedshiftServerless`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-isredshiftserverless"></a>
Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-rolearn"></a>
 The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see [Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3).
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:iam:.*:[0-9]+:.*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupName`  <a name="cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-workgroupname"></a>
The name of an Amazon Redshift workgroup.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties--seealso"></a>
+ [RedshiftConnectorProfileProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_RedshiftConnectorProfileProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

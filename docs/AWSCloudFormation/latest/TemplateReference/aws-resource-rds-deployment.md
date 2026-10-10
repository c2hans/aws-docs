---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-deployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::Deployment
<a name="aws-resource-rds-deployment"></a>

Creates a blue/green deployment.

A blue/green deployment creates a staging environment that copies the production environment. In a blue/green deployment, the blue environment is the current production environment. The green environment is the staging environment, and it stays in sync with the current production environment.

You can make changes to the databases in the green environment without affecting production workloads. For example, you can upgrade the major or minor DB engine version, change database parameters, or make schema changes in the staging environment. You can thoroughly test changes in the green environment. When ready, you can switch over the environments to promote the green environment to be the new production environment. The switchover typically takes under a minute.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [ Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-resource-rds-deployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-deployment-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::Deployment",
  "Properties" : {
      "[BlueGreenDeploymentName](#cfn-rds-deployment-bluegreendeploymentname)" : {{String}},
      "[Source](#cfn-rds-deployment-source)" : {{String}},
      "[Tags](#cfn-rds-deployment-tags)" : {{[ Tag, ... ]}},
      "[TargetAllocatedStorage](#cfn-rds-deployment-targetallocatedstorage)" : {{Integer}},
      "[TargetDBClusterParameterGroupName](#cfn-rds-deployment-targetdbclusterparametergroupname)" : {{String}},
      "[TargetDBInstanceClass](#cfn-rds-deployment-targetdbinstanceclass)" : {{String}},
      "[TargetDBParameterGroupName](#cfn-rds-deployment-targetdbparametergroupname)" : {{String}},
      "[TargetEngineVersion](#cfn-rds-deployment-targetengineversion)" : {{String}},
      "[TargetIops](#cfn-rds-deployment-targetiops)" : {{Integer}},
      "[TargetStorageThroughput](#cfn-rds-deployment-targetstoragethroughput)" : {{Integer}},
      "[TargetStorageType](#cfn-rds-deployment-targetstoragetype)" : {{String}},
      "[UpgradeTargetStorageConfig](#cfn-rds-deployment-upgradetargetstorageconfig)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-rds-deployment-syntax.yaml"></a>

```
Type: AWS::RDS::Deployment
Properties:
  [BlueGreenDeploymentName](#cfn-rds-deployment-bluegreendeploymentname): {{String}}
  [Source](#cfn-rds-deployment-source): {{String}}
  [Tags](#cfn-rds-deployment-tags): {{
    - Tag}}
  [TargetAllocatedStorage](#cfn-rds-deployment-targetallocatedstorage): {{Integer}}
  [TargetDBClusterParameterGroupName](#cfn-rds-deployment-targetdbclusterparametergroupname): {{String}}
  [TargetDBInstanceClass](#cfn-rds-deployment-targetdbinstanceclass): {{String}}
  [TargetDBParameterGroupName](#cfn-rds-deployment-targetdbparametergroupname): {{String}}
  [TargetEngineVersion](#cfn-rds-deployment-targetengineversion): {{String}}
  [TargetIops](#cfn-rds-deployment-targetiops): {{Integer}}
  [TargetStorageThroughput](#cfn-rds-deployment-targetstoragethroughput): {{Integer}}
  [TargetStorageType](#cfn-rds-deployment-targetstoragetype): {{String}}
  [UpgradeTargetStorageConfig](#cfn-rds-deployment-upgradetargetstorageconfig): {{Boolean}}
```

## Properties
<a name="aws-resource-rds-deployment-properties"></a>

`BlueGreenDeploymentName`  <a name="cfn-rds-deployment-bluegreendeploymentname"></a>
The user-supplied name of the blue/green deployment.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z](?:-?[a-zA-Z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-rds-deployment-source"></a>
The source database for the blue/green deployment.
Before switchover, the source database is the production database in the blue environment.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-deployment-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-deployment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetAllocatedStorage`  <a name="cfn-rds-deployment-targetallocatedstorage"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetDBClusterParameterGroupName`  <a name="cfn-rds-deployment-targetdbclusterparametergroupname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z](?!.*--)[0-9A-Za-z-]*[^-]|^default(?!.*--)(?!.*\.\.)[0-9A-Za-z-.]*[^-]$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetDBInstanceClass`  <a name="cfn-rds-deployment-targetdbinstanceclass"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^db\.[0-9a-z]{2,6}\.[0-9a-z]{4,9}$`
*Minimum*: `5`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetDBParameterGroupName`  <a name="cfn-rds-deployment-targetdbparametergroupname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z](?!.*--)[0-9A-Za-z-]*[^-]|^default(?!.*--)(?!.*\.\.)[0-9A-Za-z-.]*[^-]$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetEngineVersion`  <a name="cfn-rds-deployment-targetengineversion"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z-_.]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetIops`  <a name="cfn-rds-deployment-targetiops"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetStorageThroughput`  <a name="cfn-rds-deployment-targetstoragethroughput"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetStorageType`  <a name="cfn-rds-deployment-targetstoragetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpgradeTargetStorageConfig`  <a name="cfn-rds-deployment-upgradetargetstorageconfig"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-deployment-return-values"></a>

### Ref
<a name="aws-resource-rds-deployment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rds-deployment-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-deployment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`BlueGreenDeploymentIdentifier`  <a name="BlueGreenDeploymentIdentifier-fn::getatt"></a>
The unique identifier of the blue/green deployment.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time when the blue/green deployment was created, in Universal Coordinated Time (UTC).

`Status`  <a name="Status-fn::getatt"></a>
The status of the blue/green deployment.
Valid Values:
+ `PROVISIONING` - Resources are being created in the green environment.
+ `AVAILABLE` - Resources are available in the green environment.
+ `SWITCHOVER_IN_PROGRESS` - The deployment is being switched from the blue environment to the green environment.
+ `SWITCHOVER_COMPLETED` - Switchover from the blue environment to the green environment is complete.
+ `INVALID_CONFIGURATION` - Resources in the green environment are invalid, so switchover isn't possible.
+ `SWITCHOVER_FAILED` - Switchover was attempted but failed.
+ `DELETING` - The blue/green deployment is being deleted.

`SwitchoverDetails`  <a name="SwitchoverDetails-fn::getatt"></a>
The details about each source and target resource in the blue/green deployment.

`Target`  <a name="Target-fn::getatt"></a>
The target database for the blue/green deployment.
Before switchover, the target database is the clone database in the green environment.

`Tasks`  <a name="Tasks-fn::getatt"></a>
Either tasks to be performed or tasks that have been completed on the target database before switchover.

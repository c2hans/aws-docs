---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-redshiftiamparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource RedshiftIAMParameters
<a name="aws-properties-quicksight-datasource-redshiftiamparameters"></a>

A structure that grants Quick Sight access to your cluster and make a call to the `redshift:GetClusterCredentials` API. For more information on the `redshift:GetClusterCredentials` API, see [https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html).

## Syntax
<a name="aws-properties-quicksight-datasource-redshiftiamparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-redshiftiamparameters-syntax.json"></a>

```
{
  "[AutoCreateDatabaseUser](#cfn-quicksight-datasource-redshiftiamparameters-autocreatedatabaseuser)" : {{Boolean}},
  "[DatabaseGroups](#cfn-quicksight-datasource-redshiftiamparameters-databasegroups)" : {{[ String, ... ]}},
  "[DatabaseUser](#cfn-quicksight-datasource-redshiftiamparameters-databaseuser)" : {{String}},
  "[RoleArn](#cfn-quicksight-datasource-redshiftiamparameters-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-redshiftiamparameters-syntax.yaml"></a>

```
  [AutoCreateDatabaseUser](#cfn-quicksight-datasource-redshiftiamparameters-autocreatedatabaseuser): {{Boolean}}
  [DatabaseGroups](#cfn-quicksight-datasource-redshiftiamparameters-databasegroups): {{
    - String}}
  [DatabaseUser](#cfn-quicksight-datasource-redshiftiamparameters-databaseuser): {{String}}
  [RoleArn](#cfn-quicksight-datasource-redshiftiamparameters-rolearn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-redshiftiamparameters-properties"></a>

`AutoCreateDatabaseUser`  <a name="cfn-quicksight-datasource-redshiftiamparameters-autocreatedatabaseuser"></a>
Automatically creates a database user. If your database doesn't have a `DatabaseUser`, set this parameter to `True`. If there is no `DatabaseUser`, Quick Sight can't connect to your cluster. The `RoleArn` that you use for this operation must grant access to `redshift:CreateClusterUser` to successfully create the user.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseGroups`  <a name="cfn-quicksight-datasource-redshiftiamparameters-databasegroups"></a>
A list of groups whose permissions will be granted to Quick Sight to access the cluster. These permissions are combined with the permissions granted to Quick Sight by the `DatabaseUser`. If you choose to include this parameter, the `RoleArn` must grant access to `redshift:JoinGroup`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseUser`  <a name="cfn-quicksight-datasource-redshiftiamparameters-databaseuser"></a>
The user whose permissions and group memberships will be used by Quick Sight to access the cluster. If this user already exists in your database, Amazon Quick Sight is granted the same permissions that the user has. If the user doesn't exist, set the value of `AutoCreateDatabaseUser` to `True` to create a new user with PUBLIC permissions.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-quicksight-datasource-redshiftiamparameters-rolearn"></a>
Use the `RoleArn` structure to allow Quick Sight to call `redshift:GetClusterCredentials` on your cluster. The calling principal must have `iam:PassRole` access to pass the role to Quick Sight. The role's trust policy must allow the Quick Sight service principal to assume the role.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-stackset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet
<a name="aws-resource-cloudformation-stackset"></a>

The `AWS::CloudFormation::StackSet` resource contains information about a StackSet. With StackSets, you can provision stacks across AWS accounts and Regions from a single CloudFormation template. Each stack is based on the same CloudFormation template, but you can customize individual stacks using parameters.

**Important**
Run deployments to nested StackSets from the parent stack, not directly through the StackSet API.

## Syntax
<a name="aws-resource-cloudformation-stackset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-stackset-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::StackSet",
  "Properties" : {
      "[AdministrationRoleARN](#cfn-cloudformation-stackset-administrationrolearn)" : {{String}},
      "[AutoDeployment](#cfn-cloudformation-stackset-autodeployment)" : {{AutoDeployment}},
      "[CallAs](#cfn-cloudformation-stackset-callas)" : {{String}},
      "[Capabilities](#cfn-cloudformation-stackset-capabilities)" : {{[ String, ... ]}},
      "[Description](#cfn-cloudformation-stackset-description)" : {{String}},
      "[ExecutionRoleName](#cfn-cloudformation-stackset-executionrolename)" : {{String}},
      "[ManagedExecution](#cfn-cloudformation-stackset-managedexecution)" : {{ManagedExecution}},
      "[OperationPreferences](#cfn-cloudformation-stackset-operationpreferences)" : {{OperationPreferences}},
      "[Parameters](#cfn-cloudformation-stackset-parameters)" : {{[ Parameter, ... ]}},
      "[PermissionModel](#cfn-cloudformation-stackset-permissionmodel)" : {{String}},
      "[StackInstancesGroup](#cfn-cloudformation-stackset-stackinstancesgroup)" : {{[ StackInstances, ... ]}},
      "[StackSetName](#cfn-cloudformation-stackset-stacksetname)" : {{String}},
      "[Tags](#cfn-cloudformation-stackset-tags)" : {{[ Tag, ... ]}},
      "[TemplateBody](#cfn-cloudformation-stackset-templatebody)" : {{String}},
      "[TemplateURL](#cfn-cloudformation-stackset-templateurl)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-stackset-syntax.yaml"></a>

```
Type: AWS::CloudFormation::StackSet
Properties:
  [AdministrationRoleARN](#cfn-cloudformation-stackset-administrationrolearn): {{String}}
  [AutoDeployment](#cfn-cloudformation-stackset-autodeployment): {{
    AutoDeployment}}
  [CallAs](#cfn-cloudformation-stackset-callas): {{String}}
  [Capabilities](#cfn-cloudformation-stackset-capabilities): {{
    - String}}
  [Description](#cfn-cloudformation-stackset-description): {{String}}
  [ExecutionRoleName](#cfn-cloudformation-stackset-executionrolename): {{String}}
  [ManagedExecution](#cfn-cloudformation-stackset-managedexecution): {{
    ManagedExecution}}
  [OperationPreferences](#cfn-cloudformation-stackset-operationpreferences): {{
    OperationPreferences}}
  [Parameters](#cfn-cloudformation-stackset-parameters): {{
    - Parameter}}
  [PermissionModel](#cfn-cloudformation-stackset-permissionmodel): {{String}}
  [StackInstancesGroup](#cfn-cloudformation-stackset-stackinstancesgroup): {{
    - StackInstances}}
  [StackSetName](#cfn-cloudformation-stackset-stacksetname): {{String}}
  [Tags](#cfn-cloudformation-stackset-tags): {{
    - Tag}}
  [TemplateBody](#cfn-cloudformation-stackset-templatebody): {{String}}
  [TemplateURL](#cfn-cloudformation-stackset-templateurl): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-stackset-properties"></a>

`AdministrationRoleARN`  <a name="cfn-cloudformation-stackset-administrationrolearn"></a>
The Amazon Resource Number (ARN) of the IAM role to use to create this StackSet. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account.
Use customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *CloudFormation User Guide*.
Valid only if the permissions model is `SELF_MANAGED`.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoDeployment`  <a name="cfn-cloudformation-stackset-autodeployment"></a>
Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see [Enable or disable automatic deployments for StackSets in AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html) in the *CloudFormation User Guide*.
Required if the permissions model is `SERVICE_MANAGED`. (Not used with self-managed permissions.)
*Required*: Conditional
*Type*: [AutoDeployment](aws-properties-cloudformation-stackset-autodeployment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CallAs`  <a name="cfn-cloudformation-stackset-callas"></a>
Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.
By default, `SELF` is specified. Use `SELF` for StackSets with self-managed permissions.
+ To create a StackSet with service-managed permissions while signed in to the management account, specify `SELF`.
+ To create a StackSet with service-managed permissions while signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated admin in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide*.
StackSets with service-managed permissions are created in the management account, including StackSets that are created by delegated administrators.
Valid only if the permissions model is `SERVICE_MANAGED`.
*Required*: No
*Type*: String
*Allowed values*: `SELF | DELEGATED_ADMIN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Capabilities`  <a name="cfn-cloudformation-stackset-capabilities"></a>
The capabilities that are allowed in the StackSet. Some StackSet templates might include resources that can affect permissions in your AWS account—for example, by creating new IAM users. For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities) in the *CloudFormation User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cloudformation-stackset-description"></a>
A description of the StackSet.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleName`  <a name="cfn-cloudformation-stackset-executionrolename"></a>
The name of the IAM execution role to use to create the StackSet. If you don't specify an execution role, CloudFormation uses the `AWSCloudFormationStackSetExecutionRole` role for the StackSet operation.
Valid only if the permissions model is `SELF_MANAGED`.
*Pattern*: `[a-zA-Z_0-9+=,.@-]+`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedExecution`  <a name="cfn-cloudformation-stackset-managedexecution"></a>
Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
When active, StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order.
If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting.
You can't modify your StackSet's execution configuration while there are running or queued operations for that StackSet.
When inactive (default), StackSets performs one operation at a time in request order.
*Required*: No
*Type*: [ManagedExecution](aws-properties-cloudformation-stackset-managedexecution.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperationPreferences`  <a name="cfn-cloudformation-stackset-operationpreferences"></a>
The user-specified preferences for how CloudFormation performs a StackSet operation.
*Required*: No
*Type*: [OperationPreferences](aws-properties-cloudformation-stackset-operationpreferences.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-cloudformation-stackset-parameters"></a>
The input parameters for the StackSet template.
*Required*: No
*Type*: Array of [Parameter](aws-properties-cloudformation-stackset-parameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PermissionModel`  <a name="cfn-cloudformation-stackset-permissionmodel"></a>
Describes how the IAM roles required for StackSet operations are created.
+ With `SELF_MANAGED` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *CloudFormation User Guide*.
+ With `SERVICE_MANAGED` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see [Activate trusted access for StackSets with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html) in the *CloudFormation User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVICE_MANAGED | SELF_MANAGED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StackInstancesGroup`  <a name="cfn-cloudformation-stackset-stackinstancesgroup"></a>
A group of stack instances with parameters in some specific accounts and Regions.
*Required*: No
*Type*: Array of [StackInstances](aws-properties-cloudformation-stackset-stackinstances.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackSetName`  <a name="cfn-cloudformation-stackset-stacksetname"></a>
The name to associate with the StackSet. The name must be unique in the Region where you create your StackSet.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9\-]{0,127}$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudformation-stackset-tags"></a>
Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.
If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you specify an empty value, CloudFormation removes all associated tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudformation-stackset-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateBody`  <a name="cfn-cloudformation-stackset-templatebody"></a>
The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
You must include either `TemplateURL` or `TemplateBody` in a StackSet, but you can't use both. Dynamic references in the `TemplateBody` may not work correctly in all cases. It's recommended to pass templates that contain dynamic references through `TemplateUrl` instead.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateURL`  <a name="cfn-cloudformation-stackset-templateurl"></a>
The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://`.
Conditional: You must specify only one of the following parameters: `TemplateBody`, `TemplateURL`.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `5120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-stackset-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-stackset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `StackSetId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-stackset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-stackset-return-values-fn--getatt-fn--getatt"></a>

`StackSetId`  <a name="StackSetId-fn::getatt"></a>
Returns the unique identifier of the resource.

## Examples
<a name="aws-resource-cloudformation-stackset--examples"></a>

**Topics**
+ [Activate managed execution for your StackSet](#aws-resource-cloudformation-stackset--examples--Activate_managed_execution_for_your_StackSet)
+ [Specifying Secrets Manager secrets in CloudFormation](#aws-resource-cloudformation-stackset--examples--Specifying_secrets_in)

### Activate managed execution for your StackSet
<a name="aws-resource-cloudformation-stackset--examples--Activate_managed_execution_for_your_StackSet"></a>

The following example creates a StackSet and specifies `ManagedExecution`. With managed execution activated, StackSets performs non-conflicting operations concurrently and queues conflicting operations.

#### JSON
<a name="aws-resource-cloudformation-stackset--examples--Activate_managed_execution_for_your_StackSet--json"></a>

```
{
    "TestStackSet1": {
        "Type": "AWS::CloudFormation::StackSet",
        "DeletionPolicy": "Retain",
        "Properties": {
            "StackSetName": "TestStackSet12345",
            "Description": "Updatedescription1",
            "PermissionModel": "SELF_MANAGED",
            "ManagedExecution": {
                "Active": true
            },
            "Tags": [
                {
                    "Key": "tag1",
                    "Value": "value1"
                }
            ],
            "TemplateBody": "{\n  \"AWSTemplateFormatVersion\": \"2010-09-09\",\n  \"Resources\": {\n    \"testWaitHandle\": {\n      \"Type\": \"AWS::CloudFormation::WaitConditionHandle\"\n    }\n  }\n}\n"
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-stackset--examples--Activate_managed_execution_for_your_StackSet--yaml"></a>

```
TestStackSet1:
  Type: AWS::CloudFormation::StackSet
  DeletionPolicy: Retain
  Properties:
    StackSetName: TestStackSet12345
    Description: Updatedescription1
    PermissionModel: SELF_MANAGED
    ManagedExecution:
      Active: true
    Tags:
      - Key: tag1
        Value: value1
    TemplateBody: |
      {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Resources": {
          "testWaitHandle": {
            "Type": "AWS::CloudFormation::WaitConditionHandle"
          }
        }
      }
```

### Specifying Secrets Manager secrets in CloudFormation
<a name="aws-resource-cloudformation-stackset--examples--Specifying_secrets_in"></a>

When using the `TemplateBody` property, if the template intends to resolve secrets from Secrets Manager secret's through an `ARN` and `!Join` is used to construct Secrets Manager's dynamic reference, secrets resolution needs to be avoided at stack level so that it will only be performed upon stack instance creation.

In the following example, a secrets resolution is avoided at the stack level by providing `{{` and `resolve:secretsmanager:` as separate strings to \!Join instead of `{{resolve:secretsmanager:` being provided as a single string:

#### JSON
<a name="aws-resource-cloudformation-stackset--examples--Specifying_secrets_in--json"></a>

```
{
    "Fn::Join": [
        "",
        [
            "{{",
            "resolve:secretsmanager:",
            {
                "Fn::Sub": "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:my-secret"
            },
            "::my-secret-key::}}"
        ]
    ]
}
```

#### YAML
<a name="aws-resource-cloudformation-stackset--examples--Specifying_secrets_in--yaml"></a>

```
!Join
- ''
- - '{{'
  - 'resolve:secretsmanager:'
  - !Sub 'arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:my-secret'
  - '::my-secret-key::}}'
```

## See also
<a name="aws-resource-cloudformation-stackset--seealso"></a>
+ [CloudFormation StackSets sample templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.html) in the *CloudFormation User Guide*

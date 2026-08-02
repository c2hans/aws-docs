---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-guardhook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GuardHook
<a name="aws-resource-cloudformation-guardhook"></a>

The `AWS::CloudFormation::GuardHook` resource creates and activates a Guard Hook. Using the Guard domain specific language (DSL), you can author Guard Hooks to evaluate your resources before allowing stack operations.

For more information, see [Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html) in the *CloudFormation Hooks User Guide*.

## Syntax
<a name="aws-resource-cloudformation-guardhook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-guardhook-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::GuardHook",
  "Properties" : {
      "[Alias](#cfn-cloudformation-guardhook-alias)" : {{String}},
      "[ExecutionRole](#cfn-cloudformation-guardhook-executionrole)" : {{String}},
      "[FailureMode](#cfn-cloudformation-guardhook-failuremode)" : {{String}},
      "[HookStatus](#cfn-cloudformation-guardhook-hookstatus)" : {{String}},
      "[LogBucket](#cfn-cloudformation-guardhook-logbucket)" : {{String}},
      "[Options](#cfn-cloudformation-guardhook-options)" : {{Options}},
      "[RuleLocation](#cfn-cloudformation-guardhook-rulelocation)" : {{S3Location}},
      "[StackFilters](#cfn-cloudformation-guardhook-stackfilters)" : {{StackFilters}},
      "[TargetFilters](#cfn-cloudformation-guardhook-targetfilters)" : {{TargetFilters}},
      "[TargetOperations](#cfn-cloudformation-guardhook-targetoperations)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-guardhook-syntax.yaml"></a>

```
Type: AWS::CloudFormation::GuardHook
Properties:
  [Alias](#cfn-cloudformation-guardhook-alias): {{String}}
  [ExecutionRole](#cfn-cloudformation-guardhook-executionrole): {{String}}
  [FailureMode](#cfn-cloudformation-guardhook-failuremode): {{String}}
  [HookStatus](#cfn-cloudformation-guardhook-hookstatus): {{String}}
  [LogBucket](#cfn-cloudformation-guardhook-logbucket): {{String}}
  [Options](#cfn-cloudformation-guardhook-options): {{
    Options}}
  [RuleLocation](#cfn-cloudformation-guardhook-rulelocation): {{
    S3Location}}
  [StackFilters](#cfn-cloudformation-guardhook-stackfilters): {{
    StackFilters}}
  [TargetFilters](#cfn-cloudformation-guardhook-targetfilters): {{
    TargetFilters}}
  [TargetOperations](#cfn-cloudformation-guardhook-targetoperations): {{
    - String}}
```

## Properties
<a name="aws-resource-cloudformation-guardhook-properties"></a>

`Alias`  <a name="cfn-cloudformation-guardhook-alias"></a>
The type name alias for the Hook. This alias must be unique per account and Region.
The alias must be in the form `Name1::Name2::Name3` and must not begin with `AWS`. For example, `Private::Guard::MyTestHook`.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRole`  <a name="cfn-cloudformation-guardhook-executionrole"></a>
The IAM role that the Hook assumes to retrieve your Guard rules from S3 and optionally write a detailed Guard output report back.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.+:iam::[0-9]{12}:role/.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailureMode`  <a name="cfn-cloudformation-guardhook-failuremode"></a>
Specifies how the Hook responds when rules fail their evaluation.
+ `FAIL`: Prevents the action from proceeding. This is helpful for enforcing strict compliance or security policies.
+ `WARN`: Issues warnings to users but allows actions to continue. This is useful for non-critical validations or informational checks.
*Required*: Yes
*Type*: String
*Allowed values*: `FAIL | WARN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HookStatus`  <a name="cfn-cloudformation-guardhook-hookstatus"></a>
Specifies if the Hook is `ENABLED` or `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogBucket`  <a name="cfn-cloudformation-guardhook-logbucket"></a>
Specifies the name of an S3 bucket to store the Guard output report. This report contains the results of your Guard rule validations.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-cloudformation-guardhook-options"></a>
Specifies the S3 location of your input parameters.
*Required*: No
*Type*: [Options](aws-properties-cloudformation-guardhook-options.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleLocation`  <a name="cfn-cloudformation-guardhook-rulelocation"></a>
Specifies the S3 location of your Guard rules.
*Required*: Yes
*Type*: [S3Location](aws-properties-cloudformation-guardhook-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackFilters`  <a name="cfn-cloudformation-guardhook-stackfilters"></a>
Specifies the stack level filters for the Hook.
Example stack level filter in JSON:

```
"StackFilters": {"FilteringCriteria": "ALL", "StackNames": {"Exclude": [ "stack-1", "stack-2"]}}
```
Example stack level filter in YAML:

```
StackFilters:
  FilteringCriteria: ALL
  StackNames:
    Exclude:
      - stack-1
      - stack-2
```
*Required*: No
*Type*: [StackFilters](aws-properties-cloudformation-guardhook-stackfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFilters`  <a name="cfn-cloudformation-guardhook-targetfilters"></a>
Specifies the target filters for the Hook.
Example target filter in JSON:

```
"TargetFilters": {"Actions": [ "CREATE", "UPDATE", "DELETE" ]}
```
Example target filter in YAML:

```
TargetFilters:
  Actions:
    - CREATE
    - UPDATE
    - DELETE
```
*Required*: No
*Type*: [TargetFilters](aws-properties-cloudformation-guardhook-targetfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetOperations`  <a name="cfn-cloudformation-guardhook-targetoperations"></a>
Specifies the list of operations the Hook is run against. For more information, see [Hook targets](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-concepts.html#hook-terms-hook-target) in the *CloudFormation Hooks User Guide*.
Valid values: `STACK` \| `RESOURCE` \| `CHANGE_SET` \| `CLOUD_CONTROL`
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-guardhook-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-guardhook-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Hook Amazon Resource Name (ARN). For example: `arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyGuardHook`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-guardhook-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-guardhook-return-values-fn--getatt-fn--getatt"></a>

`HookArn`  <a name="HookArn-fn::getatt"></a>
Returns the ARN of a Guard Hook.

## Examples
<a name="aws-resource-cloudformation-guardhook--examples"></a>

### Creating a Guard Hook in a template
<a name="aws-resource-cloudformation-guardhook--examples--Creating_a_Hook_in_a_template"></a>

The following example demonstrates how to create a Guard Hook in a template.

#### JSON
<a name="aws-resource-cloudformation-guardhook--examples--Creating_a_Hook_in_a_template--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Create a Guard Hook",
    "Parameters": {
        "GuardRulesS3Bucket": {
            "Description": "S3 bucket where your rules are",
            "Type": "String"
        },
        "GuardRulesS3Path": {
            "Description": "Location within GuardRulesS3Bucket where your Guard rules are",
            "Type": "String"
        },
        "GuardOutputBucket": {
            "Description": "S3 bucket to put Guard output",
            "Type": "String"
        },
        "HookName": {
            "Description": "The name of your Hook",
            "Type": "String",
            "Default": "Test::Guard::Hook",
            "AllowedPattern": "^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$"
        }
    },
    "Resources": {
        "GuardHookRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": ["hooks.cloudformation.amazonaws.com"]
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "root",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject",
                                        "s3:GetObjectVersion",
                                        "s3:ListBucket"
                                    ],
                                    "Resource": [
                                        {"Fn::Sub": "arn:aws:s3:::${GuardRulesS3Bucket}"},
                                        {"Fn::Sub": "arn:aws:s3:::${GuardRulesS3Bucket}/*"}
                                    ]
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": ["s3:PutObject"],
                                    "Resource": [{"Fn::Sub": "arn:aws:s3:::${GuardOutputBucket}/*"}]
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "GuardHook": {
            "Type": "AWS::CloudFormation::GuardHook",
            "Properties": {
                "TargetOperations": [
                    "RESOURCE",
                    "STACK"
                ],
                "Alias": {"Ref": "HookName"},
                "ExecutionRole": {
                    "Fn::GetAtt": [
                        "GuardHookRole",
                        "Arn"
                    ]
                },
                "FailureMode": "WARN",
                "HookStatus": "ENABLED",
                "LogBucket": {"Ref": "GuardOutputBucket"},
                "RuleLocation": {
                    "Uri": {"Fn::Sub": "s3://${GuardRulesS3Bucket}/${GuardRulesS3Path}"}
                },
                "TargetFilters": {
                    "Actions": [
                        "CREATE",
                        "UPDATE",
                        "DELETE"
                    ]
                },
                "StackFilters": {
                    "FilteringCriteria": "ALL",
                    "StackNames": {
                        "Exclude": [{"Ref": "AWS::StackName"}]
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-guardhook--examples--Creating_a_Hook_in_a_template--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Create a Guard Hook
Parameters:
  GuardRulesS3Bucket:
    Description: S3 bucket where your rules are
    Type: String
  GuardRulesS3Path:
    Description: Location within GuardRulesS3Bucket where your Guard rules are
    Type: String
  GuardOutputBucket:
    Description: S3 bucket to put Guard output
    Type: String
  HookName:
    Description: The name of your Hook
    Type: String
    Default: 'Test::Guard::Hook'
    AllowedPattern: '^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$'
Resources:
  GuardHookRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - hooks.cloudformation.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetObjectVersion
                  - s3:ListBucket
                Resource:
                  - !Sub arn:aws:s3:::${GuardRulesS3Bucket}
                  - !Sub arn:aws:s3:::${GuardRulesS3Bucket}/*
              - Effect: Allow
                Action:
                  - s3:PutObject
                Resource:
                  - !Sub arn:aws:s3:::${GuardOutputBucket}/*
  GuardHook:
    Type: AWS::CloudFormation::GuardHook
    Properties:
      TargetOperations:
        - RESOURCE
        - STACK
      Alias: !Ref HookName
      ExecutionRole: !GetAtt GuardHookRole.Arn
      FailureMode: WARN
      HookStatus: ENABLED
      LogBucket: !Ref GuardOutputBucket
      RuleLocation:
        Uri: !Sub s3://${GuardRulesS3Bucket}/${GuardRulesS3Path}
      TargetFilters:
        Actions:
          - CREATE
          - UPDATE
          - DELETE
      StackFilters:
        FilteringCriteria: ALL
        StackNames:
          Exclude:
            - !Ref AWS::StackName
```

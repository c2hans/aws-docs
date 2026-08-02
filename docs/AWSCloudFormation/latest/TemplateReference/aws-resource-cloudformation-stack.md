---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-stack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::Stack
<a name="aws-resource-cloudformation-stack"></a>

The `AWS::CloudFormation::Stack` resource nests a stack as a resource in a top-level template. For more information, see [Nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) in the *CloudFormation User Guide*.

You can add output values from a nested stack within the containing template. You use the [GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html) function with the nested stack's logical name and the name of the output value in the nested stack in the format `Outputs.NestedStackOutputName`.

We strongly recommend that updates to nested stacks are run from the parent stack.

When you apply template changes to update a top-level stack, CloudFormation updates the top-level stack and initiates an update to its nested stacks. CloudFormation updates the resources of modified nested stacks, but doesn't update the resources of unmodified nested stacks.

For stacks that contain IAM resources, you must acknowledge IAM capabilities. Also, make sure that you have cancel update stack permissions, which are required if an update rolls back. For more information about IAM and CloudFormation, see [Controlling access with AWS Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html) in the *CloudFormation User Guide*.

**Note**
A subset of `AWS::CloudFormation::Stack` resource type properties listed below are available to customers using CloudFormation, AWS CDK, and AWS Cloud Control API to configure.
 `NotificationARNs`
 `Parameters`
 `Tags`
 `TemplateURL`
 `TimeoutInMinutes`
These properties can be configured only when using AWS Cloud Control API. This is because the below properties are set by the parent stack, and thus cannot be configured using CloudFormation or AWS CDK but only AWS Cloud Control API.
 `Capabilities`
 `Description`
 `DisableRollback`
 `EnableTerminationProtection`
 `RoleARN`
 `StackName`
 `StackPolicyBody`
 `StackPolicyURL`
 `StackStatusReason`
 `TemplateBody`
Customers that configure `AWS::CloudFormation::Stack` using CloudFormation and AWS CDK can do so for nesting a CloudFormation stack as a resource in their top-level template.
These read-only properties can be accessed only when using AWS Cloud Control API.
 `ChangeSetId`
 `CreationTime`
 `LastUpdateTime`
 `Outputs`
 `ParentId`
 `RootId`
 `StackId`
 `StackStatus`

## Syntax
<a name="aws-resource-cloudformation-stack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-stack-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::Stack",
  "Properties" : {
      "[Capabilities](#cfn-cloudformation-stack-capabilities)" : {{[ String, ... ]}},
      "[Description](#cfn-cloudformation-stack-description)" : {{String}},
      "[DisableRollback](#cfn-cloudformation-stack-disablerollback)" : {{Boolean}},
      "[EnableTerminationProtection](#cfn-cloudformation-stack-enableterminationprotection)" : {{Boolean}},
      "[NotificationARNs](#cfn-cloudformation-stack-notificationarns)" : {{[ String, ... ]}},
      "[Parameters](#cfn-cloudformation-stack-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[RoleARN](#cfn-cloudformation-stack-rolearn)" : {{String}},
      "[StackName](#cfn-cloudformation-stack-stackname)" : {{String}},
      "[StackPolicyBody](#cfn-cloudformation-stack-stackpolicybody)" : {{Json}},
      "[StackPolicyURL](#cfn-cloudformation-stack-stackpolicyurl)" : {{String}},
      "[StackStatusReason](#cfn-cloudformation-stack-stackstatusreason)" : {{String}},
      "[Tags](#cfn-cloudformation-stack-tags)" : {{[ Tag, ... ]}},
      "[TemplateBody](#cfn-cloudformation-stack-templatebody)" : {{Json}},
      "[TemplateURL](#cfn-cloudformation-stack-templateurl)" : {{String}},
      "[TimeoutInMinutes](#cfn-cloudformation-stack-timeoutinminutes)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-stack-syntax.yaml"></a>

```
Type: AWS::CloudFormation::Stack
Properties:
  [Capabilities](#cfn-cloudformation-stack-capabilities): {{
    - String}}
  [Description](#cfn-cloudformation-stack-description): {{String}}
  [DisableRollback](#cfn-cloudformation-stack-disablerollback): {{Boolean}}
  [EnableTerminationProtection](#cfn-cloudformation-stack-enableterminationprotection): {{Boolean}}
  [NotificationARNs](#cfn-cloudformation-stack-notificationarns): {{
    - String}}
  [Parameters](#cfn-cloudformation-stack-parameters): {{
    {{Key}}: {{Value}}}}
  [RoleARN](#cfn-cloudformation-stack-rolearn): {{String}}
  [StackName](#cfn-cloudformation-stack-stackname): {{String}}
  [StackPolicyBody](#cfn-cloudformation-stack-stackpolicybody): {{Json}}
  [StackPolicyURL](#cfn-cloudformation-stack-stackpolicyurl): {{String}}
  [StackStatusReason](#cfn-cloudformation-stack-stackstatusreason): {{String}}
  [Tags](#cfn-cloudformation-stack-tags): {{
    - Tag}}
  [TemplateBody](#cfn-cloudformation-stack-templatebody): {{Json}}
  [TemplateURL](#cfn-cloudformation-stack-templateurl): {{String}}
  [TimeoutInMinutes](#cfn-cloudformation-stack-timeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-resource-cloudformation-stack-properties"></a>

`Capabilities`  <a name="cfn-cloudformation-stack-capabilities"></a>
In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.
+ `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`

  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.

  The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
  + If you have IAM resources, you can specify either capability.
  + If you have IAM resources with custom names, you *must* specify `CAPABILITY_NAMED_IAM`.
  + If you don't specify either of these capabilities, CloudFormation returns an `InsufficientCapabilities` error.

  If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
  +  [AWS::IAM::AccessKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html)
  +  [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html)
  +  [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html)
  +  [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html)
  +  [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html)
  +  [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html)
  +  [ AWS::IAM::UserToGroupAddition ](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html)

  For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities) in the *CloudFormation User Guide*.
+  `CAPABILITY_AUTO_EXPAND`

  Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation.

  If you want to create a stack from a stack template that contains macros *and* nested stacks, you must create the stack directly from the template using this capability.
**Important**
You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.
Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.

  For more information, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *CloudFormation User Guide*.
*Required*: No
*Type*: Array of String
*Allowed values*: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cloudformation-stack-description"></a>
A user-defined description associated with the stack.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableRollback`  <a name="cfn-cloudformation-stack-disablerollback"></a>
Set to `true` to disable rollback of the stack if stack creation failed. You can specify either `DisableRollback` or `OnFailure`, but not both.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableTerminationProtection`  <a name="cfn-cloudformation-stack-enableterminationprotection"></a>
Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see [Protect CloudFormation stacks from being deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html) in the *CloudFormation User Guide*. Termination protection is deactivated on stacks by default.
For nested stacks, termination protection is set on the root stack and can't be changed directly on the nested stack.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationARNs`  <a name="cfn-cloudformation-stack-notificationarns"></a>
The Amazon SNS topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-cloudformation-stack-parameters"></a>
The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter.
If you use the `Ref` function to pass a parameter value to a nested stack, comma-delimited list parameters must be of type `String`. In other words, you can't pass values that are of type `CommaDelimitedList` to nested stacks.
Required if the nested stack requires input parameters.
Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
*Required*: Conditional
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-cloudformation-stack-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackName`  <a name="cfn-cloudformation-stack-stackname"></a>
The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.
A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StackPolicyBody`  <a name="cfn-cloudformation-stack-stackpolicybody"></a>
Structure that contains the stack policy body. For more information, see [Prevent updates to stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html) in the *CloudFormation User Guide*. You can specify either the `StackPolicyBody` or the `StackPolicyURL` parameter, but not both.
*Required*: No
*Type*: Json
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackPolicyURL`  <a name="cfn-cloudformation-stack-stackpolicyurl"></a>
Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the `StackPolicyBody` or the `StackPolicyURL` parameter, but not both.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StackStatusReason`  <a name="cfn-cloudformation-stack-stackstatusreason"></a>
Success/failure message associated with the stack status.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudformation-stack-tags"></a>
Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudformation-stack-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateBody`  <a name="cfn-cloudformation-stack-templatebody"></a>
Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
Conditional: You must specify either the `TemplateBody` or the `TemplateURL` parameter, but not both.
*Required*: No
*Type*: Json
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateURL`  <a name="cfn-cloudformation-stack-templateurl"></a>
The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket. The location for an Amazon S3 bucket must start with `https://`.
Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutInMinutes`  <a name="cfn-cloudformation-stack-timeoutinminutes"></a>
The length of time, in minutes, that CloudFormation waits for the nested stack to reach the `CREATE_COMPLETE` state. The default is no timeout. When CloudFormation detects that the nested stack has reached the `CREATE_COMPLETE` state, it marks the nested stack resource as `CREATE_COMPLETE` in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches `CREATE_COMPLETE`, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack.
Updates aren't supported.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-stack-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-stack-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the stack ID. For example:

 `arn:aws:cloudformation:us-west-2:123456789012:stack/mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-stack-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-stack-return-values-fn--getatt-fn--getatt"></a>

`ChangeSetId`  <a name="ChangeSetId-fn::getatt"></a>
Returns the unique identifier of the change set.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Returns the time the stack was created.

`LastUpdateTime`  <a name="LastUpdateTime-fn::getatt"></a>
Returns the time the stack was last updated. This will only be returned if the stack has been updated at least once.

`Outputs`  <a name="Outputs-fn::getatt"></a>
Returns a list of output structures.

`ParentId`  <a name="ParentId-fn::getatt"></a>
For nested stacks, returns the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.

`RootId`  <a name="RootId-fn::getatt"></a>
For nested stacks, returns the stack ID of the top-level stack to which the nested stack ultimately belongs.

`StackId`  <a name="StackId-fn::getatt"></a>
Returns the unique identifier of the stack.

`StackStatus`  <a name="StackStatus-fn::getatt"></a>
Returns a success or failure message associated with the stack status.

## Examples
<a name="aws-resource-cloudformation-stack--examples"></a>

**Topics**
+ [Specify stack parameters](#aws-resource-cloudformation-stack--examples--Specify_stack_parameters)
+ [Nested stack](#aws-resource-cloudformation-stack--examples--Nested_stack)

### Specify stack parameters
<a name="aws-resource-cloudformation-stack--examples--Specify_stack_parameters"></a>

The sample template EC2ChooseAMI.template contains the following Parameters section:

#### JSON
<a name="aws-resource-cloudformation-stack--examples--Specify_stack_parameters--json"></a>

```
{
    "Parameters": {
        "InstanceType": {
            "Type": "String",
            "Default": "m1.small",
            "Description": "EC2 instance type, e.g. m1.small, m1.large, etc."
        },
        "WebServerPort": {
            "Type": "String",
            "Default": "80",
            "Description": "TCP/IP port of the web server"
        },
        "KeyName": {
            "Type": "String",
            "Description": "Name of an existing EC2 KeyPair to enable SSH access to the web server"
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-stack--examples--Specify_stack_parameters--yaml"></a>

```
Parameters:
  InstanceType:
    Type: String
    Default: m1.small
    Description: 'EC2 instance type, e.g. m1.small, m1.large, etc.'
  WebServerPort:
    Type: String
    Default: '80'
    Description: TCP/IP port of the web server
  KeyName:
    Type: String
    Description: Name of an existing EC2 KeyPair to enable SSH access to the web server
```

### Nested stack
<a name="aws-resource-cloudformation-stack--examples--Nested_stack"></a>

You could use the following template to embed a stack (`myStackWithParams`) using the `my-template.yaml` and use the `Parameters` property in the `AWS::CloudFormation::Stack` resource to specify an `InstanceType` and `KeyName`.

#### JSON
<a name="aws-resource-cloudformation-stack--examples--Nested_stack--json"></a>

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {
    "myStackWithParams" : {
      "Type" : "AWS::CloudFormation::Stack",
      "Properties" : {
        "TemplateURL" : "https://s3.amazonaws.com/amzn-s3-demo-bucket/my-template.yaml",
        "Parameters" : {
          "InstanceType" : "t1.micro",
          "KeyName" : "mykey"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudformation-stack--examples--Nested_stack--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myStackWithParams:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/amzn-s3-demo-bucket/MyTemplate.yaml
      Parameters:
        InstanceType: t1.micro
        KeyName: mykey
```

## See also
<a name="aws-resource-cloudformation-stack--seealso"></a>
+ For sample template snippets, see [CloudFormation template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudformation.html) in the *CloudFormation User Guide*.
+ If you have nested stacks that are stuck in an in-progress operation, see Troubleshooting Errors in [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html) in the *CloudFormation User Guide*.

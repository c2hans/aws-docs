---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::WaitCondition
<a name="aws-resource-cloudformation-waitcondition"></a>

The `AWS::CloudFormation::WaitCondition` resource provides a way to coordinate stack resource creation with configuration actions that are external to the stack creation or to track the status of a configuration process. In these situations, we recommend that you associate a `CreationPolicy` attribute with the wait condition instead of using a wait condition handle. For more information and an example, see [CreationPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-creationpolicy.html) in the *CloudFormation User Guide*. If you use a `CreationPolicy` with a wait condition, don't specify any of the wait condition's properties.

**Note**
If you use AWS PrivateLink, resources in the VPC that respond to wait conditions must have access to CloudFormation, specific Amazon S3 buckets. Resources must send wait condition responses to a presigned Amazon S3 URL. If they can't send responses to Amazon S3, CloudFormation won't receive a response and the stack operation fails. For more information, see [Access CloudFormation using an interface endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/vpc-interface-endpoints.html) in the *CloudFormation User Guide*.

**Important**
For Amazon EC2 and Auto Scaling resources, we recommend that you use a `CreationPolicy` attribute instead of wait conditions. Add a `CreationPolicy` attribute to those resources, and use the `cfn-signal` helper script to signal when an instance creation process has completed successfully.

## Syntax
<a name="aws-resource-cloudformation-waitcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-waitcondition-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::WaitCondition",
  "Properties" : {
      "[Count](#cfn-cloudformation-waitcondition-count)" : {{Integer}},
      "[Handle](#cfn-cloudformation-waitcondition-handle)" : {{String}},
      "[Timeout](#cfn-cloudformation-waitcondition-timeout)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-waitcondition-syntax.yaml"></a>

```
Type: AWS::CloudFormation::WaitCondition
Properties:
  [Count](#cfn-cloudformation-waitcondition-count): {{Integer}}
  [Handle](#cfn-cloudformation-waitcondition-handle): {{String}}
  [Timeout](#cfn-cloudformation-waitcondition-timeout): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-waitcondition-properties"></a>

`Count`  <a name="cfn-cloudformation-waitcondition-count"></a>
The number of success signals that CloudFormation must receive before it continues the stack creation process. When the wait condition receives the requisite number of success signals, CloudFormation resumes the creation of the stack. If the wait condition doesn't receive the specified number of success signals before the Timeout period expires, CloudFormation assumes that the wait condition has failed and rolls the stack back.
Updates aren't supported.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Handle`  <a name="cfn-cloudformation-waitcondition-handle"></a>
A reference to the wait condition handle used to signal this wait condition. Use the `Ref` intrinsic function to specify an [AWS::CloudFormation::WaitConditionHandle](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitconditionhandle.html) resource.
Anytime you add a `WaitCondition` resource during a stack update, you must associate the wait condition with a new WaitConditionHandle resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command.
Updates aren't supported.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-cloudformation-waitcondition-timeout"></a>
The length of time (in seconds) to wait for the number of signals that the `Count` property specifies. `Timeout` is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. The maximum time that can be specified for this property is 12 hours (43200 seconds).
Updates aren't supported.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-waitcondition-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-waitcondition-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-waitcondition-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-waitcondition-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
Returns a unique identifier for the resource.

## Examples
<a name="aws-resource-cloudformation-waitcondition--examples"></a>

### WaitCondition that has a timeout of 300 seconds
<a name="aws-resource-cloudformation-waitcondition--examples--WaitCondition_that_has_a_timeout_of_300_seconds"></a>

#### JSON
<a name="aws-resource-cloudformation-waitcondition--examples--WaitCondition_that_has_a_timeout_of_300_seconds--json"></a>

```
{
    "WaitHandle": {
        "Type": "AWS::CloudFormation::WaitConditionHandle"
    },
    "WaitCondition": {
        "Type": "AWS::CloudFormation::WaitCondition",
        "DependsOn": "MyResource",
        "Properties": {
            "Handle": {
                "Ref": "WaitHandle"
            },
            "Timeout": "300"
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-waitcondition--examples--WaitCondition_that_has_a_timeout_of_300_seconds--yaml"></a>

```
WaitHandle:
  Type: AWS::CloudFormation::WaitConditionHandle
WaitCondition:
  Type: AWS::CloudFormation::WaitCondition
  DependsOn: MyResource
  Properties:
    Handle: !Ref 'WaitHandle'
    Timeout: '300'
```

## See also
<a name="aws-resource-cloudformation-waitcondition--seealso"></a>
+ [Create wait conditions in a CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html) in the *CloudFormation User Guide*
+ [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html) in the *CloudFormation User Guide*

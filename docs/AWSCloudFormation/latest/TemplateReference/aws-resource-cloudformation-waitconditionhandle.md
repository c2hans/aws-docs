---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitconditionhandle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::WaitConditionHandle
<a name="aws-resource-cloudformation-waitconditionhandle"></a>

The `AWS::CloudFormation::WaitConditionHandle` type has no properties. When you reference the `WaitConditionHandle` resource by using the `Ref` function, CloudFormation returns a presigned URL. You pass this URL to applications or scripts that are running on your Amazon EC2 instances to send signals to that URL. An associated `AWS::CloudFormation::WaitCondition` resource checks the URL for the required number of success signals or for a failure signal.

For more information, see [Create wait conditions in a CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html) in the *CloudFormation User Guide*.

Anytime you add a `WaitCondition` resource during a stack update or update a resource with a wait condition, you must associate the wait condition with a new `WaitConditionHandle` resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command.

Updates aren't supported for this resource.

## Syntax
<a name="aws-resource-cloudformation-waitconditionhandle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-waitconditionhandle-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::WaitConditionHandle"
}
```

### YAML
<a name="aws-resource-cloudformation-waitconditionhandle-syntax.yaml"></a>

```
Type: AWS::CloudFormation::WaitConditionHandle
```

## Return values
<a name="aws-resource-cloudformation-waitconditionhandle-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-cloudformation-waitconditionhandle-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-waitconditionhandle-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
Returns a unique identifier for the resource.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::CustomResource
<a name="aws-resource-cloudformation-customresource"></a>

The `AWS::CloudFormation::CustomResource` resource creates a custom resource. Custom resources provide a way for you to write custom provisioning logic into your CloudFormation templates and have CloudFormation run it anytime you create, update (if you changed the custom resource), or delete a stack.

For more information, see [Create custom provisioning logic with custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) in the *CloudFormation User Guide*.

**Note**
If you use AWS PrivateLink, custom resources in the VPC must have access to CloudFormation-specific Amazon S3 buckets. Custom resources must send responses to a presigned Amazon S3 URL. If they can't send responses to Amazon S3, CloudFormation won't receive a response and the stack operation fails. For more information, see [Access CloudFormation using an interface endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/vpc-interface-endpoints.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-cloudformation-customresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-customresource-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::CustomResource",
  "Properties" : {
      "[ServiceTimeout](#cfn-cloudformation-customresource-servicetimeout)" : {{String}},
      "[ServiceToken](#cfn-cloudformation-customresource-servicetoken)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-customresource-syntax.yaml"></a>

```
Type: AWS::CloudFormation::CustomResource
Properties:
  [ServiceTimeout](#cfn-cloudformation-customresource-servicetimeout): {{String}}
  [ServiceToken](#cfn-cloudformation-customresource-servicetoken): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-customresource-properties"></a>

`ServiceTimeout`  <a name="cfn-cloudformation-customresource-servicetimeout"></a>
The maximum time, in seconds, that can elapse before a custom resource operation times out.
The value must be an integer from 1 to 3600. The default value is 3600 seconds (1 hour).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceToken`  <a name="cfn-cloudformation-customresource-servicetoken"></a>
The service token, such as an Amazon SNS topic ARN or Lambda function ARN. The service token must be from the same Region as the stack.
Updates aren't supported.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-customresource-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-cloudformation-customresource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Remarks
<a name="aws-resource-cloudformation-customresource--remarks"></a>

 *Specifying custom resource type names*

For custom resources, you can specify `AWS::CloudFormation::CustomResource` as the resource type, or you can specify your own resource type name. For example, instead of using `AWS::CloudFormation::CustomResource`, you can use `Custom::MyCustomResourceTypeName`.

Custom resource type names can include alphanumeric characters and the following characters: `_@-`. You can specify a custom resource type name up to a maximum length of 60 characters. You can't change the type during an update.

Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as `Custom::PingTester` to make them easily identifiable as ping testers (instead of using `AWS::CloudFormation::CustomResource`).

 *Replacing a custom resource during an update*

You can update custom resources that require a replacement of the underlying physical resource. When you update a custom resource in a CloudFormation template, CloudFormation sends an update request to that custom resource. If the custom resource requires a replacement, the new custom resource must send a response with the new physical ID. When CloudFormation receives the response, it compares the `PhysicalResourceId` between the old and new custom resources. If they're different, CloudFormation recognizes the update as a replacement and sends a delete request to the old resource. For more information about updating custom resources, see [Amazon SNS-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-sns.html) in the *CloudFormation User Guide*.

For information about monitoring the progress of the update, see [Monitor stack progress](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/monitor-stack-progress.html) in the *CloudFormation User Guide*.

 *Retrieving return values*

For a custom resource, return values are defined by the custom resource provider, and are retrieved by calling `Fn::GetAtt` on the provider-defined attributes.

## Examples
<a name="aws-resource-cloudformation-customresource--examples"></a>

**Topics**
+ [Creating a custom resource definition in a template](#aws-resource-cloudformation-customresource--examples--Creating_a_custom_resource_definition_in_a_template)
+ [Using a Lambda function in a custom resource](#aws-resource-cloudformation-customresource--examples--Using_a_function_in_a_custom_resource)

### Creating a custom resource definition in a template
<a name="aws-resource-cloudformation-customresource--examples--Creating_a_custom_resource_definition_in_a_template"></a>

The following example demonstrates how to create a custom resource definition in a template.

#### JSON
<a name="aws-resource-cloudformation-customresource--examples--Creating_a_custom_resource_definition_in_a_template--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyFrontEndTest": {
            "Type": "Custom::PingTester",
            "Version": "1.0",
            "Properties": {
                "ServiceToken": "arn:aws:sns:us-west-2:123456789012:CRTest",
                "ServiceTimeout": "600",
                "key1": "string",
                "key2": [
                    "list"
                ],
                "key3": {
                    "key4": "map"
                }
            }
        }
    },
    "Outputs": {
        "CustomResourceAttribute1": {
            "Value": {
                "Fn::GetAtt": [
                    "MyFrontEndTest",
                    "responseKey1"
                ]
            }
        },
        "CustomResourceAttribute2": {
            "Value": {
                "Fn::GetAtt": [
                    "MyFrontEndTest",
                    "responseKey2"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-customresource--examples--Creating_a_custom_resource_definition_in_a_template--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyFrontEndTest:
    Type: 'Custom::PingTester'
    Version: '1.0'
    Properties:
      ServiceToken: 'arn:aws:sns:us-west-2:123456789012:CRTest'
      ServiceTimeout: 600
      key1: string
      key2:
        - list
      key3:
        key4: map
Outputs:
  CustomResourceAttribute1:
    Value: !GetAtt
      - MyFrontEndTest
      - responseKey1
  CustomResourceAttribute2:
    Value: !GetAtt
      - MyFrontEndTest
      - responseKey2
```

### Using a Lambda function in a custom resource
<a name="aws-resource-cloudformation-customresource--examples--Using_a_function_in_a_custom_resource"></a>

With Lambda functions and custom resources, you can run custom code in response to stack events (create, update, and delete). The following custom resource invokes a Lambda function and sends it the `StackName` property as input. The function uses this property to get outputs from the appropriate stack.

#### JSON
<a name="aws-resource-cloudformation-customresource--examples--Using_a_function_in_a_custom_resource--json"></a>

```
{
    "MyCustomResource": {
        "Type": "Custom::TestLambdaCrossStackRef",
        "Properties": {
            "ServiceToken": {
                "Fn::Join": [
                    "",
                    [
                        "arn:aws:lambda:",
                        {
                            "Ref": "AWS::Region"
                        },
                        ":",
                        {
                            "Ref": "AWS::AccountId"
                        },
                        ":function:",
                        {
                            "Ref": "LambdaFunctionName"
                        }
                    ]
                ]
            },
            "ServiceTimeout": "35",
            "StackName": {
                "Ref": "NetworkStackName"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-customresource--examples--Using_a_function_in_a_custom_resource--yaml"></a>

```
MyCustomResource:
  Type: 'Custom::TestLambdaCrossStackRef'
  Properties:
    ServiceToken: !Join
      - ''
      - - 'arn:aws:lambda:'
        - !Ref 'AWS::Region'
        - ':'
        - !Ref 'AWS::AccountId'
        - ':function:'
        - !Ref LambdaFunctionName
    ServiceTimeout: 35
    StackName: !Ref NetworkStackName
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::ResourcePolicy
<a name="aws-resource-lambda-resourcepolicy"></a>

Use the `AWS::Lambda::ResourcePolicy` resource to attach a resource-based policy to a Lambda resource. A resource-based policy applies to a single Lambda resource, for example, a function, function version, or function alias. To learn more about using resource-based policies with Lambda, see [Working with resource-based policies in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *AWS Lambda Developer Guide*.

You can use resource-based policies to grant permissions to other AWS services, AWS accounts and organizations, and IAM users and roles to access your Lambda resource. You can also deny access to specific entities, and use the full range of IAM global condition keys to further restrict who has access to your Lambda resource. For example, you can limit access to calls originating from a specified IP address or Amazon VPC.

A resource-based policy is a JSON document containing a number of statements. Each statement defines the entities you want to grant permission to, the API actions you want to allow or deny, and the Lambda resource you want the statement to apply to. A statement can also optionally include an array of logical conditions using the IAM global condition keys.

To use the `AWS::Lambda::ResourcePolicy` resource, make sure that you have the [resource-based policy permissions for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#access-control-resource-based-permissions).

To learn more about creating resource-based policies, see [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *AWS Identity and Access Management User Guide*. For more information about example policies for providing permissions to AWS services, other AWS accounts, and IAM users and roles, see [Example resource-based policies for Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-examples.html) in the *AWS Lambda Developer Guide*.

**Avoid mixing permission resource types**
To grant permissions to access your function, we recommend using the `AWS::Lambda::ResourcePolicy` resource to set access permissions. With this resource, you have more flexibility and fine-grained control than `AWS::Lambda::Permission`. This resource grants an AWS service or another account permission to call a particular API action on a function.
You can also use the `AWS::Lambda::Permission` resource, however using both `AWS::Lambda::Permission` and `AWS::Lambda::ResourcePolicy` to set permissions on a function can result in errors. Permissions defined in `AWS::Lambda::Permission` can be unintentionally overwritten, whether in a single CloudFormation stack or across multiple stacks. Don't use both resource types to set permissions on a function.
To migrate existing permissions for a function from `AWS::Lambda::Permission` to `AWS::Lambda::ResourcePolicy`, do the following:
Set a `Retain`[deletion policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) on the `AWS::Lambda::Permission` resources you want to migrate. This is necessary so that Lambda does not delete statements with the same statement ID when you delete these resources.
Use the [GetResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetResourcePolicy.html)Lambda API to retrieve the resource-based policy currently attached to the function.
Use this policy to create a new `AWS::Lambda::ResourcePolicy` resource.
Delete all the existing `AWS::Lambda::Permission` resources for the function.

## Syntax
<a name="aws-resource-lambda-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::ResourcePolicy",
  "Properties" : {
      "[PolicyDocument](#cfn-lambda-resourcepolicy-policydocument)" : {{Json}},
      "[ResourceArn](#cfn-lambda-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::Lambda::ResourcePolicy
Properties:
  [PolicyDocument](#cfn-lambda-resourcepolicy-policydocument): {{Json}}
  [ResourceArn](#cfn-lambda-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-lambda-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-lambda-resourcepolicy-policydocument"></a>
The policy document you want to add to your Lambda resource. This is formatted as a JSON string.
For more information, see [Working with resource-based policies in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *AWS Lambda Developer Guide*.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-lambda-resourcepolicy-resourcearn"></a>
The Amazon Resource Name (ARN) of the Lambda resource you want to add the policy to. For a function, you can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?$`
*Minimum*: `12`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-lambda-resourcepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the primary ID of the resource (`ResourceArn`)

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-lambda-resourcepolicy--examples"></a>

### Grant invoke permission to another AWS account
<a name="aws-resource-lambda-resourcepolicy--examples--Grant_invoke_permission_to_another_account"></a>

The following example templates attach an IAM policy to a Lambda function using the `PolicyDocument` property that allows the function to be invoked by another AWS account.

For more information about example resource-based policies for a variety of use cases, see [Working with resource-based IAM policies in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *AWS Lambda Developer Guide*.

#### JSON
<a name="aws-resource-lambda-resourcepolicy--examples--Grant_invoke_permission_to_another_account--json"></a>

```
"LambdaResourcePolicy": {
    "Type": "AWS::Lambda::ResourcePolicy",
    "Properties": {
        "ResourceArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::111122223333:root"
                    },
                    "Action": "lambda:InvokeFunction",
                    "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function"
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-lambda-resourcepolicy--examples--Grant_invoke_permission_to_another_account--yaml"></a>

```
LambdaResourcePolicy:
  Type: AWS::Lambda::ResourcePolicy
  Properties:
    ResourceArn: arn:aws:lambda:us-east-2:123456789012:function:my-function
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
      - Sid: Statement1
        Effect: Allow
        Principal:
          AWS: arn:aws:iam::111122223333:root
        Action: lambda:InvokeFunction
        Resource: arn:aws:lambda:us-east-2:123456789012:function:my-function
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

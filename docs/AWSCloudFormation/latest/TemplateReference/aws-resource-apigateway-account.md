---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-account.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Account
<a name="aws-resource-apigateway-account"></a>

The `AWS::ApiGateway::Account` resource specifies the IAM role that Amazon API Gateway uses to write API logs to Amazon CloudWatch Logs. To avoid overwriting other roles, you should only have one `AWS::ApiGateway::Account` resource per region per account.

When you delete a stack containing this resource, API Gateway can still assume the provided IAM role to write API logs to CloudWatch Logs. To deny API Gateway access to write API logs to CloudWatch logs, update the permissions policies or change the IAM role to deny access.

## Syntax
<a name="aws-resource-apigateway-account-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-account-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::Account",
  "Properties" : {
      "[CloudWatchRoleArn](#cfn-apigateway-account-cloudwatchrolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-account-syntax.yaml"></a>

```
Type: AWS::ApiGateway::Account
Properties:
  [CloudWatchRoleArn](#cfn-apigateway-account-cloudwatchrolearn): {{String}}
```

## Properties
<a name="aws-resource-apigateway-account-properties"></a>

`CloudWatchRoleArn`  <a name="cfn-apigateway-account-cloudwatchrolearn"></a>
The ARN of an Amazon CloudWatch role for the current Account.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-apigateway-account-return-values"></a>

### Ref
<a name="aws-resource-apigateway-account-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the resource, such as `mysta-accou-01234b567890example`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apigateway-account-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigateway-account-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID for the account. For example: `abc123`.

## Examples
<a name="aws-resource-apigateway-account--examples"></a>

### Associate account with IAM role
<a name="aws-resource-apigateway-account--examples--Associate_account_with_IAM_role"></a>

The following example creates an IAM role that API Gateway can assume to push logs to CloudWatch Logs. The example associates the role with the `AWS::ApiGateway::Account resource`.

#### JSON
<a name="aws-resource-apigateway-account--examples--Associate_account_with_IAM_role--json"></a>

```
{
    "CloudWatchRole": {
        "Type": "AWS::IAM::Role",
        "Properties": {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17"		 	 	 ,
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": [
                                "apigateway.amazonaws.com"
                            ]
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            },
            "Path": "/",
            "ManagedPolicyArns": [
                "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
            ]
        }
    },
    "Account": {
        "Type": "AWS::ApiGateway::Account",
        "Properties": {
            "CloudWatchRoleArn": {
                "Fn::GetAtt": [
                    "CloudWatchRole",
                    "Arn"
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-account--examples--Associate_account_with_IAM_role--yaml"></a>

```
CloudWatchRole:
  Type: 'AWS::IAM::Role'
  Properties:
    AssumeRolePolicyDocument:
      Version: 2012-10-17
      Statement:
        - Effect: Allow
          Principal:
            Service:
              - apigateway.amazonaws.com
          Action: 'sts:AssumeRole'
    Path: /
    ManagedPolicyArns:
      - >-
        arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs
Account:
  Type: 'AWS::ApiGateway::Account'
  Properties:
    CloudWatchRoleArn: !GetAtt
      - CloudWatchRole
      - Arn
```

## See also
<a name="aws-resource-apigateway-account--seealso"></a>
+ [account:update](https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateAccount.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

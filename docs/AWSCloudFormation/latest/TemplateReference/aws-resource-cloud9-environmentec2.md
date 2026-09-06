---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloud9-environmentec2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cloud9::EnvironmentEC2
<a name="aws-resource-cloud9-environmentec2"></a>

The `AWS::Cloud9::EnvironmentEC2` resource creates an Amazon EC2 development environment in AWS Cloud9. For more information, see [Creating an Environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html) in the *AWS Cloud9 User Guide*.

## Syntax
<a name="aws-resource-cloud9-environmentec2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloud9-environmentec2-syntax.json"></a>

```
{
  "Type" : "AWS::Cloud9::EnvironmentEC2",
  "Properties" : {
      "[AutomaticStopTimeMinutes](#cfn-cloud9-environmentec2-automaticstoptimeminutes)" : {{Integer}},
      "[ConnectionType](#cfn-cloud9-environmentec2-connectiontype)" : {{String}},
      "[Description](#cfn-cloud9-environmentec2-description)" : {{String}},
      "[ImageId](#cfn-cloud9-environmentec2-imageid)" : {{String}},
      "[InstanceType](#cfn-cloud9-environmentec2-instancetype)" : {{String}},
      "[Name](#cfn-cloud9-environmentec2-name)" : {{String}},
      "[OwnerArn](#cfn-cloud9-environmentec2-ownerarn)" : {{String}},
      "[Repositories](#cfn-cloud9-environmentec2-repositories)" : {{[ Repository, ... ]}},
      "[SubnetId](#cfn-cloud9-environmentec2-subnetid)" : {{String}},
      "[Tags](#cfn-cloud9-environmentec2-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloud9-environmentec2-syntax.yaml"></a>

```
Type: AWS::Cloud9::EnvironmentEC2
Properties:
  [AutomaticStopTimeMinutes](#cfn-cloud9-environmentec2-automaticstoptimeminutes): {{Integer}}
  [ConnectionType](#cfn-cloud9-environmentec2-connectiontype): {{String}}
  [Description](#cfn-cloud9-environmentec2-description): {{String}}
  [ImageId](#cfn-cloud9-environmentec2-imageid): {{String}}
  [InstanceType](#cfn-cloud9-environmentec2-instancetype): {{String}}
  [Name](#cfn-cloud9-environmentec2-name): {{String}}
  [OwnerArn](#cfn-cloud9-environmentec2-ownerarn): {{String}}
  [Repositories](#cfn-cloud9-environmentec2-repositories): {{
    - Repository}}
  [SubnetId](#cfn-cloud9-environmentec2-subnetid): {{String}}
  [Tags](#cfn-cloud9-environmentec2-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloud9-environmentec2-properties"></a>

`AutomaticStopTimeMinutes`  <a name="cfn-cloud9-environmentec2-automaticstoptimeminutes"></a>
The number of minutes until the running instance is shut down after the environment was last used.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `20160`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionType`  <a name="cfn-cloud9-environmentec2-connectiontype"></a>
The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` (default) and `CONNECT_SSM` (connected through AWS Systems Manager).
*Required*: No
*Type*: String
*Allowed values*: `CONNECT_SSH | CONNECT_SSM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cloud9-environmentec2-description"></a>
The description of the environment to create.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageId`  <a name="cfn-cloud9-environmentec2-imageid"></a>
The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid AWS Systems Manager path.
From December 04, 2023, you will be required to include the `ImageId` parameter for the `CreateEnvironmentEC2` action. This change will be reflected across all direct methods of communicating with the API, such as AWS SDK, AWS CLI and AWS CloudFormation. This change will only affect direct API consumers, and not AWS Cloud9 console users.
Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04.
 **AMI aliases **
+ Amazon Linux 2: `amazonlinux-2-x86_64`
+ Amazon Linux 2023 (recommended): `amazonlinux-2023-x86_64`
+ Ubuntu 18.04: `ubuntu-18.04-x86_64`
+ Ubuntu 22.04: `ubuntu-22.04-x86_64`
 **SSM paths**
+ Amazon Linux 2: `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
+ Amazon Linux 2023 (recommended): `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64`
+ Ubuntu 18.04: `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
+ Ubuntu 22.04: `resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64`
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-cloud9-environmentec2-instancetype"></a>
The type of instance to connect to the environment (for example, `t2.micro`).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z]+[1-9][.][a-z0-9]+$`
*Minimum*: `5`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloud9-environmentec2-name"></a>
The name of the environment.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerArn`  <a name="cfn-cloud9-environmentec2-ownerarn"></a>
The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS Identity and Access Management principal. If this value is not specified, the ARN defaults to this environment's creator.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Repositories`  <a name="cfn-cloud9-environmentec2-repositories"></a>
Any AWS CodeCommit source code repositories to be cloned into the development environment.
*Required*: No
*Type*: Array of [Repository](aws-properties-cloud9-environmentec2-repository.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-cloud9-environmentec2-subnetid"></a>
The ID of the subnet in Amazon Virtual Private Cloud (Amazon VPC) that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
*Required*: No
*Type*: String
*Pattern*: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`
*Minimum*: `15`
*Maximum*: `24`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloud9-environmentec2-tags"></a>
An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloud9-environmentec2-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloud9-environmentec2-return-values"></a>

### Ref
<a name="aws-resource-cloud9-environmentec2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the development environment, such as `2bc3642873c342e485f7e0c561234567`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloud9-environmentec2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloud9-environmentec2-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the development environment, such as `arn:aws:cloud9:us-east-2:123456789012:environment:2bc3642873c342e485f7e0c561234567`.

`Name`  <a name="Name-fn::getatt"></a>
The name of the environment.

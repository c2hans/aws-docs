---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-notebookinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::NotebookInstance
<a name="aws-resource-sagemaker-notebookinstance"></a>

The `AWS::SageMaker::NotebookInstance` resource creates an Amazon SageMaker notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook. For more information, see [Use Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html).

## Syntax
<a name="aws-resource-sagemaker-notebookinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-notebookinstance-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::NotebookInstance",
  "Properties" : {
      "[AcceleratorTypes](#cfn-sagemaker-notebookinstance-acceleratortypes)" : {{[ String, ... ]}},
      "[AdditionalCodeRepositories](#cfn-sagemaker-notebookinstance-additionalcoderepositories)" : {{[ String, ... ]}},
      "[DefaultCodeRepository](#cfn-sagemaker-notebookinstance-defaultcoderepository)" : {{String}},
      "[DirectInternetAccess](#cfn-sagemaker-notebookinstance-directinternetaccess)" : {{String}},
      "[InstanceMetadataServiceConfiguration](#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration)" : {{InstanceMetadataServiceConfiguration}},
      "[InstanceType](#cfn-sagemaker-notebookinstance-instancetype)" : {{String}},
      "[KmsKeyId](#cfn-sagemaker-notebookinstance-kmskeyid)" : {{String}},
      "[LifecycleConfigName](#cfn-sagemaker-notebookinstance-lifecycleconfigname)" : {{String}},
      "[NotebookInstanceName](#cfn-sagemaker-notebookinstance-notebookinstancename)" : {{String}},
      "[PlatformIdentifier](#cfn-sagemaker-notebookinstance-platformidentifier)" : {{String}},
      "[RoleArn](#cfn-sagemaker-notebookinstance-rolearn)" : {{String}},
      "[RootAccess](#cfn-sagemaker-notebookinstance-rootaccess)" : {{String}},
      "[SecurityGroupIds](#cfn-sagemaker-notebookinstance-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetId](#cfn-sagemaker-notebookinstance-subnetid)" : {{String}},
      "[Tags](#cfn-sagemaker-notebookinstance-tags)" : {{[ Tag, ... ]}},
      "[VolumeSizeInGB](#cfn-sagemaker-notebookinstance-volumesizeingb)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-notebookinstance-syntax.yaml"></a>

```
Type: AWS::SageMaker::NotebookInstance
Properties:
  [AcceleratorTypes](#cfn-sagemaker-notebookinstance-acceleratortypes): {{
    - String}}
  [AdditionalCodeRepositories](#cfn-sagemaker-notebookinstance-additionalcoderepositories): {{
    - String}}
  [DefaultCodeRepository](#cfn-sagemaker-notebookinstance-defaultcoderepository): {{String}}
  [DirectInternetAccess](#cfn-sagemaker-notebookinstance-directinternetaccess): {{String}}
  [InstanceMetadataServiceConfiguration](#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration): {{
    InstanceMetadataServiceConfiguration}}
  [InstanceType](#cfn-sagemaker-notebookinstance-instancetype): {{String}}
  [KmsKeyId](#cfn-sagemaker-notebookinstance-kmskeyid): {{String}}
  [LifecycleConfigName](#cfn-sagemaker-notebookinstance-lifecycleconfigname): {{String}}
  [NotebookInstanceName](#cfn-sagemaker-notebookinstance-notebookinstancename): {{String}}
  [PlatformIdentifier](#cfn-sagemaker-notebookinstance-platformidentifier): {{String}}
  [RoleArn](#cfn-sagemaker-notebookinstance-rolearn): {{String}}
  [RootAccess](#cfn-sagemaker-notebookinstance-rootaccess): {{String}}
  [SecurityGroupIds](#cfn-sagemaker-notebookinstance-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-sagemaker-notebookinstance-subnetid): {{String}}
  [Tags](#cfn-sagemaker-notebookinstance-tags): {{
    - Tag}}
  [VolumeSizeInGB](#cfn-sagemaker-notebookinstance-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-resource-sagemaker-notebookinstance-properties"></a>

`AcceleratorTypes`  <a name="cfn-sagemaker-notebookinstance-acceleratortypes"></a>
A list of Amazon Elastic Inference (EI) instance types to associate with the notebook instance. Currently, only one instance type can be associated with a notebook instance. For more information, see [Using Elastic Inference in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html).
*Valid Values:*`ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdditionalCodeRepositories`  <a name="cfn-sagemaker-notebookinstance-additionalcoderepositories"></a>
An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultCodeRepository`  <a name="cfn-sagemaker-notebookinstance-defaultcoderepository"></a>
The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
*Required*: No
*Type*: String
*Pattern*: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DirectInternetAccess`  <a name="cfn-sagemaker-notebookinstance-directinternetaccess"></a>
Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to `Disabled` this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a NAT Gateway in your VPC.
For more information, see [Notebook Instances Are Internet-Enabled by Default](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access). You can set the value of this parameter to `Disabled` only if you set a value for the `SubnetId` parameter.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceMetadataServiceConfiguration`  <a name="cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration"></a>
Information on the IMDS configuration of the notebook instance
*Required*: No
*Type*: [InstanceMetadataServiceConfiguration](aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-notebookinstance-instancetype"></a>
The type of ML compute instance to launch for the notebook instance.
Expect some interruption of service if this parameter is changed as CloudFormation stops a notebook instance and starts it up again to update it.
*Required*: Yes
*Type*: String
*Allowed values*: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p5.4xlarge | ml.p5en.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-sagemaker-notebookinstance-kmskeyid"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see [Enabling and Disabling Keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/_-]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LifecycleConfigName`  <a name="cfn-sagemaker-notebookinstance-lifecycleconfigname"></a>
The name of a lifecycle configuration to associate with the notebook instance. For information about lifecycle configurations, see [Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) in the *Amazon SageMaker Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotebookInstanceName`  <a name="cfn-sagemaker-notebookinstance-notebookinstancename"></a>
The name of the new notebook instance.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlatformIdentifier`  <a name="cfn-sagemaker-notebookinstance-platformidentifier"></a>
The platform identifier of the notebook instance runtime environment. The default value is `notebook-al2023-v1`.
*Required*: No
*Type*: String
*Pattern*: `(notebook-al1-v1|notebook-al2-v1|notebook-al2-v2|notebook-al2-v3|notebook-al2023-v1)`
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-notebookinstance-rolearn"></a>
 When you send any requests to AWS resources from the notebook instance, SageMaker AI assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so SageMaker AI can perform these tasks. The policy must allow the SageMaker AI service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to SageMaker AI, the caller of this API must have the `iam:PassRole` permission.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RootAccess`  <a name="cfn-sagemaker-notebookinstance-rootaccess"></a>
Whether root access is enabled or disabled for users of the notebook instance. The default value is `Enabled`.
Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-sagemaker-notebookinstance-securitygroupids"></a>
The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-sagemaker-notebookinstance-subnetid"></a>
The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.
*Required*: No
*Type*: String
*Pattern*: `[-0-9a-zA-Z]+`
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-notebookinstance-tags"></a>
A list of key-value pairs to apply to this resource.
For more information, see [Resource Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) and [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what).
You can add tags later by using the `CreateTags` API.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-notebookinstance-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeSizeInGB`  <a name="cfn-sagemaker-notebookinstance-volumesizeingb"></a>
The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.
Expect some interruption of service if this parameter is changed as CloudFormation stops a notebook instance and starts it up again to update it.
*Required*: No
*Type*: Integer
*Minimum*: `5`
*Maximum*: `16384`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-sagemaker-notebookinstance-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-notebookinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the notebook instance, such as `arn:aws:sagemaker:us-west-2:012345678901:notebook-instance/mynotebookinstance`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-notebookinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-notebookinstance-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The name of the notebook instance.

`NotebookInstanceName`  <a name="NotebookInstanceName-fn::getatt"></a>
The name of the notebook instance, such as `MyNotebookInstance`.

## Examples
<a name="aws-resource-sagemaker-notebookinstance--examples"></a>

### SageMaker Notebook Instance Example
<a name="aws-resource-sagemaker-notebookinstance--examples--SageMaker_Notebook_Instance_Example"></a>

The following example creates a notebook instance.

#### JSON
<a name="aws-resource-sagemaker-notebookinstance--examples--SageMaker_Notebook_Instance_Example--json"></a>

```
{
    "Description": "Create Basic Notebook",
    "Resources": {
        "BasicNotebookInstance": {
            "Type": "AWS::SageMaker::NotebookInstance",
            "Properties": {
                "InstanceType": "ml.t2.large",
                "RoleArn": {
                    "Fn::GetAtt": [
                        "ExecutionRole",
                        "Arn"
                    ]
                }
            }
        },
        "ExecutionRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "sagemaker.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
                    ]
                },
                "Path": "/",
                "ManagedPolicyArns": [
                    {
                        "Fn::Sub": "arn:${AWS::Partition}:iam::aws:policy/AmazonSageMakerFullAccess"
                    }
                ]
            }
        }
    },
    "Outputs": {
        "BasicNotebookInstanceId": {
            "Value": {
                "Ref": "BasicNotebookInstance"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-sagemaker-notebookinstance--examples--SageMaker_Notebook_Instance_Example--yaml"></a>

```
Description: "Create basic notebook instance"
Resources:
  BasicNotebookInstance:
    Type: "AWS::SageMaker::NotebookInstance"
    Properties:
      InstanceType: "ml.t2.large"
      RoleArn: !GetAtt ExecutionRole.Arn
  ExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "sagemaker.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      ManagedPolicyArns:
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AmazonSageMakerFullAccess"
Outputs:
  BasicNotebookInstanceId:
    Value: !Ref BasicNotebookInstance
```

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-infrastructureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration
<a name="aws-resource-imagebuilder-infrastructureconfiguration"></a>

Creates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.

## Syntax
<a name="aws-resource-imagebuilder-infrastructureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-infrastructureconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::InfrastructureConfiguration",
  "Properties" : {
      "[Description](#cfn-imagebuilder-infrastructureconfiguration-description)" : {{String}},
      "[InstanceMetadataOptions](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions)" : {{InstanceMetadataOptions}},
      "[InstanceProfileName](#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename)" : {{String}},
      "[InstanceTypes](#cfn-imagebuilder-infrastructureconfiguration-instancetypes)" : {{[ String, ... ]}},
      "[KeyPair](#cfn-imagebuilder-infrastructureconfiguration-keypair)" : {{String}},
      "[Logging](#cfn-imagebuilder-infrastructureconfiguration-logging)" : {{Logging}},
      "[Name](#cfn-imagebuilder-infrastructureconfiguration-name)" : {{String}},
      "[Placement](#cfn-imagebuilder-infrastructureconfiguration-placement)" : {{Placement}},
      "[ResourceTags](#cfn-imagebuilder-infrastructureconfiguration-resourcetags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[SecurityGroupIds](#cfn-imagebuilder-infrastructureconfiguration-securitygroupids)" : {{[ String, ... ]}},
      "[SnsTopicArn](#cfn-imagebuilder-infrastructureconfiguration-snstopicarn)" : {{String}},
      "[SubnetId](#cfn-imagebuilder-infrastructureconfiguration-subnetid)" : {{String}},
      "[Tags](#cfn-imagebuilder-infrastructureconfiguration-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TerminateInstanceOnFailure](#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-infrastructureconfiguration-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::InfrastructureConfiguration
Properties:
  [Description](#cfn-imagebuilder-infrastructureconfiguration-description): {{String}}
  [InstanceMetadataOptions](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions): {{
    InstanceMetadataOptions}}
  [InstanceProfileName](#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename): {{String}}
  [InstanceTypes](#cfn-imagebuilder-infrastructureconfiguration-instancetypes): {{
    - String}}
  [KeyPair](#cfn-imagebuilder-infrastructureconfiguration-keypair): {{String}}
  [Logging](#cfn-imagebuilder-infrastructureconfiguration-logging): {{
    Logging}}
  [Name](#cfn-imagebuilder-infrastructureconfiguration-name): {{String}}
  [Placement](#cfn-imagebuilder-infrastructureconfiguration-placement): {{
    Placement}}
  [ResourceTags](#cfn-imagebuilder-infrastructureconfiguration-resourcetags): {{
    {{Key}}: {{Value}}}}
  [SecurityGroupIds](#cfn-imagebuilder-infrastructureconfiguration-securitygroupids): {{
    - String}}
  [SnsTopicArn](#cfn-imagebuilder-infrastructureconfiguration-snstopicarn): {{String}}
  [SubnetId](#cfn-imagebuilder-infrastructureconfiguration-subnetid): {{String}}
  [Tags](#cfn-imagebuilder-infrastructureconfiguration-tags): {{
    {{Key}}: {{Value}}}}
  [TerminateInstanceOnFailure](#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure): {{Boolean}}
```

## Properties
<a name="aws-resource-imagebuilder-infrastructureconfiguration-properties"></a>

`Description`  <a name="cfn-imagebuilder-infrastructureconfiguration-description"></a>
The description of the infrastructure configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceMetadataOptions`  <a name="cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions"></a>
The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches during image creation. If you don't set these options, the EC2 launch defaults for the instance apply. For more information about instance metadata options, see one of the following links:
+ [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* * for Linux instances.
+ [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 Windows Guide* * for Windows instances.
*Required*: No
*Type*: [InstanceMetadataOptions](aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileName`  <a name="cfn-imagebuilder-infrastructureconfiguration-instanceprofilename"></a>
The instance profile to associate with the instance used to customize your Amazon EC2 AMI. The instance profile must exist in your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceTypes`  <a name="cfn-imagebuilder-infrastructureconfiguration-instancetypes"></a>
The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. Image Builder picks one of these instance types based on availability. If you don't specify instance types, Image Builder selects compatible instance types automatically. If you specify a Dedicated Host, Image Builder uses only instance types that the host supports.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPair`  <a name="cfn-imagebuilder-infrastructureconfiguration-keypair"></a>
The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-imagebuilder-infrastructureconfiguration-logging"></a>
The logging configuration of the infrastructure configuration. When you configure S3 logs, Image Builder writes logs from the build and test process to the specified bucket under the key prefix.
*Required*: No
*Type*: [Logging](aws-properties-imagebuilder-infrastructureconfiguration-logging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-infrastructureconfiguration-name"></a>
The name of the infrastructure configuration. Infrastructure configuration names must be unique to your account in each AWS Region. Image Builder generates the infrastructure configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Placement`  <a name="cfn-imagebuilder-infrastructureconfiguration-placement"></a>
The instance placement settings that define where the build and test instances that Image Builder launches during image creation run. These settings don't affect instances that you launch from the output image.
*Required*: No
*Type*: [Placement](aws-properties-imagebuilder-infrastructureconfiguration-placement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-imagebuilder-infrastructureconfiguration-resourcetags"></a>
The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs. Tag keys can't begin with `aws:` or match one of the following reserved keys: `CreatedBy`, `Ec2ImageBuilderArn`, `Name`, or `Tags`.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-imagebuilder-infrastructureconfiguration-securitygroupids"></a>
The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsTopicArn`  <a name="cfn-imagebuilder-infrastructureconfiguration-snstopicarn"></a>
The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications. Specify a standard topic. Image Builder doesn't support FIFO topics. Image Builder validates the topic when you create or update the configuration. You must have permission to publish to the topic.
EC2 Image Builder can't send notifications to SNS topics that are encrypted using keys from other accounts. If your SNS topic is encrypted, the key must be owned by the same account that owns your Image Builder resources.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:sns:[^:]+:[0-9]{12}:[a-zA-Z0-9-_]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-imagebuilder-infrastructureconfiguration-subnetid"></a>
The subnet ID in which to place the instance used to customize your Amazon EC2 AMI. If you specify `subnetId`, you must also specify one or more security group IDs in `securityGroupIds`. Otherwise, the request fails.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-imagebuilder-infrastructureconfiguration-tags"></a>
The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerminateInstanceOnFailure`  <a name="cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure"></a>
Specifies whether to terminate the instance on failure. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails. Defaults to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-imagebuilder-infrastructureconfiguration-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-infrastructureconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-infrastructureconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-infrastructureconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the infrastructure configuration. For example, `arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/myexampleinfrastructure`.

`Name`  <a name="Name-fn::getatt"></a>
The name of the infrastructure configuration.

## Examples
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples"></a>

**Topics**
+ [Create an infrastructure configuration](#aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration)
+ [Create an infrastructure configuration with placement and metadata options](#aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration_with_placement_and_metadata_options)

### Create an infrastructure configuration
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration"></a>

The following example shows the template for the InfrastructureConfiguration resource in both JSON and YAML format.

#### JSON
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration--json"></a>

```
{
	"Resources": {
		"InfrastructureConfigurationAll": {
			"Type": "AWS::ImageBuilder::InfrastructureConfiguration",
			"Properties": {
				"Name": "infrastructure-configuration-name",
				"InstanceProfileName": "instance-profile-name",
				"Description": "description",
				"InstanceTypes": [
					"m4.large",
					"m5.large"
				],
				"KeyPair": "key-pair",
				"Logging": {
					"S3Logs": {
						"S3BucketName": "imagebuilder-logging-bucket",
						"S3KeyPrefix": "imagebuilder-bucket-prefix"
					}
				},
				"SnsTopicArn": {
					"Ref": "SnsTopicArn"
				},
				"TerminateInstanceOnFailure": true,
				"SecurityGroupIds": [
					"security-group-id-1",
					"security-group-id-2"
				],
				"SubnetId": "subnet-id",
				"Tags": {
					"CustomerInfraConfigTagKey1": "CustomerInfraConfigTagValue1",
					"CustomerInfraConfigTagKey2": "CustomerInfraConfigTagValue2"
				}
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration--yaml"></a>

```
Resources:
  InfrastructureConfigurationAll:
    Type: 'AWS::ImageBuilder::InfrastructureConfiguration'
    Properties:
      Name: 'infrastructure-configuration-name'
      InstanceProfileName: 'instance-profile-name'
      Description: 'description'
      InstanceTypes:
        - 'm4.large'
        - 'm5.large'
      KeyPair: 'key-pair'
      Logging:
        S3Logs:
          S3BucketName: 'imagebuilder-logging-bucket'
          S3KeyPrefix: 'imagebuilder-bucket-prefix'
      SnsTopicArn: !Ref SnsTopicArn
      TerminateInstanceOnFailure: true
      SecurityGroupIds:
        - 'security-group-id-1'
        - 'security-group-id-2'
      SubnetId: 'subnet-id'
      Tags:
        CustomerInfraConfigTagKey1: 'CustomerInfraConfigTagValue1'
        CustomerInfraConfigTagKey2: 'CustomerInfraConfigTagValue2'
```

### Create an infrastructure configuration with placement and metadata options
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration_with_placement_and_metadata_options"></a>

The following example creates an infrastructure configuration that uses dedicated tenancy and requires Instance Metadata Service Version 2 (IMDSv2) tokens. The configuration also applies resource tags to the build instance.

#### YAML
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration_with_placement_and_metadata_options--yaml"></a>

```
Resources:
  InfraConfigAdvanced:
    Type: AWS::ImageBuilder::InfrastructureConfiguration
    Properties:
      Name: infra-config-advanced
      InstanceProfileName: !Ref ImageBuilderInstanceProfile
      InstanceTypes:
        - m5.large
        - m5.xlarge
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref BuildSecurityGroup
      Placement:
        Tenancy: dedicated
        AvailabilityZone: us-west-2a
      InstanceMetadataOptions:
        HttpTokens: required
        HttpPutResponseHopLimit: 2
      ResourceTags:
        CostCenter: imaging
        Environment: build
      TerminateInstanceOnFailure: true
      Logging:
        S3Logs:
          S3BucketName: !Ref LogBucket
          S3KeyPrefix: image-builder/logs
```

#### JSON
<a name="aws-resource-imagebuilder-infrastructureconfiguration--examples--Create_an_infrastructure_configuration_with_placement_and_metadata_options--json"></a>

```
{
    "Resources": {
        "InfraConfigAdvanced": {
            "Type": "AWS::ImageBuilder::InfrastructureConfiguration",
            "Properties": {
                "Name": "infra-config-advanced",
                "InstanceProfileName": {
                    "Ref": "ImageBuilderInstanceProfile"
                },
                "InstanceTypes": ["m5.large", "m5.xlarge"],
                "SubnetId": {
                    "Ref": "PrivateSubnet"
                },
                "SecurityGroupIds": [
                    {
                        "Ref": "BuildSecurityGroup"
                    }
                ],
                "Placement": {
                    "Tenancy": "dedicated",
                    "AvailabilityZone": "us-west-2a"
                },
                "InstanceMetadataOptions": {
                    "HttpTokens": "required",
                    "HttpPutResponseHopLimit": 2
                },
                "ResourceTags": {
                    "CostCenter": "imaging",
                    "Environment": "build"
                },
                "TerminateInstanceOnFailure": true,
                "Logging": {
                    "S3Logs": {
                        "S3BucketName": {
                            "Ref": "LogBucket"
                        },
                        "S3KeyPrefix": "image-builder/logs"
                    }
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-infrastructureconfiguration--seealso"></a>
+ [Manage infrastructure configurations](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-infra-config.html) in the *Image Builder User Guide*.

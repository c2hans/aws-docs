---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate
<a name="aws-resource-ec2-launchtemplate"></a>

Specifies the properties for creating a launch template.

The minimum required properties for specifying a launch template are as follows:
+ You must specify at least one property for the launch template data.
+ You can optionally specify a name for the launch template. If you do not specify a name, CloudFormation creates a name for you.

A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the `ImageId` property, which has no default value. If you do not specify an AMI ID for the launch template `ImageId` property, you must specify an AMI ID for the instance `ImageId` property.

For more information, see [Launch an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-resource-ec2-launchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-launchtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::LaunchTemplate",
  "Properties" : {
      "[LaunchTemplateData](#cfn-ec2-launchtemplate-launchtemplatedata)" : {{LaunchTemplateData}},
      "[LaunchTemplateName](#cfn-ec2-launchtemplate-launchtemplatename)" : {{String}},
      "[TagSpecifications](#cfn-ec2-launchtemplate-tagspecifications)" : {{[ LaunchTemplateTagSpecification, ... ]}},
      "[VersionDescription](#cfn-ec2-launchtemplate-versiondescription)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-launchtemplate-syntax.yaml"></a>

```
Type: AWS::EC2::LaunchTemplate
Properties:
  [LaunchTemplateData](#cfn-ec2-launchtemplate-launchtemplatedata): {{
    LaunchTemplateData}}
  [LaunchTemplateName](#cfn-ec2-launchtemplate-launchtemplatename): {{String}}
  [TagSpecifications](#cfn-ec2-launchtemplate-tagspecifications): {{
    - LaunchTemplateTagSpecification}}
  [VersionDescription](#cfn-ec2-launchtemplate-versiondescription): {{String}}
```

## Properties
<a name="aws-resource-ec2-launchtemplate-properties"></a>

`LaunchTemplateData`  <a name="cfn-ec2-launchtemplate-launchtemplatedata"></a>
The information for the launch template.
*Required*: Yes
*Type*: [LaunchTemplateData](aws-properties-ec2-launchtemplate-launchtemplatedata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplateName`  <a name="cfn-ec2-launchtemplate-launchtemplatename"></a>
A name for the launch template.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagSpecifications`  <a name="cfn-ec2-launchtemplate-tagspecifications"></a>
The tags to apply to the launch template on creation. To tag the launch template, the resource type must be `launch-template`.
To specify the tags for resources that are created during instance launch, use [TagSpecifications](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications).
*Required*: No
*Type*: Array of [LaunchTemplateTagSpecification](aws-properties-ec2-launchtemplate-launchtemplatetagspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionDescription`  <a name="cfn-ec2-launchtemplate-versiondescription"></a>
A description for the first version of the launch template.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-launchtemplate-return-values"></a>

### Ref
<a name="aws-resource-ec2-launchtemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the launch template, for example, `lt-01238c059e3466abc`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-launchtemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-launchtemplate-return-values-fn--getatt-fn--getatt"></a>

`DefaultVersionNumber`  <a name="DefaultVersionNumber-fn::getatt"></a>
The default version of the launch template, such as 2.
The default version of a launch template cannot be specified in AWS CloudFormation. The default version can be set in the Amazon EC2 console or by using the `modify-launch-template`AWS CLI command.

`LatestVersionNumber`  <a name="LatestVersionNumber-fn::getatt"></a>
The latest version of the launch template, such as `5`.

`LaunchTemplateId`  <a name="LaunchTemplateId-fn::getatt"></a>
The ID of the launch template.

## Examples
<a name="aws-resource-ec2-launchtemplate--examples"></a>

**Topics**
+ [Launch template with an IAM instance profile](#aws-resource-ec2-launchtemplate--examples--Launch_template_with_an_IAM_instance_profile)
+ [Launch template with a block device mapping](#aws-resource-ec2-launchtemplate--examples--Launch_template_with_a_block_device_mapping)
+ [Launch template with instance metadata options](#aws-resource-ec2-launchtemplate--examples--Launch_template_with_instance_metadata_options)
+ [Launch template with public IP addresses for Amazon EC2 Auto Scaling](#aws-resource-ec2-launchtemplate--examples--Launch_template_with_public_IP_addresses_for)

### Launch template with an IAM instance profile
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_an_IAM_instance_profile"></a>

The following example creates a launch template and an instance profile. The instance profile contains the IAM role named `MyAdminRole` and can provide the role's temporary credentials to an application that runs on the instances created by this launch template.

The launch template also prevents accidental instance termination when using the Amazon EC2 console, CLI, or API, by specifying `true` for the `DisableApiTermination` property. If the instances created by this launch template are launched in a default VPC, they receive a public IP address by default. If the instances are launched in a nondefault VPC, they do not receive a public IP address by default.

To see another example that uses an IAM role, user data, and tags for the instances and volumes launched by that launch template, see [Create launch templates with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2-launch-templates.html).

#### JSON
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_an_IAM_instance_profile--json"></a>

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources":{
    "MyIamInstanceProfile":{
      "Type":"AWS::IAM::InstanceProfile",
      "Properties":{
        "InstanceProfileName":"MyIamInstanceProfile",
        "Path":"/",
        "Roles":["MyAdminRole"]
      }
    },
    "MyLaunchTemplate":{
      "Type":"AWS::EC2::LaunchTemplate",
      "Properties":{
        "LaunchTemplateName":"MyLaunchTemplate",
        "LaunchTemplateData":{
          "IamInstanceProfile":{
          "Arn":{"Fn::GetAtt": ["MyIamInstanceProfile", "Arn"]}
          },
          "DisableApiTermination":"true",
          "ImageId":"ami-04d5cc9b88example",
          "InstanceType":"t2.micro",
          "KeyName":"MyKeyPair",
          "SecurityGroupIds":[
            "sg-083cd3bfb8example"
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_an_IAM_instance_profile--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyIamInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: MyIamInstanceProfile
      Path: "/"
      Roles:
      - MyAdminRole
  MyLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: MyLaunchTemplate
      LaunchTemplateData:
        IamInstanceProfile:
          Arn: !GetAtt
            - MyIamInstanceProfile
            - Arn
        DisableApiTermination: true
        ImageId: ami-04d5cc9b88example
        InstanceType: t2.micro
        KeyName: MyKeyPair
        SecurityGroupIds:
          - sg-083cd3bfb8example
```

### Launch template with a block device mapping
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_a_block_device_mapping"></a>

The following example creates a launch template with a block device mapping: an encrypted 22 gigabyte EBS volume mapped to /dev/xvdcz. The /dev/xvdcz volume uses the General Purpose SSD (gp2) volume type and is deleted when terminating the instance it is attached to. This example uses the Fn::Sub function to customize the name of the launch template to include the stack name.

The launch template also provisions T2 instances in unlimited mode by specifying a value of `unlimited` for the `CPUCredits` property. Because `Monitoring` is enabled, EC2 metric data will be available at 1-minute intervals (known as detailed monitoring) through CloudWatch.

#### JSON
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_a_block_device_mapping--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources":{
    "myLaunchTemplate":{
      "Type":"AWS::EC2::LaunchTemplate",
      "Properties":{
        "LaunchTemplateName":{"Fn::Sub":"${AWS::StackName}-launch-template"},
        "LaunchTemplateData":{
          "BlockDeviceMappings":[{
            "Ebs":{
              "VolumeSize":"22",
              "VolumeType":"gp2",
              "DeleteOnTermination": true,
              "Encrypted": true
            },
            "DeviceName":"/dev/xvdcz"
          }],
          "CreditSpecification":{
            "CpuCredits":"unlimited"
          },
          "Monitoring":{"Enabled":true},
          "ImageId":"ami-04d5cc9b88example",
          "InstanceType":"t2.micro",
          "KeyName":"MyKeyPair",
          "SecurityGroupIds":["sg-7c2270198example", "sg-903004f88example"]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_a_block_device_mapping--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
      LaunchTemplateData:
        BlockDeviceMappings:
          - Ebs:
              VolumeSize: 22
              VolumeType: gp2
              DeleteOnTermination: true
              Encrypted: true
            DeviceName: /dev/xvdcz
        CreditSpecification:
          CpuCredits: Unlimited
        Monitoring:
          Enabled: true
        ImageId: ami-04d5cc9b88example
        InstanceType: t2.micro
        KeyName: MyKeyPair
        SecurityGroupIds:
          - sg-7c2270198example
          - sg-903004f88example
```

### Launch template with instance metadata options
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_instance_metadata_options"></a>

The following example creates a launch template with instance metadata options. The option to allow access to the instance tags through instance metadata is enabled.

#### JSON
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_instance_metadata_options--json"></a>

```
{
    "Resources": {
        "myLaunchTemplate": {
            "Type": "AWS::EC2::LaunchTemplate",
            "Properties": {
                "LaunchTemplateData": {
                    "ImageId": "ami-0a70b9d193ae8a799",
                    "InstanceType": "t2.micro",
                    "MetadataOptions": {
                        "InstanceMetadataTags": "enabled"
                    },
                    "SecurityGroupIds": [
                        "sg-12a4c434"
                    ],
                    "TagSpecifications": [
                        {
                            "ResourceType": "instance",
                            "Tags": [
                                {
                                    "Key": "department",
                                    "Value": "dev"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_instance_metadata_options--yaml"></a>

```
Resources:
   myLaunchTemplate:
     Type: 'AWS::EC2::LaunchTemplate'
     Properties:
       LaunchTemplateData:
          ImageId: ami-0a70b9d193ae8a799
          InstanceType: t2.micro
          MetadataOptions:
            InstanceMetadataTags: enabled
          SecurityGroupIds:
            - sg-12a4c434
          TagSpecifications:
            - ResourceType: instance
              Tags:
              - Key: department
                Value: dev
```

### Launch template with public IP addresses for Amazon EC2 Auto Scaling
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_public_IP_addresses_for"></a>

The following example creates and configures a launch template to assign public IP addresses to instances launched in a nondefault VPC. Note that when you specify a network interface for Amazon EC2 Auto Scaling, specify the VPC subnets as properties of the Auto Scaling group, and not in the launch template (because they will be ignored).

This example launch template also sets the instance placement tenancy to `dedicated`.

For more information about creating launch templates for Amazon EC2 Auto Scaling, see [Creating a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*.

#### JSON
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_public_IP_addresses_for--json"></a>

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources":{
    "myLaunchTemplate":{
      "Type":"AWS::EC2::LaunchTemplate",
      "Properties":{
        "LaunchTemplateName":{
          "Fn::Sub":"${AWS::StackName}-launch-template-for-auto-scaling"
        },
        "LaunchTemplateData":{
          "NetworkInterfaces":[
            {
              "DeviceIndex":0,
              "AssociatePublicIpAddress":true,
              "Groups":[
                "sg-7c2270198example",
                "sg-903004f88example"
              ],
              "DeleteOnTermination":true
            }
          ],
          "Placement":{
            "Tenancy": "dedicated"
          },
          "ImageId":"ami-04d5cc9b88example",
          "InstanceType":"t2.micro",
          "KeyName":"MyKeyPair"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-ec2-launchtemplate--examples--Launch_template_with_public_IP_addresses_for--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myLaunchTemplate:
    Type: 'AWS::EC2::LaunchTemplate'
    Properties:
      LaunchTemplateName: !Sub '${AWS::StackName}-launch-template-for-auto-scaling'
      LaunchTemplateData:
        NetworkInterfaces:
          - DeviceIndex: 0
            AssociatePublicIpAddress: true
            Groups:
              - sg-7c2270198example
              - sg-903004f88example
            DeleteOnTermination: true
        Placement:
          Tenancy: dedicated
        ImageId: ami-04d5cc9b88example
        InstanceType: t2.micro
        KeyName: MyKeyPair
```

## See also
<a name="aws-resource-ec2-launchtemplate--seealso"></a>
+ [ CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) in the *Amazon EC2 API Reference*

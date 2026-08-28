---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-accesspoint-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessPoint VpcConfiguration
<a name="aws-properties-s3-accesspoint-vpcconfiguration"></a>

The Virtual Private Cloud (VPC) configuration for this access point.

## Syntax
<a name="aws-properties-s3-accesspoint-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-accesspoint-vpcconfiguration-syntax.json"></a>

```
{
  "[VpcId](#cfn-s3-accesspoint-vpcconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-accesspoint-vpcconfiguration-syntax.yaml"></a>

```
  [VpcId](#cfn-s3-accesspoint-vpcconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-s3-accesspoint-vpcconfiguration-properties"></a>

`VpcId`  <a name="cfn-s3-accesspoint-vpcconfiguration-vpcid"></a>
If this field is specified, the access point will only allow connections from the specified VPC ID.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-s3-accesspoint-vpcconfiguration--examples"></a>

### Create an S3 Access Point restricted to a VPC
<a name="aws-properties-s3-accesspoint-vpcconfiguration--examples--Create_an_S3_Access_Point_restricted_to_a_VPC"></a>

The following example creates an Amazon S3 access point restricted to a virtual private cloud (VPC). For more information, see [Configuring IAM policies for using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html) in the *Amazon S3 User Guide*.

#### JSON
<a name="aws-properties-s3-accesspoint-vpcconfiguration--examples--Create_an_S3_Access_Point_restricted_to_a_VPC--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket"
        },
        "S3BucketPolicy": {
            "Type": "AWS::S3::BucketPolicy",
            "Properties": {
                "Bucket": {
                    "Ref": "S3Bucket"
                },
                "PolicyDocument": {
                    "Version": "2012-10-17"		 	 	 ,
                    "Statement": [
                        {
                            "Action": "*",
                            "Effect": "Allow",
                            "Resource": [
                                {
                                    "Fn::GetAtt": [
                                        "S3Bucket",
                                        "Arn"
                                    ]
                                },
                                {
                                    "Fn::Join": [
                                        "",
                                        [
                                            {
                                                "Fn::GetAtt": [
                                                    "S3Bucket",
                                                    "Arn"
                                                ]
                                            },
                                            "/*"
                                        ]
                                    ]
                                }
                            ],
                            "Principal": {
                                "AWS": "*"
                            },
                            "Condition": {
                                "StringEquals": {
                                    "s3:DataAccessPointAccount": {
                                        "Ref": "AWS::AccountId"
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "VPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16"
            }
        },
        "S3AccessPoint": {
            "Type": "AWS::S3::AccessPoint",
            "Properties": {
                "Bucket": {
                    "Ref": "S3Bucket"
                },
                "Name": "my-access-point",
                "VpcConfiguration": {
                    "VpcId": {
                        "Ref": "VPC"
                    }
                },
                "PublicAccessBlockConfiguration": {
                    "BlockPublicAcls": true,
                    "IgnorePublicAcls": true,
                    "BlockPublicPolicy": true,
                    "RestrictPublicBuckets": true
                }
            }
        }
    },
    "Outputs": {
        "S3AccessPointArn": {
            "Value": {
                "Ref": "S3AccessPoint"
            },
            "Description": "ARN of the sample Amazon S3 access point."
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-accesspoint-vpcconfiguration--examples--Create_an_S3_Access_Point_restricted_to_a_VPC--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
  S3BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket:
        Ref: S3Bucket
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Action: "*"
            Effect: Allow
            Resource:
              - Fn::GetAtt:
                  - S3Bucket
                  - Arn
              - Fn::Join:
                  - ""
                  - - Fn::GetAtt:
                        - S3Bucket
                        - Arn
                    - /*
            Principal:
              AWS: "*"
            Condition:
              StringEquals:
                s3:DataAccessPointAccount:
                  Ref: AWS::AccountId
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  S3AccessPoint:
    Type: AWS::S3::AccessPoint
    Properties:
      Bucket:
        Ref: S3Bucket
      Name: my-access-point
      VpcConfiguration:
        VpcId:
          Ref: VPC
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        IgnorePublicAcls: true
        BlockPublicPolicy: true
        RestrictPublicBuckets: true
Outputs:
  S3AccessPointArn:
    Value:
      Ref: S3AccessPoint
    Description: ARN of the sample Amazon S3 access point.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution
<a name="aws-resource-cloudfront-distribution"></a>

A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.

## Syntax
<a name="aws-resource-cloudfront-distribution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-distribution-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::Distribution",
  "Properties" : {
      "[DistributionConfig](#cfn-cloudfront-distribution-distributionconfig)" : {{DistributionConfig}},
      "[Tags](#cfn-cloudfront-distribution-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-distribution-syntax.yaml"></a>

```
Type: AWS::CloudFront::Distribution
Properties:
  [DistributionConfig](#cfn-cloudfront-distribution-distributionconfig): {{
    DistributionConfig}}
  [Tags](#cfn-cloudfront-distribution-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-distribution-properties"></a>

`DistributionConfig`  <a name="cfn-cloudfront-distribution-distributionconfig"></a>
The distribution's configuration.
*Required*: Yes
*Type*: [DistributionConfig](aws-properties-cloudfront-distribution-distributionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudfront-distribution-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-distribution-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-distribution-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-distribution-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the CloudFront distribution ID. For example: `E27LVI50CSW06W`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudfront-distribution-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-distribution-return-values-fn--getatt-fn--getatt"></a>

`DomainName`  <a name="DomainName-fn::getatt"></a>
The domain name of the resource, such as `d111111abcdef8.cloudfront.net`.

`Id`  <a name="Id-fn::getatt"></a>
The distribution's identifier. For example: `E1U5RQF7T870K0`.

## Examples
<a name="aws-resource-cloudfront-distribution--examples"></a>

**Topics**
+ [Create a standard distribution](#aws-resource-cloudfront-distribution--examples--Create_a_standard_distribution)
+ [Create a multi-tenant distribution without a certificate](#aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_without_a_certificate)
+ [Create a multi-tenant distribution with a wildcard certificate](#aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_with_a_wildcard_certificate)

### Create a standard distribution
<a name="aws-resource-cloudfront-distribution--examples--Create_a_standard_distribution"></a>

The following example specifies a standard distribution and assigns it a single tag.

#### JSON
<a name="aws-resource-cloudfront-distribution--examples--Create_a_standard_distribution--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "cloudfrontdistribution": {
            "Type": "AWS::CloudFront::Distribution",
            "Properties": {
                "DistributionConfig": {
                    "CacheBehaviors": [
                        {
                            "LambdaFunctionAssociations": [
                                {
                                    "EventType": "string-value",
                                    "LambdaFunctionARN": "string-value"
                                }
                            ]
                        }
                    ],
                    "DefaultCacheBehavior": {
                        "LambdaFunctionAssociations": [
                            {
                                "EventType": "string-value",
                                "LambdaFunctionARN": "string-value"
                            }
                        ]
                    },
                    "IPV6Enabled": "boolean-value",
                    "Origins": [
                        {
                            "CustomOriginConfig": {
                                "OriginKeepaliveTimeout": "integer-value",
                                "OriginReadTimeout": "integer-value"
                            }
                        }
                    ]
                },
                "Tags": [
                    {
                        "Key": "string-value",
                        "Value": "string-value"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudfront-distribution--examples--Create_a_standard_distribution--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  cloudfrontdistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: string-value
                LambdaFunctionARN: string-value
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: string-value
              LambdaFunctionARN: string-value
        IPV6Enabled: boolean-value
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: integer-value
              OriginReadTimeout: integer-value
      Tags:
        - Key: string-value
          Value: string-value
```

### Create a multi-tenant distribution without a certificate
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_without_a_certificate"></a>

The following example specifies a basic multi-tenant distribution without a certificate.

#### JSON
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_without_a_certificate--json"></a>

```
{
  "Resources": {
    "MyMultiTenantDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "ConnectionMode": "tenant-only",
          "TenantConfig": {
            "ParameterDefinitions": [
              {
                "Name": "tenantName",
                "Definition": {
                  "StringSchema": {
                    "Comment": "Tenant name",
                    "DefaultValue": "root",
                    "Required": false
                  }
                }
              }
            ]
          },
          "DefaultCacheBehavior": {
            "TargetOriginId": "MyBucket.Arn",
            "ViewerProtocolPolicy": "allow-all",
            "AllowedMethods": [
              "GET",
              "HEAD"
            ],
            "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6"
          },
          "Enabled": true,
          "Origins": [
            {
              "DomainName": "MyBucket.RegionalDomainName",
              "Id": "MyBucket.Arn",
              "OriginPath": "/{{tenantName}}",
              "S3OriginConfig": {
                "OriginAccessIdentity": ""
              }
            }
          ]
        }
      }
    },
    "MyBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket",
        "BucketEncryption": {
          "ServerSideEncryptionConfiguration": [
            {
              "ServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "alias/aws/s3"
              }
            }
          ]
        },
        "PublicAccessBlockConfiguration": {
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": true
        }
      }
    },
    "MyBucketBucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": "MyBucket",
        "PolicyDocument": {
          "Id": "RequireEncryptionInTransit",
          "Version": "2012-10-17",
          "Statement": [
            {
              "Principal": "*",
              "Action": "*",
              "Effect": "Deny",
              "Resource": [
                "MyBucket.Arn",
                "${MyBucket.Arn}/*"
              ],
              "Condition": {
                "Bool": {
                  "aws:SecureTransport": "false"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_without_a_certificate--yaml"></a>

```
Resources:
  MyMultiTenantDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        ConnectionMode: tenant-only
        TenantConfig:
          ParameterDefinitions:
            - Name: tenantName
              Definition:
                StringSchema:
                  Comment: "Tenant name"
                  DefaultValue: "root"
                  Required: false
        DefaultCacheBehavior:
          TargetOriginId: !GetAtt MyBucket.Arn
          ViewerProtocolPolicy: allow-all
          AllowedMethods:
            - GET
            - HEAD
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6 # CachingOptimized PolicyId
        Enabled: true
        Origins:
          - DomainName: !GetAtt MyBucket.RegionalDomainName
            Id: !GetAtt MyBucket.Arn
            OriginPath: "/{{tenantName}}"
            S3OriginConfig:
              OriginAccessIdentity: ""

  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
              KMSMasterKeyID: alias/aws/s3
      PublicAccessBlockConfiguration:
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
  MyBucketBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref MyBucket
      PolicyDocument:
        Id: RequireEncryptionInTransit
        Version: '2012-10-17		 	 	 '
        Statement:
          - Principal: '*'
            Action: '*'
            Effect: Deny
            Resource:
              - !GetAtt MyBucket.Arn
              - !Sub ${MyBucket.Arn}/*
            Condition:
              Bool:
                aws:SecureTransport: 'false'
```

### Create a multi-tenant distribution with a wildcard certificate
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_with_a_wildcard_certificate"></a>

The following example specifies a basic multi-tenant distribution with a wildcard certificate.

#### JSON
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_with_a_wildcard_certificate--json"></a>

```
{
  "Resources": {
    "MyMultiTenantDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "ConnectionMode": "tenant-only",
          "ViewerCertificate": {
            "AcmCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/1954f095-11b6-4daf-9952-0c308a00944d",
            "SslSupportMethod": "sni-only"
          },
          "TenantConfig": {
            "ParameterDefinitions": [
              {
                "Name": "tenantName",
                "Definition": {
                  "StringSchema": {
                    "Comment": "Tenant name",
                    "DefaultValue": "root",
                    "Required": false
                  }
                }
              }
            ]
          },
          "DefaultCacheBehavior": {
            "TargetOriginId": "MyBucket.Arn",
            "ViewerProtocolPolicy": "allow-all",
            "AllowedMethods": [
              "GET",
              "HEAD"
            ],
            "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6"
          },
          "Enabled": true,
          "Origins": [
            {
              "DomainName": "MyBucket.RegionalDomainName",
              "Id": "MyBucket.Arn",
              "OriginPath": "/{{tenantName}}",
              "S3OriginConfig": {
                "OriginAccessIdentity": ""
              }
            }
          ]
        }
      }
    },
    "MyBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "amzn-s3-demo-bucket",
        "BucketEncryption": {
          "ServerSideEncryptionConfiguration": [
            {
              "ServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "alias/aws/s3"
              }
            }
          ]
        },
        "PublicAccessBlockConfiguration": {
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": true
        }
      }
    },
    "MyBucketBucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": "MyBucket",
        "PolicyDocument": {
          "Id": "RequireEncryptionInTransit",
          "Version": "2012-10-17",
          "Statement": [
            {
              "Principal": "*",
              "Action": "*",
              "Effect": "Deny",
              "Resource": [
                "MyBucket.Arn",
                "${MyBucket.Arn}/*"
              ],
              "Condition": {
                "Bool": {
                  "aws:SecureTransport": "false"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distribution--examples--Create_a_multi-tenant_distribution_with_a_wildcard_certificate--yaml"></a>

```
Resources:
  MyMultiTenantDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        ConnectionMode: tenant-only
        ViewerCertificate:
          AcmCertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/1954f095-11b6-4daf-9952-0c308a00944d
          SslSupportMethod: sni-only
        TenantConfig:
          ParameterDefinitions:
            - Name: tenantName
              Definition:
                StringSchema:
                  Comment: "Tenant name"
                  DefaultValue: "root"
                  Required: false
        DefaultCacheBehavior:
          TargetOriginId: !GetAtt MyBucket.Arn
          ViewerProtocolPolicy: allow-all
          AllowedMethods:
            - GET
            - HEAD
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6 # CachingOptimized PolicyId
        Enabled: true
        Origins:
          - DomainName: !GetAtt MyBucket.RegionalDomainName
            Id: !GetAtt MyBucket.Arn
            OriginPath: "/{{tenantName}}"
            S3OriginConfig:
              OriginAccessIdentity: ""

  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
              KMSMasterKeyID: alias/aws/s3
      PublicAccessBlockConfiguration:
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
  MyBucketBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref MyBucket
      PolicyDocument:
        Id: RequireEncryptionInTransit
        Version: '2012-10-17		 	 	 '
        Statement:
          - Principal: '*'
            Action: '*'
            Effect: Deny
            Resource:
              - !GetAtt MyBucket.Arn
              - !Sub ${MyBucket.Arn}/*
            Condition:
              Bool:
                aws:SecureTransport: 'false'
```

## See also
<a name="aws-resource-cloudfront-distribution--seealso"></a>
+ [CreateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html) in the *Amazon CloudFront API Reference*
+ [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html) in the *Amazon CloudFront Developer Guide*

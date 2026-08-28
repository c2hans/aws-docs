---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distributiontenant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant
<a name="aws-resource-cloudfront-distributiontenant"></a>

The distribution tenant.

## Syntax
<a name="aws-resource-cloudfront-distributiontenant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-distributiontenant-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::DistributionTenant",
  "Properties" : {
      "[ConnectionGroupId](#cfn-cloudfront-distributiontenant-connectiongroupid)" : {{String}},
      "[Customizations](#cfn-cloudfront-distributiontenant-customizations)" : {{Customizations}},
      "[DistributionId](#cfn-cloudfront-distributiontenant-distributionid)" : {{String}},
      "[Domains](#cfn-cloudfront-distributiontenant-domains)" : {{[ String, ... ]}},
      "[Enabled](#cfn-cloudfront-distributiontenant-enabled)" : {{Boolean}},
      "[ManagedCertificateRequest](#cfn-cloudfront-distributiontenant-managedcertificaterequest)" : {{ManagedCertificateRequest}},
      "[Name](#cfn-cloudfront-distributiontenant-name)" : {{String}},
      "[Parameters](#cfn-cloudfront-distributiontenant-parameters)" : {{[ Parameter, ... ]}},
      "[Tags](#cfn-cloudfront-distributiontenant-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-distributiontenant-syntax.yaml"></a>

```
Type: AWS::CloudFront::DistributionTenant
Properties:
  [ConnectionGroupId](#cfn-cloudfront-distributiontenant-connectiongroupid): {{String}}
  [Customizations](#cfn-cloudfront-distributiontenant-customizations): {{
    Customizations}}
  [DistributionId](#cfn-cloudfront-distributiontenant-distributionid): {{String}}
  [Domains](#cfn-cloudfront-distributiontenant-domains): {{
    - String}}
  [Enabled](#cfn-cloudfront-distributiontenant-enabled): {{Boolean}}
  [ManagedCertificateRequest](#cfn-cloudfront-distributiontenant-managedcertificaterequest): {{
    ManagedCertificateRequest}}
  [Name](#cfn-cloudfront-distributiontenant-name): {{String}}
  [Parameters](#cfn-cloudfront-distributiontenant-parameters): {{
    - Parameter}}
  [Tags](#cfn-cloudfront-distributiontenant-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-distributiontenant-properties"></a>

`ConnectionGroupId`  <a name="cfn-cloudfront-distributiontenant-connectiongroupid"></a>
The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Customizations`  <a name="cfn-cloudfront-distributiontenant-customizations"></a>
Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.
*Required*: No
*Type*: [Customizations](aws-properties-cloudfront-distributiontenant-customizations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DistributionId`  <a name="cfn-cloudfront-distributiontenant-distributionid"></a>
The ID of the multi-tenant distribution.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domains`  <a name="cfn-cloudfront-distributiontenant-domains"></a>
The domains associated with the distribution tenant.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-cloudfront-distributiontenant-enabled"></a>
Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedCertificateRequest`  <a name="cfn-cloudfront-distributiontenant-managedcertificaterequest"></a>
An object that represents the request for the Amazon CloudFront managed ACM certificate.
*Required*: No
*Type*: [ManagedCertificateRequest](aws-properties-cloudfront-distributiontenant-managedcertificaterequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-distributiontenant-name"></a>
The name of the distribution tenant.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-cloudfront-distributiontenant-parameters"></a>
A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.
*Required*: No
*Type*: Array of [Parameter](aws-properties-cloudfront-distributiontenant-parameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudfront-distributiontenant-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-distributiontenant-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-distributiontenant-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-distributiontenant-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-distributiontenant-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-distributiontenant-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the distribution tenant.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The date and time when the distribution tenant was created.

`DomainResults`  <a name="DomainResults-fn::getatt"></a>
Property description not available.

`ETag`  <a name="ETag-fn::getatt"></a>
The current version of the distribution tenant.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the distribution tenant.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time when the distribution tenant was updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the distribution tenant.

## Examples
<a name="aws-resource-cloudfront-distributiontenant--examples"></a>

**Topics**
+ [Create a distribution tenant that inherits its certificate](#aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_that_inherits_its_certificate)
+ [Create a distribution tenant with its own certificate](#aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_with_its_own_certificate)
+ [Create a CloudFront hosted distribution tenant](#aws-resource-cloudfront-distributiontenant--examples--Create_a_hosted_distribution_tenant)
+ [Create a self hosted distribution tenant](#aws-resource-cloudfront-distributiontenant--examples--Create_a_self_hosted_distribution_tenant)

### Create a distribution tenant that inherits its certificate
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_that_inherits_its_certificate"></a>

The following example specifies a distribution tenant that inherits its certificate from its parent multi-tenant distribution.

#### JSON
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_that_inherits_its_certificate--json"></a>

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
    },
    "MyDistributionTenant": {
      "Type": "AWS::CloudFront::DistributionTenant",
      "Properties": {
        "Domains": [
          "my-distribution-tenant.example.com"
        ],
        "DistributionId": "MyMultiTenantDistribution.Id",
        "Name": "MyDistributionTenant",
        "Enabled": true,
        "Parameters": [
          {
            "Name": "tenantName",
            "Value": "first-user"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_that_inherits_its_certificate--yaml"></a>

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

  MyDistributionTenant:
    Type: AWS::CloudFront::DistributionTenant
    Properties:
      Domains:
        - my-distribution-tenant.example.com
      DistributionId: !GetAtt MyMultiTenantDistribution.Id
      Name: MyDistributionTenant
      Enabled: true
      Parameters:
        - Name: tenantName
          Value: first-user
```

### Create a distribution tenant with its own certificate
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_with_its_own_certificate"></a>

The following example specifies a distribution tenant with its own certificate.

#### JSON
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_with_its_own_certificate--json"></a>

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
    },
    "MyDistributionTenant": {
      "Type": "AWS::CloudFront::DistributionTenant",
      "Properties": {
        "Domains": [
          "my-distribution-tenant.example.com"
        ],
        "DistributionId": "MyMultiTenantDistribution.Id",
        "Name": "MyDistributionTenant",
        "Enabled": true,
        "Parameters": [
          {
            "Name": "tenantName",
            "Value": "first-user"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_distribution_tenant_with_its_own_certificate--yaml"></a>

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

  MyDistributionTenant:
    Type: AWS::CloudFront::DistributionTenant
    Properties:
      Domains:
        - my-distribution-tenant.example.com
      DistributionId: !GetAtt MyMultiTenantDistribution.Id
      Name: MyDistributionTenant
      Enabled: true
      Customizations:
        Certificate:
          Arn: arn:aws:acm:us-east-1:123456789012:certificate/1954f095-11b6-4daf-9952-0c308a00944d
      Parameters:
        - Name: tenantName
          Value: first-user
```

### Create a CloudFront hosted distribution tenant
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_hosted_distribution_tenant"></a>

The following example specifies a CloudFront hosted distribution tenant.

#### JSON
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_hosted_distribution_tenant--json"></a>

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
    },
    "MyConnectionGroup": {
      "Type": "AWS::CloudFront::ConnectionGroup",
      "Properties": {
        "Name": "cf-hosted-connection-group-cfn"
      }
    },
    "RecordSet": {
      "Type": "AWS::Route53::RecordSet",
      "Properties": {
        "Name": "my-distribution-tenant.example.com",
        "Type": "CNAME",
        "HostedZoneId": "Z06559422OQIFCZO0EORK",
        "TTL": 300,
        "ResourceRecords": [
          "MyConnectionGroup.RoutingEndpoint"
        ]
      }
    },
    "MyDistributionTenant": {
      "Type": "AWS::CloudFront::DistributionTenant",
      "Properties": {
        "ConnectionGroupId": "MyConnectionGroup.Id",
        "Domains": [
          "my-distribution-tenant.example.com"
        ],
        "DistributionId": "MyMultiTenantDistribution.Id",
        "Name": "MyDistributionTenant",
        "Enabled": true,
        "ManagedCertificateRequest": {
          "ValidationTokenHost": "cloudfront"
        },
        "Parameters": [
          {
            "Name": "tenantName",
            "Value": "first-user"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_hosted_distribution_tenant--yaml"></a>

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

  MyConnectionGroup:
    Type: AWS::CloudFront::ConnectionGroup
    Properties:
      Name: cf-hosted-connection-group-cfn

  RecordSet:
    Type: AWS::Route53::RecordSet
    Properties:
      Name: my-distribution-tenant.example.com
      Type: CNAME
      HostedZoneId: Z06559422OQIFCZO0EORK
      TTL: 300
      ResourceRecords:
        - !GetAtt MyConnectionGroup.RoutingEndpoint

  MyDistributionTenant:
    Type: AWS::CloudFront::DistributionTenant
    Properties:
      ConnectionGroupId: !GetAtt MyConnectionGroup.Id
      Domains:
        - my-distribution-tenant.example.com
      DistributionId: !GetAtt MyMultiTenantDistribution.Id
      Name: MyDistributionTenant
      Enabled: true
      ManagedCertificateRequest:
        ValidationTokenHost: cloudfront
      Parameters:
        - Name: tenantName
          Value: first-user
```

### Create a self hosted distribution tenant
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_self_hosted_distribution_tenant"></a>

The following example specifies a self hosted distribution tenant.

**Important**
You must set up token validation for the distribution tenant when using this option. For more information, see [Request certificates for your CloudFront distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managed-cloudfront-certificates.html) in the *Amazon CloudFront Developer Guide*.

#### JSON
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_self_hosted_distribution_tenant--json"></a>

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
    },
    "MyConnectionGroup": {
      "Type": "AWS::CloudFront::ConnectionGroup",
      "Properties": {
        "Name": "cf-hosted-connection-group-cfn"
      }
    },
    "RecordSet": {
      "Type": "AWS::Route53::RecordSet",
      "Properties": {
        "Name": "my-distribution-tenant.example.com",
        "Type": "CNAME",
        "HostedZoneId": "Z06559422OQIFCZO0EORK",
        "TTL": 300,
        "ResourceRecords": [
          "MyConnectionGroup.RoutingEndpoint"
        ]
      }
    },
    "MyDistributionTenant": {
      "Type": "AWS::CloudFront::DistributionTenant",
      "Properties": {
        "ConnectionGroupId": "MyConnectionGroup.Id",
        "Domains": [
          "my-distribution-tenant.example.com"
        ],
        "DistributionId": "MyMultiTenantDistribution.Id",
        "Name": "MyDistributionTenant",
        "Enabled": true,
        "ManagedCertificateRequest": {
          "ValidationTokenHost": "self-hosted",
          "PrimaryDomainName": "my-distribution-tenant.example.com"
        },
        "Parameters": [
          {
            "Name": "tenantName",
            "Value": "first-user"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cloudfront-distributiontenant--examples--Create_a_self_hosted_distribution_tenant--yaml"></a>

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

  MyConnectionGroup:
    Type: AWS::CloudFront::ConnectionGroup
    Properties:
      Name: cf-hosted-connection-group-cfn

  RecordSet:
    Type: AWS::Route53::RecordSet
    Properties:
      Name: my-distribution-tenant.example.com
      Type: CNAME
      HostedZoneId: Z06559422OQIFCZO0EORK
      TTL: 300
      ResourceRecords:
        - !GetAtt MyConnectionGroup.RoutingEndpoint

  MyDistributionTenant:
    Type: AWS::CloudFront::DistributionTenant
    Properties:
      ConnectionGroupId: !GetAtt MyConnectionGroup.Id
      Domains:
        - my-distribution-tenant.example.com
      DistributionId: !GetAtt MyMultiTenantDistribution.Id
      Name: MyDistributionTenant
      Enabled: true
      ManagedCertificateRequest:
        ValidationTokenHost: self-hosted
        PrimaryDomainName: my-distribution-tenant.example.com
      Parameters:
        - Name: tenantName
          Value: first-user
```

## See also
<a name="aws-resource-cloudfront-distributiontenant--seealso"></a>
+ [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html) in the *Amazon CloudFront Developer Guide*
+ [Request certificates for your CloudFront distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managed-cloudfront-certificates.html) in the *Amazon CloudFront Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-analyzerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer AnalyzerConfiguration
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration"></a>

Contains information about the configuration of an analyzer for an AWS organization or account.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration-syntax.json"></a>

```
{
  "[InternalAccessConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration-internalaccessconfiguration)" : {{InternalAccessConfiguration}},
  "[UnusedAccessConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration-unusedaccessconfiguration)" : {{UnusedAccessConfiguration}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration-syntax.yaml"></a>

```
  [InternalAccessConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration-internalaccessconfiguration): {{
    InternalAccessConfiguration}}
  [UnusedAccessConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration-unusedaccessconfiguration): {{
    UnusedAccessConfiguration}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration-properties"></a>

`InternalAccessConfiguration`  <a name="cfn-accessanalyzer-analyzer-analyzerconfiguration-internalaccessconfiguration"></a>
Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates access within your AWS environment.
*Required*: No
*Type*: [InternalAccessConfiguration](aws-properties-accessanalyzer-analyzer-internalaccessconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UnusedAccessConfiguration`  <a name="cfn-accessanalyzer-analyzer-analyzerconfiguration-unusedaccessconfiguration"></a>
Specifies the configuration of an unused access analyzer for an AWS organization or account.
*Required*: No
*Type*: [UnusedAccessConfiguration](aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Examples
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration--examples"></a>

### Declare an AnalyzerConfiguration Resource
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration--examples--Declare_an_AnalyzerConfiguration_Resource"></a>

The following example shows how to declare a IAM Access Analyzer `AnalyzerConfiguration` resource:

#### JSON
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration--examples--Declare_an_AnalyzerConfiguration_Resource--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "Analyzer": {
      "Properties": {
        "AnalyzerName": "DevUnusedAccessAccountAnalyzer",
        "AnalyzerConfiguration": {
          "UnusedAccessConfiguration": {
            "UnusedAccessAge": 90,
            "AnalysisRule": {
              "Exclusions": [
                {
                  "ResourceTags": [
                    [
                      {
                        "Key": "Kind",
                        "Value": "Dev"
                      }
                    ],
                    [
                      {
                        "Key": "AnotherKey"
                      }
                    ]
                  ]
                }
              ]
            }
          }
        },
        "ArchiveRules": [
          {
            "Filter": [
              {
                "Eq": [
                  "123456789012"
                ],
                "Property": "resourceOwnerAccount"
              }
            ],
            "RuleName": "ArchiveTrustedAccountAccess"
          },
          {
            "Filter": [
              {
                "Contains": [
                  "arn:aws:s3:::amzn-s3-demo-logging-bucket",
                  "arn:aws:s3:::amzn-s3-demo-website-bucket"
                ],
                "Property": "resource"
              }
            ],
            "RuleName": "ArchivePublicS3BucketsAccess"
          }
        ],
        "Tags": [
          {
            "Key": "Kind",
            "Value": "Dev"
          }
        ],
        "Type": "ACCOUNT_UNUSED_ACCESS"
      },
      "Type": "AWS::AccessAnalyzer::Analyzer"
    }
  }
}
```

#### YAML
<a name="aws-properties-accessanalyzer-analyzer-analyzerconfiguration--examples--Declare_an_AnalyzerConfiguration_Resource--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  Analyzer:
    Properties:
      AnalyzerName: DevUnusedAccessAccountAnalyzer
      AnalyzerConfiguration:
        UnusedAccessConfiguration:
          UnusedAccessAge: 90
          AnalysisRule:
            Exclusions:
            - ResourceTags:
              - - Key: Kind
                  Value: Dev
              - - Key: AnotherKey
      ArchiveRules:
      - Filter:
        - Eq:
          - '123456789012'
          Property: resourceOwnerAccount
        RuleName: ArchiveTrustedAccountAccess
      - Filter:
        - Contains:
          - arn:aws:s3:::amzn-s3-demo-logging-bucket
          - arn:aws:s3:::amzn-s3-demo-website-bucket
          Property: resource
        RuleName: ArchivePublicS3BucketsAccess
      Tags:
      - Key: Kind
        Value: Dev
      Type: ACCOUNT_UNUSED_ACCESS
    Type: AWS::AccessAnalyzer::Analyzer
```

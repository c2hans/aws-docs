---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-accessanalyzer-analyzer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer
<a name="aws-resource-accessanalyzer-analyzer"></a>

The `AWS::AccessAnalyzer::Analyzer` resource specifies a new analyzer. The analyzer is an object that represents the IAM Access Analyzer feature. An analyzer is required for Access Analyzer to become operational.

## Syntax
<a name="aws-resource-accessanalyzer-analyzer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-accessanalyzer-analyzer-syntax.json"></a>

```
{
  "Type" : "AWS::AccessAnalyzer::Analyzer",
  "Properties" : {
      "[AnalyzerConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration)" : {{AnalyzerConfiguration}},
      "[AnalyzerName](#cfn-accessanalyzer-analyzer-analyzername)" : {{String}},
      "[ArchiveRules](#cfn-accessanalyzer-analyzer-archiverules)" : {{[ ArchiveRule, ... ]}},
      "[Tags](#cfn-accessanalyzer-analyzer-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-accessanalyzer-analyzer-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-accessanalyzer-analyzer-syntax.yaml"></a>

```
Type: AWS::AccessAnalyzer::Analyzer
Properties:
  [AnalyzerConfiguration](#cfn-accessanalyzer-analyzer-analyzerconfiguration): {{
    AnalyzerConfiguration}}
  [AnalyzerName](#cfn-accessanalyzer-analyzer-analyzername): {{String}}
  [ArchiveRules](#cfn-accessanalyzer-analyzer-archiverules): {{
    - ArchiveRule}}
  [Tags](#cfn-accessanalyzer-analyzer-tags): {{
    - Tag}}
  [Type](#cfn-accessanalyzer-analyzer-type): {{String}}
```

## Properties
<a name="aws-resource-accessanalyzer-analyzer-properties"></a>

`AnalyzerConfiguration`  <a name="cfn-accessanalyzer-analyzer-analyzerconfiguration"></a>
Contains information about the configuration of an analyzer for an AWS organization or account.
*Required*: No
*Type*: [AnalyzerConfiguration](aws-properties-accessanalyzer-analyzer-analyzerconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AnalyzerName`  <a name="cfn-accessanalyzer-analyzer-analyzername"></a>
The name of the analyzer.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ArchiveRules`  <a name="cfn-accessanalyzer-analyzer-archiverules"></a>
Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.
*Required*: No
*Type*: Array of [ArchiveRule](aws-properties-accessanalyzer-analyzer-archiverule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-accessanalyzer-analyzer-tags"></a>
An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.
For the tag value, you can specify a value that is 0 to 256 characters in length.
*Required*: No
*Type*: Array of [Tag](aws-properties-accessanalyzer-analyzer-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-accessanalyzer-analyzer-type"></a>
The type represents the zone of trust for the analyzer.
*Allowed Values*: ACCOUNT \| ORGANIZATION \| ACCOUNT\_UNUSED\_ACCESS \| ACCOUNT\_INTERNAL\_ACCESS \| ORGANIZATION\_INTERNAL\_ACCESS \| ORGANIZATION\_UNUSED\_ACCESS
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-accessanalyzer-analyzer-return-values"></a>

### Ref
<a name="aws-resource-accessanalyzer-analyzer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the analyzer created.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-accessanalyzer-analyzer-return-values-fn--getatt"></a>

####
<a name="aws-resource-accessanalyzer-analyzer-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the analyzer that was created.

## Examples
<a name="aws-resource-accessanalyzer-analyzer--examples"></a>

### Declare an Analyzer Resource
<a name="aws-resource-accessanalyzer-analyzer--examples--Declare_an_Analyzer_Resource"></a>

The following example shows how to declare a IAM Access Analyzer `Analyzer` resource:

#### JSON
<a name="aws-resource-accessanalyzer-analyzer--examples--Declare_an_Analyzer_Resource--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "Analyzer": {
      "Properties": {
        "AnalyzerName": "DevAccountAnalyzer",
        "ArchiveRules": [
          {
            "Filter": [
              {
                "Eq": [
                  "123456789012"
                ],
                "Property": "principal.AWS"
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
        "Type": "ACCOUNT"
      },
      "Type": "AWS::AccessAnalyzer::Analyzer"
    }
  }
}
```

#### YAML
<a name="aws-resource-accessanalyzer-analyzer--examples--Declare_an_Analyzer_Resource--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Analyzer:
    Type: 'AWS::AccessAnalyzer::Analyzer'
    Properties:
      AnalyzerName: MyAccountAnalyzer
      Type: ACCOUNT
      Tags:
        -
          Key: Kind
          Value: Dev
      ArchiveRules:
        -
          # Archive findings for a trusted AWS account
          RuleName: ArchiveTrustedAccountAccess
          Filter:
            -
              Property: 'principal.AWS'
              Eq:
                - '123456789012'
        -
          # Archive findings for known public S3 buckets
          RuleName: ArchivePublicS3BucketsAccess
          Filter:
            -
              Property: 'resource'
              Contains:
                - 'arn:aws:s3:::amzn-s3-demo-logging-bucket'
                - 'arn:aws:s3:::amzn-s3-demo-website-bucket'
```

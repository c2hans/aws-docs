---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securitylake-awslogsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::AwsLogSource
<a name="aws-resource-securitylake-awslogsource"></a>

Adds a natively supported AWS service as an AWS source. Enables source types for member accounts in required AWS Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an AWS service as a source, Security Lake starts collecting logs and events from it.

**Important**
If you want to create multiple sources using `AWS::SecurityLake::AwsLogSource`, you must use the `DependsOn` attribute to create the sources sequentially. With the `DependsOn` attribute you can specify that the creation of a specific `AWSLogSource`follows another. When you add a `DependsOn` attribute to a resource, that resource is created only after the creation of the resource specified in the `DependsOn` attribute. For an example, see [Add AWS log sources](https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#aws-resource-securitylake-awslogsource--examples).

## Syntax
<a name="aws-resource-securitylake-awslogsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securitylake-awslogsource-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityLake::AwsLogSource",
  "Properties" : {
      "[Accounts](#cfn-securitylake-awslogsource-accounts)" : {{[ String, ... ]}},
      "[DataLakeArn](#cfn-securitylake-awslogsource-datalakearn)" : {{String}},
      "[SourceName](#cfn-securitylake-awslogsource-sourcename)" : {{String}},
      "[SourceVersion](#cfn-securitylake-awslogsource-sourceversion)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securitylake-awslogsource-syntax.yaml"></a>

```
Type: AWS::SecurityLake::AwsLogSource
Properties:
  [Accounts](#cfn-securitylake-awslogsource-accounts): {{
    - String}}
  [DataLakeArn](#cfn-securitylake-awslogsource-datalakearn): {{String}}
  [SourceName](#cfn-securitylake-awslogsource-sourcename): {{String}}
  [SourceVersion](#cfn-securitylake-awslogsource-sourceversion): {{String}}
```

## Properties
<a name="aws-resource-securitylake-awslogsource-properties"></a>

`Accounts`  <a name="cfn-securitylake-awslogsource-accounts"></a>
Specify the AWS account information where you want to enable Security Lake.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLakeArn`  <a name="cfn-securitylake-awslogsource-datalakearn"></a>
The Amazon Resource Name (ARN) used to create the data lake.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceName`  <a name="cfn-securitylake-awslogsource-sourcename"></a>
The name for a AWS source. This must be a Regionally unique value. For the list of sources supported by Amazon Security Lake see [Collecting data from AWS services](https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html) in the Amazon Security Lake User Guide.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceVersion`  <a name="cfn-securitylake-awslogsource-sourceversion"></a>
The version for a AWS source. For more details about source versions supported by Amazon Security Lake see [OCSF source identification](https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification) in the Amazon Security Lake User Guide. This must be a Regionally unique value.
*Required*: Yes
*Type*: String
*Pattern*: `^(latest|[0-9]\.[0-9])$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securitylake-awslogsource-return-values"></a>

### Ref
<a name="aws-resource-securitylake-awslogsource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `ref` function, `ref` returns the `AwsLogSource` name. For example, `VPC_FLOW`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-securitylake-awslogsource--examples"></a>

### Add AWS log sources
<a name="aws-resource-securitylake-awslogsource--examples--Add_log_sources"></a>

After deploying Security Lake, use this example to add AWS log sources.

#### JSON
<a name="aws-resource-securitylake-awslogsource--examples--Add_log_sources--json"></a>

```
{
"AWSTemplateFormatVersion": "2010-09-09",
"Description": "Security Lake Already Deployed",
"Resources": {
    "SecurityLakeSourcesRoute53": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "ROUTE53",
            "SourceVersion": "2.0"
        }
    },
    "SecurityLakeSourcesSecurityHub": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "SH_FINDINGS",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesRoute53"
    },
    "SecurityLakeSourcesVPCFlow": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "VPC_FLOW",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesSecurityHub"
    },
    "SecurityLakeSourcesCloudTrailMgmt": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "CLOUD_TRAIL_MGMT",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesVPCFlow"
    },
    "SecurityLakeSourcesLambdaExecution": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "LAMBDA_EXECUTION",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesCloudTrailMgmt"
    },
    "SecurityLakeSourcesS3": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "S3_DATA",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesLambdaExecution"
    },
    "SecurityLakeSourcesEKSAudit": {
        "Type": "AWS::SecurityLake::AwsLogSource",
        "Properties": {
            "DataLakeArn": {
                "Fn::Sub": "arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default"
            },
            "SourceName": "EKS_AUDIT",
            "SourceVersion": "2.0"
        },
        "DependsOn": "SecurityLakeSourcesS3"
    }
}
}
```

#### YAML
<a name="aws-resource-securitylake-awslogsource--examples--Add_log_sources--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Security Lake Already Deployed
Resources:
  SecurityLakeSourcesRoute53:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: ROUTE53
      SourceVersion: "2.0"
  SecurityLakeSourcesSecurityHub:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: SH_FINDINGS
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesRoute53
  SecurityLakeSourcesVPCFlow:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: VPC_FLOW
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesSecurityHub
  SecurityLakeSourcesCloudTrailMgmt:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: CLOUD_TRAIL_MGMT
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesVPCFlow
  SecurityLakeSourcesLambdaExecution:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: LAMBDA_EXECUTION
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesCloudTrailMgmt
  SecurityLakeSourcesS3:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: S3_DATA
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesLambdaExecution
  SecurityLakeSourcesEKSAudit:
    Type: AWS::SecurityLake::AwsLogSource
    Properties:
      DataLakeArn: !Sub arn:aws:securitylake:${AWS::Partition}:${AWS::AccountId}:data-lake/default
      SourceName: EKS_AUDIT
      SourceVersion: "2.0"
    DependsOn: SecurityLakeSourcesS3
```

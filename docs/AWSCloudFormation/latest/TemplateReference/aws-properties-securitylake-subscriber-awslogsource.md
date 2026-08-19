---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscriber-awslogsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber AwsLogSource
<a name="aws-properties-securitylake-subscriber-awslogsource"></a>

Adds a natively supported AWS service as an Amazon Security Lake source. Enables source types for member accounts in required AWS Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an AWS service as a source, Security Lake starts collecting logs and events from it.

## Syntax
<a name="aws-properties-securitylake-subscriber-awslogsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscriber-awslogsource-syntax.json"></a>

```
{
  "[SourceName](#cfn-securitylake-subscriber-awslogsource-sourcename)" : {{String}},
  "[SourceVersion](#cfn-securitylake-subscriber-awslogsource-sourceversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-subscriber-awslogsource-syntax.yaml"></a>

```
  [SourceName](#cfn-securitylake-subscriber-awslogsource-sourcename): {{String}}
  [SourceVersion](#cfn-securitylake-subscriber-awslogsource-sourceversion): {{String}}
```

## Properties
<a name="aws-properties-securitylake-subscriber-awslogsource-properties"></a>

`SourceName`  <a name="cfn-securitylake-subscriber-awslogsource-sourcename"></a>
Source name of the natively supported AWS service that is supported as an Amazon Security Lake source. For the list of sources supported by Amazon Security Lake see [Collecting data from AWS services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the Amazon Security Lake User Guide.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceVersion`  <a name="cfn-securitylake-subscriber-awslogsource-sourceversion"></a>
Source version of the natively supported AWS service that is supported as an Amazon Security Lake source. For more details about source versions supported by Amazon Security Lake see [OCSF source identification](https://docs.aws.amazon.com/security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification) in the Amazon Security Lake User Guide.
*Required*: No
*Type*: String
*Pattern*: `^(latest|[0-9]\.[0-9])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

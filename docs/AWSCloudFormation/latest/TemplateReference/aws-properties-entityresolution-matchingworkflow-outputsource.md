---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-outputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow OutputSource
<a name="aws-properties-entityresolution-matchingworkflow-outputsource"></a>

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed`. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-outputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-outputsource-syntax.json"></a>

```
{
  "[ApplyNormalization](#cfn-entityresolution-matchingworkflow-outputsource-applynormalization)" : {{Boolean}},
  "[CustomerProfilesIntegrationConfig](#cfn-entityresolution-matchingworkflow-outputsource-customerprofilesintegrationconfig)" : {{CustomerProfilesIntegrationConfig}},
  "[KMSArn](#cfn-entityresolution-matchingworkflow-outputsource-kmsarn)" : {{String}},
  "[Output](#cfn-entityresolution-matchingworkflow-outputsource-output)" : {{[ OutputAttribute, ... ]}},
  "[OutputS3Path](#cfn-entityresolution-matchingworkflow-outputsource-outputs3path)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-outputsource-syntax.yaml"></a>

```
  [ApplyNormalization](#cfn-entityresolution-matchingworkflow-outputsource-applynormalization): {{Boolean}}
  [CustomerProfilesIntegrationConfig](#cfn-entityresolution-matchingworkflow-outputsource-customerprofilesintegrationconfig): {{
    CustomerProfilesIntegrationConfig}}
  [KMSArn](#cfn-entityresolution-matchingworkflow-outputsource-kmsarn): {{String}}
  [Output](#cfn-entityresolution-matchingworkflow-outputsource-output): {{
    - OutputAttribute}}
  [OutputS3Path](#cfn-entityresolution-matchingworkflow-outputsource-outputs3path): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-outputsource-properties"></a>

`ApplyNormalization`  <a name="cfn-entityresolution-matchingworkflow-outputsource-applynormalization"></a>
Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER`, and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerProfilesIntegrationConfig`  <a name="cfn-entityresolution-matchingworkflow-outputsource-customerprofilesintegrationconfig"></a>
Specifies the Customer Profiles integration configuration for sending matched output directly to Customer Profiles. When configured, AWS Entity Resolution automatically creates and updates customer profiles based on match clusters, eliminating the need for manual Amazon S3 integration setup.
*Required*: No
*Type*: [CustomerProfilesIntegrationConfig](aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSArn`  <a name="cfn-entityresolution-matchingworkflow-outputsource-kmsarn"></a>
Customer KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):kms:.*:[0-9]+:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-entityresolution-matchingworkflow-outputsource-output"></a>
A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed`. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.
*Required*: Yes
*Type*: Array of [OutputAttribute](aws-properties-entityresolution-matchingworkflow-outputattribute.md)
*Minimum*: `0`
*Maximum*: `750`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputS3Path`  <a name="cfn-entityresolution-matchingworkflow-outputsource-outputs3path"></a>
The S3 path to which AWS Entity Resolution will write the output table.
*Required*: No
*Type*: String
*Pattern*: `^s3://([^/]+)/?(.*?([^/]+)/?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

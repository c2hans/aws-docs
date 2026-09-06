---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-intermediatetable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable
<a name="aws-resource-cleanrooms-intermediatetable"></a>

Contains the details of an intermediate table in AWS Clean Rooms. An intermediate table stores a query definition and its materialized results within a collaboration.

## Syntax
<a name="aws-resource-cleanrooms-intermediatetable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-intermediatetable-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::IntermediateTable",
  "Properties" : {
      "[AnalysisRules](#cfn-cleanrooms-intermediatetable-analysisrules)" : {{[ IntermediateTableAnalysisRule, ... ]}},
      "[Description](#cfn-cleanrooms-intermediatetable-description)" : {{String}},
      "[KmsKeyArn](#cfn-cleanrooms-intermediatetable-kmskeyarn)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanrooms-intermediatetable-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanrooms-intermediatetable-name)" : {{String}},
      "[PopulationAnalysisConfiguration](#cfn-cleanrooms-intermediatetable-populationanalysisconfiguration)" : {{PopulationAnalysisConfiguration}},
      "[Tags](#cfn-cleanrooms-intermediatetable-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-intermediatetable-syntax.yaml"></a>

```
Type: AWS::CleanRooms::IntermediateTable
Properties:
  [AnalysisRules](#cfn-cleanrooms-intermediatetable-analysisrules): {{
    - IntermediateTableAnalysisRule}}
  [Description](#cfn-cleanrooms-intermediatetable-description): {{String}}
  [KmsKeyArn](#cfn-cleanrooms-intermediatetable-kmskeyarn): {{String}}
  [MembershipIdentifier](#cfn-cleanrooms-intermediatetable-membershipidentifier): {{String}}
  [Name](#cfn-cleanrooms-intermediatetable-name): {{String}}
  [PopulationAnalysisConfiguration](#cfn-cleanrooms-intermediatetable-populationanalysisconfiguration): {{
    PopulationAnalysisConfiguration}}
  [Tags](#cfn-cleanrooms-intermediatetable-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-intermediatetable-properties"></a>

`AnalysisRules`  <a name="cfn-cleanrooms-intermediatetable-analysisrules"></a>
Property description not available.
*Required*: No
*Type*: Array of [IntermediateTableAnalysisRule](aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cleanrooms-intermediatetable-description"></a>
The description of the intermediate table.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-cleanrooms-intermediatetable-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the intermediate table data.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MembershipIdentifier`  <a name="cfn-cleanrooms-intermediatetable-membershipidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-intermediatetable-name"></a>
The name of the intermediate table.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PopulationAnalysisConfiguration`  <a name="cfn-cleanrooms-intermediatetable-populationanalysisconfiguration"></a>
The analysis configuration that defines the query used to populate the intermediate table.
*Required*: Yes
*Type*: [PopulationAnalysisConfiguration](aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanrooms-intermediatetable-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-intermediatetable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-intermediatetable-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-intermediatetable-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cleanrooms-intermediatetable-return-values-fn--getatt"></a>

####
<a name="aws-resource-cleanrooms-intermediatetable-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the intermediate table.

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the collaboration that contains the intermediate table.

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
Property description not available.

`IntermediateTableIdentifier`  <a name="IntermediateTableIdentifier-fn::getatt"></a>
The unique identifier of the intermediate table associated with this analysis rule.

`MembershipArn`  <a name="MembershipArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the membership that contains the intermediate table.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the intermediate table.

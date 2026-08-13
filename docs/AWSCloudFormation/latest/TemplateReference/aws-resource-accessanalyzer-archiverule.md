---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-accessanalyzer-archiverule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::ArchiveRule
<a name="aws-resource-accessanalyzer-archiverule"></a>

Creates an archive rule.

## Syntax
<a name="aws-resource-accessanalyzer-archiverule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-accessanalyzer-archiverule-syntax.json"></a>

```
{
  "Type" : "AWS::AccessAnalyzer::ArchiveRule",
  "Properties" : {
      "[AnalyzerName](#cfn-accessanalyzer-archiverule-analyzername)" : {{String}},
      "[Filter](#cfn-accessanalyzer-archiverule-filter)" : {{{{{Key}}: {{Value}}, ...}}},
      "[RuleName](#cfn-accessanalyzer-archiverule-rulename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-accessanalyzer-archiverule-syntax.yaml"></a>

```
Type: AWS::AccessAnalyzer::ArchiveRule
Properties:
  [AnalyzerName](#cfn-accessanalyzer-archiverule-analyzername): {{String}}
  [Filter](#cfn-accessanalyzer-archiverule-filter): {{
    {{Key}}: {{Value}}}}
  [RuleName](#cfn-accessanalyzer-archiverule-rulename): {{String}}
```

## Properties
<a name="aws-resource-accessanalyzer-archiverule-properties"></a>

`AnalyzerName`  <a name="cfn-accessanalyzer-archiverule-analyzername"></a>
The name of the created analyzer.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_.-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Filter`  <a name="cfn-accessanalyzer-archiverule-filter"></a>
The criteria for the rule.
*Required*: Yes
*Type*: Object of Object
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-accessanalyzer-archiverule-rulename"></a>
The name of the rule to create.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_.-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-accessanalyzer-archiverule-return-values"></a>

### Ref
<a name="aws-resource-accessanalyzer-archiverule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-accessanalyzer-archiverule-return-values-fn--getatt"></a>

####
<a name="aws-resource-accessanalyzer-archiverule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the archive rule was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the archive rule was last updated.

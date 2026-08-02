---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-matchingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow MatchingConfig
<a name="aws-properties-entityresolution-matchingworkflow-matchingconfig"></a>

An object that contains configuration settings for the matching process in a rule-based matching workflow.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-matchingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-matchingconfig-syntax.json"></a>

```
{
  "[EnableTransitiveMatching](#cfn-entityresolution-matchingworkflow-matchingconfig-enabletransitivematching)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-matchingconfig-syntax.yaml"></a>

```
  [EnableTransitiveMatching](#cfn-entityresolution-matchingworkflow-matchingconfig-enabletransitivematching): {{Boolean}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-matchingconfig-properties"></a>

`EnableTransitiveMatching`  <a name="cfn-entityresolution-matchingworkflow-matchingconfig-enabletransitivematching"></a>
Enables transitive matching for the rule-based matching workflow. When enabled, records that match through different rules are grouped together into the same match group.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-matchingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain MatchingRule
<a name="aws-properties-customerprofiles-domain-matchingrule"></a>

Specifies how the rule-based matching process should match profiles.

## Syntax
<a name="aws-properties-customerprofiles-domain-matchingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-matchingrule-syntax.json"></a>

```
{
  "[Rule](#cfn-customerprofiles-domain-matchingrule-rule)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-matchingrule-syntax.yaml"></a>

```
  [Rule](#cfn-customerprofiles-domain-matchingrule-rule): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-matchingrule-properties"></a>

`Rule`  <a name="cfn-customerprofiles-domain-matchingrule-rule"></a>
A single rule level of the `MatchRules`. Configures how the rule-based matching process should match profiles.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

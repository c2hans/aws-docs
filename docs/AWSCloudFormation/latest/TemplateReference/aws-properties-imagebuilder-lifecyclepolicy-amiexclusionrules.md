---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy AmiExclusionRules
<a name="aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules"></a>

Defines criteria for AMIs that are excluded from lifecycle actions.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules-syntax.json"></a>

```
{
  "[IsPublic](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-ispublic)" : {{Boolean}},
  "[LastLaunched](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-lastlaunched)" : {{LastLaunched}},
  "[Regions](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-regions)" : {{[ String, ... ]}},
  "[SharedAccounts](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-sharedaccounts)" : {{[ String, ... ]}},
  "[TagMap](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-tagmap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules-syntax.yaml"></a>

```
  [IsPublic](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-ispublic): {{Boolean}}
  [LastLaunched](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-lastlaunched): {{
    LastLaunched}}
  [Regions](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-regions): {{
    - String}}
  [SharedAccounts](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-sharedaccounts): {{
    - String}}
  [TagMap](#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-tagmap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules-properties"></a>

`IsPublic`  <a name="cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-ispublic"></a>
Configures whether public AMIs are excluded from the lifecycle action.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastLaunched`  <a name="cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-lastlaunched"></a>
Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.
*Required*: No
*Type*: [LastLaunched](aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-regions"></a>
Configures AWS Regions that are excluded from the lifecycle action.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharedAccounts`  <a name="cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-sharedaccounts"></a>
Specifies AWS accounts whose resources are excluded from the lifecycle action.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagMap`  <a name="cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-tagmap"></a>
Lists tags that should be excluded from lifecycle actions for the AMIs that have them.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

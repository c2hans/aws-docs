---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-dataprotectionsettings-custompattern.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::DataProtectionSettings CustomPattern
<a name="aws-properties-workspacesweb-dataprotectionsettings-custompattern"></a>

The pattern configuration for redacting custom data types in session.

## Syntax
<a name="aws-properties-workspacesweb-dataprotectionsettings-custompattern-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-dataprotectionsettings-custompattern-syntax.json"></a>

```
{
  "[KeywordRegex](#cfn-workspacesweb-dataprotectionsettings-custompattern-keywordregex)" : {{String}},
  "[PatternDescription](#cfn-workspacesweb-dataprotectionsettings-custompattern-patterndescription)" : {{String}},
  "[PatternName](#cfn-workspacesweb-dataprotectionsettings-custompattern-patternname)" : {{String}},
  "[PatternRegex](#cfn-workspacesweb-dataprotectionsettings-custompattern-patternregex)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-dataprotectionsettings-custompattern-syntax.yaml"></a>

```
  [KeywordRegex](#cfn-workspacesweb-dataprotectionsettings-custompattern-keywordregex): {{String}}
  [PatternDescription](#cfn-workspacesweb-dataprotectionsettings-custompattern-patterndescription): {{String}}
  [PatternName](#cfn-workspacesweb-dataprotectionsettings-custompattern-patternname): {{String}}
  [PatternRegex](#cfn-workspacesweb-dataprotectionsettings-custompattern-patternregex): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-dataprotectionsettings-custompattern-properties"></a>

`KeywordRegex`  <a name="cfn-workspacesweb-dataprotectionsettings-custompattern-keywordregex"></a>
The keyword regex for the customer pattern. After there is a match to the pattern regex, the keyword regex is used to search within the proximity of the match. If there is a keyword match, then the match is confirmed. If no keyword regex is provided, the pattern regex match will automatically be confirmed. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example, “/ab\+c/gi”
*Required*: No
*Type*: String
*Pattern*: `^\/((?:[^\n])+)\/([gimsuyvd]{0,8})$`
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatternDescription`  <a name="cfn-workspacesweb-dataprotectionsettings-custompattern-patterndescription"></a>
The pattern description for the customer pattern.
*Required*: No
*Type*: String
*Pattern*: `^[ _\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatternName`  <a name="cfn-workspacesweb-dataprotectionsettings-custompattern-patternname"></a>
The pattern name for the custom pattern.
*Required*: Yes
*Type*: String
*Pattern*: `^[_\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatternRegex`  <a name="cfn-workspacesweb-dataprotectionsettings-custompattern-patternregex"></a>
The pattern regex for the customer pattern. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example: “/ab\+c/gi”.
*Required*: Yes
*Type*: String
*Pattern*: `^\/((?:[^\n])+)\/([gimsuyvd]{0,8})$`
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::DataProtectionSettings InlineRedactionPattern
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern"></a>

The set of patterns that determine the data types redacted in session.

## Syntax
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern-syntax.json"></a>

```
{
  "[BuiltInPatternId](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-builtinpatternid)" : {{String}},
  "[ConfidenceLevel](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-confidencelevel)" : {{Number}},
  "[CustomPattern](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-custompattern)" : {{CustomPattern}},
  "[EnforcedUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-enforcedurls)" : {{[ String, ... ]}},
  "[ExemptUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-exempturls)" : {{[ String, ... ]}},
  "[RedactionPlaceHolder](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-redactionplaceholder)" : {{RedactionPlaceHolder}}
}
```

### YAML
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern-syntax.yaml"></a>

```
  [BuiltInPatternId](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-builtinpatternid): {{String}}
  [ConfidenceLevel](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-confidencelevel): {{Number}}
  [CustomPattern](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-custompattern): {{
    CustomPattern}}
  [EnforcedUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-enforcedurls): {{
    - String}}
  [ExemptUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-exempturls): {{
    - String}}
  [RedactionPlaceHolder](#cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-redactionplaceholder): {{
    RedactionPlaceHolder}}
```

## Properties
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern-properties"></a>

`BuiltInPatternId`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-builtinpatternid"></a>
The built-in pattern from the list of preconfigured patterns. Either a customPattern or builtInPatternId is required. To view the entire list of data types and their corresponding built-in pattern IDs, see [Base inline redaction](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/base-inline-redaction.html).
*Required*: No
*Type*: String
*Pattern*: `^[_\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfidenceLevel`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-confidencelevel"></a>
The confidence level for inline redaction pattern. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern \+ unformatted pattern without keyword. This overrides the global confidence level.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPattern`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-custompattern"></a>
The configuration for a custom pattern. Either a customPattern or builtInPatternId is required.
*Required*: No
*Type*: [CustomPattern](aws-properties-workspacesweb-dataprotectionsettings-custompattern.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnforcedUrls`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-enforcedurls"></a>
The enforced URL configuration for the inline redaction pattern. This will override the global enforced URL configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExemptUrls`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-exempturls"></a>
The exempt URL configuration for the inline redaction pattern. This will override the global exempt URL configuration for the inline redaction pattern.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedactionPlaceHolder`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionpattern-redactionplaceholder"></a>
The redaction placeholder that will replace the redacted text in session for the inline redaction pattern.
*Required*: Yes
*Type*: [RedactionPlaceHolder](aws-properties-workspacesweb-dataprotectionsettings-redactionplaceholder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

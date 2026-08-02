---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::DataProtectionSettings InlineRedactionConfiguration
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration"></a>

The configuration for in-session inline redaction.

## Syntax
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-syntax.json"></a>

```
{
  "[GlobalConfidenceLevel](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalconfidencelevel)" : {{Number}},
  "[GlobalEnforcedUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalenforcedurls)" : {{[ String, ... ]}},
  "[GlobalExemptUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalexempturls)" : {{[ String, ... ]}},
  "[InlineRedactionPatterns](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-inlineredactionpatterns)" : {{[ InlineRedactionPattern, ... ]}}
}
```

### YAML
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-syntax.yaml"></a>

```
  [GlobalConfidenceLevel](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalconfidencelevel): {{Number}}
  [GlobalEnforcedUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalenforcedurls): {{
    - String}}
  [GlobalExemptUrls](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalexempturls): {{
    - String}}
  [InlineRedactionPatterns](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-inlineredactionpatterns): {{
    - InlineRedactionPattern}}
```

## Properties
<a name="aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-properties"></a>

`GlobalConfidenceLevel`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalconfidencelevel"></a>
The global confidence level for the inline redaction configuration. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern \+ unformatted pattern without keyword. This is applied to patterns that do not have a pattern-level confidence level. Defaults to confidence level 2.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalEnforcedUrls`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalenforcedurls"></a>
The global enforced URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level enforced URL list.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalExemptUrls`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-globalexempturls"></a>
The global exempt URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level exempt URL list.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InlineRedactionPatterns`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration-inlineredactionpatterns"></a>
The inline redaction patterns to be enabled for the inline redaction configuration.
*Required*: Yes
*Type*: Array of [InlineRedactionPattern](aws-properties-workspacesweb-dataprotectionsettings-inlineredactionpattern.md)
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

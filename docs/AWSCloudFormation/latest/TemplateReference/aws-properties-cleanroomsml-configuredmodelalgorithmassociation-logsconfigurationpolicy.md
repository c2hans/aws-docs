---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation LogsConfigurationPolicy
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy"></a>

Provides the information necessary for a user to access the logs.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-syntax.json"></a>

```
{
  "[AllowedAccountIds](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-allowedaccountids)" : {{[ String, ... ]}},
  "[FilterPattern](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-filterpattern)" : {{String}},
  "[LogRedactionConfiguration](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logredactionconfiguration)" : {{LogRedactionConfiguration}},
  "[LogType](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-syntax.yaml"></a>

```
  [AllowedAccountIds](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-allowedaccountids): {{
    - String}}
  [FilterPattern](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-filterpattern): {{String}}
  [LogRedactionConfiguration](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logredactionconfiguration): {{
    LogRedactionConfiguration}}
  [LogType](#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logtype): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-properties"></a>

`AllowedAccountIds`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-allowedaccountids"></a>
A list of account IDs that are allowed to access the logs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterPattern`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-filterpattern"></a>
A regular expression pattern that is used to parse the logs and return information that matches the pattern.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogRedactionConfiguration`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logredactionconfiguration"></a>
Specifies the log redaction configuration for this policy.
*Required*: No
*Type*: [LogRedactionConfiguration](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogType`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logtype"></a>
Specifies the type of log this policy applies to. The currently supported policies are ALL or ERROR\_SUMMARY.
*Required*: No
*Type*: String
*Allowed values*: `ALL | ERROR_SUMMARY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

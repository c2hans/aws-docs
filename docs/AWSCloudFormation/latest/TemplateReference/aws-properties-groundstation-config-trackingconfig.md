---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-trackingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config TrackingConfig
<a name="aws-properties-groundstation-config-trackingconfig"></a>

 Provides information about how AWS Ground Station should track the satellite through the sky during a contact.

## Syntax
<a name="aws-properties-groundstation-config-trackingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-trackingconfig-syntax.json"></a>

```
{
  "[Autotrack](#cfn-groundstation-config-trackingconfig-autotrack)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-trackingconfig-syntax.yaml"></a>

```
  [Autotrack](#cfn-groundstation-config-trackingconfig-autotrack): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-trackingconfig-properties"></a>

`Autotrack`  <a name="cfn-groundstation-config-trackingconfig-autotrack"></a>
 Specifies whether or not to use autotrack. `REMOVED` specifies that program track should only be used during the contact. `PREFERRED` specifies that autotracking is preferred during the contact but fallback to program track if the signal is lost. `REQUIRED` specifies that autotracking is required during the contact and not to use program track if the signal is lost.
*Required*: No
*Type*: String
*Allowed values*: `REQUIRED | PREFERRED | REMOVED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-trackingconfig--examples"></a>

### Create a TrackingConfig
<a name="aws-properties-groundstation-config-trackingconfig--examples--Create_a_TrackingConfig"></a>

The following example creates a Ground Station `TrackingConfig`

#### JSON
<a name="aws-properties-groundstation-config-trackingconfig--examples--Create_a_TrackingConfig--json"></a>

```
{
  "TrackingConfig": {
    "Autotrack": "PREFERRED"
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-trackingconfig--examples--Create_a_TrackingConfig--yaml"></a>

```
TrackingConfig:
  Autotrack: "PREFERRED"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

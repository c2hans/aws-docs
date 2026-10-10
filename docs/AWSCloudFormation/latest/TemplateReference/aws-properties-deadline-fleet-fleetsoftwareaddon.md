---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-fleetsoftwareaddon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet FleetSoftwareAddOn
<a name="aws-properties-deadline-fleet-fleetsoftwareaddon"></a>

Software that the service installs on worker hosts in a service-managed fleet.

## Syntax
<a name="aws-properties-deadline-fleet-fleetsoftwareaddon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-fleetsoftwareaddon-syntax.json"></a>

```
{
  "[Name](#cfn-deadline-fleet-fleetsoftwareaddon-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-fleetsoftwareaddon-syntax.yaml"></a>

```
  [Name](#cfn-deadline-fleet-fleetsoftwareaddon-name): {{String}}
```

## Properties
<a name="aws-properties-deadline-fleet-fleetsoftwareaddon-properties"></a>

`Name`  <a name="cfn-deadline-fleet-fleetsoftwareaddon-name"></a>
The name of the software add-on. The supported value is `docker`.
*Required*: Yes
*Type*: String
*Allowed values*: `docker`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

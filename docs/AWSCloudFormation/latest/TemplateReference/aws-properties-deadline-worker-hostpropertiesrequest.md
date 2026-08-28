---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-worker-hostpropertiesrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Worker HostPropertiesRequest
<a name="aws-properties-deadline-worker-hostpropertiesrequest"></a>

The host property details.

## Syntax
<a name="aws-properties-deadline-worker-hostpropertiesrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-worker-hostpropertiesrequest-syntax.json"></a>

```
{
  "[HostName](#cfn-deadline-worker-hostpropertiesrequest-hostname)" : {{String}},
  "[IpAddresses](#cfn-deadline-worker-hostpropertiesrequest-ipaddresses)" : {{IpAddresses}}
}
```

### YAML
<a name="aws-properties-deadline-worker-hostpropertiesrequest-syntax.yaml"></a>

```
  [HostName](#cfn-deadline-worker-hostpropertiesrequest-hostname): {{String}}
  [IpAddresses](#cfn-deadline-worker-hostpropertiesrequest-ipaddresses): {{
    IpAddresses}}
```

## Properties
<a name="aws-properties-deadline-worker-hostpropertiesrequest-properties"></a>

`HostName`  <a name="cfn-deadline-worker-hostpropertiesrequest-hostname"></a>
The host name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\.\-]{0,255}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddresses`  <a name="cfn-deadline-worker-hostpropertiesrequest-ipaddresses"></a>
The IP address of the host.
*Required*: No
*Type*: [IpAddresses](aws-properties-deadline-worker-ipaddresses.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

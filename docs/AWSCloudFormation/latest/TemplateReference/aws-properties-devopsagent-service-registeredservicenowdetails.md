---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredservicenowdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredServiceNowDetails
<a name="aws-properties-devopsagent-service-registeredservicenowdetails"></a>

ServiceNow service details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registeredservicenowdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredservicenowdetails-syntax.json"></a>

```
{
  "[InstanceUrl](#cfn-devopsagent-service-registeredservicenowdetails-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredservicenowdetails-syntax.yaml"></a>

```
  [InstanceUrl](#cfn-devopsagent-service-registeredservicenowdetails-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredservicenowdetails-properties"></a>

`InstanceUrl`  <a name="cfn-devopsagent-service-registeredservicenowdetails-instanceurl"></a>
The ServiceNow instance URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

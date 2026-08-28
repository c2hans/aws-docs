---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-ingressconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service IngressConfiguration
<a name="aws-properties-apprunner-service-ingressconfiguration"></a>

Network configuration settings for inbound network traffic.

## Syntax
<a name="aws-properties-apprunner-service-ingressconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-ingressconfiguration-syntax.json"></a>

```
{
  "[IsPubliclyAccessible](#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-apprunner-service-ingressconfiguration-syntax.yaml"></a>

```
  [IsPubliclyAccessible](#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible): {{Boolean}}
```

## Properties
<a name="aws-properties-apprunner-service-ingressconfiguration-properties"></a>

`IsPubliclyAccessible`  <a name="cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible"></a>
Specifies whether your App Runner service is publicly accessible. To make the service publicly accessible set it to `True`. To make the service privately accessible, from only within an Amazon VPC set it to `False`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

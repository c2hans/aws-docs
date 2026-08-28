---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Shield::Protection ApplicationLayerAutomaticResponseConfiguration
<a name="aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration"></a>

The automatic application layer DDoS mitigation settings for a [AWS::Shield::Protection](aws-resource-shield-protection.md). This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.

If you use CloudFormation to manage the web ACLs that you use with Shield Advanced automatic mitigation, see the guidance for the `AWS::WAFv2::WebACL` resource.

## Syntax
<a name="aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration-syntax.json"></a>

```
{
  "[Action](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-action)" : {{Action}},
  "[Status](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration-syntax.yaml"></a>

```
  [Action](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-action): {{
    Action}}
  [Status](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration-properties"></a>

`Action`  <a name="cfn-shield-protection-applicationlayerautomaticresponseconfiguration-action"></a>
Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.
*Required*: Yes
*Type*: [Action](aws-properties-shield-protection-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-shield-protection-applicationlayerautomaticresponseconfiguration-status"></a>
Indicates whether automatic application layer DDoS mitigation is enabled for the protection.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

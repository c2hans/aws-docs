---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-nodelifecycleactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup NodeLifecycleActions
<a name="aws-properties-pcs-computenodegroup-nodelifecycleactions"></a>

The lifecycle actions configured on a compute node group. Lifecycle actions define scripts that AWS PCS runs on compute nodes at specific stages of their lifecycle.

## Syntax
<a name="aws-properties-pcs-computenodegroup-nodelifecycleactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-nodelifecycleactions-syntax.json"></a>

```
{
  "[ScriptCachingPolicy](#cfn-pcs-computenodegroup-nodelifecycleactions-scriptcachingpolicy)" : {{String}},
  "[Stages](#cfn-pcs-computenodegroup-nodelifecycleactions-stages)" : {{NodeLifecycleStages}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-nodelifecycleactions-syntax.yaml"></a>

```
  [ScriptCachingPolicy](#cfn-pcs-computenodegroup-nodelifecycleactions-scriptcachingpolicy): {{String}}
  [Stages](#cfn-pcs-computenodegroup-nodelifecycleactions-stages): {{
    NodeLifecycleStages}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-nodelifecycleactions-properties"></a>

`ScriptCachingPolicy`  <a name="cfn-pcs-computenodegroup-nodelifecycleactions-scriptcachingpolicy"></a>
The caching policy for node lifecycle scripts. The default value is `CACHE_ONCE`. Valid values:
+ `CACHE_ONCE` – Downloads each script once and reuses it on subsequent boots.
+ `REFRESH_ON_REBOOT` – Downloads each script on every boot.
*Required*: No
*Type*: String
*Allowed values*: `CACHE_ONCE | REFRESH_ON_REBOOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stages`  <a name="cfn-pcs-computenodegroup-nodelifecycleactions-stages"></a>
The lifecycle stages where you configure scripts to run.
*Required*: Yes
*Type*: [NodeLifecycleStages](aws-properties-pcs-computenodegroup-nodelifecyclestages.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

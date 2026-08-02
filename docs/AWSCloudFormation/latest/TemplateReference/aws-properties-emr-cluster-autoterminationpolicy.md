---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-autoterminationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster AutoTerminationPolicy
<a name="aws-properties-emr-cluster-autoterminationpolicy"></a>

An auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see [Control cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html).

## Syntax
<a name="aws-properties-emr-cluster-autoterminationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-autoterminationpolicy-syntax.json"></a>

```
{
  "[IdleTimeout](#cfn-emr-cluster-autoterminationpolicy-idletimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-cluster-autoterminationpolicy-syntax.yaml"></a>

```
  [IdleTimeout](#cfn-emr-cluster-autoterminationpolicy-idletimeout): {{Integer}}
```

## Properties
<a name="aws-properties-emr-cluster-autoterminationpolicy-properties"></a>

`IdleTimeout`  <a name="cfn-emr-cluster-autoterminationpolicy-idletimeout"></a>
Specifies the amount of idle time in seconds after which the cluster automatically terminates. You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

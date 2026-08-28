---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-vpcconnectivitysasl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster VpcConnectivitySasl
<a name="aws-properties-msk-cluster-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

## Syntax
<a name="aws-properties-msk-cluster-vpcconnectivitysasl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-vpcconnectivitysasl-syntax.json"></a>

```
{
  "[Iam](#cfn-msk-cluster-vpcconnectivitysasl-iam)" : {{VpcConnectivityIam}},
  "[Scram](#cfn-msk-cluster-vpcconnectivitysasl-scram)" : {{VpcConnectivityScram}}
}
```

### YAML
<a name="aws-properties-msk-cluster-vpcconnectivitysasl-syntax.yaml"></a>

```
  [Iam](#cfn-msk-cluster-vpcconnectivitysasl-iam): {{
    VpcConnectivityIam}}
  [Scram](#cfn-msk-cluster-vpcconnectivitysasl-scram): {{
    VpcConnectivityScram}}
```

## Properties
<a name="aws-properties-msk-cluster-vpcconnectivitysasl-properties"></a>

`Iam`  <a name="cfn-msk-cluster-vpcconnectivitysasl-iam"></a>
Details for ClientAuthentication using IAM for VpcConnectivity.
*Required*: No
*Type*: [VpcConnectivityIam](aws-properties-msk-cluster-vpcconnectivityiam.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scram`  <a name="cfn-msk-cluster-vpcconnectivitysasl-scram"></a>
Details for SASL/SCRAM client authentication for VpcConnectivity.
*Required*: No
*Type*: [VpcConnectivityScram](aws-properties-msk-cluster-vpcconnectivityscram.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

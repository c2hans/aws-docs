---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-sasl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster Sasl
<a name="aws-properties-msk-cluster-sasl"></a>

Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true.

## Syntax
<a name="aws-properties-msk-cluster-sasl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-sasl-syntax.json"></a>

```
{
  "[Iam](#cfn-msk-cluster-sasl-iam)" : {{Iam}},
  "[Scram](#cfn-msk-cluster-sasl-scram)" : {{Scram}}
}
```

### YAML
<a name="aws-properties-msk-cluster-sasl-syntax.yaml"></a>

```
  [Iam](#cfn-msk-cluster-sasl-iam): {{
    Iam}}
  [Scram](#cfn-msk-cluster-sasl-scram): {{
    Scram}}
```

## Properties
<a name="aws-properties-msk-cluster-sasl-properties"></a>

`Iam`  <a name="cfn-msk-cluster-sasl-iam"></a>
Details for ClientAuthentication using IAM.
*Required*: No
*Type*: [Iam](aws-properties-msk-cluster-iam.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scram`  <a name="cfn-msk-cluster-sasl-scram"></a>
Details for SASL/SCRAM client authentication.
*Required*: No
*Type*: [Scram](aws-properties-msk-cluster-scram.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

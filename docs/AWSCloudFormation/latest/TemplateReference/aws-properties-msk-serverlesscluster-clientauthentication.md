---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-serverlesscluster-clientauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::ServerlessCluster ClientAuthentication
<a name="aws-properties-msk-serverlesscluster-clientauthentication"></a>

Includes all client authentication information.

## Syntax
<a name="aws-properties-msk-serverlesscluster-clientauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-serverlesscluster-clientauthentication-syntax.json"></a>

```
{
  "[Sasl](#cfn-msk-serverlesscluster-clientauthentication-sasl)" : {{Sasl}}
}
```

### YAML
<a name="aws-properties-msk-serverlesscluster-clientauthentication-syntax.yaml"></a>

```
  [Sasl](#cfn-msk-serverlesscluster-clientauthentication-sasl): {{
    Sasl}}
```

## Properties
<a name="aws-properties-msk-serverlesscluster-clientauthentication-properties"></a>

`Sasl`  <a name="cfn-msk-serverlesscluster-clientauthentication-sasl"></a>
Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true.
*Required*: Yes
*Type*: [Sasl](aws-properties-msk-serverlesscluster-sasl.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

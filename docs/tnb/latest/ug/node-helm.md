---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-helm.html
---

# AWS.Artifacts.Helm
<a name="node-helm"></a>

Defines an AWS Helm Node.

## Syntax
<a name="node-helm-syntax"></a>

```
tosca.nodes.AWS.Artifacts.Helm:
  properties:
    implementation: String
```

## Properties
<a name="node-helm-properties"></a>

 `implementation`
The local directory that contains the Helm chart within the CSAR package.
Required: Yes
Type: String

## Example
<a name="node-helm-example"></a>

```
SampleHelm:
  type: tosca.nodes.AWS.Artifacts.Helm
  properties:
    implementation: "./vnf-helm"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

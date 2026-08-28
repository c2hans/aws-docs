---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/vnfd-template.html
---

# VNFD template
<a name="vnfd-template"></a>

Defines a virtual network function descriptor (VNFD) template.

## Syntax
<a name="vnfd-syntax"></a>

```
tosca_definitions_version: tnb_simple_yaml_1_0

topology_template:

  inputs:
    SampleInputParameter:
      type: String
      description: "Sample parameter description"
      default: "DefaultSampleValue"

  node\_templates:
    SampleNode1: tosca.nodes.AWS.VNF
```

## Topology template
<a name="vnfd-topology-template"></a>

 `node_templates`
The TOSCA AWS Nodes. The possible nodes are:
+ [AWS.VNF](node-vnf.md)
+ [AWS.Artifacts.Helm](node-helm.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

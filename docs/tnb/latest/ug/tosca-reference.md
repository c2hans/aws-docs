---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/tosca-reference.html
---

# TOSCA reference for AWS TNB
<a name="tosca-reference"></a>

Topology and Orchestration Specification for Cloud Applications (TOSCA) is a declarative syntax that CSPs use to describe a topology of cloud based web services, their components, relationships, and the processes that manage them. CSPs describe the connection points, the logical links between the connection points, and the policies such as affinity and security in a TOSCA template. CSPs then upload the template to AWS TNB which synthesizes the resources needed to establish a functioning 5G network across AWS Availability Zones.

**Topics**
+ [VNFD template](vnfd-template.md)
+ [Network service descriptor template](nsd-template.md)
+ [Common nodes](common-nodes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

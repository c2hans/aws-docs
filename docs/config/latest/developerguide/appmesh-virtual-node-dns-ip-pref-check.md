---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appmesh-virtual-node-dns-ip-pref-check.html
---

# appmesh-virtual-node-dns-ip-pref-check
<a name="appmesh-virtual-node-dns-ip-pref-check"></a>

Checks if an AWS App Mesh virtual node is configured with the specified IP preference for DNS service discovery. The rule is NON\_COMPLIANT if the virtual node is not configured with the IP preference specified in the required rule parameter.

**Identifier:** APPMESH\_VIRTUAL\_NODE\_DNS\_IP\_PREF\_CHECK

**Resource Types:** AWS::AppMesh::VirtualNode

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

ipPreferenceType: String
The IP preference value for DNS service discovery. The rule is NON\_COMPLIANT if a virtual node is configured with a value that does not match this value. Valid values include: 'IPv6\_PREFERRED', 'IPv4\_PREFERRED', 'IPv4\_ONLY', and 'IPv6\_ONLY'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d149c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

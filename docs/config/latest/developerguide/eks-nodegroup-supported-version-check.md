---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/eks-nodegroup-supported-version-check.html
---

# eks-nodegroup-supported-version-check
<a name="eks-nodegroup-supported-version-check"></a>

Checks if an Amazon Elastic Kubernetes Service (EKS) nodegroup is running the oldest supported version.

**Identifier:** EKS\_NODEGROUP\_SUPPORTED\_VERSION\_CHECK

**Resource Types:** AWS::EKS::Nodegroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Middle East (UAE) Region

**Parameters:**

oldestVersionSupportedType: String
Value of the oldest version of Kubernetes supported on AWS.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d733c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

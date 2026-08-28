---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/eks-cluster-secrets-encrypted.html
---

# eks-cluster-secrets-encrypted
<a name="eks-cluster-secrets-encrypted"></a>

Checks if Amazon EKS clusters are configured to have Kubernetes secrets encrypted using AWS KMS. The rule is NON\_COMPLIANT if an EKS cluster does not have an encryptionConfig resource or if encryptionConfig does not name secrets as a resource.

**Identifier:** EKS\_CLUSTER\_SECRETS\_ENCRYPTED

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV
Comma-separated list of KMS key Amazon Resource Names (ARNs) that are approved for EKS usage.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d725c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](http://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution aims to create IAM roles with least privilege where resource access is required. The Amazon EKS deployment uses [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) to associate an IAM role with the Kubernetes service accounts used by the Migration Console pod (`migration-console-access-role`) and the Argo workflow executor pods (`argo-workflow-executor`). The IAM role is named `<eks-cluster-name>-migrations-role` and is created automatically by the CDK stack. This means the Migration Console and the migration jobs can authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, Amazon S3, AWS Secrets Manager, and other AWS services without long-lived credentials.

## Security groups
<a name="security-groups"></a>

The solution creates security groups designed to control and isolate network traffic between Migration Assistant pods on Amazon EKS, as well as between certain Migration Assistant pods and associated services such as Amazon S3 (via VPC endpoints), Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and Amazon EFS. We recommend that you review the security groups and further restrict access as needed once the deployment is up and running. For source and target clusters, the source and target security groups must allow inbound traffic from the Amazon EKS cluster security group.

## Basic-auth credential storage
<a name="aws-secrets-manager"></a>

Migration Assistant for Amazon OpenSearch Service stores workflow HTTP Basic credentials as Kubernetes Secrets in the `ma` namespace. The Workflow CLI can create and manage them with `workflow configure credentials create <NAME>`; reference those names in `authConfig.basic.secretName`. If you already manage credentials in an external secrets system, sync the `username` and `password` values into a Kubernetes Secret before referencing them from workflow configuration. The Migration Console pod, Argo workflow executor pods, Reindex-from-Snapshot workers, Capture Proxy, and Traffic Replayer workloads use these credentials when they connect to authenticated source or target clusters.

## Fine-grained access control
<a name="fine-grained-access-control"></a>

If your Amazon OpenSearch Service domain has fine-grained access control (FGAC) enabled, the Migration Assistant IAM role must be mapped to a security role on the domain (typically `all_access` during migration, then scoped down). Authentication gets you to the domain; FGAC authorizes what you can do once you are in. Both must be in place. The role mapping API path differs by engine: Elasticsearch 7.x uses `/_opendistro/_security/api/rolesmapping/<role>`, and OpenSearch 1.x and later uses `/_plugins/_security/api/rolesmapping/<role>`. See [Troubleshooting](troubleshooting.md) for details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

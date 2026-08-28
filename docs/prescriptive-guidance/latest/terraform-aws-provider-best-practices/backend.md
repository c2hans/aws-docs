---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html
---

# Backend best practices
<a name="backend"></a>

Using a proper remote backend to store your state file is critical for enabling collaboration, ensuring state file integrity through locking, providing reliable backup and recovery, integrating with CI/CD workflows, and taking advantage of advanced security, governance, and management features offered by managed services such as HCP Terraform.

Terraform supports various backend types such as Kubernetes, HashiCorp Consul, and HTTP. However, this guide focuses on Amazon S3, which is an optimal backend solution for most AWS users.

As a fully managed object storage service that offers high durability and availability, Amazon S3 provides a secure, scalable and low-cost backend for managing Terraform state on AWS. The global footprint and resilience of Amazon S3 exceeds what most teams can achieve by self-managing state storage. Additionally, being natively integrated with AWS access controls, encryption options, versioning capabilities, and other services makes Amazon S3 a convenient backend choice.

This guide doesn't provide backend guidance for other solutions such as Kubernetes or Consul because the primary target audience is AWS customers. For teams that are fully in the AWS Cloud, Amazon S3 is typically the ideal choice over Kubernetes or HashiCorp Consul clusters. The simplicity, resilience, and tight AWS integration of Amazon S3 state storage provides an optimal foundation for most users who follow AWS best practices. Teams can take advantage of the durability, backup protections, and availability of AWS services to keep remote Terraform state highly resilient.

Following the backend recommendations in this section will lead to more collaborative Terraform code bases while limiting the impact of errors or unauthorized modifications. By implementing a well-architected remote backend, teams can optimize Terraform workflows.

## Use Amazon S3 for remote storage
<a name="amazon-s3"></a>

Storing Terraform state remotely in Amazon S3 and implementing [state locking](https://developer.hashicorp.com/terraform/language/settings/backends/s3#dynamodb-state-locking) and consistency checking by using Amazon DynamoDB provide major benefits over local file storage. Remote state enables team collaboration, change tracking, backup protections, and remote locking for increased safety.

Using Amazon S3 with the S3 Standard storage class (default) instead of ephemeral local storage or self-managed solutions provides 99.999999999% durability and 99.99% availability protections to prevent accidental state data loss. AWS managed services such as Amazon S3 and DynamoDB provide service-level agreements (SLAs) that exceed what most organizations can achieve when they self-manage storage. Rely on these protections to keep remote backends accessible.

### Enable remote state locking
<a name="enable-remote-state-locking.09eb533b-48bf-5d74-91c4-e54b1ccca125"></a>

State locking restricts access to prevent concurrent write operations and reduces errors from simultaneous modifications by multiple users. Terraform supports two locking mechanisms for Amazon S3 backends:
+ Amazon S3 native state locking (recommended): Available since Terraform 1.10.0; uses the native locking capabilities in Amazon S3
+ DynamoDB state locking (deprecated): Legacy approach that will be removed in future Terraform versions

Example backend configuration with Amazon S3 state locking:

```
terraform {
  backend "s3" {
    bucket       = "myorg-terraform-states"
    key          = "myapp/production/tfstate"
    region       = "us-east-1"
    use_lockfile = true
  }
}
```

For backward compatibility during migration, you can configure both Amazon S3 and DynamoDB locking simultaneously. However, we recommend that you migrate to Amazon S3 native locking because DynamoDB-based locking is being deprecated.

### Enable versioning and automatic backups
<a name="enable-versioning-and-automatic-backups.b39ed2b1-ef8e-5f38-a5de-3d8560ab6647"></a>

For additional safeguarding, enable [automatic versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) and [backups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html) by using AWS Backup on Amazon S3 backends. Versioning preserves all previous versions of the state whenever changes are made. It also lets you restore previous working state snapshots if needed to roll back unwanted changes or recover from accidents.

### Restore previous versions if needed
<a name="restore-previous-versions-if-needed.f6731227-22d6-5f5d-b63c-3f487af24364"></a>

Versioned Amazon S3 state buckets make it easy to revert changes by restoring a previous known good state snapshot. This helps protect against accidental changes and provides additional backup capabilities.

### Use HCP Terraform
<a name="use-hcp-terraform.27c51030-469f-5326-aff3-b0eacbd182bd"></a>

[HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs) provides a fully managed backend alternative to configuring your own state storage. HCP Terraform automatically handles the secure storage of state and encryption while unlocking additional features.

When you use HCP Terraform, state is stored remotely by default, which enables state sharing and locking across your organization. Detailed policy controls help you restrict state access and changes.

Additional capabilities include version control integrations, policy guardrails, workflow automation, variables management, and single sign-on integrations with SAML. You can also use Sentinel policy as code to implement governance controls.

Although HCP Terraform requires using a software as a service (SaaS) platform, for many teams the benefits around security, access controls, automated policy checks, and collaboration features make it an optimal choice over self-managing state storage with Amazon S3 or DynamoDB.

Easy integration with services such as GitHub and GitLab with minor configuration also appeals to users who fully embrace cloud and SaaS tools for better team workflows.

## Facilitate team collaboration
<a name="team-collaboration"></a>

Use remote backends to share state data across all the members of your Terraform team. This facilitates collaboration because it gives the entire team visibility into infrastructure changes. Shared backend protocols combined with state history transparency simplify internal change management. All infrastructure changes go through the established pipeline, which increases business agility across the enterprise.

### Improve accountability by using AWS CloudTrail
<a name="improve-accountability-by-using-9999999999999999ctlong-.24f5507b-889c-5606-add4-4178bd4b66fc"></a>

Integrate AWS CloudTrail with the Amazon S3 bucket to capture API calls made to the state bucket. Filter [CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events) to track `PutObject`, `DeleteObject,` and other relevant calls.

CloudTrail logs show the AWS identity of the principal that made each API call for state change. The user's identity can be matched to a machine account or to members of the team who interact with the backend storage.

Combine CloudTrail logs with Amazon S3 state versioning to tie infrastructure changes to the principal who applied them. By analyzing multiple revisions, you can attribute any updates to the machine account or responsible team member.

If an unintended or disruptive change occurs, state versioning provides rollback capabilities. CloudTrail traces the change to the user so you can discuss preventative improvements.

We also recommend that you enforce IAM permissions to limit state bucket access. Overall, S3 Versioning and CloudTrail monitoring supports auditing across infrastructure changes. Teams gain improved accountability, transparency, and audit capabilities into the Terraform state history.

## Separate the backends for each environment
<a name="separate-backends"></a>

Use distinct Terraform backends for each application environment. Separate backends isolate state between development, test, and production.

### Reduce the scope of impact
<a name="reduce-the-scope-of-impact.ef74f6c2-07a4-5127-8ac1-e541f8216d43"></a>

Isolating state helps ensure that changes in lower environments don't impact production infrastructure. Accidents or experiments in development and test environments have limited impact.

### Restrict production access
<a name="restrict-production-access.9e397e86-6b6d-575b-89e9-097056aa8df9"></a>

Lock down permissions for the production state backend to read-only access for most users. Limit who can modify the production infrastructure to the CI/CD pipeline and [break glass](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html) roles.

### Simplify access controls
<a name="simplify-access-controls.62ea8a95-ec7f-55b7-a9fc-a82378bf62a6"></a>

Managing permissions at the backend level simplifies access control between environments. Using distinct S3 buckets for each application and environment means that broad read or write permissions can be granted on entire backend buckets.

### Avoid shared workspaces
<a name="avoid-shared-workspaces.6d3b0b5f-9c9f-5ad3-81a5-8c0b2d671630"></a>

Although you can use [Terraform workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces) to separate state between environments, distinct backends provide stronger isolation. If you have shared workspaces, accidents can still impact multiple environments.

Keeping environment backends fully isolated minimizes the impact of any single failure or breach. Separate backends also align access controls to the environment's sensitivity level. For example, you can provide write protection for the production environment and broader access for development and test environments.

## Actively monitor remote state activity
<a name="monitor-remote-state-activity"></a>

Continuously monitoring remote state activity is critical for detecting potential issues early. Look for anomalous unlocks, changes, or access attempts.

### Get alerts on suspicious unlocks
<a name="get-alerts-on-suspicious-unlocks.8986597d-6ba3-5129-81f5-4e7af5dc2e64"></a>

Most state changes should run through CI/CD pipelines. Generate alerts if state unlocks occur directly through developer workstations, which could signal unauthorized or untested changes.

### Monitor access attempts
<a name="monitor-access-attempts.52ac9910-4fb6-5348-9665-97963faf1768"></a>

Authentication failures on state buckets might indicate reconnaissance activity. Notice if multiple accounts are trying to access state, or unusual IP addresses appear, which signals compromised credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

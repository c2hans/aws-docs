---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html
---

# Backend best practices
<a name="backend"></a>

Using a proper remote backend to store your state file is critical for enabling collaboration, ensuring state file integrity through locking, providing reliable backup and recovery, integrating with CI/CD workflows, and taking advantage of advanced security, governance, and management features offered by managed services such as HCP Terraform.

Terraform supports various backend types such as Kubernetes, HashiCorp Consul, and HTTP. However, this guide focuses on Amazon S3, which is a recommended backend solution for most AWS users.

As a fully managed object storage service that offers high durability and availability, Amazon S3 provides a secure, scalable, and cost-effective backend for managing Terraform state on AWS. The global footprint and resilience of Amazon S3 can be difficult to replicate when self-managing state storage. Additionally, being natively integrated with AWS access controls, encryption options, versioning capabilities, and other services makes Amazon S3 a convenient backend choice.

This guide doesn't provide backend guidance for other solutions such as Kubernetes or Consul because the primary target audience is AWS customers. For teams working primarily in the AWS Cloud, Amazon S3 is typically a recommended choice over Kubernetes or HashiCorp Consul clusters. The simplicity, resilience, and tight AWS integration of Amazon S3 state storage provides a strong foundation for most users who follow AWS best practices. Teams can take advantage of the durability, backup protections, and availability of AWS services to keep remote Terraform state highly resilient.

Following the backend recommendations in this section can help teams build more collaborative Terraform code bases while reducing the impact of errors or unauthorized modifications. By implementing a well-architected remote backend, teams can improve Terraform workflows.

## Use Amazon S3 for remote storage
<a name="amazon-s3"></a>

Storing Terraform state remotely in Amazon S3, with [S3 native state locking](https://developer.hashicorp.com/terraform/language/backend/s3), provides key benefits over local file storage. Remote state enables team collaboration, change tracking, backup protections, and locking to help prevent concurrent write conflicts.

The S3 Standard storage class (the default) is designed for 99.999999999% durability and 99.99% availability, which helps protect state from accidental loss compared to local storage or self-managed solutions. For details, see [Comparing the Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare) in the Amazon S3 User Guide.

### Enable remote state locking
<a name="enable-remote-state-locking.d089408a-63a4-52c6-b892-30583f961387"></a>

State locking prevents concurrent write operations and reduces errors from simultaneous changes by multiple users. Use S3 native state locking by setting `use_lockfile = true`. It's generally available in Terraform 1.11 and later, so set `required_version = ">= 1.11"`. Locking through Amazon DynamoDB (the `dynamodb_table` argument) is deprecated, and HashiCorp plans to remove it in a future version.

While a run holds the lock, Terraform keeps a lock object named `<key>.tflock` next to the state file. Another run that tries to take the lock fails with `Error acquiring the state lock` and shows who holds it. To wait for a lock instead of failing, set `-lock-timeout`, for example `-lock-timeout=5m`.

Example backend configuration with S3 native locking and SSE-KMS encryption:

```
terraform {
  backend "s3" {
    bucket       = "example-terraform-state-111122223333"
    key          = "network/prod/terraform.tfstate"
    region       = "us-west-2"
    encrypt      = true
    kms_key_id   = "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    use_lockfile = true
  }
}
```

With `encrypt = true`, `kms_key_id` selects the key that encrypts the state. Without `encrypt`, the backend ignores `kms_key_id`. If the role that runs Terraform doesn't have access to the state, add an `assume_role` block to the backend configuration with a role that does. The backend's role is separate from the provider's, so you can keep state access out of the role that changes resources.

To migrate from DynamoDB locking, set `use_lockfile = true` alongside `dynamodb_table` and run `terraform init -reconfigure`. Terraform then takes both locks. After every user and pipeline that uses the state runs Terraform 1.11 or later with the new configuration, remove `dynamodb_table`.

### Configure the state bucket
<a name="configure-the-state-bucket.8bfc4cd3-1140-5683-a6af-14a80c13b9f9"></a>

Apply the controls from [Enable encryption and access controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html#remote-state-storage) to the state bucket. Add a bucket policy statement that denies `s3:*` to every principal on the bucket and its objects when `aws:SecureTransport` is `false`. For an example, see [Enforce encryption of data in transit](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html#transit) in the Amazon S3 documentation.

### Enable versioning and automatic backups
<a name="enable-versioning-and-automatic-backups.b0d42c2d-9f8c-5512-af1b-8ba030a6ee1c"></a>

Enable [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) and [backups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html) by using AWS Backup on Amazon S3 backends to add additional data protection. Versioning preserves all previous versions of the state each time Terraform writes a change. It also lets you restore previous working state snapshots to roll back unwanted changes or recover from accidents.

### Restore previous versions if needed
<a name="restore-previous-versions-if-needed.e9bafbb8-e995-5e77-9498-3019541a3307"></a>

Versioned Amazon S3 state buckets let you revert changes by restoring a previous valid state snapshot. This helps protect against accidental changes and provides additional backup capabilities.

### Use HCP Terraform
<a name="use-hcp-terraform.ad0218ea-fdce-503d-b40c-c7aa0b06999e"></a>

[HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs) provides a fully managed backend alternative to configuring your own state storage. HCP Terraform automatically handles the secure storage of state and encryption while unlocking additional features.

When you use HCP Terraform, state is stored remotely by default, which enables state sharing and locking across your organization. Detailed policy controls help you restrict state access and changes.

Additional capabilities include version control integrations, policy guardrails, workflow automation, variables management, and single sign-on integrations with SAML. You can enforce policy as code with Sentinel, OPA, or Terraform policy to implement governance controls.

Although HCP Terraform requires using a software as a service (SaaS) offering, for many teams the benefits around security, access controls, automated policy checks, and collaboration features make it a strong alternative to self-managing state storage in Amazon S3.

If your team uses cloud and SaaS tools such as GitHub and GitLab, you can integrate them with HCP Terraform to support your team workflows.

## Facilitate team collaboration
<a name="team-collaboration"></a>

Use remote backends to share state data across all the members of your Terraform team. This facilitates collaboration because it gives the entire team visibility into infrastructure changes. Shared backend protocols combined with state history transparency simplify internal change management. All infrastructure changes go through the established pipeline, which helps teams deliver infrastructure updates consistently and at scale.

### Improve accountability by using AWS CloudTrail
<a name="improve-accountability-by-using-9999999999999999ctlong-.9159c824-1062-5818-8749-f30561ec39c0"></a>

Use CloudTrail to record the API calls made to the state bucket. Object-level operations such as `PutObject`, `GetObject`, and `DeleteObject` are [data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). Trails don't log data events by default, and CloudTrail charges for them, so limit the trail to the state bucket with an [advanced event selector](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/filtering-data-events.html). Select `eventCategory` equals `Data`, `resources.type` equals `AWS::S3::Object`, and `resources.ARN` starts with the state bucket's ARN followed by `/`. In Terraform, these are `field_selector` blocks in the `advanced_event_selector` block of `aws_cloudtrail`. Also set `enable_log_file_validation = true`.

CloudTrail logs show the IAM identity of the principal that made each API call for state change. You can match the user's identity to a machine account or to members of the team who interact with the backend storage.

Combine CloudTrail logs with S3 Versioning to tie infrastructure changes to the principal who applied them. By analyzing multiple revisions, you can attribute any updates to the machine account or responsible team member.

If an unintended or disruptive change occurs, state versioning provides rollback capabilities. CloudTrail traces the change to the user so you can discuss preventive improvements.

Also enforce IAM permissions to limit state bucket access. Overall, S3 Versioning and CloudTrail monitoring support auditing across infrastructure changes. Teams gain improved accountability, transparency, and audit capabilities for the Terraform state history.

## Separate the backends for each environment
<a name="separate-backends"></a>

Use distinct Terraform backends for each application environment. Separate backends isolate state between development, test, and production. For the strongest isolation, put each environment in its own AWS account, in line with [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html), and keep each environment's state bucket in that account.

### Reduce the scope of impact
<a name="reduce-the-scope-of-impact.24bff4e2-1343-53e8-b2d9-53bc78ac9e04"></a>

Isolating state helps ensure that changes in lower environments don't impact production infrastructure. Accidents or experiments in development and test environments have limited impact.

### Restrict production access
<a name="restrict-production-access.cf257cf9-cf55-515d-8551-50b4d9aa7fc7"></a>

Restrict permissions for the production state backend to read-only access for most users. Limit who can modify the production infrastructure to the CI/CD pipeline and [break glass](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html#break-glass-access) roles.

### Simplify access controls
<a name="simplify-access-controls.62ea8a95-ec7f-55b7-a9fc-a82378bf62a6"></a>

Managing permissions at the backend level simplifies access control between environments. Using distinct S3 buckets for each application and environment means that broad read or write permissions can be granted on entire backend buckets.

### Avoid shared workspaces
<a name="avoid-shared-workspaces.305423ed-5d87-5004-8eb0-51d3df93bf74"></a>

Although you can use [Terraform workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces) to separate state between environments, distinct backends provide stronger isolation. If you have shared workspaces, accidents can still impact multiple environments.

Keeping environment backends fully isolated minimizes the impact of any single failure or unauthorized access event. Separate backends also align access controls to the environment's sensitivity level. For example, you can provide write protection for the production environment and broader access for development and test environments.

## Actively monitor remote state activity
<a name="monitor-remote-state-activity"></a>

Monitor remote state activity continuously to detect anomalies early. Look for unexpected unlocks, unauthorized changes, or suspicious access attempts.

### Get alerts on suspicious unlocks
<a name="get-alerts-on-suspicious-unlocks.bfd9b841-d874-56e0-9229-3968af7ae586"></a>

With S3 native locking, the lock is the `<key>.tflock` object, and releasing a lock deletes that object. Your pipeline releases its lock at the end of every run, and `terraform force-unlock` or a manual delete releases another principal's lock. Most state changes should run through CI/CD pipelines, so alert when a principal other than the pipeline role deletes a lock object.

Create an Amazon EventBridge rule whose event pattern matches `source` `aws.s3`, `detail-type` `AWS API Call via CloudTrail`, `detail.eventName` `DeleteObject`, a `detail.requestParameters.key` that ends with `.tflock`, and a `detail.userIdentity.arn` that doesn't start with the pipeline role's assumed-role ARN. EventBridge receives these events only from a trail that logs data events for the state bucket, as described in the previous section.

Send the matches to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon Simple Queue Service (Amazon SQS) queue that your team monitors.

### Monitor access attempts
<a name="monitor-access-attempts.b7397a02-1b79-5a01-946e-fd1b6833cdc8"></a>

Authentication failures on state buckets might indicate unauthorized access attempts. Monitor for access from multiple unexpected accounts or unusual IP addresses, which may indicate unauthorized credential use.

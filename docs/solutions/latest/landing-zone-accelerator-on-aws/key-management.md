---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/key-management.html
---

# Key management
<a name="key-management"></a>

 **Architecture diagram showing key management for accounts.**

![image6](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image6.png)

The solution uses AWS KMS keys to provide encryption at rest capabilities for resources deployed by the solution. Some AWS KMS keys are deployed to every account and Region managed by the solution, while others are centralized in a single core account.

## All accounts
<a name="all-accounts"></a>
+  **Amazon CloudWatch key** - used to encrypt CloudWatch Logs groups created by the solution
+  **Amazon S3 key** - used to encrypt Amazon S3 buckets created by the solution
+  **AWS Lambda key** - used to encrypt environment variables for Lambda functions created by the solution
+  **AWS Systems Manager Session Manager key (optional)** - used to encrypt [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) sessions if Session Manager logging is activated in the `global-config.yaml` file
+  **Amazon Elastic Block Store (Amazon EBS) key (optional)** - used for default encryption of Amazon EBS volumes if activated in the `security-config.yaml` file

## Management account
<a name="management-account"></a>
+  **Installer key** - created by `AWSAccelerator-InstallerStack` to activate encryption at rest for Installer pipeline dependencies
+  **Management key** - created by `AWSAccelerator-PipelineStack` to activate encryption at rest for Core pipeline dependencies
+  **AWS Backup key (optional)** - used to activate encryption at rest for [AWS Backup](https://aws.amazon.com/backup/) vault if configured in the `organization-config.yaml` file

## LogArchive account
<a name="logarchive-account"></a>
+  **Central logs key** - used to encrypt the `aws-accelerator-central-logs` Amazon S3 bucket
**Note**
This key is distinct from the per-account/Region key because additional services such as Config, CloudTrail, and log delivery require access. Macie, GuardDuty, and Audit Manager might also require access, if activated.
+  **Log replication key** - used to encrypt a Kinesis Data Stream used as a destination for log replication from CloudWatch Logs to Amazon S3

## Audit account
<a name="audit-account"></a>
+  **Accelerator KMS key** - used by the entire organization to decrypt AWS Systems Manager parameters (SSM parameters) stored centrally in the **Audit** account
+  **Audit S3 key** - used to encrypt authorize-created CloudTrail Amazon S3 buckets and Audit Manager publishing bucket, if configured
+  **Amazon SNS key (optional)** - used to encrypt Amazon SNS topics created to alert on security events, if configured

## Key retention policy
<a name="key-retention-policy"></a>

The solution sets a `RETAIN` removal policy on every customer-data-bearing KMS key listed above. This applies across all stacks (`Prepare`, `Key`, `Logging`, `Security`, `Operations`, `Network`) and all account types (`Management`, `LogArchive`, `Audit`, and workload accounts). The retention policy is applied even on initial-create rollback, which means a KMS key created during a failed deployment is preserved rather than discarded by AWS CloudFormation.

This is a deliberate design choice. The KMS keys provisioned by the solution encrypt data at rest in CloudWatch Logs, Amazon S3 buckets, AWS Lambda environment variables, AWS Systems Manager Session Manager logs, Amazon EBS volumes, AWS Backup vaults, and the central audit logs in the LogArchive account. Some of this data falls under regulatory retention requirements that span multiple years. Allowing AWS CloudFormation to discard a KMS key would render any data already encrypted under that key permanently unreadable, including data needed to demonstrate compliance.

**Note**
The `RETAIN` policy is the default for all customer-data-bearing CMKs in this solution and is not configurable. Keys are preserved on stack rollback, stack deletion, and account removal.

## Orphaned KMS keys
<a name="orphaned-kms-keys"></a>

After a failed deployment, a deleted stack, or an account removal, you might find KMS keys in your account with the following characteristics:
+ No alias attached. AWS KMS aliases are created in the same stack as the key and are removed when that stack rolls back, even though the key itself is retained.
+ The `Accelerator` tag (or your configured prefix) and a creation timestamp that matches the failed deployment.
+ A status of **Enabled**. The key is active and continues to incur a monthly key-storage charge. See [AWS KMS pricing](https://aws.amazon.com/kms/pricing/) for current rates.

These keys do not block subsequent deployments. A successful redeploy creates fresh keys with their aliases attached. The orphaned keys remain in your account until you decide how to handle them.

## Cleanup options for orphaned keys
<a name="cleanup-options-for-orphaned-keys"></a>

You have three options for handling orphaned KMS keys.

1.  **Leave the keys in place.** This is the safest option. The orphaned keys do not interfere with subsequent deployments and preserve any data that might have been encrypted under them.

1.  **Exclude the keys from cost reports.** Apply a custom tag (for example, `accelerator:status=orphan-cleanup`) to the orphaned keys and filter that tag out of your billing reports. The keys remain available if any retained data needs to be decrypted.

1.  **Schedule the keys for deletion.** Before scheduling deletion, audit AWS CloudTrail for `kms:GenerateDataKey` and `kms:Encrypt` events against each key ID to confirm that no data was encrypted under the key. After you confirm the key was unused, schedule deletion with a 30-day pending window so that you can cancel the deletion if you discover that the key is needed.

   ```
   aws kms schedule-key-deletion --key-id <key-id> --pending-window-in-days 30
   ```

**Important**
Scheduling a KMS key for deletion is irreversible after the pending window expires. Any data encrypted under a deleted key becomes permanently unreadable. Always audit AWS CloudTrail before scheduling deletion, and prefer the maximum 30-day pending window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

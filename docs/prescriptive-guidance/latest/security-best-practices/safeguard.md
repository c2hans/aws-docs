---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/safeguard.html
---

# Step 6. Safeguard backups using immutable storage
<a name="safeguard"></a>

Organizations can use immutable storage to write data in a Write Once Read Many (WORM) state. While in a WORM state, data can be written one time, and read and used as often as needed after it has been committed or written to the storage medium. Immutable storage helps to ensure that data integrity is maintained. It also provides protection against the following:
+ Deletes
+ Overwrites
+ Inadvertent and unauthorized access
+ Ransomware compromise

Immutable storage offers an efficient mechanism to address potential security events that might have real impacts on your business operations.

You can use immutable storage for better governance when paired with strong SCP restrictions. You can also use immutable storage in a compliance WORM mode when the letter of the law (such as a legal hold) requires access to immutable data.

To maintain data availability and integrity, you can use  [AWS Backup Vault Lock](https://aws.amazon.com/blogs/storage/enhance-the-security-posture-of-your-backups-with-aws-backup-vault-lock/) to protect your backups. When you use AWS Backup Vault Lock, unauthorized entities can't erase, alter, or corrupt your customer or business data during the required retention period. AWS Backup Vault Lock helps you meet your organization's data protection policies by preventing the following:
+ Deletions by privileged users (including the AWS account root user)
+ Changes to your backup lifecycle settings
+ Updates that alter your defined retention period

AWS Backup Vault Lock ensures immutability and adds an additional layer of defense that protects backups (recovery points) in your backup vaults. This is especially useful in highly regulated industries that have stringent integrity needs for backups and archives. AWS Backup Vault Lock makes sure your data is preserved along with a backup to recover from in case of unintended or malicious actions.

**Important**

+ AWS Backup Vault Lock has not yet been assessed for compliance with the Securities and Exchange Commission (SEC) rule 17a-4(f) and the Commodity Futures Trading Commission (CFTC) in regulation 17 C.F.R. 1.31(b)-(c).
+ AWS Backup Vault Lock takes effect immediately. It gives you a *minimum three-day (72-hour) cooling-off period* to delete or update its configuration before it permanently locks your vault. You can optionally extend the duration of this cooling-off period. Use this cooling-off period to test AWS Backup Vault Lock against your workloads and use cases. After your cooling-off period expires, neither you nor AWS Support can delete or otherwise alter AWS Backup Vault Lock or the contents of your locked vault. For more information, see the documentation on [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

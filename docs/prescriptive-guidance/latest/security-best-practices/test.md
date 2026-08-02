---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/test.html
---

# Step 9. Test data recovery capabilities
<a name="test"></a>

Your backup strategy must include testing your backups. A backup strategy is not effective if backed up data cannot be restored. Regularly test your ability to find certain [recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html) and restore them.

While AWS Backup automatically copies tags from the resources it protects to the  recovery points, tags are not by default copied from recovery points to the corresponding restored resources. To scale your inventory management and locate recovery points, consider using AWS Backup events to [initiate a tag replication process](https://aws.amazon.com/blogs/storage/how-to-retain-resource-tags-in-aws-backup-restore-jobs/)  on resources created by AWS Backup restore jobs.

You can start your data recovery workflow by establishing data recovery patterns and then regularly testing them. To increase confidence in your ability to recover backup data, create a basic, repeatable process for performing continuous data recovery testing. For example, you can create a pattern to test a cross-account, cross-Region restore operation from a central DR backup vault encrypted with a customer-managed AWS KMS key to a source account backup vault encrypted with a different customer-managed AWS KMS key.

If you don't frequently test such restore operations, you might find that your assumptions on AWS KMS encryption for cross-account, cross-Region operations are incorrect. Often, the only backup recovery pattern that actually works is the path you test frequently. Through routine testing of supported backup resource types, you can spot early warnings that could potentially cause future disturbances and loss of critical data. If possible, maintain a limited but feasible number of recovery paths and patterns to prevent wasted storage space, optimize costs, and save time. Fixing the problem when a recovery test fails is easier than losing valuable or critical data.

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/appendix-c-backup-and-recovery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix C: Backup and recovery
<a name="appendix-c-backup-and-recovery"></a>

 Recovering from failure in AWS is faster and easier to do compared to traditional hosting environments. For example, you can launch a replacement instance in minutes in response to a hardware failure, or you can make use of automated failover in many of our managed services to negate the impact of a reboot due to routine maintenance.

 However, you still need to ensure you are backing up the right data in order to successfully recover it. To re-establish the availability of a WordPress website, you must be able to recover the following components:
+  Operating system (OS) and services installation and configuration (Apache, MySQL, and so on)
+  WordPress application code and configuration
+  WordPress themes and plugins
+  Uploads (for example, media files for posts)
+  Database content (posts, comments, and so on)

AWS provides a variety of methods for backing up and restoring your web application data and assets.

This whitepaper previously discussed making use of Lightsail snapshots to protect all data stored on the instance’s local storage. If your WordPress website runs off the Lightsail instance only, regular Lightsail snapshots should be sufficient for you to recover your WordPress website in its entirety. However, you will still lose any changes applied to your website since the last snapshot was taken if you do restore from a snapshot.

 In a multi-server deployment, you need to back up each of the components discussed earlier using different mechanisms. Each component may have a different requirement for backup frequency, for example, the OS and WordPress installation and configuration will change much less frequently than user-generated content and, therefore, can be backed up less frequently without losing data in the event of a recovery.

 To back up the OS and services installation and configuration, and the WordPress application code and configuration, you can create an AMI of a properly configured EC2 instance. AMIs can serve two purposes: to act as a backup of instance state, and to act as a template when launching new instances.

 To back up the WordPress application code and configuration, you need to make use of AMIs and also Aurora backups.

 To back up the WordPress themes and plugins installed on your website, back up the Amazon S3 bucket or the Amazon EFS file system they are stored on.
+  For themes and plugins stored in an S3 bucket, you can enable [Cross-Region replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) so that all objects uploaded to your primary bucket are automatically replicated to your backup bucket in another AWS Region. Cross-Region Replication requires that [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) is enabled on both your source and destination buckets, which provides you with an additional layer of protection and allows you to revert to a previous version of any given object in your bucket.
+  For themes and plugins stored on an EFS file system, you can create an AWS Data Pipeline to copy data from your production EFS file system to another EFS file system, as outlined in the documentation page [Backing up your Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/efs-backup-solutions.html). You can also back up an EFS file system using any backup application you are already familiar with.
+  To back up user uploads you should follow the steps outlined earlier for backing up the WordPress themes and plugins.
+  To back up database content you need to make use of [Aurora backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Managing.html#Aurora.Managing.Backups). Aurora backs up your cluster volume automatically and retains restore data for the length of the *backup retention period*. Aurora backups are continuous and incremental so you can quickly restore to any point within the backup retention period. No performance impact or interruption of database service occurs as backup data is being written. You can specify a backup retention period from 1 to 35 days. You can also create [manual database snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html), which persist until you delete them. Manual database snapshots are useful for long-term backups and archiving.

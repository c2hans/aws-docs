---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/data-protection-key-rotation.html
---

# Key rotation for AWS KMS and scope of impact
<a name="data-protection-key-rotation"></a>

We do not recommend AWS Key Management Service (AWS KMS) key rotation unless you are required to rotate keys for regulatory compliance. For example, you might be required to rotate your KMS keys due to business policies, contract rules, or government regulations. The design of AWS KMS significantly reduces the types of risk that key rotation is typically used to mitigate. If you must rotate KMS keys, we recommend that you use automatic key rotation and use manual key rotation only if automatic key rotation is not supported.

**This section discusses the following key rotation topics:**
+ [AWS KMS symmetric key rotation](#data-protection-key-rotation-symmetric)
+ [Manual key rotation for Amazon EBS volumes](#data-protection-key-rotation-ebs)
+ [Key rotation for Amazon RDS](#data-protection-key-rotation-rds)
+ [Key rotation for Amazon S3 and Same-Region Replication](#data-protection-key-rotation-s3)
+ [Rotating KMS keys with imported material](#data-protection-key-rotation-imported)

## AWS KMS symmetric key rotation
<a name="data-protection-key-rotation-symmetric"></a>

AWS KMS supports [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) only for symmetric encryption KMS keys with key material that AWS KMS creates. Automatic rotation is optional for customer managed KMS keys. On an annual basis, AWS KMS rotates the key material for AWS managed KMS keys. AWS KMS saves all previous versions of the cryptographic material in perpetuity, so you can decrypt any data that is encrypted with that KMS key. AWS KMS does not delete any rotated key material until you delete the KMS key. Also, when you decrypt an object by using AWS KMS, the service determines the correct backing material to use for the decrypt operation; no additional input parameters need to be supplied.

Because AWS KMS retains previous versions of the cryptographic key material and because you can use that material to decrypt data, key rotation doesn't provide any additional security benefits. The key rotation mechanism exists to make it easier to rotate keys if you are operating a workload in a context where regulatory or other requirements demand it.

## Key rotation for Amazon EBS volumes
<a name="data-protection-key-rotation-ebs"></a>

You can rotate Amazon Elastic Block Store (Amazon EBS) data keys by using one of the following approaches. The approach depends on your workflows, deployment methods, and application architecture. You might want to do this when changing from an AWS managed key to a customer managed key.

**To use operating system tools to copy the data from one volume to another**

1. Create the new KMS key. For instructions, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).

1. Create a new Amazon EBS volume that is the same size as or larger than the original. For encryption, specify the KMS key that you created. For instructions, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html).

1. Mount the new volume on the same instance or container as the original volume. For instructions, see [Attach an Amazon EBS volume to an Amazon EC2 instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html).

1. Using your preferred operating system tool, copy data from the existing volume to the new volume.

1. When the sync is complete, during a pre-scheduled maintenance window, stop the traffic to the instance. For instructions, see [Manually stop and start your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#starting-stopping-instances).

1. Unmount the original volume. For instructions, see [Detach an Amazon EBS volume from an Amazon EC2 instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html).

1. Mount the new volume to the original mount point.

1. Verify that the new volume is operating correctly.

1. Delete the original volume. For instructions, see [Delete an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html).

**To use an Amazon EBS snapshot to copy the data from one volume to another**

1. Create the new KMS key. For instructions, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).

1. Create an Amazon EBS snapshot of the original volume. For instructions, see [Create Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-snapshot.html).

1. Create a new volume from the snapshot. For encryption, specify the new KMS key that you created. For instructions, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html).
**Note**
Depending on your workload, you might want to use [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html) to minimize initial latency on the volume.

1. Create a new Amazon EC2 instance. For instructions, see [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html).

1. Attach the volume that you created to the Amazon EC2 instance. For instructions, see [Attach an Amazon EBS volume to an Amazon EC2 instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html).

1. Rotate the new instance into production.

1. Rotate the original instance out of production and delete it. For instructions, see [Delete an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html).

**Note**
It is possible to copy snapshots and modify the encryption key used for the target copy. After you copy the snapshot and encrypt it with your preferred KMS keys, you can also create an Amazon Machine Image (AMI) from snapshots. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the Amazon EC2 documentation.

## Key rotation for Amazon RDS
<a name="data-protection-key-rotation-rds"></a>

For some services, such as Amazon Relational Database Service (Amazon RDS), data encryption occurs within the service and is provided by AWS KMS. Use the following instructions to rotate a key for an Amazon RDS database instance.

**To rotate a KMS key for an Amazon RDS database**

1. Create a snapshot of the original encrypted database. For instructions, see [Managing manual backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.html) in the Amazon RDS documentation.

1. Copy the snapshot to a new snapshot. For encryption, specify the new KMS key. For instructions, see [Copying a DB snapshot for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html).

1. Use the new snapshot to create a new Amazon RDS cluster. For instructions, see [Restoring to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the Amazon RDS documentation. By default, the cluster uses the new KMS key.

1. Verify the operation of the new database and the data in it.

1. Rotate the new database into production.

1. Rotate the old database out of production and delete it. For instructions, see [Deleting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).

## Key rotation for Amazon S3 and Same-Region Replication
<a name="data-protection-key-rotation-s3"></a>

For Amazon Simple Storage Service (Amazon S3), to change the encryption key of an object, you need to read and rewrite the object. When you rewrite the object, you explicitly specify the new encryption key in the write operation. To do this for many objects, you can use [Amazon S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html). Within the job settings, for the copy operation, specify the new encryption settings. For example, you might choose **SSE-KMS** and enter the **keyId**.

Alternatively, you could use [Amazon S3 Same-Region Replication (SRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#srr-scenario). SSR can re-encrypt the objects in transit.

## Rotating KMS keys with imported material
<a name="data-protection-key-rotation-imported"></a>

AWS KMS does not recover or rotate your [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-conceptual.html#import-keys-protect). To rotate a KMS key with imported key material, you must [rotate the key manually](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-manually).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

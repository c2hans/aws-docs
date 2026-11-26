---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-controller-resiliency-slurm.html
---

# Slurm controller node resiliency

SageMaker HyperPod persists Slurm controller node state on a service-managed and service-owned Amazon Elastic File System (Amazon EFS) file system, without extra costs to you, so that controller state survives node replacement, software updates, and reboots. A Slurm cluster that meets the prerequisites gets a dedicated Amazon EFS file system that HyperPod provisions, mounts, secures, monitors, and deletes on your behalf. The controller's Slurm state (the pending job queue, node and partition state, Slurm configuration, and accounting database) lives on this durable, instance-independent storage instead of the controller's root volume.

Because controller state no longer shares the root volume's lifecycle, you gain two capabilities:
+ Self-service controller node replacement through the `BatchReplaceClusterNodes` API and the SageMaker AI console, the same way you replace a worker node.
+ State preservation across software updates (`UpdateClusterSoftware`) and reboots. The job queue, configuration, and accounting history are retained automatically.

For new clusters that meet the prerequisites, this experience is zero-configuration. There is no file system to provide, no mount to configure, and no cluster setting to change. Slurm reads and writes its state through the same paths it always has (`/opt/slurm/etc`, `/var/spool/slurmctld`), which now resolve to Amazon EFS transparently.

## Prerequisites
<a name="sagemaker-hyperpod-controller-resiliency-slurm-prerequisites"></a>

Controller node resiliency requires both of the following:
+ API-driven Slurm configuration. The cluster must define its Slurm topology through the `CreateCluster` and `UpdateCluster` API requests. Clusters that use the legacy `provisioning_parameters.json` file are not supported. They are created as they are today, receive no service-managed Amazon EFS file system, and retain the existing controller behavior. For a comparison of the two approaches, see [SageMaker HyperPod Slurm configuration](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration).
+ A cluster created with a HyperPod AMI released on or after November 23, 2026. HyperPod provisions the service-managed Amazon EFS file system when it creates the cluster, and the AMI includes the controller state mount logic. Clusters created with an earlier AMI do not have the file system and keep the existing controller behavior.

**Note**
A cluster that does not meet both prerequisites continues to operate as it does today: controller state remains on the root volume, controller nodes are not valid replacement targets, and state is not persisted across replacement or a software update. This includes clusters created with an AMI released before November 23, 2026. Updating the software of those clusters does not add controller node resiliency.

## How controller state persistence works
<a name="sagemaker-hyperpod-controller-resiliency-slurm-how-it-works"></a>

In HyperPod clusters orchestrated with Slurm, the controller node runs the `slurmctld` daemon and owns the operational state of the cluster: the pending job queue, node and partition state, Slurm configuration (`slurm.conf`, `gres.conf`, and any include files or custom scripts), and the `slurmdbd` accounting database.

With controller node resiliency, HyperPod redirects these state directories onto a dedicated, service-managed Amazon EFS file system rather than leaving them on the controller instance's root volume. Because the file system has its own lifecycle, independent of any instance, the state remains available when the controller's root volume is rebuilt or the instance itself is replaced. A replacement controller mounts the same file system and resumes from the state already on it, so the job queue, configuration, and accounting history carry forward across node replacement, software updates, and reboots.

**Note**
Without controller node resiliency, all of this state lives on the controller instance's root volume and shares that volume's lifecycle. It therefore does not survive either of the two operations HyperPod performs on a controller, because both rebuild the root volume: node replacement brings up a new instance from the AMI with a fresh root volume, and a software update (`UpdateClusterSoftware`) replaces the root volume in place, keeping the instance ID but rebuilding the volume from the target AMI. This is also the behavior for clusters that are not covered by the feature. Clusters configured with the legacy `provisioning_parameters.json` file receive no service-managed Amazon EFS file system and keep controller state on the root volume, and the same is true for clusters created with an AMI released before November 23, 2026. For details, see [Prerequisites](#sagemaker-hyperpod-controller-resiliency-slurm-prerequisites).

### The mount and the redirected directories
<a name="sagemaker-hyperpod-controller-resiliency-slurm-how-it-works-mount"></a>

During node provisioning, before `slurmctld` starts, HyperPod mounts the cluster's dedicated Amazon EFS file system at `/mnt/sagemaker-controller` on the controller node, then replaces the standard Slurm state directories with symbolic links that point into that mount. The well-known paths continue to work unchanged. They now resolve onto Amazon EFS.

The following directories are redirected onto Amazon EFS:

| Standard path | What lives here |
| --- | --- |
| /opt/slurm/etc | slurm.conf, gres.conf, include files, and custom scripts |
| /var/spool/slurmctld | Live cluster state: the pending job queue and node and partition state |
| /var/lib/mysql | MariaDB data directory backing slurmdbd accounting (job history, user associations, and cluster usage). Persisted on the primary controller only. |

Because a symbolic link is resolved by the operating system below the application layer, any process that opens a file under these paths (`slurmctld`, the `scontrol` CLI, your own scripts, or a text editor) reads and writes the Amazon EFS-backed file without being aware of the redirection. Your workflow does not change. You continue to use `/opt/slurm/etc` and `/var/spool/slurmctld` exactly as before, and the data is now durable because it lives on Amazon EFS rather than the root volume.

### What persists and what does not
<a name="sagemaker-hyperpod-controller-resiliency-slurm-how-it-works-persists"></a>

Persistence comes from a file living under an Amazon EFS-backed path. Anything written under `/opt/slurm/etc` or `/var/spool/slurmctld` is on Amazon EFS and persists. Anything written elsewhere on the root volume (extra packages, a script under `/usr/local`, or data written outside the redirected directories) is not on Amazon EFS and is lost on replacement or a software update, the same as before this feature.

Keep your Slurm configuration and include files under `/opt/slurm/etc`, which is both the conventional location and the one that is now durable.

### Accounting database persistence
<a name="sagemaker-hyperpod-controller-resiliency-slurm-how-it-works-accounting"></a>

Slurm's `slurmdbd` accounting database (job history, user associations, and cluster usage) is backed by a MariaDB data directory that is relocated onto the same Amazon EFS file system on the primary controller. On a fresh cluster, HyperPod initializes an empty database on Amazon EFS; on replacement or a software update, the existing database is reused as-is, so accounting history carries forward.

**Note**
Accounting is persisted on the primary controller only. It survives replacement, a software update, and reboot of that controller, but it does not automatically fail over to a backup controller in a multi-controller cluster. High availability of the accounting database across controllers requires an external Slurm database and is a separate feature.

### Editing Slurm configuration directly
<a name="sagemaker-hyperpod-controller-resiliency-slurm-how-it-works-edit-config"></a>

If you customize Slurm by editing configuration files on the controller node directly, your workflow is unchanged. You continue to edit files under `/opt/slurm/etc`, and those edits now persist across controller replacement and software updates instead of being lost.

The following shell commands expose several partitions through an include file. Replace the partition names and node ranges with the values for your cluster:

```sh
# Create an include file with your partition definitions.
cat > /opt/slurm/etc/partitions.conf <<'EOF'
PartitionName=cpu   Nodes=ip-10-1-1-[10-20]   Default=YES MaxTime=INFINITE State=UP
PartitionName=gpu   Nodes=ip-10-1-2-[10-25]   Default=NO  MaxTime=INFINITE State=UP
PartitionName=debug Nodes=ip-10-1-1-[21-22]   Default=NO  MaxTime=01:00:00 State=UP
EOF

# Reference it from slurm.conf.
echo 'Include /opt/slurm/etc/partitions.conf' >> /opt/slurm/etc/slurm.conf

# Apply the change.
scontrol reconfigure
```

Because `/opt/slurm/etc` is backed by Amazon EFS, both `slurm.conf` and `partitions.conf` are written to Amazon EFS automatically. When the controller is later replaced or updated, the new controller mounts the same Amazon EFS, finds both files already present, and `slurmctld` comes up with your multi-partition layout intact, with no need to reapply the customization.

**Note**
Slurm provides controller high availability through multiple `SlurmctldHost` entries in `slurm.conf`: the first is the primary and each additional entry is a backup that takes over if the primary fails. Slurm requires that all controllers share a common file system for the state save location (`StateSaveLocation`, that is, `/var/spool/slurmctld`). The service-managed Amazon EFS file system meets that requirement: every controller in the cluster mounts the same file system, so the primary and backup controllers share live state and a single `slurm.conf`. Shared state alone does not make every part of Slurm high availability turnkey: the accounting database is persisted on the primary controller only and does not fail over, `SlurmctldHost` entries must list the controllers for failover to engage, and there is a brief window of non-responsiveness during failover while the backup takes over.

## Replace a Slurm controller node
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace"></a>

With controller node resiliency, controller nodes are valid targets for the standard node-replacement workflow. You initiate a controller replacement yourself, the same way you replace a worker node, and the replacement controller resumes from the Slurm state persisted on the Amazon EFS file system.

Replacement requires both that the cluster uses API-driven Slurm configuration and that it was created with a HyperPod AMI released on or after November 23, 2026. Clusters that do not meet both prerequisites keep the existing behavior: controller nodes are not valid replacement targets, and recovering one requires an AWS Support case, after which Slurm state is not carried over. For more information, see [Prerequisites](#sagemaker-hyperpod-controller-resiliency-slurm-prerequisites).

### What happens during replacement
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace-what-happens"></a>

When you replace a controller node, HyperPod:
+ Launches the replacement controller and re-mounts the cluster's existing Amazon EFS file system. The state from the previous controller is already on it.
+ Updates the controller node IP address across the cluster's internal configuration so that compute nodes automatically reconnect to the new controller.
+ Resumes `slurmctld` with the complete preserved state: pending jobs, node and partition state, your Slurm configuration, and accounting history.

Running jobs on compute nodes are unaffected throughout the replacement, and compute nodes reconnect to the new controller on their own.

**Note**
Controller replacement is a manual action that you initiate. HyperPod does not replace a controller node automatically, which gives you the opportunity to copy data off the existing controller before it is replaced.

### Before you replace your controller node
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace-before"></a>

The Amazon EFS file system holds the Slurm state under the redirected directories only. Your Slurm configuration, pending job queue, node and partition state, and accounting history are on it and carry forward to the replacement controller. Anything you added elsewhere on the controller's root volume is not, and is gone once the node is replaced. Because replacement is a deliberate action you initiate, copy that data off the existing controller first (to Amazon S3, Amazon FSx for Lustre, or another shared file system) and plan to reapply anything that was installed or configured outside the Slurm directories.

Some examples of data and customizations that are commonly kept outside the redirected directories are the following. Review your own controller for anything else your team has added.
+ Packages and drivers installed with `apt`, `pip`, or `conda`, and any Conda or Python virtual environments created on the root volume.
+ Scripts, binaries, and cron jobs under paths such as `/usr/local/bin`, `/opt`, or `/etc/cron.d`.
+ User home directories under `/home`, including SSH keys, shell profiles, and job submission scripts.
+ Prolog and epilog scripts, or other helper scripts referenced by `slurm.conf` but stored outside `/opt/slurm/etc`.
+ Local logs and job output files written to the root volume rather than to a shared file system.
+ Credentials, certificates, and configuration for third-party monitoring or logging agents.

**Tip**
To avoid this work on future replacements, keep customizations in lifecycle scripts so they are reapplied automatically when a node is provisioned, and keep Slurm configuration and include files under `/opt/slurm/etc`, which is backed by the Amazon EFS file system. For more information, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

### Replace a controller node using the console
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace-console"></a>

You can replace a controller node from the same node-actions interface you use to reboot and replace worker nodes. The following procedure replaces a controller node and resumes it from the Slurm state persisted on the Amazon EFS file system.

**To replace a controller node using the console**

1. Open the SageMaker AI console at [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. In the navigation pane, under **HyperPod**, choose **Clusters**, and then choose the name of your cluster.

1. In the cluster's node list, choose the controller node that you want to replace.

1. Choose the replace action.
**Warning**
Before you choose the replace action, confirm that you copied any data that you need off the root volume of the controller. For more information, see [Before you replace your controller node](#sagemaker-hyperpod-controller-resiliency-slurm-replace-before).

After you choose the replace action, HyperPod launches a replacement controller that mounts the same Amazon EFS file system, and compute nodes reconnect to the new controller on their own.

### Replace a controller node using the replace API
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace-api"></a>

Use the `BatchReplaceClusterNodes` API to replace a controller node. In the following AWS Command Line Interface command, replace {{<cluster-arn>}} with the ARN of your cluster and {{<node-id>}} with the ID of the controller node that you want to replace:

```sh
aws sagemaker batch-replace-cluster-nodes \
    --cluster-name {{<cluster-arn>}} \
    --node-ids {{<node-id>}}
```

### After replacement
<a name="sagemaker-hyperpod-controller-resiliency-slurm-replace-after"></a>

Reapply the customizations you identified before the replacement, and restore any data you copied off the previous controller. For details on which paths are backed by the Amazon EFS file system, see [How controller state persistence works](#sagemaker-hyperpod-controller-resiliency-slurm-how-it-works).

## Manage controller storage
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage"></a>

The controller Amazon EFS file system is sized for Slurm state, which stays well under the storage limit for a typical cluster. Amazon EFS auto-scales with no hard ceiling, so HyperPod applies usage guardrails to keep the shared, service-managed storage used for its intended purpose. If you operate Slurm normally, you will not encounter these limits.

### Storage limit
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage-limit"></a>

The controller storage is for Slurm state and configuration. The storage limit is 5 GB. Do not use the controller mount (`/mnt/sagemaker-controller`) as general-purpose storage for training data, datasets, or logs. Store that data on Amazon S3, Amazon FSx for Lustre, or another shared file system.

HyperPod monitors controller storage and notifies you well before any enforcement, through the AWS Health Dashboard, email to your account contacts, and an on-login message on the controller node. The storage limit is configurable per cluster when there is an approved need; notifications render the applicable limit for your cluster along with the cluster name and ARN.

### Notifications as storage grows
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage-notifications"></a>

HyperPod sends notifications through the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html) (visible in the console with no setup required) and by email to your account contacts. The same events are delivered to your default EventBridge bus as `aws.health` events.

| Stage | Usage level | What you see | Service behavior |
| --- | --- | --- | --- |
| Early warning | 2 GB | AWS Health notification and a yellow on-login message advising you to clean up unused files. | No change to access. |
| Storage limit reached | 5 GB | Critical AWS Health notification and a red on-login message warning that write access will be revoked if usage is not reduced. | Writes remain available for a short period so you have time to clean up. |
| Write access revoked | Above the limit | Write-revoked AWS Health notification directing you to AWS Support. | Amazon EFS write access is revoked. Read access and running jobs remain available. |

The 5 GB limit is the value you should operate against and the target you must return below when you clean up. Reduce usage below 5 GB during the early-warning and critical stages to avoid an interruption to new job submissions.

### On-login message
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage-motd"></a>

When controller storage crosses the warning threshold, HyperPod adds a storage notice to the controller node's login banner (the message of the day, or MOTD), so anyone who connects over SSH or SSM sees it immediately. The notice shows a yellow warning while usage approaches the 5 GB limit and a red critical message once the limit is exceeded, along with the live usage value at login. The following example shows the on-login message:

```
Controller EFS usage: 2.1G
  Write access will be revoked if usage exceeds 5 GB.
  Do not remove system directories: slurmctld/, slurm.conf, mysql/
  Please remove any user-added files from /mnt/sagemaker-controller.
```

### What write-access revocation means
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage-revocation"></a>

If write access is revoked, the cluster keeps running and read access is preserved. The behavior is deliberately non-disruptive to running work.

The following continue to work while write access is revoked:
+ Running jobs on compute nodes are unaffected.
+ `slurmctld` stays up and serves read queries such as `squeue` and `sinfo`.
+ SSH to the controller works.
+ Controller node replacement still works.

The following are restricted until you reduce storage below the limit:
+ New `sbatch` job submissions fail because `slurmctld` cannot write job state.
+ Job completion logging and `slurm.conf` changes are blocked.
+ Deleting files from the Amazon EFS file system is blocked, because a delete is itself a write. You cannot remove the excess files until write access is restored.

### Restore write access and clean up
<a name="sagemaker-hyperpod-controller-resiliency-slurm-storage-restore"></a>

Because the file system policy is enforced server-side by Amazon EFS, you cannot restore writes yourself from the controller, even with root. Use the following procedure:

**To restore write access and clean up**

1. Inspect usage on the controller to identify what filled the file system, typically non-Slurm files under `/mnt/sagemaker-controller`. The read-only inspection commands work even while write access is revoked, so you can plan the cleanup first. For the exact commands, see [Freeing up space on your HyperPod cluster's controller storage](#sagemaker-hyperpod-controller-resiliency-slurm-freeing-space).

1. Open an AWS Support case for the affected cluster, referencing the cluster identifier from the notification.

1. AWS Support temporarily restores write access and starts a 24-hour grace period during which writes stay enabled.

1. Within the grace period, connect to the controller and delete the excess files you added under `/mnt/sagemaker-controller` to bring usage below the 5 GB limit.

1. Storage is re-evaluated automatically on the next monitoring sweep. Once usage is below the limit, enforcement clears and normal read/write operation resumes. If usage is still above the limit when the grace period ends, write access is revoked again.

**Warning**
The HyperPod-managed directories under the controller mount must not be deleted or modified. Removing them can cause job loss, accounting-data loss, or an unrecoverable cluster. These are the Slurm state directory (`/var/spool/slurmctld`), the Slurm configuration directory (`/opt/slurm/etc`), and the accounting database directory (`/var/lib/mysql`). Delete only the non-Slurm data you added.

To avoid recurrence, store datasets, checkpoints, and logs on Amazon S3 or Amazon FSx for Lustre, not on the controller storage.

## Freeing up space on your HyperPod cluster's controller storage
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space"></a>

Your Amazon SageMaker AI HyperPod cluster (Slurm orchestration) stores Slurm controller state on an Amazon EFS file system mounted at `/mnt/sagemaker-controller` on the controller node. This storage has a 5 GB limit. If usage exceeds the limit, write access to the file system is revoked and new Slurm job submissions fail until you reduce usage.

Use the following procedure to identify and remove data that you added to the controller storage.

**Warning**
The following directories are managed by SageMaker HyperPod and are required for your cluster to operate. Do not delete or modify them, because deleting files in these directories can cause job loss, accounting-data loss, or an unrecoverable cluster state:
`/var/spool/slurmctld`: Slurm controller state (job queue, node states)
`/opt/slurm/etc`: Slurm configuration
`/var/lib/mysql`: Slurm accounting database

**Note**
If write access to the file system has been revoked, contact AWS Support to restore it before you delete files. You can still run the inspection commands (steps 1 and 2) while write access is revoked. After write access is restored, you have 24 hours to reduce usage below the limit.

### Step 1: Check current usage
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space-step1"></a>

Connect to the controller node using SSH or SSM, then run the following shell command:

```sh
sudo du -sh /mnt/sagemaker-controller
```

### Step 2: Identify what is using space
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space-step2"></a>

List usage by directory, excluding the HyperPod-managed paths. This shows the data that you or your workloads added:

```sh
sudo du -h --max-depth=2 \
  --exclude=/mnt/sagemaker-controller/var/spool/slurmctld \
  --exclude=/mnt/sagemaker-controller/opt/slurm/etc \
  --exclude=/mnt/sagemaker-controller/var/lib/mysql \
  /mnt/sagemaker-controller 2>/dev/null | sort -rh | head -20
```

To list the 20 largest individual files outside the managed paths:

```sh
sudo find /mnt/sagemaker-controller \
  -path /mnt/sagemaker-controller/var/spool/slurmctld -prune -o \
  -path /mnt/sagemaker-controller/opt/slurm/etc -prune -o \
  -path /mnt/sagemaker-controller/var/lib/mysql -prune -o \
  -type f -printf '%s\t%p\n' 2>/dev/null | sort -rn | head -20 | \
  awk -F'\t' '{ printf "%.1f MB\t%s\n", $1/1048576, $2 }'
```

**Note**
These commands can take several minutes on file systems with many files.

### Step 3: Review files before deleting
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space-step3"></a>

List all files outside the managed paths without deleting anything:

```sh
sudo find /mnt/sagemaker-controller \
  -path /mnt/sagemaker-controller/var/spool/slurmctld -prune -o \
  -path /mnt/sagemaker-controller/opt/slurm/etc -prune -o \
  -path /mnt/sagemaker-controller/var/lib/mysql -prune -o \
  -type f -print 2>/dev/null
```

Review the output and confirm the files are safe to remove. If your team stores data you still need (for example, datasets or checkpoints), copy it to Amazon S3 or an Amazon FSx for Lustre file system before deleting it. The controller storage is intended for Slurm controller state only.

### Step 4: Delete the files you identified
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space-step4"></a>

In the following shell commands, replace {{<path-to-file>}} and {{<path-to-directory>}} with the file or directory that you identified in Step 3:

```sh
sudo rm /mnt/sagemaker-controller/{{<path-to-file>}}
sudo rm -r /mnt/sagemaker-controller/{{<path-to-directory>}}
```

To delete files one at a time with a confirmation prompt for each:

```sh
sudo find /mnt/sagemaker-controller \
  -path /mnt/sagemaker-controller/var/spool/slurmctld -prune -o \
  -path /mnt/sagemaker-controller/opt/slurm/etc -prune -o \
  -path /mnt/sagemaker-controller/var/lib/mysql -prune -o \
  -type f -exec rm -i {} \;
```

### Step 5: Verify usage is below the limit
<a name="sagemaker-hyperpod-controller-resiliency-slurm-freeing-space-step5"></a>

```sh
sudo du -sh /mnt/sagemaker-controller
```

Confirm the total is below 5 GB. Storage usage is re-evaluated automatically; if usage remains above the limit after the 24-hour window following a write-access restore, write access is revoked again.

To avoid recurrence, store datasets, checkpoints, logs, and other workload data on Amazon S3, Amazon FSx for Lustre, or instance storage instead of the controller storage.

---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY.html
---

# BOOTSTRAP\_FAILURE\_INSUFFICIENT\_DISK\_SPACE\_PRIMARY
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY"></a>

## Overview
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY_overview"></a>

 The `BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY` error indicates that the primary instance does not have enough disk space when installing necessary software.

## Resolution
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY_resolution"></a>

 To resolve this error, confirm that your primary instance has sufficient disk space on the root volume.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`primary-instance-id`**
The ID of the primary instance with insufficient disk space.

**`public-doc`**
The public URL of the documentation for the error code.

## Steps to complete
<a name="BOOTSTRAP_FAILURE_INSUFFICIENT_DISK_SPACE_PRIMARY_stc"></a>

1.  Review the best practices for your cluster’s EBS root device volume. See [Customizing the Amazon EBS root device volume](emr-custom-ami-root-volume-size.md) in the *Amazon EMR Management Guide*.

1. Launch a new cluster with a larger EBS root device volume size.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

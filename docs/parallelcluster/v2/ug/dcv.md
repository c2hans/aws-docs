---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/dcv.html
---

# Connect to the head node through Amazon DCV
<a name="dcv"></a>

Amazon DCV is a remote visualization technology that enables users to securely connect to graphic-intensive 3D applications that are hosted on a remote high-performance server. For more information, see [Amazon DCV](https://docs.aws.amazon.com/dcv/).

Amazon DCV software is automatically installed on the head node when using [`base_os`](cluster-definition.md#base-os)` = alinux2`, [`base_os`](cluster-definition.md#base-os)` = centos7`, [`base_os`](cluster-definition.md#base-os)` = ubuntu1804` or [`base_os`](cluster-definition.md#base-os)` = ubuntu2004`.

If the head node is an ARM instance, the Amazon DCV software is automatically installed on it when using [`base_os`](cluster-definition.md#base-os)` = alinux2`, [`base_os`](cluster-definition.md#base-os)` = centos7`, or [`base_os`](cluster-definition.md#base-os)` = ubuntu1804`.

To enable Amazon DCV on the head node, [`dcv_settings`](cluster-definition.md#dcv-settings) must contain the name of a [`[dcv]` section](dcv-section.md) that has [`enable`](dcv-section.md#dcv-section-enable)` = master` and [`base_os`](cluster-definition.md#base-os) must be set to `alinux2`, `centos7`, `ubuntu1804`, or `ubuntu2004`. If the head node is an ARM instance, [`base_os`](cluster-definition.md#base-os) must be set to `alinux2`, `centos7`, or `ubuntu1804`. This way, AWS ParallelCluster sets the cluster configuration parameter [`shared_dir`](cluster-definition.md#cluster-shared-dir) to the [DCV server storage folder](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-storage.html).

```
[cluster custom-cluster]
...
dcv_settings = custom-dcv
...
[dcv custom-dcv]
enable = master
```

For more information about Amazon DCV configuration parameters, see [`dcv_settings`](cluster-definition.md#dcv-settings). To connect to the Amazon DCV session, use the [`pcluster dcv`](pcluster.dcv.md) command.

**Note**
Support for Amazon DCV on `centos8` was removed in AWS ParallelCluster version 2.10.4. Support for Amazon DCV on `centos8` was added in AWS ParallelCluster version 2.10.0. Support for Amazon DCV on AWS Graviton-based instances was added in AWS ParallelCluster version 2.9.0. Support for Amazon DCV on `alinux2` and `ubuntu1804` was added in AWS ParallelCluster version 2.6.0. Support for Amazon DCV on `centos7` was added in AWS ParallelCluster version 2.5.0.

**Note**
Amazon DCV is not supported on AWS Graviton-based instances in AWS ParallelCluster versions 2.8.0 and 2.8.1.

## Amazon DCV HTTPS certificate
<a name="dcv-certificate"></a>

Amazon DCV automatically generates a self-signed certificate to secure traffic between the Amazon DCV client and Amazon DCV server.

To replace the default self-signed Amazon DCV certificate with another certificate, first connect to the head node. Then, copy both the certificate and key to the `/etc/dcv` folder before running the [`pcluster dcv`](pcluster.dcv.md) command.

For more information, see [Changing the TLS certificate](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-cert.html) in the *Amazon DCV Administrator Guide*.

## Licensing Amazon DCV
<a name="dcv-license"></a>

The Amazon DCV server doesn't require a license server when running on Amazon EC2 instances. However, the Amazon DCV server must periodically connect to an Amazon S3 bucket to determine if a valid license is available.

AWS ParallelCluster automatically adds the required permissions to the `ParallelClusterInstancePolicy`. When using a custom IAM Instance Policy, use the permissions described in [Amazon DCV on Amazon EC2](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-license.html#setting-up-license-ec2) in the *Amazon DCV Administrator Guide*.

For troubleshooting tips, see [Troubleshooting issues in Amazon DCV](troubleshooting.md#nice-dcv-troubleshooting).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER.html
---

# BOOTSTRAP\_FAILURE\_HIVE\_METASTORE\_CONNECTION\_ERROR\_WORKER
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER"></a>

## Overview
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER_overview"></a>

 The `BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER` error indicates that one or more worker instances are unable to establish a connection to the configured external Hive Metastore.

## Resolution
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER_resolution"></a>

 To resolve this error, confirm that your external Hive Metastore is configured properly and the worker instances are allowed to connect to it.

To troubleshoot the failed EMR cluster, refer to the `ErrorDetail` information returned from the `DescribeCluster` and `ListClusters` APIs. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md). The `ErrorData` array within `ErrorDetail` returns the following information for this error code:

**`worker-instance-ids`**
The IDs of the worker instances unable to establish a connection to the configured external Hive Metastore.

**`public-doc`**
The public URL of the documentation for the error code.

## Steps to complete
<a name="BOOTSTRAP_FAILURE_HIVE_METASTORE_CONNECTION_ERROR_WORKER_stc"></a>

1.  Review the best practices for for configuring an external metastore for Hive. See [Configuring an external metastore for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-metastore-external-hive.html).

1. Launch a new cluster with your updated cluster configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

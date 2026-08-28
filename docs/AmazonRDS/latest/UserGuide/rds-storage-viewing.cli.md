---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-storage-viewing.cli.html
---

# CLI
<a name="rds-storage-viewing.cli"></a>

To view your storage volume configuration from the AWS CLI, use the `describe-db-instances` command.

```
aws rds describe-db-instances --db-instance-identifier my-database
```

In the output, find the `AdditionalStorageVolumes` array to view details for the added volumes.

```
    "AdditionalStorageVolumes": [
        {
            "VolumeName": "rdsdbdata2",
            "StorageVolumeStatus": "Not-in-use",
            "AllocatedStorage": 5000,
            "IOPS": 25000,
            "StorageThroughput": 500,
            "StorageType": "gp3"
        }
    ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

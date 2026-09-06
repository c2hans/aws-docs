---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/metadata-storage.html
---

# Metadata storage
<a name="metadata-storage"></a>

By default, the guidance deploys an Amazon Aurora PostgreSQL cluster in an isolated subnet to serve as metadata storage for the Druid cluster, ensuring TLS connectivity to secure communication with the DB cluster. It also generates a secret to store the credentials of the DB cluster’s master user. For example, for credentials for the master user of Amazon Aurora cluster.

```
{
        "dbClusterIdentifier": "druidec2stack-<cluster name>-druidmetadataconstructaurorac-<random characters>",
        "password": "<password>",
        "dbname": "DruidMetadata",
        "engine": "postgres",
        "port": 5432,
        "host": "druidec2stack-<cluster name>-druidmetadataconstructaurorac-<random characters>.cluster-<random characters>.<region>.rds.amazonaws.com",
        "username": "druid"
}
```

Aurora automatically backs up your cluster volume and preserves restore data for the duration of the backup retention period. By default, the guidance configures the backup retention period as 14 days.

Aurora automated backups are continuous and incremental, so you can quickly restore to any point within the backup retention period. Additionally, the guidance offers support for using AWS Backup to create backups for the Aurora cluster.

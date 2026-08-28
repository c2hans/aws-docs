---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-s3-prereqs.html
---

# S3 repository prerequisites
<a name="solr-s3-prereqs"></a>

To back up Solr directly to Amazon S3, configure the S3 backup repository on every Solr node before you create the backup. This is required for both workflow-managed Solr backup creation and manual Solr backups that write directly to Amazon S3.

1.  **Install the S3 repository plugin.** Place the `solr-s3-repository` JAR in the shared library directory referenced by `sharedLib` on every node so Solr can load the `org.apache.solr.s3.S3BackupRepository` class:

   ```
   cp /opt/solr/dist/solr-s3-repository-*.jar /opt/solr/contrib/s3-repository/lib/
   ```

1.  **Configure `solr.xml`.** Add a `backup` block with an S3 `repository` and point `sharedLib` at the plugin directory:

   ```
   str name="sharedLib"/opt/solr/contrib/s3-repository/lib/str

   backup
     repository name="s3" class="org.apache.solr.s3.S3BackupRepository" default="true"
       str name="s3.bucket.name"${S3_BUCKET_NAME:}/str
       str name="s3.region"${S3_REGION:us-east-1}/str
       str name="s3.endpoint"${S3_ENDPOINT:}/str
     /repository
   /backup
   ```
**Note**
The repository `name` you set here (`s3`) is the value you reference as `repoName` in the workflow configuration. Keep them identical.

1.  **Set `SOLR_OPTS`.** Supply the bucket, Region, and the security-manager flag that the S3 client requires:

   ```
   export SOLR_OPTS="-DS3_BUCKET_NAME=BUCKET \
                     -DS3_REGION=REGION \
                     -DSOLR_SECURITY_MANAGER_ENABLED=false"
   ```

   If you use a custom S3-compatible endpoint, also set `-DS3_ENDPOINT=S3_ENDPOINT` to the endpoint form accepted by Solr’s S3 client, and set the matching `sourceClusters.source.snapshotInfo.repos.repoName.endpoint` value in the workflow configuration.

1.  **Grant IAM permissions.** The identity Solr uses to reach Amazon S3 must allow the following actions on the backup bucket. Use a least-privilege [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) policy scoped to only the backup bucket and prefix:
   +  `s3:PutObject`
   +  `s3:GetObject`
   +  `s3:DeleteObject`
   +  `s3:ListBucket`
   +  `s3:GetBucketLocation`

1.  **Publish `solr.xml` and restart.** For SolrCloud, upload `solr.xml` to ZooKeeper; for standalone, copy it into the Solr data directory. Then restart each node so it picks up the repository:

   ```
   # SolrCloud
   /opt/solr/bin/solr zk cp PATH_TO_SOLR_XML zk:/solr.xml -z ZK_HOST:2181
   /opt/solr/bin/solr restart -force

   # Standalone
   cp PATH_TO_SOLR_XML /var/solr/data/solr.xml
   /opt/solr/bin/solr restart -force
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

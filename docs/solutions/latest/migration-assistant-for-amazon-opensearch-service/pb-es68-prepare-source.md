---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-prepare-source.html
---

# Step 1: Prepare the source cluster
<a name="pb-es68-prepare-source"></a>

Migration Assistant reads the source data from a snapshot in Amazon S3, so the source cluster must be able to write a snapshot to an S3 repository.

1.  **Install the `repository-s3` plugin** on every node of the source cluster, then restart the nodes one at a time so the cluster stays available:

   ```
   sudo bin/elasticsearch-plugin install repository-s3
   ```

1.  **Grant the source nodes IAM permission to write to the snapshot bucket.** Attach an IAM policy to the instance role used by the Elasticsearch nodes that allows the snapshot operations against your bucket. Replace `<SNAPSHOT_BUCKET>` with your bucket name:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "s3:ListBucket",
           "s3:GetBucketLocation"
         ],
         "Resource": "arn:aws:s3:::<SNAPSHOT_BUCKET>"
       },
       {
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:PutObject",
           "s3:DeleteObject"
         ],
         "Resource": "arn:aws:s3:::<SNAPSHOT_BUCKET>/*"
       }
     ]
   }
   ```

1.  **Register a snapshot repository** named `migration-repo` on the source cluster. Replace `<SNAPSHOT_BUCKET>` and `<REGION>` with your values:

   ```
   curl -X PUT "http://<SOURCE_ENDPOINT>:9200/_snapshot/migration-repo" \
     -H "Content-Type: application/json" -d '{
       "type": "s3",
       "settings": {
         "bucket": "<SNAPSHOT_BUCKET>",
         "base_path": "migration-snapshots",
         "region": "<REGION>"
       }
     }'
   ```

1.  **Verify the repository** so you catch credential or connectivity problems now rather than mid-migration:

   ```
   curl -X POST "http://<SOURCE_ENDPOINT>:9200/_snapshot/migration-repo/_verify"
   ```

   A successful response lists the source nodes that can reach the repository. If verification fails, fix the IAM permissions or network path before continuing.

**Note**
You can let the workflow create and monitor the snapshot by configuring `sourceClusters.<source>.snapshotInfo.snapshots.<snapshot>.config.createSnapshotConfig`. Register `migration-repo` yourself when you want to control the repository name, base path, or bucket explicitly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

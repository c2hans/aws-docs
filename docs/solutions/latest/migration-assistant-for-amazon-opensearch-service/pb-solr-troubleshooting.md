---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-troubleshooting.html
---

# Troubleshooting
<a name="pb-solr-troubleshooting"></a>

| Symptom | What to check |
| --- | --- |
| RFS cannot find or read the backup | Confirm `snapshotInfo.s3RepoPathUri` matches the exact Amazon S3 path you synced the backup to in [Step 1](pb-solr-step1.md), and that the migration IAM role (`<eks-cluster-name>-migrations-role`) can read that bucket and prefix. For SolrCloud, confirm the backup `location` was reachable from every node so the backup is complete. |
| Backfill fails with HTTP 401 or 403 on the target | Verify SigV4 settings. For an Amazon OpenSearch Service domain use `service: es`; for an Amazon OpenSearch Serverless NextGen collection use `service: aoss` and confirm the migration IAM role is in the collection’s data access policy. If the domain uses fine-grained access control, map the migration IAM role to a security role. |
| A Solr field type is not translated as expected | Review the evaluated metadata at the `evaluateMetadata` gate before approving, and supply a custom metadata transformer (`metadataTransforms`) to override the default mapping in [Schema translation reference](pb-solr-schema.md). |
| Target document count is lower than the source | Check the workflow logs with `workflow log all --follow` for bulk-indexing errors. Document counts can legitimately differ if the Solr backup was taken while writes were still occurring — confirm writes were paused before the backup in [Step 1](pb-solr-step1.md). |

For broader diagnostics across all migration phases, see [Troubleshooting](troubleshooting.md).

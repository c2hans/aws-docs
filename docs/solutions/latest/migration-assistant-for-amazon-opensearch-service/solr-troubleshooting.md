---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-troubleshooting.html
---

# Troubleshooting
<a name="solr-troubleshooting"></a>

| Symptom | Resolution |
| --- | --- |
|  `ClassNotFoundException` for `S3BackupRepository`  | The `solr-s3-repository` JAR is missing from the directory referenced by `sharedLib`. Copy the JAR onto every node, then restart Solr. See [S3 repository prerequisites](solr-s3-prereqs.md). |
|  `Repository default-s3 not found` (or `Repository s3 not found`) | The `backup` block with the S3 `repository` is missing from `solr.xml`, or `solr.xml` was not republished after editing. Add the block, publish `solr.xml`, and restart. |
|  `AccessDenied` when writing the backup | The IAM identity Solr uses lacks one of the required Amazon S3 actions. Confirm the policy grants `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`, `s3:ListBucket`, and `s3:GetBucketLocation` on the backup bucket. |
| Replayer running but `requests=0`  | The replayer image does not include Solr transform logic. Verify the replayer image includes the Solr transform JARs. Check the `migration-image-config` ConfigMap. |
| "Could not find provider: SolrToOpenSearchTransformProvider" | Transform JAR not on replayer classpath. Ensure the replayer image was built with Solr transform overlay. Re-run the deploy pipeline if needed. |
| "Failed to parse solrconfig.xml: Content is not allowed in prolog" | File contains ZooKeeper warning output or is JSON from the `/config` endpoint. Re-extract using `solr zk cp` to a temp file, then copy the temp file. |
| Queries for one collection replay with the wrong `match` or `term` behavior | The request is probably using the default schema instead of the collection-specific schema. Add `collection.solrSchemaXml` for that collection, and make sure `collection` exactly matches the name in request paths such as `/solr/collection/select`. |
| Solr request-handler defaults, invariants, or appends are not reflected in replayed queries | The matching `solrconfig.xml` was not loaded for that collection. Confirm the ConfigMap key and `fromFile.path`, make sure the file is XML copied from ZooKeeper rather than JSON from the `/config` endpoint, and check the replayer logs for `Loaded solrConfig` or parse-warning messages. |
|  `targetResponses={400}` with "refresh policy not supported" |  `targetType` not set for a Serverless target. Set `"targetType": {"value": "OpenSearchServerless"}` or `"NextGenOpenSearchServerless"` in the transform provider’s context values. |
|  `No zk_backup directories found for collection` in metadata or backfill logs | The backup is usually staged at the wrong S3 level or is missing the ZooKeeper backup. Set `s3RepoPathUri` to the parent path, set `externallyManagedSnapshotName` to the backup root, and verify that each collection directory contains `zk_backup_N/` or `zk_backup/` as described in [Verify the Solr backup layout](solr-prepare-backup.md#solr-backup-layout). |
| Metadata migration creates empty or mostly fallback mappings for a Solr collection | The collection’s latest ZooKeeper backup does not include a readable schema file. Confirm that `managed-schema.xml`, `managed-schema`, or `schema.xml` exists under the collection’s latest `zk_backup_N/configs/CONFIGSET/` directory. |
| NLB for capture proxy stuck in `pending`  | Subnets missing the required ELB tag. Tag subnets: `aws ec2 create-tags --resources SUBNET_IDs --tags Key=kubernetes.io/role/elb,Value=1`. |
| Kafka entity-operator CrashLoopBackOff | Startup probe timeout during initial Kafka provisioning. Delete the pod to reset backoff: `kubectl delete pod -n ma -l strimzi.io/name=default-entity-operator`. |

For broader operational issues with the backfill workflow and the target, see [Troubleshooting](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

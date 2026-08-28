---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-pilot-config.html
---

# Step 6: Configure the pilot workflow
<a name="pb-es68-pilot-config"></a>

Load the version-matched sample and then edit it down to a minimal pilot configuration:

```
workflow configure sample --load
workflow configure edit
```

Use a configuration like the following for the pilot. It declares the Elasticsearch 6.8 source and its snapshot repository, the Amazon OpenSearch Service target using SigV4 with service `es`, and a `documentBackfillConfig.indexAllowlist` that limits the run to a single pilot index. Multi-type mapping resolution is applied automatically, so there is no field to set for it. Replace the placeholders with your values:

```
{
  "sourceClusters": {
    "source": {
      "endpoint": "https://<SOURCE_ENDPOINT>:9200",
      "version": "ES 6.8",
      "allowInsecure": true,
      "authConfig": {
        "basic": {
          "secretName": "source-credentials"
        }
      },
      "snapshotInfo": {
        "repos": {
          "default": {
            "awsRegion": "<REGION>",
            "s3RepoPathUri": "s3://<SNAPSHOT_BUCKET>/migration-snapshots"
          }
        },
        "snapshots": {
          "migration-snapshot": {
            "config": {
              "createSnapshotConfig": {}
            },
            "repoName": "default"
          }
        }
      }
    }
  },
  "targetClusters": {
    "target": {
      "endpoint": "https://<DOMAIN_ENDPOINT>",
      "authConfig": {
        "sigv4": {
          "region": "<REGION>",
          "service": "es"
        }
      }
    }
  },
  "snapshotMigrationConfigs": [
    {
      "fromSource": "source",
      "toTarget": "target",
      "perSnapshotConfig": {
        "migration-snapshot": [
          {
            "metadataMigrationConfig": {
              "skipEvaluateApproval": false,
              "skipMigrateApproval": false
            },
            "documentBackfillConfig": {
              "podReplicas": 4,
              "indexAllowlist": ["<PILOT_INDEX>"]
            }
          }
        ]
      }
    }
  ]
}
```

**Note**
Set `allowInsecure` to `true` only if the source cluster presents a self-signed or otherwise untrusted certificate over HTTPS. If the source uses plaintext HTTP or a trusted certificate, omit `allowInsecure`.

By default, the built-in type-mapping sanitization transformer merges the multiple mapping types found in an Elasticsearch 6.8 index into a single index on the target (union), which is the most common choice when moving off pre-7.0 type mappings. This happens automatically with no configuration field. If you need to rename the merged output or drop routed data, configure `TypeMappingSanitizationTransformerProvider` rather than a `multiTypeBehavior` field; see [Transform type mappings](transform-type-mappings.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

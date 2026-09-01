---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores-restore.html
---

# Restoring a HealthLake data store
<a name="managing-data-stores-restore"></a>

Use `RestoreFHIRDatastore` to restore a backup-enabled AWS HealthLake data store to a point in time. The restore creates a new data store that contains the source data store's FHIR resources as they existed at the restore point. The source data store is not modified. For more information, see [`RestoreFHIRDatastore`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_RestoreFHIRDatastore.html) in the *AWS HealthLake API Reference*.

**Prerequisite: enable continuous backup**
To restore a data store, continuous backup must be enabled on the source data store. Enable backup by including a `BackupConfiguration` when you create a data store with `CreateFHIRDatastore`, or later with `UpdateFHIRDatastore`. Backup data is retained for the retention period you choose (1–30 days).

```
aws healthlake create-fhir-datastore \
  --datastore-name "BackupEnabledFhirDatastore" \
  --datastore-type-version R4 \
  --backup-configuration '{ "Status": "ENABLED", "BackupType": "CONTINUOUS", "RetentionPeriodInDays": 7 }'
```

To find the available restore window for a data store, use `DescribeFHIRDatastore`. The `BackupStatusInfo` object in the response includes the `EarliestRestorePoint` and `LatestRestorePoint` timestamps that bound the restore window.

```
"BackupStatusInfo": {
    "Configuration": {
        "Status": "ENABLED",
        "BackupType": "CONTINUOUS",
        "RetentionPeriodInDays": 7,
        "BackupTagsEnabled": false
    },
    "BackupEnabledAt": "2026-08-01T00:00:00+00:00",
    "EarliestRestorePoint": "2026-08-01T00:00:00+00:00",
    "LatestRestorePoint": "2026-08-01T01:00:00+00:00"
}
```

**Important**
The `RestorePointTime` that you request must fall within the restore window returned by `DescribeFHIRDatastore`. If you omit `RestorePointTime`, the data store is restored to the latest available restore point. The restored data store starts in `CREATING` status and changes to `ACTIVE` when the restore completes. Only one restore can be in progress for a source data store at a time; a second restore submitted while one is running returns `ConflictException`. Use `DescribeFHIRDatastore` on the restored data store to track its status.

**Configuration of the restored data store**
The restored data store does not inherit configuration from the source data store. Each configuration you omit from the request is set to the same default that `CreateFHIRDatastore` uses, not the source data store's setting:
+ If you omit `SseConfiguration`, the restored data store is encrypted with an AWS owned KMS key—even if the source data store uses a customer managed key. To encrypt the restored data store with a customer managed key, specify it in the request. For the AWS KMS permissions that a restore requires on the source and target keys, see [Encryption at REST for AWS HealthLake](encryption-at-rest.md).
+ If you omit `IdentityProviderConfiguration`, the restored data store uses AWS SigV4 (IAM) authorization—even if the source data store uses SMART on FHIR.
+ The NLP, analytics, and FHIR validation profile configurations are also not inherited—specify them in the request to enable them on the restored data store.
+ Tags are the exception: if `BackupTagsEnabled` is `true` on the source data store, the source data store's tags are applied to the restored data store.

**Security considerations**
A restore creates a new data store with a new Amazon Resource Name (ARN). IAM policies that reference the source data store's ARN—including `Deny` statements—do not apply to the restored data store, even though it contains the same data. If your access controls must follow the data across restore operations, use tag-based (attribute-based) access control with `aws:ResourceTag` condition keys and enable `BackupTagsEnabled` so the source data store's tags carry over to the restored data store. Grant the `healthlake:RestoreFHIRDatastore` permission only to principals who should be able to create a new copy of a data store's data.

**Restoring a deleted data store**
If backup is enabled when a data store is deleted, its backup data is retained for the backup retention period after deletion. During that period, you can restore the deleted data store by calling `RestoreFHIRDatastore` with its data store ID. The `ScheduledPermanentDeletionTime` field in `BackupStatusInfo` shows when the retained backup data is permanently deleted.

**To restore a HealthLake data store**
Choose a menu based on your access preference to AWS HealthLake.

## AWS CLI and SDKs
<a name="managing-data-stores-restore-cli-sdk"></a>

------
#### [ AWS CLI ]

**Example 1: Restore a data store to a point in time**

```
aws healthlake restore-fhir-datastore \
  --source-datastore-id "{{source-datastore-id}}" \
  --restore-configuration '{ "ContinuousBackupRestoreConfiguration": { "RestorePointTime": "2026-08-01T00:00:00Z" } }' \
  --datastore-name "RestoredFhirDatastore"
```

**Example 2: Restore a data store to the latest available restore point**

```
aws healthlake restore-fhir-datastore \
  --source-datastore-id "{{source-datastore-id}}" \
  --restore-configuration '{ "ContinuousBackupRestoreConfiguration": {} }' \
  --datastore-name "RestoredFhirDatastore"
```

**Example 3: Restore a data store with a customer managed AWS KMS key**

```
aws healthlake restore-fhir-datastore \
  --source-datastore-id "{{source-datastore-id}}" \
  --restore-configuration '{ "ContinuousBackupRestoreConfiguration": { "RestorePointTime": "2026-08-01T00:00:00Z" } }' \
  --datastore-name "RestoredFhirDatastore" \
  --sse-configuration '{ "KmsEncryptionConfig": { "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:{{account-id}}:key/{{key-id}}" } }'
```

The response returns the identifiers of the new data store created by the restore.

```
{
    "DatastoreId": "{{restored-datastore-id}}",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:{{account-id}}:datastore/fhir/{{restored-datastore-id}}",
    "DatastoreStatus": "CREATING",
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/{{restored-datastore-id}}/r4/"
}
```

For API details, see [restore-fhir-datastore](https://docs.aws.amazon.com/cli/latest/reference/healthlake/restore-fhir-datastore.html) in the *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**

```
def restore_fhir_datastore(
    self,
    source_datastore_id: str,
    restore_point_time: datetime,
    datastore_name: str,
) -> dict[str, any]:
    """
    Restores a backup-enabled HealthLake data store to a point in time.

    The restore creates a new data store containing the source data
    store's FHIR resources as of the restore point.

    :param source_datastore_id: The ID of the source data store.
    :param restore_point_time: The point in time to restore to. Must be
        within the restore window returned by DescribeFHIRDatastore.
    :param datastore_name: The name for the restored data store.
    :return: The response, including the new data store's ID and status.
    """
    try:
        return self.health_lake_client.restore_fhir_datastore(
            SourceDatastoreId=source_datastore_id,
            RestoreConfiguration={
                "ContinuousBackupRestoreConfiguration": {
                    "RestorePointTime": restore_point_time
                }
            },
            DatastoreName=datastore_name,
        )
    except ClientError as err:
        logger.exception(
            "Couldn't restore data store %s. Here's why: %s",
            source_datastore_id,
            err.response["Error"]["Message"],
        )
        raise
```

For API details, see [RestoreFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/RestoreFHIRDatastore) in the *AWS SDK for Python (Boto3) API Reference*.

------

**Example availability**
Can't find what you need? Request a code example using the **Provide feedback** link on the right sidebar of this page.

**Warning**
Restores currently include only the latest version of each FHIR resource as of the restore point. Prior resource version history is not restored.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

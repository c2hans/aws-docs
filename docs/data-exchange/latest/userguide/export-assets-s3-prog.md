---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/export-assets-s3-prog.html
---

# Exporting AWS Data Exchange assets to an S3 bucket (AWS SDKs)
<a name="export-assets-s3-prog"></a>

You can use the AWS SDKs to export AWS Data Exchange assets to an S3 bucket using the following instructions.

**To export assets to an S3 bucket (AWS SDKs)**

1. Create a `CreateJob` request of type `EXPORT_ASSETS_TO_S3`.

1. Include the following in the request:
   + `AssetDestinations`
     + `AssetID`
     + `Bucket`
     + `Key`
   + `DataSetID`
   + `Encryption`
     + `KmsKeyArn`
     + `Type`
   + `RevisionID`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. (Optional) Update the assets' name property after they are created.

**Note**
For information about exporting an entire revision as a single job, see [Exporting revisions from AWS Data Exchange](exporting-revisions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

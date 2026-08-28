---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/export-rev-s3-prog.html
---

# Exporting AWS Data Exchange asset revisions to an S3 bucket (AWS SDKs)
<a name="export-rev-s3-prog"></a>

You can use the AWS SDKs to export AWS Data Exchange asset revisions to an S3 bucket using the following instructions.

**To export a revision to an S3 bucket (AWS SDKs)**

1. Create a `CreateJob` request of type `EXPORT_REVISIONS_TO_S3`.

1. Include the following in the request:
   + `DataSetId`
   + `Encryption`
     + `KmsKeyArn`
     + `Type`
   + `RevisionDestinations`
     + `Bucket`
     + `KeyPattern`
     + `RevisionId`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. The newly created assets have a name property equal to the original S3 object's key. The Amazon S3 object key defaults to the key pattern `${Asset.Name}`.

   You can update the assets' name property after they are created.

   For more information about key patterns, see [Key patterns when exporting asset revisions from AWS Data Exchange](revision-export-keypatterns.md).

**Note**
If you are using `DataSet.Name` as the dynamic reference, you must have the IAM permission `dataexchange:GetDataSet`. For more information, see [AWS Data Exchange API permissions: actions and resources reference](api-permissions-ref.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

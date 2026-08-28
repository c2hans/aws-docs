---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/export-asset-URL-prog.html
---

# Exporting AWS Data Exchange assets to a signed URL (AWS SDKs)
<a name="export-asset-URL-prog"></a>

You can use the AWS SDKs to export AWS Data Exchange assets to destinations other than S3 buckets.

**To export assets to a signed URL (AWS SDKs)**

1. Create a `CreateJob` request of type `EXPORT_ASSET_TO_SIGNED_URL`.

1. Include the following in the request:
   + `AssetID`
   + `DataSetID`
   + `RevisionID`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. (Optional) Update the assets' name property after they are created.

1. The response details include the `SignedUrl` that you can use to import your file.

**Note**
The signed URL expires one minute after it's created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

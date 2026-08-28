---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/importing-from-url.html
---

# Importing AWS Data Exchangeassets from a signed URL
<a name="importing-from-url"></a>

You can use signed URLs to import assets that are not stored in Amazon S3.

**Topics**
+ [Importing assets from a signed URL (AWS SDKs)](#import-asset-signed-url-prog)
+ [Importing assets from a signed URL (console)](#import-asset-signed-url-via-console)

## Importing assets from a signed URL (AWS SDKs)
<a name="import-asset-signed-url-prog"></a>

**To import assets from a signed URL (AWS SDKs)**

1. Create a `CreateJob` request of type `IMPORT_ASSET_FROM_SIGNED_URL`.

1. Include the following in the request:
   + `AssetName`
   + `DataSetID`
   + `Md5Hash`
   + `RevisionID`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. (Optional) Update the assets' name property after they are created.

1. The response details include the `SignedUrl` that you can use to import your file.

**Note**
The signed URL expires one minute after it's created.

## Importing assets from a signed URL (console)
<a name="import-asset-signed-url-via-console"></a>

**To import an asset from a signed URL (console)**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, for **Publish data**, choose **Owned data sets**.

1. In **Owned data sets**, choose the data set that has the asset you want to update.

1. On the **Revisions** tab, choose **Create revision** to open the **Create revision** page.

   1. For **Revision settings**, provide an optional comment for your revision that describes the purpose of the revision.

   1. For **Add tags – optional**, add tags associated with the resource.

   1. Choose **Create**.

      Your new revision is created.

1. For the **Jobs** section, choose **Upload**.

1. Follow the prompts in the upload window, and then choose **Open**.

   A job is started to import your asset into your data set. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

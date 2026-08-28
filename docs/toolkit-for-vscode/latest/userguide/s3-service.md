---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/s3-service.html
---

# Working with Amazon S3 resources
<a name="s3-service"></a>

You can use Amazon S3 from the AWS Toolkit for Visual Studio Code to view, manage, and edit your Amazon S3 buckets and other resources.

The following sections desribe how to work with Amazon S3 resources from the AWS Toolkit for Visual Studio Code. For information about working with Amazon S3 objects, such as folders and files, from the AWS Toolkit for Visual Studio Code, see the [Working with S3 objects](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/s3-service-objects.html) topic in this User Guide.

## Creating an Amazon S3 bucket
<a name="s3-service-resources-bucket"></a>

1. From the Toolkit explorer, open the context (right-click) menu for the **S3** service, and choose **Create Bucket...**. Alternatively, choose the **Create Bucket ** icon to open the **Create Bucket** dialog box.

1. In the **Bucket Name** field, enter a valid name for the bucket.

   Press **Enter** to create the bucket and close the dialog box. Your new bucket is then displayed under the S3 service in the toolkit.
**Note**
Since Amazon S3 allows your bucket to be used as a URL that can be accessed publicly, the bucket name that you choose must be globally unique. If another account already created a bucket with the name that you want to use, you must use a different name.
If you can't create a new bucket, check the **AWS Toolkit Logs** in the **Output** tab. If you attempt to use an invalid bucket name, a `BucketAlreadyExists` error occurs.
For more information, see [Bucket restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html) in the **Amazon Simple Storage Service User Guide**.

## Adding a folder to an Amazon S3 bucket
<a name="s3-service-resources-add-folder"></a>

You can organize the contents of an S3 bucket by grouping your objects into folders. You can also create folders within folders.

1. From the Toolkit explorer, expand the **S3** service to view a list of your S3 resources.

1. Choose the **Create Folder icon** to open the **Create Folder** dialog box. Or, open the context (right-click) menu for a bucket or folder, and then choose **Create Folder**.

1. Enter a value into the **Folder Name** field and press **Enter** to create the folder and close the dialog box. Your new folder is displayed under the corresponding S3 resource in the toolkit menu.

## Deleting an Amazon S3 bucket
<a name="s3-service-resources-bucket-delete"></a>

When you delete an S3 bucket, you also delete the folders and objects that it contains. So, when you attempt to delete a bucket, you're asked to confirm that you want to delete it.

1. From the toolkit main menu, expand the **Amazon S3** service to view a list of your S3 resources.

1. Open the context (right-click) menu for a bucket or folder, then choose **Delete S3 Bucket**.

1. When you’re prompted, enter the bucket's name into the text field, and then press **Enter** to delete the bucket and close the confirmation prompt.
**Note**
If your bucket contains objects, it’s emptied before it's deleted. If you attempt to delete a large number of resources or objects at one time, it can take some time for them to be deleted. After they're deleted, you receive a notification that says that they're successfully deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

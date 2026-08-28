---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/edit-metadata-defaults.html
---

# Edit metadata defaults for your NFS file share
<a name="edit-metadata-defaults"></a>

If you don't set metadata values for your files or directories in your bucket, your S3 File Gateway sets default metadata values. These values include Unix permissions for files and folders. You can edit the metadata defaults on the Storage Gateway console.

When your S3 File Gateway stores files and folders in Amazon S3, the Unix file permissions are stored in object metadata. When your S3 File Gateway discovers objects that weren't stored by the S3 File Gateway, these objects are assigned default Unix file permissions. You can find the default Unix permissions in the following table.

| Metadata | Description |
| --- | --- |
| Directory permissions | The Unix directory mode in the form "nnnn". For example, "0666" represents the access mode for all directories inside the file share. The default value is 0777. |
| File permissions | The Unix file mode in the form "nnnn". For example, "0666" represents the file mode inside the file share. The default value is 0666. |
| User ID | The default owner ID for files in the file share. The default value is 65534. |
| Group ID | The default group ID for the file share. The default value is 65534.  |

**To edit metadata defaults**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. Choose **File shares**, and then choose the file share that you want to update.

1. For **Actions**, choose **Edit file metadata defaults**.

1. In the **Edit file metadata defaults** dialog box, provide the metadata information and choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/s3-service-objects.html
---

# Working with Amazon S3 objects
<a name="s3-service-objects"></a>

Your files, folders, and any other data that's stored in an S3 resource bucket are known as S3 objects.

The following sections describe how to work with Amazon S3 objects from the AWS Toolkit for Visual Studio Code. For details on working with Amazon S3 resources, such as S3 buckets, from the AWS Toolkit for Visual Studio Code, see the [Working with S3 resources](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/s3-service.html) topic in this User Guide.

## Object pagination
<a name="s3-service-objects-pagination"></a>

If you're working with a large number of Amazon S3 objects and folders, pagination allows you to specify the number of items that you want to display on a page.

1. Navigate to the VS Code **Activity Bar** and choose **Extensions**.

1. From the AWS Toolkit extension, choose the settings icon, and then choose **Extension Settings**.

1. On the **Settings** page, scroll down to the **AWS > S3: Max Items Per Page** setting.

1. Change the default value to the number of S3 items that you want to be displayed before "load more" is displayed.
**Note**
Valid values include any number between 3 and 1000. This setting applies only to the number of objects or folders displayed at one time. All the buckets you created are displayed at once. By default, you can create up to 100 buckets in each of your AWS accounts.

1. Close the **Settings** page to confirm your changes.

You can also update the settings in a JSON-formatted file by choosing the **Open Settings (JSON)** icon in the upper right of the **Settings** page.

## Uploading and downloading Amazon S3 objects
<a name="s3-service-objects-upload-download"></a>

You can upload locally-stored files to your Amazon S3 buckets or download remote Amazon S3 objects to your local system, from the AWS Toolkit for Visual Studio Code.

### Upload a file using the Toolkit
<a name="s3-service-objects-upload-toolkit"></a>

1. From the Toolkit explorer, expand the **Amazon S3** service to view a list of your S3 resources.

1. Choose the **Upload File icon** that's located next to a bucket or folder to open the **Upload File dialog**. Or you can open the context (right-click) menu and choose **Upload File**.
**Note**
To upload a file to the object's parent folder or resource, open the context (right-click) menu for any S3 object and choose **Upload to Parent**.

1. Use your system's file manager to select a file, then choose **Upload File** to close the dialog and upload the file.

### Upload a file using the Command Palette
<a name="s3-service-objects-upload-commandpalette"></a>

You can use the Toolkit interface or the **Command Palette** to upload a file to a bucket.

1. To select a file for upload, choose that file's tab in VS Code.

1. Press **Ctrl\+Shift\+P** to display the **Command Palette**.

1. In the **Command Palette**, enter the phrase `upload file` to display a list of recommended commands.

1. Choose the **AWS: Upload File** command to open the **AWS: Upload File** dialog.

1. When prompted, choose the file you want to upload, then choose the bucket you want to upload that file to.

1. Confirm your upload to close the dialog and begin the upload process. When the upload is complete, the object displays in the toolkit menu with metadata that includes the object size, last modification date, and path.

### Downloading an Amazon S3 object
<a name="s3-service-objects-download"></a>

1. From the Toolkit explorer, expand the **S3** service.

1. From a bucket or folder, open the context (right-click) menu for an object that you want to download. Then, choose **Download As** to open the Download As dialog box. Or, alternatively, choose the **Download As** icon near the object.

1. Using your system's file manager, choose a destination folder, enter a file name, and then choose **Download** to close the dialog and start the download.

## Editing remote objects
<a name="s3-service-edit-objects"></a>

You can use the AWS Toolkit for Visual Studio Code to edit your Amazon S3 objects that are stored in your remote Amazon S3 resources.

1. From the Toolkit explorer, expand the **S3** service.

1. Expand the S3 resource that contains the file that you want to edit.

1. To edit the file, choose the **pencil icon (Edit File)**.

1. To edit a file that's open in read-only mode, view the file in the VS Code editor, then choose the **pencil icon** located on the upper-right hand corner of the UI.

**Note**
If you restart or exit VS Code, your IDE disconnects from your S3 resources. If any remote S3 files are being edited when you disconnect, the edit stops. You must restart VS Code and reopen the edit tab to resume the edit.
The **Edit File** button is in the upper-right hand corner of the UI. It's only visible when you're actively viewing a read-only file in the VS Code editor.
Non-text files can't be opened in a read-only mode. They always open in edit-mode.
You can't toggle back to read-only mode from edit-only mode, only the other way around.

## Copying the path of an Amazon S3 object
<a name="copy-path"></a>

The following procedure describes how to copy the path of an Amazon S3 object from the AWS Toolkit for Visual Studio Code.

1. From the Toolkit explorer, expand the **S3** service.

1. Expand the resource bucket that contains the object you want to copy the path for.

1. Open the context (right-click) menu for the object that you want to copy the path for, then choose **Copy Path** to copy the object path to your local clipboard.

## Generating a presigned URL for an Amazon S3 object
<a name="presigned-s3-object"></a>

You can share private Amazon S3 objects with others by granting time-limited permissions for downloads through the presigned URL feature. For more information, see [Sharing an object with a presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).

1. From the Toolkit explorer, expand the **S3** service.

1. From a bucket or folder, open the context (right-click) menu for an object that you want to share. Then, choose **Generate Presigned URL** to open the **Command palette**.

1. From the **Command Palette**, enter the number of minutes that the URL can be used to access your object. Then, choose **Enter** to confirm and close the dialog.

1. After the presigned URL is generated, the VS Code **Status Bar** displays the presigned URL for the object that has been copied to your local **clipboard**.

## Deleting an Amazon S3 object
<a name="s3-service-delete-object"></a>

If an object is in a non-versioned bucket, you can permanently delete it. For buckets that have versioning enabled, a delete request doesn't permanently delete that object. Instead, Amazon S3 inserts a delete marker in the bucket. For more information, see [Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html).

1. From the Toolkit explorer, expand the **S3** service to view a list of your S3 resources.

1. Open the context (right-click) menu for an object you want to delete, then choose **Delete** to open the confirmation dialog.

1. Choose **Delete. . .** to confirm that you want to delete the S3 object. Then, close the dialog.

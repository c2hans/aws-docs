---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/create-first-asset.html
---

# Create Your First Asset
<a name="create-first-asset"></a>

Assets are versioned collections of files that represent a logical unit of spatial data.

## Prepare Your Asset Files
<a name="prepare-asset-files"></a>

Organize your files before uploading:

1. Create a folder on your local machine with a descriptive name (for example, `building-scan-01`)

1. Place all related files in this folder:
   + Primary data files (for example, `.e57`, `.las`, `.laz`, `.obj`, `.fbx`)
   + Supporting files (for example, textures, metadata, documentation)

1. Maintain any subfolder structure you want preserved in the asset

## Upload Your Asset
<a name="upload-asset"></a>

The desktop application uses a three-step wizard to create and upload assets.

 **Step 1: Enter Asset Information**

1. In the desktop application, navigate to your project

1. Choose **Create Asset**

1. Enter the asset details:
   +  **Asset Name** – Enter a descriptive name (for example, `Building Scan 01`)
   +  **Description** – Provide details about the asset (for example, `Initial site survey scan`)
   +  **Template** (optional) – Select an asset template if available

1. Choose **Next**

![Create asset wizard — Define your asset](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/create-asset-step-1.png)

 **Step 2: Select Files to Upload**

1. Use **Choose directory** to upload an entire folder with its structure, or choose **Select Files** to upload individual files

1. Browse to your prepared asset folder or files

1. Select the folder or files to upload
**Note**
You can also choose **Create Empty Asset** to create an asset without uploading files immediately. Files can be added later.
**Tip**
If you have the Amazon S3 Import connector configured, you can also import files directly from an S3 bucket without downloading and re-uploading them. For more information, see [Importing files from Amazon S3](connector-s3-import.md).

1. Choose **Next**

![Create asset wizard — choose your initial content](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/file-upload-screen.png)

 **Step 3: Review and Create**

1. Review all asset information and selected files

1. Verify the folder structure and file list

1. Choose **Create asset**

The application displays upload progress. Large files may take several minutes to upload.

![Create asset wizard — review asset content](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/review-asset.png)

## Verify Your Upload
<a name="verify-upload"></a>

After the upload completes:

1. In the desktop application, navigate to your project

1. Locate your newly created asset in the asset list

1. Choose the asset name to view details

1. Verify:
   + All files appear in the file list
   + Folder structure is preserved
   + Metadata is correctly populated
   + Asset state shows as `Draft`

![Asset details screen](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/upload-complete.png)

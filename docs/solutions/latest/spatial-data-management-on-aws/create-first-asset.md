---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/create-first-asset.html
---

# Create Your First Asset

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

The desktop application uses a wizard to create and upload assets. It has four steps, and the third is optional.

 **Step 1: Enter Asset Information**

1. In the desktop application, open your project

1. Choose **Create asset**

1. On **Define your asset**, enter the asset details:
   +  **Asset template** – Choose a template if one is available. If you choose one, the asset must have the attributes that the template requires. The default is **None**
   +  **Name** – Enter a descriptive name (for example, `Building scan 001`)
   +  **Description** – Provide details about the asset (for example, `Maintenance of the building’s east facade`)
   +  **Thumbnail** (optional) – Choose an image in PNG, JPEG, JPG, WebP, or AVIF format, smaller than 10 MB
   +  **Location** (optional) – Choose **This asset has no geographic location**, **This asset inherits its location from its project**, **This asset has a specific geographic location**, or **This asset has a geometry**
   +  **Attributes** – Choose **Add new attribute** to add attributes

1. Choose **Next**

![Create asset wizard step 1 of 4: Define your asset](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/create-asset-step-1.png)

 **Step 2: Choose Your Initial Content**

1. On **Choose your initial content**, under **Initial content**, choose **Upload initial content**.

1. Choose **Choose files** to add individual files, or **Choose folder contents** to add a folder with its structure. You can also drop files and folders on the drop area. A dropped folder keeps its name.

1. Select the files or folder from your prepared asset folder. The files appear under **Content**, with their paths and sizes. Use **Find a file** to search the list. To remove a file, choose the **X** on its row, or choose **Clear all** to start again.
**Note**
To create an asset without files, choose **Create an empty asset**. You can add files later.
**Tip**
When the asset template that you chose has the Amazon S3 Import connector, **Initial content** also offers to import files from an Amazon S3 bucket, without downloading and re-uploading them. Without the connector on the template, this option does not appear. For more information, see [Importing Files from Amazon S3](connector-s3-import.md).

1. Choose **Next**

![Create asset wizard step 2 of 4: Choose your initial content](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/file-upload-screen.png)

 **Step 3: Set File Attributes (optional)**

Give the files that you are adding their attributes before the asset exists. If the asset template requires attributes on files, the step title shows how many required values are still missing, for example **Set file attributes (12 required missing)**.

1. On **Set file attributes**, stay on **By type** to set attributes for groups of files. **Every file** applies to all of the files. A section for a file type, such as **E57 · 3 files**, applies to files of that type only.

1. Choose the pencil on a section to edit its attributes. Choose **Add attribute** to add one, and then choose **Done**. **Added** marks each value that you set. Use **Filter attributes** to find an attribute.

1. Choose **By file** to change the attributes of a single file.

1. Choose **Next**. To skip this step, choose **Next** without setting anything.

![Create asset wizard step 3 of 4: Set file attributes](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/create-asset-file-attributes.png)

For more information, see [Edit Attributes of Many Files at Once](edit-assets-in-the-portal.md#edit-file-attributes).

 **Step 4: Review and Create**

1. On **Review and create your asset**, check **Asset details**: the asset template, name, description, and location. Choose **Edit** to change them.

1. Use the tabs below to check the rest. The number in each tab is how many items it holds:
   +  **Content** – The files that you are adding. Use **Find a file** to search the list.
   +  **Asset attributes** – The attributes of the asset.
   +  **File attributes** – The attributes that you set on files in the previous step.

1. Choose **Create asset**. SDMA uploads the files that are new to the solution to Amazon S3.

![Create asset wizard step 4 of 4: Review and create your asset](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/review-asset.png)

The **Transfers** button, next to the notifications bell, shows upload progress. When the upload ends, the asset is listed under **Finished**. Large files may take several minutes to upload.

![Transfers panel showing the new asset as finished](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/upload-complete.png)

## Verify Your Upload
<a name="verify-upload"></a>

After the upload completes:

1. In the desktop application, open your project

1. On the **Assets** tab, find your new asset in the list

1. Choose the asset name to view details

1. Verify:
   + All files appear in the file list
   + Folder structure is preserved
   + Metadata is correctly populated
   + Asset state shows as `Draft`

The asset page shows the asset’s details at the top, with its size, state, and location. The size excludes the hidden files that SDMA keeps for the asset, and says how many there are. The **Files**, **Attributes**, and **History** tabs are below. In **Files**, **Status** shows work in progress on a file, for example **1 running**.

![Asset page for Building scan 001 with the Files tab open](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/asset-details-files.png)

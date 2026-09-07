---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/review-asset.html
---

# Review asset
<a name="review-asset"></a>

After uploading files, you can preview content and review auto-extracted metadata to verify the asset before marking it as approved.

## Preview files
<a name="preview-files"></a>

When you select a file, the solution generates a preview to help you quickly verify you uploaded the correct assets. This feature is available for certain file types.

The preview displays extracted content based on the file type. For example, the screenshot shows extracted panorama images and a simple low-resolution point cloud turntable view.

![File preview showing panorama and point cloud](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/asset-create-complete-file-preview.png)

## Review auto-extracted attributes
<a name="review-extracted-attributes"></a>

When you select a file, the solution automatically extracts attributes from the file metadata. You can review, edit, and accept these suggested attributes before persisting them to the asset metadata. Extracted metadata helps improve search.

Auto-extraction is currently supported for E57, LAZ, GLB, glTF, and image files.

1. Select a file from the asset.

1. In the right-hand panel, review the suggested attributes.

1. (Optional) Remove or edit any attributes as needed.

1. Choose **Accept** to persist the attributes to the metadata associated with the file.

The accepted attributes are now saved as part of that files metadata.

![Right-hand panel showing suggested attributes](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/auto-extracted-attribute-suggestions.png)

## Verify and approve assets
<a name="verify-and-approve"></a>

Assets are created in `Draft` state by default. After verifying the asset content and metadata, you can mark it as reviewed to indicate it has been validated.

1. Open the asset details page

1. From the actions menu, choose **Mark reviewed**

1. Confirm the action

The asset is now marked as reviewed, indicating it has been validated and is ready for use by other team members with appropriate permissions.

![Asset details screen — mark reviewed actions menu](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/mark-reviewed.png)

---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/review-asset.html
---

# Review Asset

After uploading files, you can look at their content and review auto-extracted metadata to verify the asset before marking it as approved.

## View Files
<a name="preview-files"></a>

Before you approve an asset, look at what you uploaded. SDMA opens many file types in the Portal, so you can check them without downloading them.

When you select a file, a panel opens beside the file list with a preview of the file. The preview helps you check quickly that you uploaded the right content. This feature is available for certain file types.

The preview shows content that SDMA extracts or generates, based on the file type. For example, the panel in the following screenshot is for an E57 scan. It shows a video of the point cloud, and a strip of images below it. Under the preview, **Details** lists the file’s size and when it was uploaded and modified. **Attributes** lists the values that you set in the create asset wizard, and **Attribute suggestions** shows how many suggestions SDMA has for the file.

![Asset page with the file panel open on an E57 scan showing a point cloud video and image thumbnails plus details and attributes](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/asset-create-complete-file-preview.png)

To look at the file in full, select it and choose **View**. The file opens in the viewer. The viewer has a tab at the top left for each view of the file, so you can move between them without leaving the file. An E57 scan has **Panorama**, **Image**, **Video**, and **Point cloud** tabs. In the panorama, drag to look around and scroll to zoom.

![Panorama view of an E57 scan](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-e57-panorama.png)

For what each view shows, which file types you can view, and how to compare files and layer maps, see [View and inspect your content](view-your-content.md).

## Review Auto-Extracted Attributes
<a name="review-extracted-attributes"></a>

When you select a file, the solution automatically extracts attributes from the file metadata. You can review, edit, and accept these suggested attributes before persisting them to the asset metadata. Extracted metadata helps improve search.

Auto-extraction is currently supported for E57, LAZ, GLB, glTF, and image files.

1. Select a file from the asset.

1. In the right-hand panel, under **Attribute suggestions**, review the suggested attributes. The number beside the heading is how many suggestions the file has.

1. (Optional) Remove any suggestion that you do not want, with the **X** on it.

1. Choose **Accept** to save the suggestions that remain as attributes of the file. Choose **Reject** to discard them. The number in parentheses is how many suggestions each button applies to.

1. Choose **Done**.

The accepted attributes are now saved as part of that file’s metadata.

![Right-hand panel showing suggested attributes with Accept and Reject buttons](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/auto-extracted-attribute-suggestions.png)

## Verify and Approve Assets
<a name="verify-and-approve"></a>

Assets are created in `Draft` state by default. After verifying the asset content and metadata, you can mark it as reviewed to indicate it has been validated.

1. Open the asset.

1. In **Asset details**, open the actions menu next to **Download**, and choose **Mark reviewed**.

The asset is now marked as reviewed, indicating it has been validated and is ready for use by other team members with appropriate permissions.

![Asset page with the actions menu open and Mark reviewed highlighted](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/mark-reviewed.png)

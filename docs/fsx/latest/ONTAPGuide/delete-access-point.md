---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/delete-access-point.html
---

# Deleting an S3 access point attachment
<a name="delete-access-point"></a>

This section explains how to delete S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.

The `fsx:DetatchAndDeleteS3AccessPoint` and `s3control:DeleteAccessPoint` permissions are required to delete an S3 access point attachment.

## To delete an S3 access point attached to an FSx for ONTAP volume (Amazon FSx console)
<a name="access-points-delete-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to the volume that the S3 access point attachment that you want to delete is attached to.

1. Choose **S3** to display the list of S3 access points attached to the volume.

1. Select the S3 access point attachment that you want to delete.

1. Choose **Delete**.

1. Confirm that you want to delete the S3 access point, and choose **Delete**.

## To delete an S3 access point attached to an FSx for ONTAP volume (AWS CLI)
<a name="access-points-delete-cli"></a>
+ To delete an S3 access point attachments, use the [detach-and-delete-s3-access-point](https://docs.aws.amazon.com/cli/latest/reference/fsx/detach-and-delete-s3-access-point.html) CLI command (or the equivalent [DetachAndDeleteS3AccessPoint](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DetachAndDeleteS3AccessPoint.html) API operation), as shown in the following example. Use the `--name` property to specify the name of the S3 access point attachment that you want to delete.

  ```
  aws fsx detach-and-delete-s3-access-point \
      --region {{us-east-1}} \
      --name {{my-ontap-ap}}
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

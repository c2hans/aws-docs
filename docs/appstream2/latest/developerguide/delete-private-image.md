---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/delete-private-image.html
---

# Delete a Private Image in Amazon WorkSpaces Applications
<a name="delete-private-image"></a>

You can delete your private images when you no longer need them. You can't delete an image that is used by fleets or shared with other AWS accounts. To delete an image that is used by fleets or shared, you must first remove the image from any fleets and remove all image sharing permissions. After you delete an image, you can't recover it.

**To delete a private image**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the navigation pane, choose **Images**, **Image Registry**.

1. In the image list, select the private image you want to delete.

1. Choose **Actions**, **Delete**, then choose **Delete** again.

   The image is removed from the image registry and deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

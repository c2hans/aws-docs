---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/input-advanced-managing-overwrite-of-source-metadata.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Input > Advanced: Managing Overwrite of Source Metadata
<a name="input-advanced-managing-overwrite-of-source-metadata"></a>

Use the controls under Input > Advanced to either provide missing metadata or to replace incorrect metadata. The new values are passed into every output.

To do this, choose the Force Color checkbox under Input > Advanced and choose the correct color space in the Color Space dropdown box. Do not select **Follow** from the Color Space dropdown box.

If you leave the Force Color checkbox unchecked, AWS Elemental Server ignores the value in the Color Space dropdown box and any values provided in the HDR Master Display Information (shown below).

![An image of the AWS Elemental Server web interface.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/input-adv1.png)

## For HDR10 Input Only
<a name="for-hdr10-input-only"></a>

If you select HDR10 in the Color Space dropdown box, the HDR Master Display Information fields appears below. Enter correct values in these fields. Make sure to check the Force Color checkbox (described above) to incorporate these values in your metadata.

If you leave Force Color unchecked, these HDR Master Display Information fields still show values, but these values are not used. AWS Elemental Server instead uses metadata values from the incoming stream. You can view these values in the media info display after the job starts.

![An image of the AWS Elemental Server web interface.](http://docs.aws.amazon.com/elemental-server/latest/ug/images/input-adv2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

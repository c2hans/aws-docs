---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-ad-avail-blanking.html
---

# Enabling blanking
<a name="procedure-to-enable-ad-avail-blanking"></a>

Follow this procedure if you want to enable the ad avail blanking feature in a MediaLive channel.

**To enable blanking**

1. In the channel that you are creating, in the navigation pane, choose **General settings**.

1.  Set the ad avail mode, if you have not already done so. See [Getting ready: Set the SCTE 35 source—segments or manifest](scte35-getting-ready-source.md). The mode identifies which of all possible events are treated as triggers for blanking, which determines [when video is blanked](triggers-for-ad-avail-blanking.md).

1. Still in **General settings**, in **Avail blanking**, in **State**, choose **Enabled**.

1. In **Avail blanking image**, choose the appropriate value:
   + Disable: To use a plain black image for blanking.
   + Avail blanking image: To use a special image for blanking. In the **URL** field, type the path to a file in an S3 bucket. For integration with MediaLive, the bucket name mustn't use dot notation. For example, `mycompany-videos` is acceptable but `mycompany.videos` isn't. The file must be of type .bmp or .png. Also enter the user name and Systems Manager password parameter for accessing the S3 bucket. See [About the feature for creating password parameters](requirements-for-EC2.md#about-EC2Password).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

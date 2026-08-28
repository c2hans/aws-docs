---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-your-job-for-kantar-watermarking.html
---

# Configuring a job for Kantar watermarking
<a name="setting-up-your-job-for-kantar-watermarking"></a>

After you've established your relationship with Kantar, stored your Kantar credentials in AWS Secrets Manager, and granted permission to AWS Elemental MediaConvert to get these credentials, set up your MediaConvert job to encode the Kantar watermarks.

**To set up your job to encode Kantar watermarks**

1. Set up your job as usual. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md).

1. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose **Partner integrations**.

1. Enable **Kantar SNAP file watermarking**.

1. Provide values for the Kantar settings.

   1. For **Credentials secret name**, type the name of the Secrets Manager secret that you created to store your Kantar credentials. For example, **KantarCreds**.

   1. For **Kantar license ID**, type the license ID that Kantar provides you.

   1. For **Channel name**, type one of the channel names that are listed in your Kantar audio license.

   1. For **Content reference**, type the unique identifier that Kantar uses for the asset that you're encoding.

1. Confirm that the service role you've specified in the job is the same one that you, in the previous topic, attached permissions to that grant access to your Kantar credentials. If that role Is MediaConvert\_Default\_Role, you don't need to choose it explicitly, because MediaConvert will use that role by default. To specify the role if it has a different name, do the following:

   1. In the **Job** pane on the left, choose **AWS integration**.

   1. In the **Service access** section, find **Service role**. Confirm that the specified role is the one with the correct permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

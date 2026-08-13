---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/update-the-solution.html
---

# Update the guidance
<a name="update-the-solution"></a>

If you have previously deployed the guidance, follow this procedure to update the QnABot on AWS CloudFormation stack to get the latest version of the guidance’s framework.

**For those upgrading to v7.4.0 and above**
QnABot on AWS v7.4.0 introduces a new `AlexaSkillIds` AWS CloudFormation parameter for Alexa Skill authorization. If you are using Alexa integration with an existing QnABot deployment, you must provide your Alexa Skill IDs in the `AlexaSkillIds` parameter during stack update to maintain Alexa functionality. New deployments have Alexa turned off by default. For details, see [Getting answers using Amazon Alexa](step-4-interact-with-the-chatbot.md#getting-answers-using-amazon-alexa).

**For those upgrading to v7.3.12 and above**
QnABot on AWS v7.3.12 applies server-side HTML sanitization on `alt.html` and `alt.markdown` response fields to prevent stored XSS attacks. If your Q&A responses use custom HTML tags or attributes beyond the default allow list, those tags or attributes will be excluded from responses after upgrading. Review [Server-side sanitization and using custom tags and attributes in responses](server-side-html-sanitization.md) to understand which tags and attributes are allowed by default, and for instructions on how to add custom tags or attributes to the allow list before or after upgrading.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?), select your existing QnABot on AWS CloudFormation stack, and choose **Update**.

1. Select **Replace current template**.

1. Enter the appropriate Amazon S3 URL:
   + If using the default main template: https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-main.template
   + If using the VPC template: https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-vpc.template

1. Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Step 1: Launch the stack](step-1-launch-the-stack.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template might create AWS Identity and Access Management (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a status in approximately 30 minutes.

**Note**
If you have previously deployed the guidance but do not want to perform in-place upgrade or encountered issues during in-place upgrade or in case of a breaking change which does not allow you to upgrade in-place, please refer to migration section in this [README.md](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/update_or_migrate_deployment/README.md).

**Note**
 **For those upgrading to v6.1.X and above**
You might not see your previous executions on the Import, Export, and Test All pages disappear. To restore them, go to the respective S3 buckets and copy all the folders containing the data or status for each function (Import, Export, Test All) to the `ContentDesignerOutputBucket`. Rename them as `data-{function}` or `status-{function}`. Omitting this step doesn’t effect your QandAs and only impacts these specific pages.

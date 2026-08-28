---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/facebook-step-1.html
---

# Step 1: Create a Facebook application
<a name="facebook-step-1"></a>

On the Facebook developer portal, create a Facebook application and a Facebook page.

**To create a Facebook application**

1. Open [ https://developers.facebook.com/apps ](https://developers.facebook.com/apps)

1. Choose **Create App**.

1. In the **Create an App** page, choose **Business**, then choose **Next**.

1. For the **Add on app name**, **App contact email**, and **Business Account** fields, make the appropriate choices for your app. Choose **Create App** to continue.

1. From **Add Products to Your App**, choose **Set Up** from the **Messenger** tile.

1. In the **Access Tokens** section, choose **Add or Remove pages**.

1. Choose a page to use with your app, then choose **Next**.

1. For **What is app allowed to do**, leave the defaults then choose **Done**.

1. On the confirmation page, choose **OK**.

1. In the **Access Tokens** section, choose **Generate Token**, then copy the token. You enter this token in the Amazon Lex V2 console.

1. From the left menu, choose ** Settings ** and then choose **Basic**.

1. For **App Secret**, choose **Show** and then copy the secret. You enter this token in the Amazon Lex V2 console.

## Next step
<a name="facebook-step-1-next"></a>

[Step 2: Integrate Facebook Messenger with the Amazon Lex V2 bot](facebook-step-2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

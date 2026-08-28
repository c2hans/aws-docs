---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/deployment-beanstalk-republish.html
---

# How to Republish Your Application to an Elastic Beanstalk Environment (Legacy)
<a name="deployment-beanstalk-republish"></a>

**Important**
This documentation refers to legacy services and features. For updated guides and content, see the [AWS .NET deployment tool](https://aws.github.io/aws-dotnet-deploy/) guide.

You can iterate on your application by making discrete changes and then republishing a new version to your already launched Elastic Beanstalk environment.

1. In Solution Explorer, open the context (right-click) menu for the **AEBWebAppDemo** project folder for the project you published in the previous section, and choose **Publish to AWS Elastic Beanstalk**.
![Solution Explorer context menu showing "Publish to AWS..." option for AEBWebAppDemo project.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/tkv-publish-to-aws-console.png)

   The **Publish to Elastic Beanstalk** wizard appears.
![Publish to AWS Elastic Beanstalk dialog with profile and deployment options.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/tkv-aeb-wizard-app-console2.png)

1. Select **Redeploy to an existing environment** and choose the environment you previously published to. Click **Next**.

   The **Review** wizard appears.
![Review page showing deployment profile, application environment, and configuration details.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/tkv-aeb-wizard-app-review.png)

1. Click **Deploy**. The application will redeploy to the same environment.

You cannot republish if your application is in the process of launching or terminating.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

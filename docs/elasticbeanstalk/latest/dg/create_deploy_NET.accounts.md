---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.accounts.html
---

# Managing accounts
<a name="create_deploy_NET.accounts"></a>

##
<a name="create_deploy_NET.accounts.details"></a>

If you want to set up different AWS accounts to perform different tasks, such as testing, staging, and production, you can add, edit, and delete accounts using the AWS Toolkit for Visual Studio.

**To manage multiple accounts**

1.  In Visual Studio, on the **View** menu, click **AWS Explorer**.

1.  Beside the **Account** list, click the **Add Account** button.
![AWS explorer tab](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-aws-explorer-tab.png)

    The **Add Account** dialog box appears.
![Add account dialog box](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-vs-add-account.png)

1. Fill in the requested information.

1.  Your account information now appears on the **AWS Explorer** tab. When you publish to Elastic Beanstalk, you can select which account you would like to use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

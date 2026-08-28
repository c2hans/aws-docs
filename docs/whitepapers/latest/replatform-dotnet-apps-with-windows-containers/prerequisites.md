---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/prerequisites.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Prerequisites
<a name="prerequisites"></a>

## Deploy the AWS environment
<a name="deploy-the-aws-environment"></a>

1.  If you do not have an AWS account, follow the [How do I create and activate a new AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) article to create one that you will use throughout this walkthrough.

1.  Download the [App2Container demo CloudFormation template](https://raw.githubusercontent.com/aws-samples/dotnet-modernization-music-store/ca7f3705feeaf69d36fd161fb53a3bf9c4e15655/static/app2container_demo_template.yml) to your local machine for the AWS environment that you will deploy for the demo environment.

1.  [Deploy the AWS environment with CloudFormation](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/template) (sign-in required).

1.  In the **Create stack** dialog box in **Specify template**, choose Upload a template file, and select the `app2container_demo_template.yml` file that you downloaded to your local machine. Choose **Next**.
![Screen capture of the Create stack dialog box](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/create-stack.jpg)

1.  In the **Specify stack details** dialog box, enter **`App2Container-Demo`** as the stack name. You can optionally add your public IP address in the **YourIPAddress** field to limit the access only to your IP address. The default value (0.0.0.0/0) will allow traffic for all IP addresses. Choose **Next**.
![Screen capture of the Specify stack details dialog box](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/specify-stack-details.jpg)

1.  In the **Configure stack options** dialog box, don’t make any changes, and choose **Next**.

1.  In the **Capabilities and transforms** dialog box, review, scroll to the bottom of the page, and check all check boxes. Choose **Create stack**.
![Screen capture of the Capabilities and transforms dialog box](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/capabilities-and-transforms.png)
+  If the deployment fails, go to the deployment stack **Events** tab and confirm the root cause. A common root cause is `ecsExecutionRole` or `ecsAutoscaleRole` IAM roles already exist in the AWS account. Delete them and re-run deployment of the environment from the CloudFormation template.
+  When the template is in the `CREATE_COMPLETE` status, you can find information about created source environment by going to **AWS Management Console > CloudFormation**, choosing **App2Container-Demo stack**, and choosing the **Outputs** tab.

![Screen shot of the Outputs tab](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/outputs-tab.jpg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/step-2-deploy-use-case.html
---

# Step 2: Deploy a use case
<a name="step-2-deploy-use-case"></a>

**Important**
Once the stack has been successfully deployed, a sign-up email is sent to the configured admin user email. Using those credentials, the admin user can sign in to the Deployment dashboard to use the web application.

**Note**
The DevOps user with access to the AWS Management Console must provide the admin user with the CloudFront URL of the Deployment dashboard UI when the stack completes. The URL can be found in the **Outputs** tab of the CloudFormation stack.

1. Sign in to the Deployment dashboard as an admin user.

1. On the application landing page, choose **Deploy new use case**.

   This launches the deployment wizard, which walks you through building the use case.

 **Depicts Deployment dashboard landing page - fresh deployment**

![image8](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/image8.png)

**Note**
If you need to add additional users to your deployment, refer to the [Managing Cognito user pool](customization-guide.md#managing-cognito-user-pool) for more details.

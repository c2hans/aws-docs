---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/post-deployment-tasks.html
---

# Post-deployment steps
<a name="post-deployment-tasks"></a>

After DeepRacer on AWS has successfully deployed, complete the following steps to get started:

## Set up the admin account
<a name="set-up-the-admin-account"></a>

During deployment, you provided the email address of the individual who will serve as the admin of the deployment. An email containing temporary credentials has been sent to that email address. If you will be the admin of the deployment, click the link in the email to open the web console, and use your email address and the temporary password in the email to log in. Once logged in, you will be asked to provide an alias and a new password. Once those are provided, you will be brought to the home page for the web console.

**Note**
The invitation email will be sent from *no-reply@verificationemail.com*.

If someone else will be the admin of the deployment, they will receive an email containing temporary credentials for them to set up their admin account.

Once your/their account is set up, you/they can begin inviting users, creating races, and managing the deployment.

## Set usage limits
<a name="set-usage-limits"></a>

DeepRacer on AWS uses AWS resources in order to deliver its features and intended functionality. These resources are billed as they are used. Deployments that have more users and higher training volumes will accrue higher variable costs than those with less users and lower training volumes. For more information on the cost of operating this solution, please see the [Cost](cost.md) section.

DeepRacer on AWS allows admins to set usage limits at both the deployment level and the user level. Before inviting users to the instance, we recommend developing a plan that takes into account your budget and expected usage. You can reference the [Cost and usage management](admin-functions.md#cost-and-usage-management) section in this guide to learn more about how to apply these limits.

## Invite users
<a name="invite-users"></a>

You can invite users to the deployment via the Manage instance page. For more information on how to invite users, please see the [Invite a user section](admin-functions.md#invite-a-user).

After completing these initial configuration steps, you can begin using your DeepRacer on AWS deployment. For detailed information on how to use all features of the solution, see the [Use the solution](use-the-solution.md) guide.

## (Optional) Remove AWS WAF to reduce fixed costs
<a name="remove-waf"></a>

The solution deploys an AWS WAF web access control list (Web ACL). As of this revision, the Web ACL costs about USD $25.00 per month in the US East (N. Virginia) AWS Region, whether or not the deployment is in use. For a breakdown, refer to [Fixed cost of AWS WAF](cost.md#waf-fixed-cost). For current rates, refer to [AWS WAF pricing](https://aws.amazon.com/waf/pricing/). If you use the deployment for development, evaluation, or only occasionally, you may choose to remove AWS WAF if you want to cut this cost based on your specific use case and priorities.

**Reduced protection**
Removing AWS WAF removes a layer of protection from the solution’s API. Amazon Cognito still authenticates API requests. However, the API no longer has managed protection against bots, known bad inputs, or common exploits. It also loses protection against SQL injection and against requests from anonymous and low-reputation IP addresses, as well as the request body size limit and the rate limit on `/admin/` paths.
AWS doesn’t recommend removing AWS WAF from deployments that are shared with users outside your team or that are used for events.

The solution’s `Gateway` nested stack creates the Web ACL and associates it with the `prod` stage of the solution’s Amazon API Gateway REST API, named `<Namespace>-DeepRacerIndyApi`. The solution doesn’t associate the Web ACL with the CloudFront distribution.

AWS WAF bills for every Web ACL that exists, whether or not it is associated with a resource. To stop the charges, you must disassociate the Web ACL from the API stage and then delete it. You make these changes directly to the resources in your account. The solution template doesn’t provide an option to deploy without AWS WAF.

**Stack drift**
These steps change resources outside of AWS CloudFormation, so the stack drifts from its template. A later stack update that changes the Web ACL or its association can fail. After you update the solution to a new version, check whether the Web ACL exists again, and repeat these steps if it does.

 **Using the AWS Management Console**

To remove AWS WAF using the AWS Management Console, complete the following steps:

1. Open the [AWS WAF console](https://console.aws.amazon.com/wafv2/homev2/web-acls).

1. Choose the AWS Region where you deployed the solution.

1. Choose **Web ACLs**. Open the Web ACL that is associated with the `<Namespace>-DeepRacerIndyApi` API. You can confirm this on the **Associated AWS resources** tab.

1. On the **Associated AWS resources** tab, select the API Gateway stage and choose **Disassociate**.

1. Return to **Web ACLs**, select the Web ACL, and choose **Delete**.

 **Using the AWS Command Line Interface**

To remove AWS WAF using the AWS Command Line Interface (AWS CLI), complete the following steps:

1. Set the Region and namespace of your deployment. In the following example, replace `<region>` and `<namespace>` with your values:

   ```
   REGION=<region>
   NAMESPACE=<namespace>
   ```

1. Find the ARN of the API stage and the name and ID of the Web ACL associated with it:

   ```
   REST_API_ID=$(aws apigateway get-rest-apis --region $REGION \
     --query "items[?name=='${NAMESPACE}-DeepRacerIndyApi'].id" --output text)
   STAGE_ARN="arn:aws:apigateway:${REGION}::/restapis/${REST_API_ID}/stages/prod"

   aws wafv2 get-web-acl-for-resource --region $REGION --resource-arn $STAGE_ARN \
     --query "WebACL.[Name,Id]" --output text
   ```

1. Disassociate the Web ACL from the API stage:

   ```
   aws wafv2 disassociate-web-acl --region $REGION --resource-arn $STAGE_ARN
   ```

1. Delete the Web ACL. In the following example, replace `<web-acl-name>` and `<web-acl-id>` with the values that the previous step returned:

   ```
   LOCK_TOKEN=$(aws wafv2 get-web-acl --region $REGION --scope REGIONAL \
     --name <web-acl-name> --id <web-acl-id> --query LockToken --output text)

   aws wafv2 delete-web-acl --region $REGION --scope REGIONAL \
     --name <web-acl-name> --id <web-acl-id> --lock-token $LOCK_TOKEN
   ```

CloudFormation doesn’t re-create resources that you delete outside of the stack, so if you update the stack with the same template, AWS WAF isn’t restored. To restore it, create a Web ACL in the AWS WAF console and associate it with the API stage, or delete and redeploy the stack. Before you delete the stack, review [Uninstall the solution](uninstall-the-solution.md) for the resources that are retained.

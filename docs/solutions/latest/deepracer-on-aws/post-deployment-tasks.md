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

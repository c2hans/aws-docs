---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step2-deploy-idc-stack.html
---

# Step 2: Deploy the IDC stack
<a name="step2-deploy-idc-stack"></a>

In this step, you deploy the resources required to set up IDC, including mappings, roles, policies, and other configuration.

**Important**
Ensure that you log in using the account where you have configured the IAM Identity Center Instance for your AWS Organization. This can be either the Organization Management account or a delegated administration account that has been configured for IAM Identity Center.

**Note**
 **Using a Delegated Administration Account for IAM Identity Center**: AWS recommends using a delegated administration account for IAM Identity Center rather than the Organization Management account for security best practices. If you are using a delegated administration account, ensure that:
The delegated administration account has been properly configured for IAM Identity Center
You deploy the IDC stack in the delegated administration account
You provide the Organization Management account ID in the **Org Management Account Id** parameter (not the delegated admin account ID)
For more information on setting up delegated administration for IAM Identity Center, refer to the [AWS IAM Identity Center delegated administration documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html).

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and choose the button to launch the `IDC` stack CloudFormation template.

 [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-IDC.template&redirectId=ImplementationGuide)

The template launches in the US East (N.Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack** details page, enter a stack name for your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the AWS Identity and Access Management User Guide.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
**Important**
When using an external identity provider with SCIM integration (such as Microsoft Entra or Okta), you must create the ISB user groups in the external provider using the exact names specified in the group name parameters below, or the default names if left empty.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Namespace</b> </td><td> {{myisb}} </td><td>Use the same namespace from the <code>AccountPool</code> stack deployment of Innovation Sandbox. For example, <b>myisb</b>.</td></tr>
  <tr><td> <b>Org Management Account Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The AWS Account Id of the Organization Management account. This is always the Organization Management account ID, even if you are using a delegated administration account for IAM Identity Center.</td></tr>
  <tr><td> <b>Hub Account Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The AWS Account Id where the Innovation Sandbox Hub application (Data and Compute stacks) is (to be) deployed.</td></tr>
  <tr><td> <b>Identity Store Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The Identity Store Id of the IAM Identity Center Instance. Example: d-XXXXXXXXXX. To obtain the IdentityStoreId value from the IAM Identity Center console:<br />- Log in to the account your IDC account is located in.<br />- Open the IAM Identity Center console, and from the left pane, choose <b>Settings</b>.<br />- From the Settings page, on the Identity source tab, copy the <b>Identity Store ID</b> value.</td></tr>
  <tr><td> <b>SSO Instance Arn</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The ARN of the SSO instance in IAM Identity Center. Example: arn:aws:sso:::instance/ssoins- xxxxxxxxxxxxxxxx. To obtain the SsoInstanceArn value from the IAM Identity Center console:<br />- Log in to the account your IDC account is located in.<br />- Open the IAM Identity Center console, and from the left pane, choose <b>Settings</b>.<br />- From the Settings page, under Details, copy the <b>Instance ARN</b> value.</td></tr>
  <tr><td> <b>Admin Group Name</b> </td><td> {{&lt;Empty&gt;}} </td><td>A custom name to provide for the admin group. <b>Note</b>: If left empty, the group will be created with the name <b>&lt;namespace&gt;_IsbAdminsGroup</b>.</td></tr>
  <tr><td> <b>Manager Group Name</b> </td><td> {{&lt;Empty&gt;}} </td><td>A custom name to provide for the manager group. <b>Note</b>: If left empty, the group will be created with the name <b>&lt;namespace&gt;_IsbManagersGroup</b>.</td></tr>
  <tr><td> <b>User Group Name</b> </td><td> {{&lt;Empty&gt;}} </td><td>A custom name to provide for the user group. <b>Note</b>: If left empty, the group will be created with the name <b>&lt;namespace&gt;_IsbUsersGroup</b>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, review and choose to acknowledge the messages under Capabilities and transforms, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/webui-developer-guide.html
---

# Web UI
<a name="webui-developer-guide"></a>

The solution’s Web UI allows users to remediate AWS Security Hub findings in one-click, view and download past remediations, and delegate access to the solution.

The Web UI is not required to use the solution; you can alternatively configure fully-automated remediations to avoid the need for manual execution, or leverage the AWS Security Hub CSPM console to kick-off remediations using the **Remediate with ASR** custom action.

**Note**
You must set the `ShouldDeployWebUI` parameter to "yes" when deploying the Admin stack in order to use the solution’s Web UI.

## How it works
<a name="webui-guide-how-it-works"></a>

The solution’s Web User Interface is a Single-Page Web Application hosted in your account by Amazon S3 and distributed by Amazon CloudFront. The solution also deploys a REST API using API Gateway to support operations in the Web UI.

When the Admin stack is deployed, the solution’s Lambda functions begin loading all AWS Security Hub findings supported by the solution that are present in your Admin account into DynamoDB. Once this is complete, the Findings presented in the Web UI are kept in-sync with Security Hub in near real-time thanks to the EventBridge rules deployed by the solution.

Every week, the solution’s Lambda functions are triggered to refresh the DynamoDB table storing AWS Security Hub findings displayed in the Web UI. This ensures that stale data is cleaned up and our DynamoDB tables are kept up-to-date.. If you want to configure this baseline to run more or less often, modify the EventBridge Rule named `SO0111-ASR-SynchronizationFindingsLambdaWeeklyRule` located in your Admin account in the same region where you deployed the solution.

## Run remediations directly in the Web UI
<a name="webui-guide-findings-and-remediation"></a>

![web ui findings page](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/web-ui-findings-page.png)

On the **Findings** page, Admin or Delegated Admin users can view all AWS Security Hub findings supported by the solution for remediation. This includes findings for Security Hub member accounts onboarded with the Security Hub primary account. If the solution is also deployed in the aggregation region, then findings in any onboarded region will also be displayed. To view the list of findings supported by the solution, see the [playbooks section.](playbooks-1.md)

Account Operator users will only be able to view findings which originate in AWS Accounts that they have access to as defined in their invitation. Additionally, they will only be able to run remediations for resources in the accounts they are associated with.

To run remediations, select any number of items in the table and click **Actions > Remediate**. You can also **suppress** findings by clicking **Actions > Suppress**, which hides the selected findings from the default view. You can view suppressed findings at any time by clicking the **Show suppressed findings** toggle.

Once you have begun remediation for a finding, you can click the **Remediation Status** column while the remediation is either `In Progress` or `Failed` to be taken directly to that remediation on the **Execution History** page.

## Filter available findings and remediations
<a name="webui-guide-filter-findings"></a>

On both the **Findings** and **Execution History** pages, you can filter the data displayed in the table by any of the columns present in each respective table.

For example, on the **Findings** page, you may filter on **Finding Type** to search for specific kinds of AWS Security Hub findings (e.g. Lambda.1 or Athena.4) by clicking the search bar and selecting **Finding Type**.

**Note**
Values that are autopopulated in the search bar do not represent a comprehensive list of available data. The suggested values for each search critera only represent the data currently fetched and displayed in the UI.

You may also combine multiple attributes in a single search. For example, you can apply both **Finding Type** and **Resource ID** in your search to perform a logical `AND` query. Additionally, you can apply multiple of the same filter criteria to perform a logical `OR` search, such as **Finding Type = Lambda.1** and **Finding Type = Athena.4**. The same principles apply to the **Execution History** page

## Authentication & Authorization in the Web UI
<a name="webui-guide-auth"></a>

The solution’s Web UI is protected by authentication provided by Amazon Cognito. When the solution is deployed, a Cognito User Pool, Cognito App Client, and Cognito User Pool Domain are provisioned and configured alongside the Web UI. The email address provided as a parameter to the Admin stack is assigned temporary credentials and is given Administrator access to the Web UI.

There are three permission types that define a user’s access to the Web UI:

| Permission Type | Access Level | Use Case |
| --- | --- | --- |
| Admin | Full control in the Web UI; Can view all findings and remediations, run any remediation, and invite/view any user. | Assigned only to the user who deployed the Admin stack when they provide their email address during CloudFormation deployment. |
| Delegated Admin | Elevated control in the Web UI; Can view all findings and remediations, run any remediation, and invite/view Account Operator users. Cannot invite or view Admins and Delegated Admins in the Web UI. | The Admin user can delegate access to the solution by inviting Delegated Admin users, who will be able to run and manage any remediations. |
| Account Operator | Limited control in the Web UI; Restricted to view and remediate findings only in accounts they are associated with upon invitation. Cannot invite or view additional users. | Day-to-day users who should have limited access to run remediations in a subset of onboarded accounts. Admins or Delegated Admins are responsible for inviting these users and defining their scope. |

All users must be invited by an Admin or Delegated Admin before they are able to sign in to the Web UI. To invite additional users, an Admin or Delegated Admin can enter their email address and permission level on the **Invite Users** page of the Web UI.

Admins and Delegated Admins can also view, manage, and delete existing users. To see a list of all users, navigate to the **View Users** page.

To manage an existing user, select the user from the table and click **Manage User**. You can then delete the user by clicking **Delete User**. If the user is an Account Operator, you can modify the list of AWS Account IDs they have access to in the context of the solution. Changing the permission type for an existing user is not currently supported.

Please note that Delegated Admins are only be able to view and manage Account Operator users.

## Integrating with external IdPs
<a name="webui-guide-external-idps"></a>

You can customize the authentication mechanism provided by the solution to allow users to sign-in using your own OIDC or SAML identity provider, such as Okta or Microsoft Entra ID. The following steps for integrating with external IdPs requires access to the AWS Account where the Admin stack is deployed.

**Important**
Users must still be invited prior to signing in using any external IdP you configure to work with solution. Additionally, the email address linked to their IdP profile must match the email provided in their invitation.

### Step 1 - Locate the solution’s user pool
<a name="step-1-locate-the-solutions-user-pool"></a>

In the Amazon Cognito console, locate the solution’s user pool named **SO0111-ASR-UserPool**.

Click the user pool name **SO0111-ASR-UserPool** to be taken to the **overview** page. From there, select **Social and external providers** from the navigation bar.

### Step 2 - Add your identity provider
<a name="step-2-add-your-identity-provider"></a>

On the **Social and external providers** page, click the **Add identity provider** button on the top right.

Select either **OIDC** or **SAML**, depending on your identity provider.

Once you select your provider type, you will be prompted to enter information about your identity provider.

Fill in the following fields for **SAML** providers:

1.  **Provider name**: A friendly name for your provider

1.  **IdP-initiated SAML sign-in**: Select `Require SP-initiated SAML assertions - Recommended`

1.  **Metadata document source**: Select `Upload metadata document`

1.  **Metadata document**: Upload your SAML metadata document provided by your IdP.

1. Under **Map attributes between your SAML provider and your user pool** click **Add another attribute**. For **User pool attribute** select `email` from the dropdown. For **SAML attribute**, enter the full name of the attribute where the user’s email address is stored in your SAML identity provider. For example, `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`.

1. Click **Add identity provider** to save your changes.

Fill in the following fields for **OIDC** providers:

1.  **Provider name**: A friendly name for your provider

1.  **Client ID**: Enter the client ID provided by your OpenID Connect identity provider.

1.  **Client secret**: Enter the client secret provided by OpenID Connect identity provider.

1.  **Authorized scopes**: Enter `openid profile email`

1.  **Attribute request method**: Select `GET` or `POST` based on your identity provider’s configuration.

1.  **Setup method**: Select `Auto fill through issuer URL` and enter the **Issuer URL** from your OIDC provider. Alternatively, enter the values manually.

1. Under **Map attributes between your OpenID Connect provider and your user pool** click **Add another attribute**. For **User pool attribute** select `email` from the dropdown. For **OpenID Connect attribute**, enter the full name of the attribute where the user’s email address is stored in your OIDC identity provider. For example, `email`.

1. Click **Add identity provider** to save your changes.

**Important**
You must add an attribute mapping for the `email` user pool attribute, even if your identity provider’s attribute name is also `email`.

### Step 3 - Add your provider to the solution’s App Client
<a name="step-3-add-your-provider-to-the-solutions-app-client"></a>

Navigate to the **App Clients** page and select the client named **SO0111-ASR-WebUI-UserPoolClient**.

Click the **Login Pages** tab and under **Managed login pages configuration** click **Edit**.

In the **Identity providers** field, add the identity provider you created in the previous step. Click **Save Changes**.

### Step 4 - Configure your identity provider
<a name="step-4-configure-your-identity-provider"></a>

To allow your identity provider to redirect to the solution’s Web UI after login, you must allowlist the following URLs in your IdP configuration.

Depending on your provider type, allowlist one of the following Callback URLs:

1. SAML Callback URL: https://so0111-asr-{{<your-aws-account-id>}}.auth.{{<aws-region>}}.amazoncognito.com/saml2/idpresponse

1. OIDC Callback URL: https://so0111-asr-{{<your-aws-account-id>}}.auth.{{<aws-region>}}.amazoncognito.com/oauth2/idpresponse

You should replace `<your-aws-account-id>` with the AWS Account ID where you have deployed the Admin stack, and `<aws-region>` with the region where you deployed the Admin stack.

### Step 4 - Verify your integration
<a name="step-4-verify-your-integration"></a>

Navigate to the Web UI login page. Confirm that your custom identity provider is visible on the login page.

To test the integration, invite a new user using the **Invite Users** page. Then, ensure the user can authenticate by clicking your custom identity provider on the Web UI login page.

Please note that the user’s profile in your custom IdP must be linked to the same email address provided in their invitation. In other words, the email address in your provider’s claims must match the invitation.

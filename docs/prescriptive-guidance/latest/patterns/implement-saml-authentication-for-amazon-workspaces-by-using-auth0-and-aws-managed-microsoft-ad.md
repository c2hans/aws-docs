---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad.html
---

# Implement SAML 2.0 authentication for Amazon WorkSpaces by using Auth0 and AWS Managed Microsoft AD
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad"></a>

*Siva Vinnakota and Shantanu Padhye, Amazon Web Services*

## Summary
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-summary"></a>

This pattern explores how you can integrate Auth0 with AWS Directory Service for Microsoft Active Directory to create a robust SAML 2.0 authentication solution for your Amazon WorkSpaces environment. It explains how to establish federation between these AWS services to enable advanced features such as multi-factor authentication (MFA) and custom login flows while preserving seamless desktop access through AWS Managed Microsoft AD. Whether you're managing only a handful of users or thousands, this integration helps provide flexibility and security for your organization. This pattern provides the steps for the setup process so you can implement this solution in your own environment.

## Prerequisites and limitations
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Managed Microsoft AD
+ A provisioned desktop in Amazon WorkSpaces Personal that is associated with AWS Managed Microsoft AD
+ An Amazon Elastic Compute Cloud (Amazon EC2) instance
+ An Auth0 account

**Limitations**

Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-architecture"></a>

The SAML 2.0 authentication process for a WorkSpaces client application consists of five steps that are illustrated in the following diagram. These steps represent a typical workflow for logging in. You can use this distributed approach to authentication after you follow the instructions in this pattern, to help provide a structured and secure method for user access.

![Workflow for the SAML 2.0 authentication process for a WorkSpaces client application.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5a0f227c-c111-495b-9fde-98ae7832bb10/images/957b2a11-e898-4c4f-ae4e-c2e85bfa93a0.png)

 Workflow:

1. **Registration**. The user launches the client application for WorkSpaces and enters the WorkSpaces registration code for their SAML-enabled WorkSpaces directory. WorkSpaces returns the Auth0 identity provider (IdP) URL to the client application.

1. **Login. **The WorkSpaces client redirects to the user’s web browser by using the Auth0 URL.  The user authenticates with their username and password. Auth0 returns a SAML assertion to the client browser. The SAML assertion is an encrypted token that asserts the user’s identity.

1. **Authenticate**. The client browser posts the SAML assertion to the AWS Sign-In endpoint to validate it. AWS Sign-In allows the caller to assume an AWS Identity and Access Management (IAM) role. This returns a token that contains temporary credentials for the IAM role.

1. **WorkSpaces login**. The WorkSpaces client presents the token to the WorkSpaces service endpoint. WorkSpaces exchanges the token for a session token and returns the session token to the WorkSpaces client with a login URL. When the WorkSpaces client loads the login page. the username value is populated by the `NameId` value that’s passed in the SAML response.

1. **Streaming**. The user enters their password and authenticates against the WorkSpaces directory. After authentication, WorkSpaces returns a token to the client. The client redirects back to the WorkSpaces service and presents the token. This brokers a streaming session between the WorkSpaces client and the WorkSpace.

**Note**
To set up a seamless single sign-on experience that doesn’t require a password prompt, see the [Certificate-based authentication and WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication.html) in the WorkSpaces documentation.

## Tools
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-tools"></a>

**AWS services**
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) is a fully managed virtual desktop infrastructure (VDI) service that provides users with cloud-based desktops without having to procure and deploy hardware or install complex software.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.

**Other tools**
+ [Auth0](https://auth0.com/) is an authentication and authorization platform that helps you manage access to your applications.

## Epics
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-epics"></a>

### Configure the Active Directory LDAP Connector in Auth0
<a name="configure-the-active-directory-ldap-connector-in-auth0"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the Active Directory LDAP connector in Auth0 with AWS Managed Microsoft AD. | 1. Log in to the Auth0 dashboard and choose **Authentication**, **Enterprise**, **Active Directory / LDAP**. Choose **Create a connection**.<br />2. Provide the name for your Active Directory connection, and then choose **Create**.<br />3. On the **Setup** tab, download the agent for your operating  system.<br />When the installation is complete, your default browser displays a prompt for the ticket URL.<br />4. Enter the provisioning ticket URL, which should be unique for your connection string, and then choose **Continue**.<br />5. In the **AD LDAP Configuration** dialog box, for **Username** and **Password**, enter your administrator credentials, and then choose **Save**.<br />When the connection to Auth0 has been established, the configuration log is displayed with a reporting status of **OK** for all checks. | Cloud administrator, Cloud architect |
| Create an application in Auth0 to generate the SAML metadata manifest file. | 1. Log in to the Auth0 dashboard and create a new application by following the instructions in the [Auth0 documentation](https://auth0.com/docs/get-started/auth0-overview/create-applications).<br />2. On the Auth0 dashboard, choose the application name to access its configuration settings. On the **AddOns** tab, choose **SAML2 Web App**.<br />3. On the **Settings** tab for the add-on, for **Application Callback URL**, enter **https://signin.aws.amazon.com/saml**. This is where the SAML token will send the `POST` request.<br />4. On the **Settings** tab, in the **Settings** box, paste the following SAML configuration code in JSON format:<pre>{<br />  "audience": "https://signin.aws.amazon.com/saml",<br />  "mappings": {<br />    "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sAMAccountName",<br />    "name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"<br />  },<br />  "createUpnClaim": false,<br />  "passthroughClaimsWithNoMapping": false,<br />  "mapUnknownClaimsAsIs": false,<br />  "mapIdentities": false,<br />  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",<br />  "nameIdentifierProbes": [<br />    "http://schemas.auth0.com/sAMAccountName"<br />  ]<br />}</pre><br />5. Save, and then choose **Enable**.<br />6. Choose the **Usage** tab, and download the metadata manifest file for the identity provider. This  information is required for the next steps.<br />7. Close the **SAML2 Web App** window.<br />8. On the applications screen, choose **Connections**. Under **Enterprise**, select the correct Active Directory/LDAP connector and enable it. | Cloud administrator, Cloud architect |

### Set up IdP, role, and policy for SAML 2.0 in IAM
<a name="set-up-idp-role-and-policy-for-saml-2-0-in-iam"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a SAML 2.0 IdP in IAM. | To set up SAML 2.0 as an IdP, follow the steps that are outlined in [Create a SAML identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the IAM documentation. | Cloud administrator |
| Create an IAM role and policy for SAML 2.0 federation. | 1. Create an IAM role for SAML 2.0 federation. For instructions, see [step 2](https://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html#create-saml-iam-role) in the instructions for setting up SAML 2.0 for WorkSpaces Personal in the WorkSpaces documentation.<br />2. Create an IAM policy and associate it with the role you created in the previous step. For instructions, see [step 3](https://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html#embed-inline-policy) in the instructions for setting up SAML 2.0 for WorkSpaces Personal in the WorkSpaces documentation. | Cloud administrator |

### Configure assertions in Auth0
<a name="configure-assertions-in-auth0"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Auth0 and SAML assertions. | You can use Auth0 actions to configure assertions in SAML 2.0 responses. A SAML assertion is an encrypted token that asserts the user’s identity.1. Sign in to the Auth0 dashboard. Choose **Actions**, **Library**, **Create Action**, **Build from scratch**.<br />2. Provide the following values and then choose **Create**.<br />**Name: Specify a name for the action**<br />**Trigger: Choose Login/Post Login**<br />**Runtime: Choose Node 18**<br />3. On the next screen, enter the following code:<pre>exports.onExecutePostLogin = async (event, api) => <br />{   if (event.client.name === "Workspace_Saml")<br />   {     const awsRole = 'arn:aws:iam::030784294031:role/Workspace_Auth0,arn:aws:iam::030784294031:saml-provider/Auth0';<br />     const awsRoleSession = event.user.sAMAccountName;<br />     const email = event.user.emails[0];<br />     api.samlResponse.setDestination('https://signin.aws.amazon.com/saml');<br />     api.samlResponse.setAttribute('https://aws.amazon.com/SAML/Attributes/Role', awsRole)<br />     api.samlResponse.setAttribute('https://aws.amazon.com/SAML/Attributes/RoleSessionName', awsRoleSession)<br />     api.samlResponse.setAttribute('https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email', email)<br />   } return;<br />};</pre><br />4. Choose **Deploy**.<br />This completes the setup of SAML 2.0 authentication for WorkSpaces Personal desktops. The [Architecture](#implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-architecture) section illustrates the authentication process after setup. | Cloud administrator |

## Troubleshooting
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| SAML 2.0 authentication issues in WorkSpaces<br />** ** | If you encounter any issues when you implement SAML 2.0 authentication for WorkSpaces Personal, follow the steps and links outlined in the [AWS re:Post article](https://repost.aws/knowledge-center/workspaces-saml-authentication-issues) on troubleshooting SAML 2.0 authentication.<br />For additional information about investigating SAML 2.0 errors while accessing WorkSpaces, see:+ [How do I create a HAR file and Console logs from my browser for an AWS Support case?](https://repost.aws/knowledge-center/support-case-browser-har-file) (AWS re:Post)<br />+ [View a SAML response in your browser](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml_view-saml-response.html) (IAM documentation)  |

## Related resources
<a name="implement-saml-authentication-for-amazon-workspaces-by-using-auth0-and-aws-managed-microsoft-ad-resources"></a>
+ [Set up SAML 2.0 for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html) (WorkSpaces documentation)
+ [Auth0 documentation](https://auth0.com/docs)

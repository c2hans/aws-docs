---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-openid-connect-oidc.html
---

# Launch with OpenID Connect (OIDC)
<a name="launch-with-openid-connect-oidc"></a>

 **Time to deploy**: Approximately 30 minutes

## Prerequisites
<a name="prerequisites"></a>

**Important**
The Centralized Logging with OpenSearch console is served via the CloudFront distribution, which is considered as an internet information service. If you are deploying the solution in **AWS China Regions**, the domain must have a valid [ICP Recordal](https://www.amazonaws.cn/en/support/icp).
+ A domain. You will use this domain to access the Centralized Logging with OpenSearch console (Required for AWS China Regions, optional for AWS Regions).
+ An SSL certificate in AWS IAM. The SSL must be associated with the given domain. Follow the instructions in [Upload SSL Certificate to IAM](additional-resources.md#upload-ssl-certificate-to-iam). Note that this is required for AWS China Regions, but is not recommended for all AWS Regions.
+ ACM certificate in the US East (N. Virginia) Region (us-east-1). Note that this is not required for AWS China Regions, and is optional for AWS Regions.

## Deployment Overview
<a name="deployment-overview-1"></a>

Use the following steps to deploy this solution on AWS.
+  [Step 1. Create OIDC client](#step-1.-create-oidc-client)
+  [Step 2. Launch the stack](#step-2.-launch-the-stack)
+  [Step 3. Setup DNS Resolver](#step-3.-setup-dns-resolver)
+  [Step 4. Launch the web console](#step-4.-launch-the-web-console)

## Step 1. Create OIDC client
<a name="step-1.-create-oidc-client"></a>

You can use different kinds of OpenID Connector (OIDC) providers. This section introduces Option 1 to Option 5.
+ (Option 1) Using Amazon Cognito from another Region as an OIDC provider.
+ (Option 2) [Authing](https://www.authing.cn/), which is an example of a third-party authentication provider in China.
+ (Option 3) [Keycloak](https://github.com/aws-samples/keycloak-on-aws), which is a solution maintained by AWS and can serve as an authentication identity provider.
+ (Option 4) [ADFS](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services), which is a service offered by Microsoft.
+ (Option 5) Other third-party authentication platforms such as [Auth0](https://auth0.com/).

Complete the following steps to create an OIDC client, and obtain the `client_id` and `issuer`.

### (Option 1) Using Amazon Cognito User Pool from another Region
<a name="option-1-using-amazon-cognito-user-pool-from-another-region"></a>

You can use the Amazon Cognito User Pool in a supported AWS Standard Region as the OIDC provider.

1. Go to the Amazon Cognito console in an AWS Standard Region.

1. Set up the hosted UI with the Amazon Cognito console based on this guide.

1. Choose **Public client** when selecting the **App type**.

1. Enter the **Callback URL** and **Sign out URL** using your domain name for Centralized Logging with the OpenSearch console. If your hosted UI is set up, you should be able to see something like the following.

    **Hosted UI. Configure the hosted UI for this app client.**
![image18](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image18.png)

1. Save the App client ID, User pool ID and the AWS Region to a file, which will be used later.

    **App client list. Appl clients and analytics.**
![image19](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image19.png)

    **User pool overview screen.**
![image20](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image20.png)

In [Step 2. Launch the stack](#step-2.-launch-the-stack), the OidcClientID is the App client ID, and OidcProvider is `https://cognito-idp.${REGION}.amazonaws.com/${USER_POOL_ID}`.

### (Option 2) Authing.cn OIDC client
<a name="option-2-authing.cn-oidc-client"></a>

1. Go to the [Authing console](https://console.authing.cn/console).

1. Create a user pool if you don’t have one.

1. Select the user pool.

1. On the left navigation bar, select **Self-built App** under **Applications**.

1. Choose the **Create** button.

1. Enter the **Application Name** and **Subdomain**.

1. Save the App ID (that is, client\_id) and Issuer to a text file from Endpoint Information, which will be used later.

    **Endpoint information screen.**
![image21](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image21.png)

1. Update the `Login Callback URL` and `Logout Callback URL` to your IPC recorded domain name.

1. Set the **Authorization Configuration**.

    **Authorization configuration screen.**
![image22](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image22.png)

You have successfully created an authing self-built application.

### (Option 3) Keycloak OIDC client
<a name="option-3-keycloak-oidc-client"></a>

1. Deploy the Keycloak solution by following [this guide](https://aws-samples.github.io/keycloak-on-aws/en/implementation-guide/deployment/).

1. Sign in to the Keycloak console.

1. On the left navigation bar, select **Add realm**. Skip this step if you already have a realm.

1. Go to the realm setting page. Choose **Endpoints**, and then **OpenID Endpoint Configuration** from the list.

    **Example screen with General tab and fields for data input.**
![image23](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image23.jpg)

1. In the JSON file that opens up in your browser, record the **issuer** value, which will be used later.

    **Example "issuer" value.**
![image24](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image24.jpg)

1. Go back to the Keycloak console and select **Clients** on the left navigation bar, and choose **Create**.

1. Enter a Client ID, which must contain 24 letters (case-insensitive) or numbers. Record the **Client ID**, which will be used later.

1. Change client settings. Enter `link:https://<Centralized Logging with OpenSearch Console domain>` in **Valid Redirect URIs**, and enter `*` and `\+` in \*Web Origins\*.

1. In the **Advanced Settings**, set the **Access Token Lifespan** to at least 5 minutes.

1. Select **Users** on the left navigation bar.

1. Choose **Add user** and enter **Username**.

1. After the user is created, select **Credentials**, and enter **Password**.

   The issuer value is `https://<KEYCLOAK_DOMAIN_NAME>/auth/realms/<REALM_NAME>`.

### (Option 4) ADFS OpenID Connect Client
<a name="option-4-adfs-openid-connect-client"></a>

1. Make sure your ADFS is installed. For information about how to install ADFS, refer to [this guide](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/ad-fs-deployment-guide).

1. Make sure you can log in to the ADFS Sign On page. The URL should be `https://adfs.domain.com/adfs/ls/idpinitiatedSignOn.aspx`, and you must replace **adfs.domain.com** with your real ADFS domain.

1. Log on your Domain Controller, and open Active Directory Users and Computers.

1. Create a **Security Group** for Centralized Logging with OpenSearch Users, and add your planned Centralized Logging with OpenSearch users to this Security Group.

1. Log on to the ADFS server, and open **ADFS Management**.

1. Right click **Application Groups**, choose **Application Group**, and enter the name for the Application Group. Select **Web browser accessing a web application** option under **Client-Server Applications**, and choose **Next**.

1. Record the **Client Identifier** (client\_id) under **Redirect URI**, enter your Centralized Logging with OpenSearch domain (for example, xx.domain.com), and choose **Add**, and then choose **Next**.

1. In the **Choose Access Control Policy** window, select **Permit specific group**, choose **parameters** under Policy part, add the created Security Group in Step 4, then choose **Next**. You can configure other access control policy based on your requirements.

1. Under the **Summary** window, choose **Next**, and choose **Close**.

1. Open the Windows PowerShell on ADFS Server, and run the following commands to configure ADFS to allow CORS for your planned URL.

   ```
   Set-AdfsResponseHeaders -EnableCORS $true
   Set-AdfsResponseHeaders -CORSTrustedOrigins https://<your-centralized-logging-with-opensearch-domain>
   ```

1. Under Windows PowerShell on ADFS server, run the following command to get the Issuer (issuer) of ADFS, which is similar to `https://adfs.domain.com/adfs`.

   ```
   Get-ADFSProperties | Select IdTokenIssuer
   ```

    **Example IdTokenIssuer.**
![image25](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image25.png)

### (Option 5) Other third-party authentication platforms such as Auth0
<a name="option-5-Other-third-party-authentication-platforms-such-as-Auth0"></a>

1. On Auth0, go to the [Applications page](https://manage.auth0.com/dashboard/)

1. Click **\+ Create Application**

1. Choose **Single Page Web Applications**

1. Go to Settings

1. Save `Domain` - this is your `OidcProvider` value

1. Save `Client ID` - this is your `OidcClientId` value

    **Example Auth0 application Domain & Client ID**
![image49](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image49.png)

1. Scroll down to **Application URIs**

1. Update `Allowed Callback URLs` and `Allowed Logout URLs`

    **Example Auth0 application redirect and logout URL’s**
![image50](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image50.png)

1. Click **Save Changes**

## Step 2. Launch the stack
<a name="step-2.-launch-the-stack"></a>

**Important**
You can only have one active Centralized Logging with OpenSearch solution stack in one Region of an AWS account. If your deployment failed (for example, not meeting the requirements in [prerequisites](#prerequisites)), make sure you have deleted the failed stack before retrying the deployment.

1. Sign in to the AWS Management Console and use the following buttons to launch the AWS CloudFormation template.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-openid-connect-oidc.html)

1. The template is launched in the default Region after you log in to the console. To launch the Centralized Logging with OpenSearch solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for the template and modify them as necessary.
   + If you are launching the solution in a new VPC, this solution uses the following parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-openid-connect-oidc.html)
   + If you are launching the solution in an existing VPC, this solution uses the following parameters:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-openid-connect-oidc.html)

     IMPORTANT: \* If you are deploying the solution in AWS China Regions, you must enter **Domain** and **IamCertificateID**. \* If you are deploying the solution in AWS Regions:

     \+
     + When a custom domain name is required, you must enter **Domain** and **AcmCertificateArn**.
     + If no custom domain name is required, leave it blank for **Domain**, **IamCertificateID**, and **AcmCertificateArn**.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Add new tag** and type in the following key and value:

   1. Key: `CLOSolutionCostAnalysis`

   1. Value: `CLOSolutionCostAnalysis`

   You can activate the `CLOSolutionCostAnalysis` tag after all resources have been successfully deployed. Choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

## Step 3. Setup DNS Resolver
<a name="step-3.-setup-dns-resolver"></a>

This solution provisions a CloudFront distribution that gives you access to the Centralized Logging with OpenSearch console.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).

1. Select the solution’s stack.

1. Choose the **Outputs** tab.

1. Obtain the **WebConsoleUrl** as the endpoint.

1. Create a CNAME record in the DNS resolver, which points to the endpoint address.

## Step 4. Launch the web console
<a name="step-4.-launch-the-web-console"></a>

**Important**
Your login credentials are managed by the OIDC provider. Before signing in to the Centralized Logging with OpenSearch console, make sure you have created at least one user in the OIDC provider’s user pool.

1. Use the previous assigned CNAME to open the **OIDC Customer Domain URL** using a web browser.

1. Choose Sign in to Centralized Logging with OpenSearch, and navigate to OIDC provider.

1. Enter sign-in credentials. You may be requested to change your default password for first-time login, which depends on your OIDC provider’s policy.

1. After the verification is complete, the system opens the Centralized Logging with OpenSearch web console.

Once you have logged into the Centralized Logging with OpenSearch console, you can [import an Amazon OpenSearch Service domain](getting-started.md#step-1-import-an-amazon-opensearch-domain) and build log analytics pipelines.

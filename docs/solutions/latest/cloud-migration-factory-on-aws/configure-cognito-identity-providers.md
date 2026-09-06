---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/configure-cognito-identity-providers.html
---

# Step 11: (Optional) Configure additional identity providers in Amazon Cognito
<a name="configure-cognito-identity-providers"></a>

If you selected `true` for the optional **Allow additional identity provider to be configured in Cognito** parameter when launching the stack, you can set up additional IdPs in Amazon Cognito to allow sign in using existing SAML IdP. The process for setting up the external IdP varies between providers. This section describes the Amazon Cognito configuration and generic steps to configure the external IdP.

Perform the following steps to collect information from Amazon Cognito to provide to the external IdP:

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the **Cloud Migration Factory on AWS** stack.

1. Select the **Outputs** tab.

1. In the **Key** column, locate **UserPoolId** and record the **Value** to use later during setup.

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. Choose the User pool that matches the User pool ID from the solution stack output.

1. Choose the **App Integration** tab and record the **Cognito domain** to use later during setup.

Perform the following steps within your existing IdP’s management interface:

**Note**
These instructions are generic and will differ between providers. Consult your IdP’s documentation for full details on setting up SAML applications.

1. Navigate to your IdP’s management interface.

1. Choose the option to add applications or setup SAML authentication for an application, and create or add a new application.

1. Within the setup of this SAML application, you will be asked for the following values:

   1.  **Identifier (Entity ID)** or something similar. Provide the following value:

      ```
      urn:amazon:cognito:sp:<UserPoolId recorded earlier>
      ```

   1.  **Reply URL (Assertion Consumer Service URL)** or something similar. Provide the following value:

      ```
      https://<Amazon Cognito domain recorded earlier>/saml2/idpresponse
      ```

   1.  **Attributes and Claims** or something similar. At a minimum, ensure that a unique identifier or subject is configured along with an attribute that provides the email address of the user.

1. There will either be a **Metadata URL** or the ability to download a **Metadata XML** file. Download a copy of the file or record the URL provided to use later during setup.

1. Within the setup, configure the access list of users from the IdP that are allowed to sign in to the CMF application. All users that are granted access to the application in the IdP will automatically be granted read only access to the CMF console.

Perform the following steps to add the new IdP to the Amazon Cognito user pool created during the stack deployment:

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. Choose the User pool that matches the User pool ID from the solution stack output.

1. Choose the **Sign-in experience** tab.

1. Choose **Add identity provider** then choose **SAML** as the third-party provider.

1. Provide a name for the provider; this will be displayed to the user on the CMF sign-in screen.

1. In the **Metadata document source** section, either provide the **Metadata URL** captured from the IDP SAML setup or upload the **Metadata XML** file.

1. In the **Map attributes** section, choose **Add another attribute**.

1. Choose **email** for the **User pool attribute** value. For the **SAML attribute**, enter the name of the attribute that your external IdP will provide the email address to.

1. Choose **Add identity provider** to save this configuration.

1. Choose the **App integration** tab.

1. From within the **App client list** section, choose the migration factory application client (there should only be one listed) by clicking the name.

1. From the **Hosted UI** section, choose **Edit**.

1. Update the **Identity providers** selected by selecting the new IdP name you added in step 5 and deselecting **Cognito User Pool**.
**Note**
Cognito User Pool is not required because this is built into the CMF sign-in screen, and if selected, it will show twice.

1. Choose **Save changes**.

The configuration is now complete. On the CMF sign-in page, you will see the button **Sign in with your corporate ID**. Choosing this option will display the provider you have configured previously. Users who choose this option will be directed to sign in and then return to the CMF console once successfully signed in.

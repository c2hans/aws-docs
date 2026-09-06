---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/configure-entra-id.html
---

# Configure Microsoft Entra ID
<a name="configure-entra-id"></a>

This page provides detailed walkthroughs for federating the Amazon Cognito user pool with Microsoft Entra ID (formerly Azure Active Directory) using either OIDC or SAML 2.0. Microsoft Entra ID is the most common external identity provider for SDMA.

Before you begin, complete the prerequisites and gather your Amazon Cognito values described in [Single sign-on (SSO)](sso.md). These procedures use the placeholders defined in [Placeholders used in these procedures](sso.md#sso-placeholders). For protocol-level background that applies to any identity provider, see [Configure any external identity provider](external-identity-provider.md).

## Connect Entra ID using OIDC
<a name="entra-oidc"></a>

### Step 1: Create an application registration in Entra ID
<a name="entra-oidc-create-app"></a>

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) on the Microsoft website.

1. Navigate to **Enterprise applications** > **New application**.

1. Choose **Create your own application**.

1. Enter a name for the application (for example, `Spatial Data Management`).

1. Select **Register an application to integrate with Entra ID (App you’re developing)**, and then choose **Create**.

### Step 2: Configure the application registration
<a name="entra-oidc-configure-registration"></a>

1. In the application registration, add the following **Redirect URI** with a platform type of **Web**:

   ```
   https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com/oauth2/idpresponse
   ```
**Tip**
You can find the domain portion under **Branding** > **Domain** in the Amazon Cognito console. Make sure you append `/oauth2/idpresponse` to the domain value.

1. Choose **Register**.

1. On the **Overview** page, note the **Application (client) ID** and the **Directory (tenant) ID**. You need these values later.

### Step 3: Create a client secret
<a name="entra-oidc-client-secret"></a>

1. In your registered application, choose **Certificates & secrets**.

1. Choose the **Client secrets** tab, and then choose **\+ New client secret**.

1. Enter a description (for example, `Cognito OIDC integration`).

1. Set an expiration (a maximum of 24 months is recommended), and then choose **Add**.
**Important**
Immediately copy the secret **Value** (not the **Secret ID**) and store it securely. The value is shown only once, and you provide it to Amazon Cognito in a later step.

### Step 4: Configure API permissions
<a name="entra-oidc-api-permissions"></a>

1. In your registered application, choose **API permissions** > **Add a permission**.

1. Choose **Microsoft Graph** > **Delegated permissions**.

1. Add the following permissions:
   +  `openid`
   +  `profile`
   +  `email`

### Step 5: Enable the groups claim
<a name="entra-oidc-groups-claim"></a>

If you plan to use Entra ID groups to assign permissions in SDMA, add a groups claim to the tokens.

Entra ID includes only groups that are assigned to the application when you select **Groups assigned to the application**. Before you continue, assign those groups: in the Microsoft Entra admin center, choose **Enterprise applications**, select the application you created in Step 1, choose **Users and groups**, and then choose **Add user/group**.

1. In your registered application, choose **Token configuration**.

1. Choose **Add groups claim**.

1. Select **Group ID** for all token types (ID and Access).

1. Select **Groups assigned to the application**. This is recommended for large organizations to avoid exceeding the limit on the number of groups a token can emit.

1. Choose **Save**.

### Step 6: (Optional) Emit group display names instead of group IDs
<a name="entra-oidc-group-names"></a>

By default, the groups claim emits group IDs (GUIDs). To emit group display names, edit the application manifest.

1. In your registered application, choose **Manifest**.

1. Locate the `optionalClaims` section, and add `cloud_displayname` to the groups claim for `idToken` and `accessToken`:

   ```
   "optionalClaims": {
     "idToken": [
       {
         "name": "groups",
         "source": null,
         "essential": false,
         "additionalProperties": ["cloud_displayname"]
       }
     ],
     "accessToken": [
       {
         "name": "groups",
         "source": null,
         "essential": false,
         "additionalProperties": ["cloud_displayname"]
       }
     ]
   }
   ```

1. Save the modified manifest.

### Step 7: Create the OIDC identity provider in Amazon Cognito
<a name="entra-oidc-cognito-idp"></a>

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), choose **User pools**, and then select your user pool.

1. Choose **Sign-in experience** > **Federated identity provider sign-in**.

1. Choose **Add identity provider**, and then choose **OpenID Connect (OIDC)**.

1. Configure the following:
   +  **Provider name** – Enter a name, for example `EntraID`. This name appears on the sign-in button.
   +  **Client ID** – The Entra ID **Application (client) ID** from Step 2.
   +  **Client secret** – The secret value from Step 3.
   +  **Authorized scopes** – Enter `openid email profile` (space-separated).
   +  **Attribute request method** – Keep the default (`GET`).
   +  **Issuer URL** – Enter the following, replacing `<TENANT_ID>` with your **Directory (tenant) ID**:

     ```
     https://login.microsoftonline.com/<TENANT_ID>/v2.0
     ```

1. Under **Map attributes between your OpenID Connect provider and your user pool**, configure the following mappings:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/configure-entra-id.html)

1. Choose **Add identity provider**.

Then enable the identity provider ([Enable the identity provider for the app client](external-identity-provider.md#idp-enable-app-client)) and verify the integration ([Verify the integration](external-identity-provider.md#idp-test)).

## Connect Entra ID using SAML 2.0
<a name="entra-saml"></a>

### Step 1: Create an enterprise application in Entra ID
<a name="entra-saml-create-app"></a>

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) on the Microsoft website.

1. Navigate to **Enterprise applications** > **New application**.

1. Choose **Create your own application**.

1. Enter a name for the application (for example, `Spatial Data Management SAML`).

1. Select **Integrate any other application you don’t find in the gallery (Non-gallery)**, and then choose **Create**.

### Step 2: Configure basic SAML settings
<a name="entra-saml-basic-config"></a>

1. In the enterprise application, choose **Single sign-on**, and then choose **SAML**.

1. In the **Basic SAML Configuration** section, choose **Edit**, and enter the following (see [Gather your Amazon Cognito values](sso.md#sso-gather-cognito-values) for these values):
   +  **Identifier (Entity ID)** – `urn:amazon:cognito:sp:<USER_POOL_ID>`
   +  **Reply URL (Assertion Consumer Service URL)** – `https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com/saml2/idpresponse`

1. Choose **Save**.

### Step 3: Configure attributes and claims
<a name="entra-saml-claims"></a>

1. In the **Attributes & Claims** section, choose **Edit**.

1. Confirm that the following claims are configured. Entra ID emits these standard claims by default:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/configure-entra-id.html)

1. (Optional) To use Entra ID groups for permission assignment in SDMA, add a group claim:

   1. Choose **Add a group claim**.

   1. Under **Which groups associated with the user should be returned in the claim?**, select **Groups assigned to the application**. This is recommended for large organizations to avoid exceeding the limit on the number of groups a token can emit.

   1. Under **Source attribute**, choose the value that Entra ID emits for each group:
      +  **Group ID** – Emits the group object ID (a GUID). This is the default.
      +  **Cloud-only group display names** – Emits the display name for groups created in Entra ID. Choose this to emit human-readable group names instead of GUIDs.
      +  **sAMAccountName** or `NetBIOSDomain\sAMAccountName` – Emits the name for groups synchronized from on-premises Active Directory.

   1. (Optional) Expand **Advanced options** to customize the claim name or to apply a group filter.

   1. Choose **Save**.

      The groups are emitted in the claim `http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`.
**Important**
Whichever source attribute you choose, you must use that same value form when you assign permissions to groups in SDMA. If you emit group display names, assign SDMA access using those names; if you emit group IDs, assign access using the GUIDs. For more information, see [Access Management](access-control.md).

### Step 4: Obtain the identity provider metadata
<a name="entra-saml-metadata"></a>

1. In the **SAML Certificates** section, copy the **App Federation Metadata Url**, or choose **Download** next to **Federation Metadata XML** to download the metadata file.

You provide this metadata URL or file to Amazon Cognito in Step 6.

### Step 5: Assign users and groups
<a name="entra-saml-assign-users"></a>

1. In the enterprise application, choose **Users and groups**.

1. Choose **Add user/group**, select the users or groups who should access SDMA, and then choose **Assign**.

### Step 6: Create the SAML identity provider in Amazon Cognito
<a name="entra-saml-cognito-idp"></a>

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), choose **User pools**, and then select your user pool.

1. Choose **Sign-in experience** > **Federated identity provider sign-in**.

1. Choose **Add identity provider**, and then choose **SAML**.

1. Configure the following:
   +  **Provider name** – Enter a name, for example `EntraID`. This name appears on the sign-in button.
   +  **Identifiers (optional)** – Leave blank.
   +  **Add sign-out flow** – Select this option to enable single logout.
   +  **Metadata document source** – Choose **Metadata document URL** and paste the **App Federation Metadata Url** from Step 4, or choose **Upload metadata document** and upload the XML file you downloaded.

1. Choose **Add identity provider**.

1. After the identity provider is created, locate the **Attribute mapping** section and choose **Edit**. Map the SAML attributes to user pool attributes:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/configure-entra-id.html)

1. Choose **Save changes**.

Then enable the identity provider ([Enable the identity provider for the app client](external-identity-provider.md#idp-enable-app-client)) and verify the integration ([Verify the integration](external-identity-provider.md#idp-test)).

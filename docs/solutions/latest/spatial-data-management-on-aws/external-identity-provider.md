---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/external-identity-provider.html
---

# Configure any external identity provider
<a name="external-identity-provider"></a>

This page describes the protocol-level configuration that applies to any OpenID Connect (OIDC) or SAML 2.0 identity provider, along with the steps to enable, verify, and troubleshoot federation. For a detailed walkthrough of a specific provider, see [Configure Microsoft Entra ID](configure-entra-id.md).

Before you begin, complete the prerequisites and gather your Amazon Cognito values described in [Single sign-on (SSO)](sso.md). The procedures below use the placeholders defined in [Placeholders used in these procedures](sso.md#sso-placeholders).

## Configure OIDC federation
<a name="generic-oidc"></a>

At a high level, configuring OIDC federation requires you to:

1. Register an application (relying party) in your identity provider, using the OIDC redirect endpoint from [Gather your Amazon Cognito values](sso.md#sso-gather-cognito-values) as the redirect (callback) URI.

1. Obtain a client ID, a client secret, and the issuer URL from your identity provider.

1. Register your identity provider as an OIDC identity provider in the Amazon Cognito user pool, and map identity provider claims to user pool attributes.

1. Enable the identity provider for the portal app client (see [Enable the identity provider for the app client](#idp-enable-app-client)).

To create the OIDC identity provider in Amazon Cognito:

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), choose **User pools**, and then select your user pool.

1. Choose **Sign-in experience** > **Federated identity provider sign-in**.

1. Choose **Add identity provider**, and then choose **OpenID Connect (OIDC)**.

1. Configure the following:
   +  **Provider name** – A name for the provider. This name appears on the sign-in button.
   +  **Client ID** – The client ID issued by your identity provider.
   +  **Client secret** – The client secret issued by your identity provider.
   +  **Authorized scopes** – Enter `openid email profile` (space-separated), or the scopes your provider requires.
   +  **Issuer URL** – The OIDC issuer URL for your identity provider. Amazon Cognito discovers the authorization, token, and JSON Web Key Set (JWKS) endpoints from the issuer’s `/.well-known/openid-configuration` document.

1. Under **Map attributes between your OpenID Connect provider and your user pool**, map the provider claims to user pool attributes. At a minimum, map `email`. Typical mappings are:

<table>
<thead>
  <tr><th>User pool attribute</th><th>OIDC claim</th></tr>
</thead>
<tbody>
  <tr><td> <code>email</code> </td><td> <code>email</code> </td></tr>
  <tr><td> <code>given_name</code> </td><td> <code>given_name</code> </td></tr>
  <tr><td> <code>family_name</code> </td><td> <code>family_name</code> </td></tr>
  <tr><td> <code>username</code> </td><td> <code>sub</code> </td></tr>
</tbody>
</table>

1. Choose **Add identity provider**.

Then enable the identity provider as described in [Enable the identity provider for the app client](#idp-enable-app-client).

## Configure SAML federation
<a name="generic-saml"></a>

At a high level, configuring SAML 2.0 federation requires you to:

1. Create a SAML application in your identity provider, and provide it with the Amazon Cognito service provider (SP) values from [Gather your Amazon Cognito values](sso.md#sso-gather-cognito-values) (the ACS URL and the SP entity ID / audience URI).

1. Configure the SAML attributes (claims) that the identity provider sends, and (optionally) a groups claim.

1. Obtain the identity provider metadata (a metadata URL or an XML file).

1. Register your identity provider as a SAML identity provider in the Amazon Cognito user pool, and map SAML attributes to user pool attributes.

1. Enable the identity provider for the portal app client (see [Enable the identity provider for the app client](#idp-enable-app-client)).

To create the SAML identity provider in Amazon Cognito:

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), choose **User pools**, and then select your user pool.

1. Choose **Sign-in experience** > **Federated identity provider sign-in**.

1. Choose **Add identity provider**, and then choose **SAML**.

1. Configure the following:
   +  **Provider name** – A name for the provider. This name appears on the sign-in button.
   +  **Identifiers (optional)** – Leave blank unless your provider requires an identifier.
   +  **Add sign-out flow** – Select this option to enable single logout, if your provider supports it.
   +  **Metadata document source** – Choose **Metadata document URL** and paste your provider’s federation metadata URL, or choose **Upload metadata document** and upload the metadata XML file.

1. Choose **Add identity provider**.

1. Locate the **Attribute mapping** section, choose **Edit**, and map the SAML attributes sent by your provider to user pool attributes. At a minimum, map `email`.

1. Choose **Save changes**.

Then enable the identity provider as described in [Enable the identity provider for the app client](#idp-enable-app-client).

## Enable the identity provider for the app client
<a name="idp-enable-app-client"></a>

After you create the OIDC or SAML identity provider, enable it for the portal app client so that it appears on the sign-in page.

1. In the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), select your user pool.

1. Choose **App clients**, and then select the portal app client (the name follows the pattern `spatial-data-portal-client`).

1. Choose the **Login pages** tab, and then choose **Edit**.

1. Under **Identity providers**, select and enable the identity provider you created.
**Note**
To require federation-only sign-in, clear **Cognito user pool** so that users can sign in only through the external identity provider. Leave it selected if you want to continue to allow direct Cognito user pool sign-in.

1. Choose **Save changes**.

## Verify the integration
<a name="idp-test"></a>

1. In your identity provider, make sure a test user is assigned to the SDMA application.

1. Open the Spatial Data Portal sign-in page, or the Cognito hosted UI.

1. Confirm that the **Sign in with <Provider name>** button appears.

1. Choose the button and complete authentication with your corporate credentials.

1. Confirm that you are redirected back to SDMA and signed in, and that user attributes (email, given name, family name) are populated.

**Note**
Newly federated users start with no permissions in SDMA. An administrator in the `SpatialDataManagementAdministrators` group must assign a permission level before they can work with resources. For more information, see [Access Management](access-control.md).

## Troubleshooting
<a name="idp-troubleshooting"></a>

 **The sign-in button does not appear**
+ Confirm that the identity provider is enabled for the portal app client. See [Enable the identity provider for the app client](#idp-enable-app-client).
+ Confirm that you saved the **Login pages** configuration for the correct app client.

 ** `redirect_mismatch` or `redirect_uri` error after sign-in**
+ Verify that the redirect URI in your identity provider exactly matches your Cognito domain, including `/oauth2/idpresponse` (OIDC) or `/saml2/idpresponse` (SAML).
+ Confirm the Cognito domain value under **Branding** > **Domain**.

 **User authenticates but is not signed in to SDMA**
+ Verify the attribute mappings between the identity provider and the user pool. At a minimum, `email` must be mapped.
+ For SAML, confirm that the SAML attribute claim names match the values in the **Attribute mapping** section.

 **Group permissions do not take effect**
+ Confirm that the groups claim is configured in your identity provider.
+ Confirm that the group name in your identity provider matches the Cognito group used for access assignment. For more information, see [Access Management](access-control.md).
+ Recent group changes can take a few minutes to propagate. Sign out and sign back in to refresh tokens.

---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/sso.html
---

# Single sign-on (SSO)
<a name="sso"></a>

Spatial Data Management on AWS (SDMA) authenticates users with an Amazon Cognito user pool that the solution creates at deployment time. Instead of managing users and groups directly in Amazon Cognito, you can federate the user pool with your organization’s external identity provider (IdP). With federation, you can enable single sign-on (SSO): your users sign in to the Spatial Data Portal with their existing corporate credentials, and user and group management stays centralized in your identity system.

Amazon Cognito supports two federation protocols:
+  **OpenID Connect (OIDC)** – An identity layer built on OAuth 2.0. Choose OIDC when your identity provider exposes an OIDC-compliant endpoint.
+  **Security Assertion Markup Language (SAML) 2.0** – An XML-based standard for exchanging authentication and authorization data. Choose SAML when your identity provider is configured as a SAML 2.0 IdP.

This section is organized as follows:
+  [Configure any external identity provider](external-identity-provider.md) – Protocol-level instructions that apply to any OIDC or SAML 2.0 identity provider, plus the steps to enable, verify, and troubleshoot federation.
+  [Configure Microsoft Entra ID](configure-entra-id.md) – Detailed OIDC and SAML walkthroughs for Microsoft Entra ID (formerly Azure Active Directory), the most common use case.

The prerequisites, placeholders, and Amazon Cognito values on this page apply to both.

**Note**
Groups that you pass from your identity provider can be mapped to Amazon Cognito groups and used to assign permissions in SDMA. After you configure federation, see [Access Management](access-control.md) for how to grant access to federated users and groups. To designate an initial administrator, add a federated user or group to the `SpatialDataManagementAdministrators` Cognito group. For more information, see [Core Concepts](core-concepts.md).

## Prerequisites
<a name="sso-prerequisites"></a>

Before you begin, make sure that you have:
+ A deployed SDMA stack with an Amazon Cognito user pool. For more information, see [Deploy the solution](deploy-the-solution.md).
+ Administrative access to the AWS account where SDMA is deployed, with permission to configure Amazon Cognito.
+ Administrative access to your identity provider.
+ A Cognito hosted UI domain configured for the user pool. You can find or configure this value in the Amazon Cognito console under your user pool, in **Branding** > **Domain**.

## Placeholders used in these procedures
<a name="sso-placeholders"></a>

The procedures in this section use the following placeholders. Replace them with the values from your deployment.

| Placeholder | Description |
| --- | --- |
|  `<REGION>`  | The AWS Region where the solution is deployed (for example, `us-east-1`). |
|  `<USER_POOL_ID>`  | The Amazon Cognito user pool ID. The user pool name follows the pattern `spatial-data-management-user-pool`. |
|  `<COGNITO_DOMAIN>`  | Your Cognito hosted UI domain prefix. The full domain is `https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com`. Find it under **Branding** > **Domain** in the Amazon Cognito console. |
|  `<APP_CLIENT>`  | The Cognito app client used by the portal. The name follows the pattern `spatial-data-portal-client`. |
|  `<TENANT_ID>`  | (Microsoft Entra ID only) Your **Directory (tenant) ID** (a GUID). Find it on the **Overview** page of your Entra ID app registration. |

## Gather your Amazon Cognito values
<a name="sso-gather-cognito-values"></a>

You need the following values from the Amazon Cognito console for both OIDC and SAML configuration. Record them before you start.

1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/) in the account where SDMA is deployed.

1. Choose **User pools**, and then select the user pool created by the solution (the name follows the pattern `spatial-data-management-user-pool`).

1. Note the **User pool ID** (`<USER_POOL_ID>`).

1. In the left navigation, choose **Branding** > **Domain**, and note your hosted UI domain (`<COGNITO_DOMAIN>`).

The following redirect endpoints are derived from your domain. You provide these values to your identity provider.

| Protocol | Redirect endpoint |
| --- | --- |
| OIDC |  `https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com/oauth2/idpresponse`  |
| SAML 2.0 |  `https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com/saml2/idpresponse`  |

For SAML, Amazon Cognito also acts as the service provider (SP) with the following values:

| SAML service provider value | Value for your user pool |
| --- | --- |
| Assertion consumer service (ACS) URL / Reply URL |  `https://<COGNITO_DOMAIN>.auth.<REGION>.amazoncognito.com/saml2/idpresponse`  |
| Service provider entity ID / Audience URI / Identifier |  `urn:amazon:cognito:sp:<USER_POOL_ID>`  |

## Session and token lifetimes
<a name="sso-session-lifetimes"></a>

Federation changes where users authenticate, not how long their SDMA session lasts. After a federated user signs in, the Amazon Cognito tokens issued to the portal app client govern the session, not the session lifetime you configure in your identity provider. The solution configures the portal app client with the following token lifetimes:

| Token | Validity |
| --- | --- |
| ID token | 15 minutes |
| Access token | 15 minutes |
| Refresh token | 7 days |

The portal uses the refresh token to obtain new ID and access tokens without prompting the user, so users stay signed in through up to seven days of continued use. After the refresh token expires, the user is sent back to your identity provider to authenticate again. If your identity provider still has an active SSO session for that user, this re-authentication can complete without a prompt.

Because group membership is carried in the ID token, a change to a user’s groups in your identity provider takes effect in SDMA only when Amazon Cognito issues new tokens.

You can change these lifetimes on the portal app client (`<APP_CLIENT>`) in the Amazon Cognito console. For more information about token lifetimes, see [Understanding user pool JSON web tokens (JWTs)](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html) in the *Amazon Cognito Developer Guide*.

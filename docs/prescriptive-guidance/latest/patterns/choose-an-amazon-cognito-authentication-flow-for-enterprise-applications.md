---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/choose-an-amazon-cognito-authentication-flow-for-enterprise-applications.html
---

# Choose an Amazon Cognito authentication flow for enterprise applications
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications"></a>

*Michael Daehnert and Fabian Jahnke, Amazon Web Services*

## Summary
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-summary"></a>

[Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile applications. It offers beneficial features for authentication of federated identities. To get it up and running, technical architects need to decide how they want to use those features.

Amazon Cognito supports multiple flows for authentication requests. These flows define how your users can verify their identity. The decision about which authentication flow to use depends on specific requirements of your application and can become complex. This pattern helps you decide which authentication flow is the best fit for your enterprise application. It assumes that you already have a basic knowledge of Amazon Cognito, OpenID Connect (OIDC), and federation, and it guides you through details about different federated authentication flows.

This solution is intended for technical decision makers. It helps you understand the different authentication flows and map them to your application requirements. Technical leads should gather the required insights to start the Amazon Cognito integrations. Because enterprise organizations mainly focus on SAML federation, this pattern includes  descriptions for [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) with SAML federation.

## Prerequisites and limitations
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Identity and Access Management (IAM) roles and permissions with full access to Amazon Cognito
+ (Optional) Access to your identity provider (IdP), such as Microsoft Entra ID, Active Directory Federation Service (AD FS), or Okta
+ A high level of expertise for your application
+ Basic knowledge of Amazon Cognito, OpenID Connect (OIDC), and federation

**Limitations **
+ This pattern focuses on Amazon Cognito user pools and identity providers. For information about Amazon Cognito identity pools, see the [Additional information](#choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-additional) section.

## Architecture
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-architecture"></a>

Use the following table to help you choose an authentication flow. More information about each flow is provided in this section.

|
|
| Do you need machine-to-machine authentication? | Is your app a web-based application where the frontend is rendered on the server? | Is your app a single-page application (SPA) or mobile-based frontend application? | Does your application require refresh tokens for a "keep me signed in" feature? | Does the frontend offer a browser-based redirect mechanism? | Recommended Amazon Cognito flow |
| --- |--- |--- |--- |--- |--- |
| Yes | No | No | No | No | Client Credentials flow |
| No | Yes | No | Yes | Yes | Authorization Code flow |
| No | No | Yes | Yes | Yes | Authorization Code flow with Proof Key for Code Exchange (PKCE) |
| No | No | No | No | No | Resource Owner Password flow\* |

\* Resource Owner Password flow should be used only if absolutely necessary. For more information, see the *Resource Owner Password flow* section in this pattern.

**Client Credentials flow **

The Client Credentials flow is the shortest of the Amazon Cognito flows. It should be used if systems or services communicate with each other without any user interaction. The requesting system uses the client ID and the client secret to retrieve an access token. Because both systems work without user interaction, no additional consent step is required.

![Client Credentials flow for Amazon Cognito](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7b5e567c-66a4-4386-a1f6-616ed77a6211/images/1138745d-69fa-4ecc-a9ec-c0b2a68ce7d2.png)

The diagram illustrates the following:

1. Application 1 sends an authentication request with the client ID and client secret to the Amazon Cognito endpoint, and it retrieves an access token.

1. Application 1 uses this access token for every subsequent call to Application 2.

1. Application 2 validates the access token with Amazon Cognito.

This flow should be used:
+ For communications between applications with no user interaction

This flow should not be used:
+ For any communication in which user interactions are possible

**Authorization Code flow**

The Authorization Code flow is for classic web-based authentication. In this flow, the backend handles all of the token exchange and storage. The browser-based client does not see the actual tokens. This solution is used for applications written in frameworks such as .NET Core, Jakarta Faces, or Jakarta Server Pages (JSP).

The Authorization Code flow is a redirection-based flow. The client must be able to interact with the web browser or a similar client. The client is redirected to an authentication server and authenticates against this server. If the client authenticates successfully, it is redirected back to the server.

![Authorization Code flow for Amazon Cognito](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7b5e567c-66a4-4386-a1f6-616ed77a6211/images/1008296c-d5b8-449d-99d4-f0b2b7cf5d80.png)

The diagram illustrates the following:

1. The client sends a request to the web server.

1. The web server redirects the client to Amazon Cognito by using an HTTP 302 status code. The client automatically follows this redirect to the configured IdP login.

1. The IdP checks for an existing browser session on the IdP side. If none exists, the user receives a prompt to authenticate by providing their username and password. The IdP responds with a SAML token to Amazon Cognito.

1. Amazon Cognito returns success with a JSON web token (JWT), specifically a code token. The web server calls /oauth2/token to exchange the code token for an access token. The web server sends the client ID and client secret to Amazon Cognito for validation.

1. The access token is used for every subsequent call to other applications.

1. Other applications validate the access token with Amazon Cognito.

This flow should be used:
+ If the user is able to interact with the web browser or client. The application code is run and rendered on the server to make sure that no secrets are exposed to the browser.

This flow should not be used:
+ For single-page applications (SPAs) or mobile apps because they're rendered on the client and shouldn't use client secrets.

**Authorization Code flow with PKCE**

Authorization Code flow with Proof Key for Code Exchange (PKCE) should be used for single-page applications and mobile applications. It is the successor of the Implicit flow and is more secure because it uses PKCE. PKCE is an extension to the OAuth 2.0 authorization code grant for public clients. PKCE guards against the redemption of intercepted authorization codes.

![Authorization Code flow with PKCE for Amazon Cognito](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7b5e567c-66a4-4386-a1f6-616ed77a6211/images/1609da4f-decd-4d43-afe0-31237238df6d.png)

The diagram illustrates the following:

1. The application creates a code verifier and code challenge. These are well defined, unique values that are sent to Amazon Cognito for future reference.

1. The application calls the /oauth2/authorization endpoint of Amazon Cognito. It automatically redirects the user to the configured IdP login.

1. The IdP checks for an existing session. If none exists, the user receives a prompt to authenticate by providing their username and password. The IdP responds with a SAML token to Amazon Cognito.

1. After Amazon Cognito returns success with a code token, the web server calls /oauth2/token to exchange the code token for an access token.

1. The access token is used for every subsequent call to other applications.

1. The other applications validate the access token with Amazon Cognito.

This flow should be used:
+ For SPAs or mobile applications

This flow should not be used:
+ If the application backend handles authentication

**Resource Owner Password flow**

The Resource Owner Password flow is intended for applications with no redirect capabilities. It is built by creating a login form in your own application. The login is checked on Amazon Cognito through a CLI or SDK call instead of relying on redirect flows. Federation is not possible in this authentication flow because federation requires browser-based redirects.

![Resource Owner Password flow for Amazon Cognito](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7b5e567c-66a4-4386-a1f6-616ed77a6211/images/d74bc596-08a3-40f4-a6a7-07f6610fe6b1.png)

The diagram illustrates the following:

1. The user enters their credentials on a login form provided by the application.

1. The AWS Command Line Interface (AWS CLI) makes an [admin-initiated-auth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html) call to Amazon Cognito.
**Note**
Alternatively, you can use AWS SDKs instead of the AWS CLI.

1. Amazon Cognito returns an access token.

1. The access token is used for every subsequent call to other applications.

1. The other applications validate the access token with Amazon Cognito.

This flow should be used:
+ When migrating existing clients that use direct authentication logic (such as basic access authentication or digest access authentication) to OAuth by converting the stored credentials to an access token

This flow should not be used:
+ If you want to use federated identities
+ If your application supports redirects

## Tools
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-tools"></a>

**AWS services**
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.

**Other tools**
+ [JSON web token (JWT) debugger](https://jwt.io/) is a web-based JWT validation tool.

## Epics
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-epics"></a>

### Assess your application
<a name="assess-your-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define authentication requirements. | Assess your application according to your specific authentication requirements. | App developer, App architect |
| Align requirements with authentication flows. | In the [Architecture](#choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-architecture) section, use the decision table and explanations of each flow to choose your Amazon Cognito authentication flow. | App developer, General AWS, App architect |

### Set up the Amazon Cognito user pool
<a name="set-up-the-amazon-cognito-user-pool"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a user pool. | 1. Sign in to the AWS Management Console, and then open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).<br />2. Create a new Cognito user pool. For instructions, see [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).<br />3. Update the user pool settings and attributes as needed. For example, set a [password policy](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html) for the user pool. Do not create app clients yet. | General AWS |
| (Optional) Configure an identity provider. | 1. Create a SAML identity provider in the Amazon Cognito user pool. For instructions, see [Adding and managing SAML identity providers in a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp.html).<br />2. Configure your third-party SAML identity provider to work with federation for Amazon Cognito user pools. For more information, see [Configuring your third-party SAML identity provider](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-integrating-3rd-party-saml-providers.html). If you're using AD FS, see [Building AD FS Federation for your Web App using Amazon Cognito User Pools](https://aws.amazon.com/blogs/mobile/building-adfs-federation-for-your-web-app-using-amazon-cognito-user-pools/) (AWS blog post). | General AWS, Federation administrator |
| Create an app client. | 1. Create an app client for the user pool. For instructions, see [Creating an app client](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html#cognito-user-pools-app-idp-settings-console-create). Note the following:Change settings as needed, such as token expirations.If your authentication flow doesn't require a client secret, then clear the **Generate client secret** checkbox.<br />2. Choose **App client settings** to change its integration to a user pool login (username and password) or federated login through a SAML-based IdP.<br />3. Enable your IdP by defining URLs and defining OAuth flows or scopes as needed. | General AWS |

### Integrate the application with Amazon Cognito
<a name="integrate-the-application-with-amazon-cognito"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Exchange Amazon Cognito integration details. | Depending on your authentication flow, share Amazon Cognito information with the application, such as the user pool ID and app client ID. | App developer, General AWS |
| Implement Amazon Cognito authentication. | This depends on your chosen authentication flow, your programming language, and the frameworks you're using. For some links to get started, see the [Related resources](#choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-resources) section. | App developer |

## Related resources
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-resources"></a>

**AWS documentation**
+ [User pool authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html)
+ [Verifying a JSON web token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html)
+ [Access AWS services from an ASP.NET Core app using Amazon Cognito identity pools](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-an-asp-net-core-app-using-amazon-cognito-identity-pools.html?did=pg_card&trk=pg_card)
+ Frameworks and SDKs:
  + [Amazon Amplify authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/js)
  + [Amazon Cognito Identity Provider examples](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cognito-identity-provider_code_examples.html) (AWS SDK for Java 2.x documentation)
  + [Authenticating users with Amazon Cognito](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/cognito-apis-intro.html) (AWS SDK for .NET documentation)

**AWS blog posts**
+ [Authorization@Edge using cookies: Protect your Amazon CloudFront content from being downloaded by unauthenticated users](https://aws.amazon.com/blogs/networking-and-content-delivery/authorizationedge-using-cookies-protect-your-amazon-cloudfront-content-from-being-downloaded-by-unauthenticated-users/)
+ [Building AD FS Federation for your Web App using Amazon Cognito User Pools](https://aws.amazon.com/blogs/mobile/building-adfs-federation-for-your-web-app-using-amazon-cognito-user-pools/)

**Implementation partners**
+ [AWS Partners for authentication solutions](https://partners.amazonaws.com/search/partners?keyword=authentication)

## Additional information
<a name="choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-additional"></a>

**FAQ**

*Why is the Implicit flow deprecated?*

Since the release of the [OAuth 2.1 framework](https://oauth.net/2.1/), the Implicit flow is marked as deprecated for security reasons. As an alternative, please use the Authorization Code flow with PKCE described in the [Architecture](#choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-architecture) section.

*What if Amazon Cognito doesn’t offer some functionality I require?*

AWS Partners offer different integrations for authentication and authorization solutions. For more information, see [AWS Partners for authentication solutions](https://partners.amazonaws.com/search/partners?keyword=authentication).

*What about Amazon Cognito identity pool flows?*

Amazon Cognito user pools and federated identities are for authentication. Amazon Cognito identity pools are used for authorization of AWS resources access by requesting temporary AWS credentials. The ID token and access token exchange for identity pools isn't discussed in this pattern. For more information, see [What's the difference between Amazon Cognito user pools and identity pools](https://aws.amazon.com/premiumsupport/knowledge-center/cognito-user-pools-identity-pools/) and [Common Amazon Cognito scenarios](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-scenarios.html).

**Next steps**

This pattern provides an overview of Amazon Cognito authentication flows. As a next step, the detailed implementation for the application’s programming language needs to be chosen. Multiple languages offer SDKs and frameworks, which you can use with Amazon Cognito. For helpful references, see the [Related resources](#choose-an-amazon-cognito-authentication-flow-for-enterprise-applications-resources) section.

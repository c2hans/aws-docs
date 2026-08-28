---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/federated-authentication.html
---

# Single sign-on — SAML 2.0-based federated authentication — in Client VPN
<a name="federated-authentication"></a>

AWS Client VPN supports identity federation with Security Assertion Markup Language 2.0 (SAML 2.0) for Client VPN endpoints. You can use identity providers (IdPs) that support SAML 2.0 to create centralized user identities. You can then configure a Client VPN endpoint to use SAML-based federated authentication, and associate it with the IdP. Users then connect to the Client VPN endpoint using their centralized credentials.

**Topics**
+ [Enable SAML](client-auth-enable-saml.md)
+ [Authentication workflow](#federated-authentication-workflow)
+ [Requirements and considerations for SAML-based federated authentication](#saml-requirements)
+ [SAML-based IdP configuration resources](#saml-config-resources)

## Authentication workflow
<a name="federated-authentication-workflow"></a>

The following diagram provides an overview of the authentication workflow for a Client VPN endpoint that uses SAML-based federated authentication. When you create and configure the Client VPN endpoint, you specify the IAM SAML identity provider.

![Authentication workflow](http://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/federated-auth-workflow.png)

1. The user opens the AWS provided client on their device and initiates a connection to the Client VPN endpoint.

1. The Client VPN endpoint sends an IdP URL and authentication request back to the client, based on the information that was provided in the IAM SAML identity provider.

1. The AWS provided client opens a new browser window on the user's device. The browser makes a request to the IdP and displays a login page.

1. The user enters their credentials on the login page, and the IdP sends a signed SAML assertion back to the client.

1. The AWS provided client sends the SAML assertion to the Client VPN endpoint.

1. The Client VPN endpoint validates the assertion and either allows or denies access to the user.

## Requirements and considerations for SAML-based federated authentication
<a name="saml-requirements"></a>

The following are the requirements and considerations for SAML-based federated authentication.
+ For quotas and rules for configuring users and groups in a SAML-based IdP, see [Users and groups quotas](limits.md#quotas-users-groups).
+ The SAML assertion and response must be signed.
+ AWS Client VPN only supports "AudienceRestriction" and "NotBefore and NotOnOrAfter" conditions in SAML assertions.
+ The maximum supported size for SAML responses is 128 KB.
+ AWS Client VPN does not provide signed authentication requests.
+ SAML single logout is not supported. Users can log out by disconnecting from the AWS provided client, or you can [terminate the connections](cvpn-working-connections-disassociate.md).
+ A Client VPN endpoint supports a single IdP only.
+ Multi-factor authentication (MFA) is supported when it's enabled in your IdP.
+ Users must use the AWS provided client to connect to the Client VPN endpoint. They must use version 1.2.0 or later. For more information, see [Connect using the AWS provided client](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/connect-aws-client-vpn-connect.html).
+ The following browsers are supported for IdP authentication: Apple Safari, Google Chrome, Microsoft Edge, and Mozilla Firefox.
+ The AWS provided client reserves TCP port 35001 on users' devices for the SAML response.
+ If the metadata document for the IAM SAML identity provider is updated with an incorrect or malicious URL, this can cause authentication issues for users, or result in phishing attacks. Therefore, we recommend that you use AWS CloudTrail to monitor updates that are made to the IAM SAML identity provider. For more information, see [Logging IAM and AWS STS calls with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html) in the *IAM User Guide*.
+ AWS Client VPN sends an AuthN request to the IdP via an HTTP Redirect binding. Therefore, the IdP should support HTTP Redirect binding and it should be present in the IdP's metadata document.
+ For the SAML assertion, you must use an email address format for the `NameID` attribute.
+ The maximum username (`NameID`) length is 1024 bytes. Connections with longer usernames will be rejected.
+ When certificates being used with the Client VPN service are updated, whether through ACM auto-rotation, manually importing a new certificate, or metadata updates to IAM Identity Center the Client VPN service will automatically update the Client VPN endpoint with the newer certificate. This is an automated process that can take up to 5 hours.

## SAML-based IdP configuration resources
<a name="saml-config-resources"></a>

The following table lists the SAML-based IdPs that we have tested for use with AWS Client VPN, and resources that can help you configure the IdP.

| IdP | Resource |
| --- | --- |
| Okta | [Authenticate AWS Client VPN users with SAML](https://aws.amazon.com/blogs/networking-and-content-delivery/authenticate-aws-client-vpn-users-with-saml/) |
| Microsoft Entra ID (formerly Azure Active Directory) | For more information, see [Tutorial: Microsoft Entra single sign-on (SSO) integration with AWS ClientVPN](https://learn.microsoft.com/en-gb/entra/identity/saas-apps/aws-clientvpn-tutorial) on the Microsoft documentation website. |
| JumpCloud | [Integrate with AWS Client VPN](https://jumpcloud.com/support/integrate-with-aws-client-vpn) |
| AWS IAM Identity Center | [Using IAM Identity Center with AWS Client VPN for authentication and authorization](https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-sso-with-aws-client-vpn-for-authentication-and-authorization/)  |

### Service provider information for creating an app
<a name="saml-config-service-provider-info"></a>

To create a SAML-based app using an IdP that is not listed in the preceding table, use the following information to configure the AWS Client VPN service provider information.
+ Assertion Consumer Service (ACS) URL: `http://127.0.0.1:35001`
+ Audience URI: `urn:amazon:webservices:clientvpn`

At least one attribute must be included in the SAML response from the IdP. The following are example attributes.

| Attribute | Description |
| --- | --- |
| FirstName | The first name of the user. |
| LastName | The last name of the user. |
| memberOf | The group or groups that the user belongs to. |

**Note**
The `memberOf` attribute is required for using Active Directory or SAML IdP group-based authorization rules. It is also case-sensitive, and must be configured exactly as specified. See [Network-based authorization](client-authorization.md#auth-rules) and [AWS Client VPN authorization rules](cvpn-working-rules.md) for more information.

### Support for the self-service portal
<a name="saml-self-service-support"></a>

If you enable the self-service portal for your Client VPN endpoint, users log into the portal using their SAML-based IdP credentials.

If your IdP supports multiple Assertion Consumer Service (ACS) URLs, add the following ACS URL to your app.

```
https://self-service.clientvpn.amazonaws.com/api/auth/sso/saml
```

If you are using the Client VPN endpoint in a GovCloud region, use the following ACS URL instead. If you use the same IDP app to authenticate for both standard and GovCloud regions, you can add both URLs.

```
https://gov.self-service.clientvpn.amazonaws.com/api/auth/sso/saml
```

If your IdP does not support multiple ACS URLs, do the following:

1. Create an additional SAML-based app in your IdP and specify the following ACS URL.

   ```
   https://self-service.clientvpn.amazonaws.com/api/auth/sso/saml
   ```

1. Generate and download a federation metadata document.

1. Create an IAM SAML identity provider in the same AWS account as the Client VPN endpoint. For more information, see [Creating IAM SAML Identity Providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the *IAM User Guide*.
**Note**
You create this IAM SAML identity provider in addition to the one you [create for the main app](#federated-authentication).

1. [Create the Client VPN endpoint](cvpn-working-endpoint-create.md), and specify both of the IAM SAML identity providers that you created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

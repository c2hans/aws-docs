---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-endpoint-best-practices.html
---

# Global endpoint best practices
<a name="global-endpoint-best-practices"></a>

This section provides best practices for using services with global endpoints in your recovery operations.

This section covers the following topics:
+ [AWS Security Token Service](#aws-security-token-service)
+ [AWS Management Console](#aws-management-console)
+ [AWS Sign-In](#aws-sign-in)
+ [Third-party identity providers](#third-party-identity-providers)

## AWS Security Token Service
<a name="aws-security-token-service"></a>

 AWS STS is a data plane-only service. You can use it to request temporary credentials for IAM roles or for users you authenticate (federated users). AWS STS provides both a global (`https://sts.amazonaws.com`) and regional endpoints `https://sts.{{region}}.amazonaws.com`. The regional endpoints are [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in Regions that are also enabled by default. When you enable an opt-in Region, the STS endpoint for that Region is also enabled automatically. All STS actions, except `AssumeRoot`, don’t depend on the IAM control plane, and don’t have out-of-Region AWS dependencies.

 When planning for dependencies on AWS STS, AWS recommends using the regional endpoints. If your preferred regional endpoint is unavailable, you should failover to use STS in a different Region to retrieve credentials for use with the AWS CLI or AWS SDK using `AssumeRole`, `GetFederationToken`, or `GetSessionToken` with IAM user credentials or `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity` using federation. You shouldn’t rely on `AssumeRoot` in your recovery path because it depends on the IAM control plane.

 In April 2025, AWS [made changes to the AWS STS global endpoint](https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint/) in Regions enabled by default to enhance its resilience and performance. AWS STS requests to the global endpoint are automatically served in the same AWS Region as your applications when called from a VPC in that Region using the [Route 53 Resolver](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#AmazonDNS). The current versions of the AWS SDK and AWS CLI released after July 31, 2025, default to using the regional endpoints. Both of these enhancements help make sure that STS provides regional isolation transparently to your applications. If you’re calling STS from outside an AWS VPC, or you aren’t using the VPC DNS resolver, you should configure your AWS Software Development Kit (AWS SDK) and [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli) to use a regional endpoint.

 AWS STS also provides outbound identity federation, so you can exchange your IAM credentials for a JSON Web Token (JWT). Third parties must validate these tokens when you use them. We provide an endpoint like `https://abc12345-def4-5678-90ab-cdef12345678.tokens.sts.global.api.aws` as the issuer in the JWT. These endpoints are hosted by CloudFront with origin failover configured and are available globally through the PoP network.

 When you configure IAM role trust policies for use with STS, the `saml:aud` context key comes from the SAML recipient, which is the regional AWS Sign-In Service endpoint in the Region where you called `AssumeRoleWithSAML`. To failover to another AWS STS endpoint to successfully retrieve credentials, either don’t use `saml:aud` as a condition key in your IAM role trust policy, use `StringEquals` with multiple endpoints listed, or use `StringLike` with a wildcard for the Region value, like `https://*signin.amazonaws.com/`.

## AWS Management Console
<a name="aws-management-console"></a>

 The AWS Management Console provides a global endpoint, [https://console.aws.amazon.com](https://console.aws.amazon.com), and regional endpoints in the format `https://{{region}}.console.aws.amazon.com`, for accessing the console. The global endpoint DNS record uses latency-based routing to three separate Regions, `us-east-2`, `ap-southeast-2`, and `eu-north-1`. Those endpoints are hosted using AWS Global Accelerator, use Route 53 health checks for automated fail away, and have a manual option that AWS can use to disable the endpoint. After your request is processed by one of those three global endpoint hosts, you will be redirected to your default Region, which defaults to using your last accessed Region.

 When planning for dependencies on the console for recovery, you can choose to use the global endpoint and the redundancy provided by AWS. Alternatively, you can choose to use Region-specific endpoints to directly control your dependencies and recovery process.

 If you have existing credentials, the regional console URL will take you directly to the AWS console. If you don’t have an authenticated session, this URL will automatically redirect you to the regional sign-in service, https://{{region}}.signin.aws.amazon.com/, where you can sign in with an IAM user. Accessing the console through a regional console URL helps make sure your sign-in process only takes dependencies on Regions you specify.

 If the console itself is impacted in your primary Region and you need to fail away from that Region, you should have operational runbooks that can use the AWS SDK or AWS CLI to perform the failover without dependency on the console.

## AWS Sign-In
<a name="aws-sign-in"></a>

 [AWS Sign-In](https://docs.aws.amazon.com/signin/latest/userguide/what-is-sign-in.html) provides a global endpoint, [https://signin.aws.amazon.com](https://signin.aws.amazon.com), hosted in `us-east-1`, in addition to regional endpoints, `https://{{region}}.signin.aws.amazon.com/`. The sign-in service supports different sign-in operations, such as [/saml](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html), `/console`, [/federation](https://docs.aws.amazon.com/signin/latest/userguide/federated-identity-overview.html), and `/oauth`, which are primarily used for human access to the AWS Management Console. When planning for dependencies on the AWS Sign-In service, you should consider the following guidance.
+  AWS root user sign-in is now served across `us-east-1`, `us-east-2`, and `us-west-2`, with sign-in traffic distributed across all three Regions. This change reduces reliance on `us-east-1` and improves resilience during service disruptions. However, if you need to deterministically sign in to a specific Region, use IAM roles or users instead.
+  The `/console` sign-in path, ` https://{{region}}.signin.aws.amazon.com/`, for IAM user sign-in redirects to the global AWS Management Console, [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home), during the sign in workflow. The global console endpoint is hosted redundantly in three Regions. Avoid using the `/console` sign-in path if you want to strictly control which Regions you depend on during the sign-in workflow.
+ The `/oauth` operation shouldn’t be used directly for sign-in. To sign in with an IAM user, use the `https://{{region}}.console.aws.amazon.com` endpoint to initiate the sign-in workflow.
+ The `/saml` operation relies on AWS STS in the same Region but doesn’t have out of Region dependencies.
+ The `/federation` operation doesn’t have out of Region dependencies.

If the `/saml` or the `/federation` operations are impacted in your desired Region for AWS Management Console access, you can follow two options.
+ Use the AWS Sign-In service in a different Region to gain access to the AWS Management Console. If required, you can switch Regions in the console after signing in. Follow the guidance in the Third-party identity providers section for information on updating your sign-in endpoints.
+ Use the break-glass procedure described in the [AWS IAM Identity Center](globally-scoped-operations-best-practices.md#aws-iam-identity-center) section to use IAM user credentials to gain access to emergency operational roles.

 When you configure your IAM role trust policies for use with console sign-in, note that the `saml:aud` context key comes from the SAML recipient, which is the regional AWS Sign-In service endpoint in the Region where you used the `/saml` operation. To failover to another Sign-In service endpoint to access the console successfully, either don’t use `saml:aud` as a condition key, use `StringEquals` with multiple endpoints listed, or use `StringLike` with a wildcard for the Region value, like `https://*signin.amazonaws.com/`.

## Third-party identity providers
<a name="third-party-identity-providers"></a>

 Third-party identity providers (IdPs) and federation services, such as [Okta](https://www.okta.com/), [PingFederate](https://www.pingidentity.com/en/product/pingfederate.html), [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id), [Active Directory Federation Service](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview), and [Shibboleth Identity Provider](https://shibboleth.atlassian.net/wiki/spaces/IDP5/overview) will use one or more of these services that provide global endpoints as part of their authentication flow. Typically, this includes the sign-in SAML endpoint for the Assertion Consumption Service (ACS) URL and the AWS Management Console endpoint for the relay state. You should configure your IdP to use a regional sign-in endpoint, not the global endpoint, for the ACS URL, also sometimes called the relying party endpoint.

 If your IdP supports multiple ACS URLs, you can configure them ahead of time. If the primary Region you use for SAML login is impacted, you should have a runbook to update your IdP’s configuration to use a different regional endpoint. The credentials provided by the AWS Sign-In service can be used in any Region. If your IdP is configured to use the global AWS Management Console endpoint for the relay state and it’s impaired, you should update it to use the specific regional endpoint where you want to access your AWS resources.

 If your IdP is unavailable, you should pre-provision break-glass long-term [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) credentials that are configured to use [multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) and store the IAM user credentials and tokens securely in a physical or virtual vault. You can use the IAM user credentials to access your organizations or AWS accounts and assume operational IAM roles for managing your environment. More information about this approach can be found in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html#break-glass-access) whitepaper. Make sure you regularly rotate these credentials as part of this plan, and follow the [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

 If you choose to sign in to the console with IAM user credentials as part of your break-glass process, use a regional console endpoint like `https://{{region}}.console.aws.amazon.com/` to avoid dependencies on other AWS Regions for console access. If you use the IAM user credentials to assume an IAM role directly with AWS STS, make sure you specify a different endpoint than the impaired Region.

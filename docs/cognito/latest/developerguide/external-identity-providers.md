---
source_url: https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html
---

# Identity pools third-party identity providers
<a name="external-identity-providers"></a>

With Amazon Cognito identity pools, you can integrate with a variety of external identity providers (IdPs) to provide temporary AWS credentials through federated authentication in your application. By configuring your identity pool to work with these external IdPs, you can authorize access to back-end AWS resources for your users with authentication by Amazon Cognito user pools, social providers, OIDC providers, or SAML providers. This section covers the steps to set up and integrate IdPs with your Amazon Cognito identity pool.

Using the `logins` property, you can set credentials received from an identity provider (IdP). You can also associate an identity pool with multiple IdPs. For example, you can set both the Facebook and Google tokens in the `logins` property to associate the unique Amazon Cognito identity with both IdP logins. The user can authenticate with either account, but Amazon Cognito returns the same user identifier.

The following instructions guide you through authentication with the IdPs that Amazon Cognito identity pools support.

**Topics**
+ [Setting up Facebook as an identity pools IdP](facebook.md)
+ [Setting up Login with Amazon as an identity pools IdP](amazon.md)
+ [Setting up Google as an identity pool IdP](google.md)
+ [Setting up Sign in with Apple as an identity pool IdP](apple.md)
+ [Setting up an OIDC provider as an identity pool IdP](open-id.md)
+ [Setting up a SAML provider as an identity pool IdP](saml-identity-provider.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

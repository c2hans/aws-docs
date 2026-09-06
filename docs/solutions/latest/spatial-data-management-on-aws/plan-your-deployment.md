---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section helps you plan your Spatial Data Management Application deployment by understanding prerequisites, sizing requirements, and configuration options.

## Production Deployment Recommendations
<a name="production-deployment-recommendations"></a>

For production deployments, consider the following best practices:

 **Custom Domain Configuration**

Configure a custom domain for your deployment following your organization’s security best practices and policies. You can specify a custom domain during the initial deployment, or configure it after deployment is complete.

 **External Identity Provider Integration**

Instead of managing users and groups directly in Amazon Cognito, integrate with your organization’s external identity provider. This centralizes user and group management in your existing identity system and enforces consistent security policies across your organization. For step-by-step OIDC and SAML configuration, including a Microsoft Entra ID walkthrough, see [Single sign-on (SSO)](sso.md). For more information about Amazon Cognito user pool identity federation, see [Amazon Cognito User Pools identity federation](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html) in the *Amazon Cognito Developer Guide*.

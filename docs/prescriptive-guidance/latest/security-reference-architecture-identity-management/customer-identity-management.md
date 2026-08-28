---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/customer-identity-management.html
---

# Customer identity management
<a name="customer-identity-management"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

Customer identity and access management (CIAM) is a technology that allows organizations to manage customer identities. It provides security and an enhanced user experience for signing up, signing in, and accessing consumer applications, web portals, or digital services offered by an organization. CIAM helps you identify your customers, create personalized experiences, and determine the correct access they need for customer-facing applications and services. A CIAM solution can also help an organization meet compliance mandates across industry regulatory standards and frameworks. For more information, see [What is CIAM?](https://aws.amazon.com/what-is/ciam/) on the AWS website.

[Amazon Cognito](https://aws.amazon.com/cognito/) is an identity service for web and mobile applications that provides CIAM capabilities to businesses of any scale. Amazon Cognito includes a user directory, an authentication server, and an authorization service for OAuth 2.0 access tokens, and can also provide temporary AWS credentials. You can use Amazon Cognito to authenticate and authorize users from the built-in user directory, from a federated identity provider such as your enterprise directory, or from social identity providers such as Google and Facebook.

The two main components of Amazon Cognito are user pools and identity pools. [User pools](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html#what-is-amazon-cognito-user-pools) are user directories that provide sign-up and sign-in options for your web and mobile application users. [Identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html#what-is-amazon-cognito-identity-pools) provide temporary AWS credentials to grant your users access to other AWS services.

## When to use Amazon Cognito
<a name="ciam-cognito"></a>

Amazon Cognito is a good choice when you require a secure and cost-effective  user management solution for your web and mobile applications. Here are some scenarios where you might decide to use Amazon Cognito:
+ **Authentication**. If you're prototyping an application or want to implement user login functionality quickly, you can use user pools and the hosted UI in Amazon Cognito to speed up development. You can focus on your core application features while Amazon Cognito handles user sign-up, sign-in, and security.

  Amazon Cognito supports various authentication methods, including usernames and passwords, social identity providers. and enterprise identity providers through SAML and OpenID Connect (OIDC).
+ **User management**. Amazon Cognito supports user management, including user registration, verification, and account recovery. Users can sign up and sign in with their preferred identity provider, and you can customize the registration process according to your application's requirements.
+ **Secure access to AWS resources**. Amazon Cognito integrates with IAM to provide fine-grained access control to AWS resources. You can define IAM roles and policies to control access to AWS services based on user identity and group membership.
+ **Federated identity**. Amazon Cognito supports federated identity, which allows a user to sign in by using their existing social or enterprise identities. This eliminates the need for users to create new credentials for your application, so it enhances the user experience and reduces friction during the sign-up process.
+ **Mobile and web applications**. Amazon Cognito is well-suited for both mobile and web applications. It provides SDKs for various platforms, and makes it easy to integrate authentication and access control into your application code. It supports offline access and synchronization for mobile applications, so users can access their data even when they're offline.
+ **Scalability**. Amazon Cognito is a highly available and fully managed service that can scale to millions of users. It processes more than 100 billion authentications per month.
+ **Security**. Amazon Cognito has several built-in security features, such as encryption of sensitive data, multi-factor authentication (MFA), and protection against common web attacks such as cross-site scripting (XSS) and cross-site request forgery (CSRF). Amazon Cognito also provides advanced security features such as adaptive authentication, checking for usage of compromised credentials, and access token customization.
+ **Integration with existing AWS services**. Amazon Cognito[ integrates seamlessly with AWS services](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-integrating-user-pools-with-identity-pools.html). This can simplify development and streamline user management for functionality that relies on AWS resources.

The following diagram illustrates some of these scenarios.

![Using Amazon Cognito as a customer identity and access management (CIAM).](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/a0686cf2-db62-4731-bcda-e5c6beb02240.png)

1. The application authenticates with Amazon Cognito user pools and gets tokens.

1. The application uses Amazon Cognito identity pools to exchange tokens for AWS credentials.

1. The application accesses AWS services with credentials.

We recommend that you use Amazon Cognito whenever you need to add user authentication, authorization, and user management capabilities to your web or mobile applications, especially when you have multiple identity providers, require secure access to AWS resources, and have scalability requirements.

**Design considerations:**
+ Create an Amazon Cognito user pool or identity pool based on your requirements.
+ Don't update the user profile too frequently (for example, with every sign-in request). If an update is required, store the updated attributes in an external database such as Amazon DynamoDB.
+ Do not use Amazon Cognito workforce identity management.
+ Your application should always validate JSON web tokens (JWTs) before trusting them by verifying their signature and validity. This validation should be done on the client side without sending API calls to the user pool. After the token is verified, you can trust the claims in the token and use them instead of making additional `getUser` API calls. For more information, see [Verifying JSON web tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html) in the Amazon Cognito documentation. You can also use [additional JWT libraries](https://jwt.io/#libraries-io) for token verification.
+ Enable the advanced security features in Amazon Cognito only if you aren't using a `CUSTOM_AUTH` flow, [AWS Lambda triggers for custom authentication challenges](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html), or federated sign-in. For considerations and limitations around advanced security features, see the [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html#cognito-user-pool-advanced-security-considerations) documentation.
+ Enable AWS WAF to protect Amazon Cognito user pools by using rate-based rules and combining multiple request parameters. For more information, see the AWS blog post [Protect your Amazon Cognito user pool with AWS WAF](https://aws.amazon.com/blogs/security/protect-your-amazon-cognito-user-pool-with-aws-waf/).
+ If you want an extra layer of protection, use an Amazon CloudFront proxy for additional processing and validation of incoming requests, as explained in the AWS blog post [Protect public clients for Amazon Cognito by using an Amazon CloudFront proxy](https://aws.amazon.com/blogs/security/protect-public-clients-for-amazon-cognito-by-using-an-amazon-cloudfront-proxy/).
+ All API calls after user sign-in should be made from backend services. For example, use AWS WAF to deny calls to `UpdateUserAttribute`, but then call `AdminUpdateUserAttribute` from the application backend instead, to update the user attribute.
+ When you create a user pool, you choose how users will sign in―for example, with a username, email address, or phone number. This configuration cannot be changed after the user pool is created. Similarly, custom attributes cannot be changed or removed after they are added to the user pool.
+ We recommend that you enable [multi-factor authentication (MFA)](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) in your user pool.
+ Amazon Cognito doesn't currently provide built-in backup or export functions. To back up or export your users' data, you can use the [Amazon Cognito profiles export reference architecture](https://aws.amazon.com/solutions/implementations/cognito-user-profiles-export-reference-architecture/).
+ Use IAM roles for general access to AWS resources. For fine-grained authorization requirements, use Amazon Verified Permissions. This permission management service [natively integrates with Amazon Cognito](https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/). You can also use [access token customization](https://aws.amazon.com/blogs/security/how-to-customize-access-tokens-in-amazon-cognito-user-pools/) to enrich application-specific claims in order to determine the level of access and content available to the user. If your application uses Amazon API Gateway as an entry point, use the Amazon Cognito feature to secure API Gateway by using Verified Permissions. This service manages and evaluates granular security policies that reference user attributes and groups.You can ensure that only users in authorized Amazon Cognito groups have access to the application's APIs. For more information, see the article [Protect API Gateway with Amazon Verified Permissions](https://community.aws/content/2euY03dfEImW1VDerX1ILegHqRb/protect-api-gateway-with-amazon-verified-permissions) in AWS Builder Center.
+ Use AWS SDKs to access user data from the backend by calling and retrieving user attributes, statuses, and group information. You can store custom app data in Amazon Cognito user attributes and keep it synchronized across devices.

The following sections discuss three patterns for integrating Amazon Cognito with other AWS services: [Application Load Balancers](#cognito-alb), [API Gateway](#cognito-api-gateway), and [Amazon OpenSearch Service](#cognito-opensearch).

## Integration with an Application Load Balancer
<a name="cognito-alb"></a>

You can configure an Application Load Balancer with Amazon Cognito to authenticate application users, as illustrated in the following diagram.

![Configuring an Application Load Balancer with Amazon Cognito for identification management.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/af4db1f6-4833-4a1a-b295-6f8933c4ccd6.png)

By configuring the HTTPS listener default rule, you can offload user identification to the Application Load Balancer and create an automatic authentication process. For details, see [How do I set up an Application Load Balancer to authenticate users through an Amazon Cognito user pool](https://repost.aws/knowledge-center/cognito-user-pool-alb-authentication) in the AWS Knowledge Center. If your application is hosted on Kubernetes, see the AWS blog post [How to use Application Load Balancer and Amazon Cognito to authenticate users for your Kubernetes web apps](https://aws.amazon.com/blogs/containers/how-to-use-application-load-balancer-and-amazon-cognito-to-authenticate-users-for-your-kubernetes-web-apps/).

## Integration with Amazon API Gateway
<a name="cognito-api-gateway"></a>

Amazon API Gateway is a fully managed, cloud-based API gateway service that makes it easy to create, publish and manage APIs at scale. It is an entry point for user traffic into the backend services. You can integrate Amazon Cognito with API Gateway to implement authentication and access control, either to protect the APIs from misuse or for any other security or business use case. There are two methods for securing access to API Gateway:  by using an Amazon Cognito authorizer (as illustrated in the following diagram) or by using an AWS Lambda authorizer. For more information about these implementations, see [How do I set up an Amazon Cognito user pool as an authorizer on an API Gateway REST API?](https://repost.aws/knowledge-center/api-gateway-cognito-user-pool-authorizer) in the AWS Knowledge Base.

![Using an Amazon Cognito authorizer with API Gateway for identification management.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/487ab392-fe78-4fca-a519-fc657caa9c4b.png)

## Integration with Amazon OpenSearch Service
<a name="cognito-opensearch"></a>

You can use Amazon Cognito to secure Amazon OpenSearch Service domains. For example, if a user might need access to OpenSearch Dashboards from the internet, as illustrated in the following diagram. In this scenario, Amazon Cognito can provide access permissions, including fine-grained permissions, by mapping Amazon Cognito groups and users to internal OpenSearch Service permissions. For more information, see [Configuring Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html) in the OpenSearch Service documentation.

![Using an Amazon Cognito authorizer with API Gateway for identification management.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/a335f878-28b0-4150-b6c9-7905fed65579.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

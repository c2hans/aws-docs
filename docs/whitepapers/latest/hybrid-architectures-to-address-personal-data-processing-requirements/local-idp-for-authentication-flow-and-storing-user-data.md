---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/local-idp-for-authentication-flow-and-storing-user-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.2 Local IdP for authentication flow and storing user data
<a name="local-idp-for-authentication-flow-and-storing-user-data"></a>

 Requirements addressed:
+  **REQ1** (data residency)

 AWS services – [Amazon Cognito](https://aws.amazon.com/cognito/), [AWS AppSync](https://aws.amazon.com/appsync/), and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

![Local identity provider for cloud-based application](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/local-identity-provider-cloud-based-apps.png)

 Local identity provider for cloud-based application

 For web applications that require only a minimal set of personal data, specifically related to the authentication flow, you can fulfill **REQ1** by using identity pools with local identity providers. This functionality is provided by [Amazon Cognito](https://aws.amazon.com/cognito/), which can be integrated with third-party Identity Providers (IdPs).

 On the diagram, **Auth (1)** is the initial authentication from the mobile application to Amazon Cognito. Cognito further redirects the identity validation to external IdP **Auth (2)**, which provides the user with required authentication tokens **Auth (3**) and further validation. Next, the mobile application uses the GraphQL API to access the locally hosted GraphQL application, which is based on Apollo Framework schema federation. This allows you to join portions of authentication data from multiple sources in a declarative way:
+  Personal data from a local database in an on-premises data center
+  All other application data from AWS AppSync that also works as GraphQL backend, which persists other data in [Amazon DynamoDB](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-resolvers.html) (or another AWS database service)

 The AWS part of the GraphQL data is handled by [AWS AppSync](https://aws.amazon.com/appsync/) (GraphQL).

 Amazon Cognito supports a number of [social IdPs](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-social-idp.html), [SAML providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html), [OIDC providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html), and [Apple](https://docs.aws.amazon.com/cognito/latest/developerguide/apple.html). Amazon Cognito and user applications will work with these IdPs using the OAuth 2.0 protocol.

 In this scenario, the storage of personal data (used for authentication in application) is delegated to Local IdP.

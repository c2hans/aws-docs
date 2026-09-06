---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/cognito-identity.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Amazon Cognito Identity
<a name="cognito-identity"></a>

## What is Amazon Cognito Identity?
<a name="what-is-amazon-cognito-identity"></a>

Amazon Cognito Identity enables you to create unique identities for your users and authenticate them with identity providers. With an identity, you can obtain temporary, limited-privilege AWS credentials to synchronize data with Amazon Cognito Sync, or directly access other AWS services. Amazon Cognito Identity supports public identity providers—Amazon, Facebook, and Google—as well as unauthenticated identities. It also supports developer authenticated identities, which let you register and authenticate users via your own backend authentication process.

For more information on Cognito Identity, see the [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html).

For information about Cognito Authentication Region availability, see [AWS Service Region Availability](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

### Using a Public Provider to Authenticate Users
<a name="using-a-public-provider-to-authenticate-users"></a>

Using Amazon Cognito Identity, you can create unique identities for your users and authenticate them for secure access to your AWS resources like Amazon S3 or Amazon DynamoDB. Amazon Cognito Identity supports public identity providers—Amazon, Facebook, Twitter/Digits, Google, or any OpenID Connect-compatible provider—as well as unauthenticated identities.

For information on using public identity providers like Amazon, Facebook, Twitter/Digits, or Google to authenticate users, see the [External Providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html) in the Amazon Cognito Developer Guide.

### Using Developer Authenticated Identities
<a name="using-developer-authenticated-identities"></a>

Amazon Cognito supports developer authenticated identities, in addition to web identity federation through Facebook, Google, and Amazon. With developer authenticated identities, you can register and authenticate users via your own existing authentication process, while still using [Amazon Cognito Sync](cognito-sync.md) to synchronize user data and access AWS resources. Using developer authenticated identities involves interaction between the end user device, your backend for authentication, and Amazon Cognito.

For information on developer authenticated identities, see the [Developer Authenticated Identities](https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html) in the Amazon Cognito Developer Guide.

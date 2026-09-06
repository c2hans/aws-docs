---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html
---

# CreateOpenIDConnectProvider
<a name="API_CreateOpenIDConnectProvider"></a>

Creates an IAM entity to describe an identity provider (IdP) that supports [OpenID Connect (OIDC)](http://openid.net/connect/).

The OIDC provider that you create with this operation can be used as a principal in a role's trust policy. Such a policy establishes a trust relationship between AWS and the OIDC provider.

If you are using an OIDC identity provider from Google, Facebook, or Amazon Cognito, you don't need to create a separate IAM identity provider. These OIDC identity providers are already built-in to AWS and are available for your use. Instead, you can move directly to creating new roles using your identity provider. To learn more, see [Creating a role for web identity or OpenID connect federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) in the *IAM User Guide*.

When you create the IAM OIDC provider, you specify the following:
+ The URL of the OIDC identity provider (IdP) to trust
+ A list of client IDs (also known as audiences) that identify the application or applications allowed to authenticate using the OIDC provider
+ A list of tags that are attached to the specified IAM OIDC provider
+ A list of thumbprints of one or more server certificates that the IdP uses

You get all of this information from the OIDC IdP you want to use to access AWS.

**Note**
 AWS secures communication with OIDC identity providers (IdPs) using our library of trusted root certificate authorities (CAs) to verify the JSON Web Key Set (JWKS) endpoint's TLS certificate. If your OIDC IdP relies on a certificate that is not signed by one of these trusted CAs, only then we secure communication using the thumbprints set in the IdP's configuration.

**Note**
The trust for the OIDC provider is derived from the IAM provider that this operation creates. Therefore, it is best to limit access to the [CreateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html) operation to highly privileged users.

## Request Parameters
<a name="API_CreateOpenIDConnectProvider_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ClientIDList.member.N**
Provides a list of client IDs, also known as audiences. When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. This is the value that's sent as the `client_id` parameter on OAuth requests.
You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.
There is no defined format for a client ID. The `CreateOpenIDConnectProviderRequest` operation accepts client IDs up to 255 characters long.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 **Tags.member.N**
A list of tags that you want to attach to the new IAM OpenID Connect (OIDC) provider. Each tag consists of a key name and an associated value. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 **ThumbprintList.member.N**
A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.
This parameter is optional. If it is not included, IAM will retrieve and use the top intermediate certificate authority (CA) thumbprint of the OpenID Connect identity provider server certificate.
The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
For example, assume that the OIDC provider is `server.example.com` and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by `https://keys.server.example.com.`
For more information about obtaining the OIDC provider thumbprint, see [Obtaining the thumbprint for an OpenID Connect provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/identity-providers-oidc-obtain-thumbprint.html) in the *IAM user Guide*.
If your OIDC provider's discovery endpoint and JWKS endpoint (`jwks_uri`) use different certificates or hosts, include the thumbprints for both endpoints in this list.
Type: Array of strings
Length Constraints: Fixed length of 40.
Required: No

 ** Url **
The URL of the identity provider. The URL must begin with `https://` and should correspond to the `iss` claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like `https://server.example.org` or `https://example.com`. The URL should not contain a port number.
You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_CreateOpenIDConnectProvider_ResponseElements"></a>

The following elements are returned by the service.

 ** OpenIDConnectProviderArn **
The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For more information, see [OpenIDConnectProviderListEntry](https://docs.aws.amazon.com/IAM/latest/APIReference/API_OpenIDConnectProviderListEntry.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 **Tags.member.N**
A list of tags that are attached to the new IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_CreateOpenIDConnectProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** EntityAlreadyExists **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** OpenIdIdpCommunicationError **
The request failed because IAM cannot connect to the OpenID Connect identity provider URL.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_CreateOpenIDConnectProvider_Examples"></a>

### Example
<a name="API_CreateOpenIDConnectProvider_Example_1"></a>

This example illustrates one usage of CreateOpenIDConnectProvider.

#### Sample Request
<a name="API_CreateOpenIDConnectProvider_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=CreateOpenIDConnectProvider
&ThumbprintList.list.1=c3768084dfb3d2b68b7897bf5f565da8eEXAMPLE
&ClientIDList.list.1=my-application-ID
&Url=https://server.example.com
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateOpenIDConnectProvider_Example_1_Response"></a>

```
<CreateOpenIDConnectProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateOpenIDConnectProviderResult>
    <OpenIDConnectProviderArn>
      arn:aws:iam::123456789012:oidc-provider/server.example.com
    </OpenIDConnectProviderArn>
  </CreateOpenIDConnectProviderResult>
  <ResponseMetadata>
    <RequestId>f248366a-4f64-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateOpenIDConnectProviderResponse>
```

## See Also
<a name="API_CreateOpenIDConnectProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/CreateOpenIDConnectProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/CreateOpenIDConnectProvider)

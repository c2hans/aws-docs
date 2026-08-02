---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role-web.html
---

# Assuming a role with web identity or OpenID Connect to authenticate AWS SDKs and tools
<a name="access-assume-role-web"></a>

Assuming a role involves using a set of temporary security credentials to access AWS resources that you might not have access to otherwise. These temporary credentials consist of an access key ID, a secret access key, and a security token. To learn more about AWS Security Token Service (AWS STS) API requests, see [Actions](https://docs.aws.amazon.com/STS/latest/APIReference/API_Operations.html) in the *AWS Security Token Service API Reference*.

To set up your SDK or tool to assume a role, you must first create or identify a specific *role* to assume. IAM roles are uniquely identified by a role Amazon Resource Name ([ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)). Roles establish trust relationships with another entity. The trusted entity that uses the role might be a web identity provider or OpenID Connect(OIDC), or SAML federation. To learn more about IAM roles, see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

After the IAM role is configured in your SDK, if that role is configured to trust your identity provider, you can further configure your SDK to assume that role in order to get temporary AWS credentials.

**Note**
It is an AWS best practice to use Regional endpoints whenever possible and to configure your [AWS Region](feature-region.md).

## Federate with web identity or OpenID Connect
<a name="webidentity"></a>

You can use the JSON Web Tokens (JWTs) from public identity providers, such as Login With Amazon, Facebook, Google to get temporary AWS credentials using `AssumeRoleWithWebIdentity`. Depending on how they are used, these JWTs may be called ID tokens or access tokens. You may also use JWTs issued from identity providers (IdPs) that are compatible with OIDC's discovery protocol, such as EntraId or PingFederate.

If you are using Amazon Elastic Kubernetes Service, this feature provides the ability to specify different IAM roles for each one of your service accounts in an Amazon EKS cluster. This Kubernetes feature distributes JWTs to your pods which are then used by this credential provider to obtain temporary AWS credentials. For more information on this Amazon EKS configuration, see [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) in the **Amazon EKS User Guide**. However, for a simpler option, we recommend you use [Amazon EKS Pod Identities](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) instead if your [SDK supports it](feature-container-credentials.md#feature-container-credentials-sdk-compat).

### Step 1: Set up an identity provider and IAM role
<a name="webidentity_step1"></a>

To configure federation with an external IdP, use an IAM identity provider to inform AWS about the external IdP and its configuration. This establishes *trust* between your AWS account and the external IdP. Before configuring the SDK to use the JSON Web Token (JWT) for authentication, you must first set up the identity provider (IdP) and the IAM role used to access it. To set these up, see [Creating a role for web identity or OpenID Connect Federation (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) in the *IAM User Guide*.

### Step 2: Configure the SDK or tool
<a name="webidentity_step2"></a>

Configure the SDK or tool to use a JSON Web Token (JWT) from AWS STS for authentication.

When you specify this in a profile, the SDK or tool automatically makes the corresponding AWS STS [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) API call for you. To retrieve and use temporary credentials using web identity federation, specify the following configuration values in the shared AWS `config` file. For more details on each of these settings, see the [Assume role credential provider settings](feature-assume-role-credentials.md#feature-assume-role-credentials-settings) section.
+ `role_arn` - From the IAM role you created in Step 1
+ `web_identity_token_file` - From the external IdP
+ (Optional) `duration_seconds`
+ (Optional) `role_session_name`

The following is an example of a shared `config` file configuration to assume a role with web identity:

```
[profile {{web-identity}}]
role_arn=arn:aws:iam::{{123456789012}}:role/{{my-role-name}}
web_identity_token_file={{/path/to/a/token}}
```

**Note**
For mobile applications, consider using Amazon Cognito. Amazon Cognito acts as an identity broker and does much of the federation work for you. However, the Amazon Cognito identity provider isn't included in the SDKs and tools core libraries like other identity providers. To access the Amazon Cognito API, include the Amazon Cognito service client in the build or libraries for your SDK or tool. For usage with AWS SDKs, see [Code Examples](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples.html) in the *Amazon Cognito Developer Guide*.

For details on all assume role credential provider settings, see [Assume role credential provider](feature-assume-role-credentials.md) in this guide.

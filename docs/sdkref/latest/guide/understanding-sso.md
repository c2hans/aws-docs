---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html
---

# How IAM Identity Center authentication is resolved for AWS SDKs and tools
<a name="understanding-sso"></a>

## Relevant IAM Identity Center terms
<a name="ssoterms"></a>

The following terms help you understand the process and configuration behind AWS IAM Identity Center. The documentation for AWS SDK APIs uses different names than IAM Identity Center for some of these authentication concepts. It's helpful to know both names.

The following table shows how alternative names relate to each other.

| IAM Identity Center name | SDK API name | Description |
| --- | --- | --- |
| Identity Center  | sso  | Although AWS Single Sign-On is renamed, the sso API namespaces will keep their original name for backward compatibility purposes. For more information, see [IAM Identity Center rename](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html#renamed) in the AWS IAM Identity Center User Guide. |
| IAM Identity Center console<br />Administrative console |   | The console you use to configure single sign-on.  |
| AWS access portal URL  |  | A URL unique to your IAM Identity Center account, like https://{{xxx}}.awsapps.com/start. You sign in to this portal using your IAM Identity Center sign-in credentials.  |
| IAM Identity Center Access Portal session  | Authentication session  | Provides a bearer access token to the caller.  |
| Permission set session  |   | The IAM session that the SDK uses internally to make the AWS service calls. In informal discussions, you might see this incorrectly referred to as "role session." |
| Permission set credentials  | AWS credentials<br />sigv4 credentials | The credentials the SDK actually uses for most AWS service calls (specifically, all sigv4 AWS service calls). In informal discussions, you might see this incorrectly referred to as "role credentials." |
| IAM Identity Center credential provider  | SSO credential provider  | How you get the credentials, such as the class or module providing the functionality.  |

## Understand SDK credential resolution for AWS services
<a name="idccredres"></a>

The IAM Identity Center API exchanges bearer token credentials for sigv4 credentials. Most AWS services are sigv4 APIs, with a few exceptions like Amazon CodeWhisperer and Amazon CodeCatalyst. The following describes the credential resolution process for supporting most AWS service calls for your application code through AWS IAM Identity Center.

### Start an AWS access portal session
<a name="idccredres1"></a>
+ Start the process by signing in to the session with your credentials.
  + Use the `aws sso login` command in the AWS Command Line Interface (AWS CLI). This starts a new IAM Identity Center session if you don't already have an active session.
+ When you start a new session, you receive a refresh token and access token from IAM Identity Center. The AWS CLI also updates an SSO cache JSON file with a new access token and refresh token and makes it available for use by SDKs.
+ If you already have an active session, the AWS CLI command reuses the existing session and will expire whenever the existing session expires. To learn how to set the length of an IAM Identity Center session, see [Configure the duration of your users' AWS access portal sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html) in the *AWS IAM Identity Center User Guide*.
  + The maximum session length has been extended to 90 days to reduce the need for frequent sign-ins.

### How the SDK gets credentials for AWS service calls
<a name="idccredres2"></a>

SDKs provide access to AWS services when you instantiate a client object per service. When the selected profile of the shared AWS `config` file is configured for IAM Identity Center credential resolution, IAM Identity Center is used to resolve credentials for your application.
+ The [credential resolution process](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain) is completed during runtime when a client is created.

To retrieve credentials for sigv4 APIs using IAM Identity Center single sign-on, the SDK uses the IAM Identity Center access token to get an IAM session. This IAM session is called a permission set session, and it provides AWS access to the SDK by assuming an IAM role.
+  The permission set session duration is set independently from the IAM Identity Center session duration.
  + To learn how to set the permission set session duration, see [Set session duration](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html) in the *AWS IAM Identity Center User Guide*.
+  Be aware that the permission set credentials are also referred to as *AWS credentials* and *sigv4 credentials* in most AWS SDK API documentation.

The permission set credentials are returned from a call to [getRoleCredentials](https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html) of the IAM Identity Center API to the SDK. The SDK's client object uses that assumed IAM role to make calls to the AWS service, such as asking Amazon S3 to list the buckets in your account. The client object can continue to operate using those permission set credentials until the permission set session expires.

### Session expiration and refresh
<a name="idccredres3"></a>

When using the [SSO token provider configuration](feature-sso-credentials.md#sso-token-config), the hourly access token obtained from IAM Identity Center is automatically refreshed using the refresh token.
+ If the access token is expired when the SDK tries to use it, the SDK uses the refresh token to try to get a new access token. The IAM Identity Center compares the refresh token to your IAM Identity Center access portal session duration. If the refresh token is not expired, the IAM Identity Center responds with another access token.
+ This access token can be used to either refresh the permission set session of existing clients, or to resolve credentials for new clients.

However, if the IAM Identity Center access portal session is expired, then no new access token is granted. Therefore, the permission set duration cannot be renewed. It will expire (and access will be lost) whenever the cached permission set session length times out for existing clients.

Any code that creates a new client will fail authentication as soon as the IAM Identity Center session expires. This is because the permission set credentials are not cached. Your code won't be able to create a new client and complete the credential resolution process until you have a valid access token.

To recap, when the SDK needs new permission set credentials, the SDK first checks for any valid, existing credentials and uses those. This applies whether the credentials are for a new client or for an existing client with expired credentials. If credentials aren't found or they're not valid, then the SDK calls the IAM Identity Center API to get new credentials. To call the API, it needs the access token. If the access token is expired, the SDK uses the refresh token to try to get a new access token from the IAM Identity Center service. This token is granted if your IAM Identity Center access portal session is not expired.

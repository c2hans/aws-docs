---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-credential-providers.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Credential providers
<a name="migrate-credential-providers"></a>

 In v2, the SDK for JavaScript provides a list of credential providers to choose from, as well as a credentials provider chain, available by default on Node.js, that tries to load the AWS credentials from all the most common providers. The SDK for JavaScript v3 simplifies the credential provider's interface, making it easier to use and write custom credential providers. On top of a new credentials provider chain, the SDK for JavaScript v3 all provides a list of credential providers aiming to provide equivalent to v2.

 Here are all the credential providers in v2 and their equivalents in v3.

## Default Credential Provider
<a name="default-credential-provider"></a>

 The default credential provider is how the SDK for JavaScript resolve the AWS credential if you *do not* provide one explicitly.
+  **v2**: [CredentialProviderChain](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CredentialProviderChain.html) in Node.js resolves credential from sources as following order:
  +  [Environmental variable](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-environment.html)
  +  [Shared credentials file](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html)
  +  [ECS container credentials](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/RemoteCredentials.html)
  +  [Spawning external process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html)
  +  [OIDC token from specified file](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TokenFileWebIdentityCredentials.html)
  +  [Amazon EC2 instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

   If one of the credential providers above fails to resolve the AWS credential, the chain falls back to next provider until a valid credential is resolved, and the chain will throw an error when all of the providers fail.

   In Browser and React Native runtimes, the credential chain is empty, and credentials must be set explicitly.
+  **v3**: [defaultProvider](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers#fromnodejsproviderchain-1). The credential sources and fallback order *does not* change in v3. It also supports [AWS IAM Identity Center credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

## Temporary Credentials
<a name="temporary-credentials"></a>
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/ChainableTemporaryCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/ChainableTemporaryCredentials.html) represents temporary credentials retrieved from `AWS.STS`. Without any extra parameters, credentials will be fetched from the `AWS.STS.getSessionToken()` operation. If an IAM role is provided, the `AWS.STS.assumeRole()` operation will be used to fetch credentials for the role instead. `AWS.ChainableTemporaryCredentials` differs from `AWS.TemporaryCredentials` in the way masterCredentials and refreshes are handled. `AWS.ChainableTemporaryCredentials` refreshes expired credentials using the masterCredentials passed by the user to support chaining of STS credentials. However, `AWS.TemporaryCredentials` recursively collapses the masterCredentials during instantiation, precluding the ability to refresh credentials which require intermediate, temporary credentials.

   The original [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TemporaryCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TemporaryCredentials.html) has been **deprecated** in favor of `ChainableTemporaryCredentials` in v2.
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromtemporarycredentials](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromtemporarycredentials). You can call `fromTemporaryCredentials()` from the `@aws-sdk/credential-providers` package. Here's an example:

  ```
  import { FooClient } from "@aws-sdk/client-foo";
  import { fromTemporaryCredentials } from "@aws-sdk/credential-providers"; // ES6 import
  // const { FooClient } = require("@aws-sdk/client-foo");
  // const { fromTemporaryCredentials } = require("@aws-sdk/credential-providers"); // CommonJS import

  const sourceCredentials = {
    // A credential can be a credential object or an async function that returns a credential object
  };
  const client = new FooClient({
    credentials: fromTemporaryCredentials({
      masterCredentials: sourceCredentials,
      params: { RoleArn },
    }),
  });
  ```

## Amazon Cognito Identity Credentials
<a name="cognito-identity-credentials"></a>

 Load credentials from the Amazon Cognito Identity service, normally used in browsers.
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityCredentials.html) Represents credentials retrieved from STS Web Identity Federation using the Amazon Cognito Identity service.
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html) The [`@aws/credential-providers` package](https://www.npmjs.com/package/@aws-sdk/credential-providers) provides two credential provider functions, one of which [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html) takes an identity ID and calls `cognitoIdentity:GetCredentialsForIdentity`, while the other [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html) takes an identity pool ID, calls `cognitoIdentity:GetId` on the first invocation, and then calls`fromCognitoIdentity`. Subsequent invocations of the latter do not re-invoke GetId.

   The provider implements the "Simplified Flow" described in the [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html). The "Classic Flow" which involves calling `cognito:GetOpenIdToken` and then calling `sts:AssumeRoleWithWebIdentity` is *not* supported. Please open a [feature request](https://github.com/aws/aws-sdk-js-v3/issues/new?assignees=&labels=feature-request&template=---feature-request.md&title=) to us if you need it.

  ```
  // fromCognitoIdentityPool example
  import { fromCognitoIdentityPool } from "@aws-sdk/credential-providers"; // ES6 import
  // const { fromCognitoIdentityPool } = require("@aws-sdk/credential-providers"); // CommonJS import

  const client = new FooClient({
    region: "us-east-1",
    credentials: fromCognitoIdentityPool({
      clientConfig: cognitoIdentityClientConfig, // Optional
      identityPoolId: "us-east-1:1699ebc0-7900-4099-b910-2df94f52a030",
      customRoleArn: "arn:aws:iam::1234567890:role/MYAPP-CognitoIdentity", // Optional
      logins: {
        // Optional
        "graph.facebook.com": "FBTOKEN",
        "www.amazon.com": "AMAZONTOKEN",
        "api.twitter.com": "TWITTERTOKEN",
      },
    }),
  });
  ```

  ```
  // fromCognitoIdentity example
  import { fromCognitoIdentity } from "@aws-sdk/credential-providers"; // ES6 import
  // const { fromCognitoIdentity } = require("@aws-sdk/credential-provider-cognito-identity"); // CommonJS import

  const client = new FooClient({
    region: "us-east-1",
    credentials: fromCognitoIdentity({
      clientConfig: cognitoIdentityClientConfig, // Optional
      identityId: "us-east-1:128d0a74-c82f-4553-916d-90053e4a8b0f",
      customRoleArn: "arn:aws:iam::1234567890:role/MYAPP-CognitoIdentity", // Optional
      logins: {
        // Optional
        "graph.facebook.com": "FBTOKEN",
        "www.amazon.com": "AMAZONTOKEN",
        "api.twitter.com": "TWITTERTOKEN",
      },
    }),
  });
  ```

## Amazon EC2 Metadata (IMDS) Credential
<a name="ec2-metadataimds-credential"></a>

 Represents credentials received from the metadata service on an Amazon EC2 instance.
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityCredentials.html)
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata). Creates a credential provider that will source credentials from the Amazon EC2 Instance Metadata Service.

  ```
  import { fromInstanceMetadata } from "@aws-sdk/credential-providers"; // ES6 import
  // const { fromInstanceMetadata } = require("@aws-sdk/credential-providers"); // CommonJS import

  const client = new FooClient({
    credentials: fromInstanceMetadata({
      maxRetries: 3, // Optional
      timeout: 0, // Optional
    }),
  });
  ```

## Amazon ECS Credentials
<a name="ecs-credentials"></a>

 Represents credentials received from specified URL. This provider will request temporary credentials from URI specified by the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or the `AWS_CONTAINER_CREDENTIALS_FULL_URI` environment variable.
+  **v2**: `ECSCredentials` or [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/RemoteCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/RemoteCredentials.html)
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata). Creates a credential provider that will source credentials from the Amazon ECS Container Metadata Service.

  ```
  import { fromContainerMetadata } from "@aws-sdk/credential-providers"; // ES6 import

  const client = new FooClient({
    credentials: fromContainerMetadata({
      maxRetries: 3, // Optional
      timeout: 0, // Optional
    }),
  });
  ```

## File System Credentials
<a name="file-system-credentials"></a>
+ **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/FileSystemCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/FileSystemCredentials.html). Represents credentials from a JSON file on disk.
+  **v3**: **Deprecated**. You can explicitly read the JSON file and supply to the client. Please open a [feature request](https://github.com/aws/aws-sdk-js-v3/issues/new?assignees=&labels=feature-request&template=---feature-request.md&title=) to us if you need it.

## SAML Credential Provider
<a name="saml-credential-provider"></a>
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SAMLCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SAMLCredentials.html) Represents credentials retrieved from STS SAML support.
+  **v3**: **Not available**. Please open a [feature request](https://github.com/aws/aws-sdk-js-v3/issues/new?assignees=&labels=feature-request&template=---feature-request.md&title=) to us if you need it.

## Shared Credential File Credentials
<a name="shared-credential-file-credentials"></a>

 Loads credentials from shared credentials file (defaulting to `~/.aws/credentials` or defined by the `AWS_SHARED_CREDENTIALS_FILE` environment variable). This file is supported across different AWS SDKs and tools. You can refer to the [shared config and credentials files document](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) for more information.
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SharedIniFileCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SharedIniFileCredentials.html)
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_credential_providers.html)

  ```
  import { fromIni } from "@aws-sdk/credential-providers";
  // const { fromIni } from("@aws-sdk/credential-providers");

  const client = new FooClient({
    credentials: fromIni({
      configFilepath: "~/.aws/config", // Optional
      filepath: "~/.aws/credentials", // Optional
      mfaCodeProvider: async (mfaSerial) => {
        // implement a pop-up asking for MFA code
        return "some_code";
      }, // Optional
      profile: "default", // Optional
      clientConfig: { region }, // Optional
    }),
  });
  ```

## Web Identity Credentials
<a name="web-identity-credentials"></a>

 Retrieves credentials using OIDC token from a file on disk. Commonly used in Amazon EKS.
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TokenFileWebIdentityCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TokenFileWebIdentityCredentials.html)
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromtokenfile](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromtokenfile)

  ```
  import { fromTokenFile } from "@aws-sdk/credential-providers"; // ES6 import
  // const { fromTokenFile } from("@aws-sdk/credential-providers"); // CommonJS import

  const client = new FooClient({
    credentials: fromTokenFile({
      // Optional. If skipped, read from `AWS_ROLE_ARN` environmental variable
      roleArn: "arn:xxxx",
      // Optional. If skipped, read from `AWS_ROLE_SESSION_NAME` environmental variable
      roleSessionName: "session:a",
      // Optional. STS client config to make the assume role request.
      clientConfig: { region },
    }),
  });
  ```

## Web Identity Federation Credentials
<a name="web-identity-federation-credentials"></a>

 Retrieves credentials from STS web identity federation support.
+  **v2**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/WebIdentityCredentials.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/WebIdentityCredentials.html)
+  **v3**: [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromwebtoken](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromwebtoken)

  ```
  import { fromWebToken } from "@aws-sdk/credential-providers"; // ES6 import
  // const { fromWebToken } from("@aws-sdk/credential-providers"); // CommonJS import

  const client = new FooClient({
    credentials: fromWebToken({
      // Optional. If skipped, read from `AWS_ROLE_ARN` environmental variable
      roleArn: "arn:xxxx",
      // Optional. If skipped, read from `AWS_ROLE_SESSION_NAME` environmental variable
      roleSessionName: "session:a",
      // Optional. STS client config to make the assume role request.
      clientConfig: { region },
    }),
  });
  ```

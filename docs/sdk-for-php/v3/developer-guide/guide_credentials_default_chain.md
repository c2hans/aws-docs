---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_default_chain.html
---

# Understanding the default credential provider chain in the AWS SDK for PHP Version 3
<a name="guide_credentials_default_chain"></a>

The default credential provider chain is made up of a series of built-in credential providers that the SDK invokes. It is implemented by the [defaultProvider](defaultprovider-provider.md) credential provider function with no parameters. After valid credentials are found, the search is stopped.

The AWS SDK for PHP executes credential providers in the following order:
+ [**`env` provider**](env-provider.md) - the SDK searches for [AWS access keys that have been set as environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html).
+ [**`assumeRoleWithWebIdentityCredentialProvider` provider**](assume-role-with-web-identity-provider.md) - The SDK searches for IAM role and web identity token file settings.
+ At this point in the chain, the SDK looks for configuration in the shared AWS `config` and `credentials` files. The SDK looks for configuration under the "default" profile, but if the `AWS_PROFILE` environment variable is set, the SDK uses its named profile value.
  +  [**`sso` provider**](sso-provider.md) - The SDK looks for [IAM Identity Center configuration settings](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config) in the shared `config` file.
  +  [**`login provider` **](login-provider.md) - The SDK looks for AWS console login session configuration settings in the shared `config` file.
  + [**`process` provider **](process-provider.md) - The SDK looks for the `credential_process` setting in the shared `credentials` file.
  + [**`ini` provider**](ini-provider.md) - The SDK looks for the AWS credentials or IAM role information in the shared `credentials` file.
  + [**`process` provider**](process-provider.md) - The SDK looks for the `credential_process` setting in the shared `config` file.
  + [**`ini` provider**](ini-provider.md) - The SDK looks for the AWS credentials or IAM role information in the shared `config` file.
+ [**`ecsCredentials` provider**](ecscredentials-provider.md) - The SDK looks for the environment variables `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI `or `AWS_CONTAINER_CREDENTIALS_FULL_URI` that provide information to acquire temporary credentials.
+ [**`instanceProfile` provider**](instanceprofile-provider.md) - The SDK uses the EC2 Instance Metadata service to get the IAM role specified in the instance profile. Using the role information, the SDK acquires temporary credentials.

**Note**
The result of the default provider is automatically memoized.

You can review the code for the chain in the GitHub [source code](https://github.com/aws/aws-sdk-php/blob/0a99dab427f0a1c082775301141aeac3558691ad/src/Credentials/CredentialProvider.php#L77).

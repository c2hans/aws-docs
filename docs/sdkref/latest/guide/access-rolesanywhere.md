---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-rolesanywhere.html
---

# Using IAM Roles Anywhere to authenticate AWS SDKs and tools
<a name="access-rolesanywhere"></a>

You can use IAM Roles Anywhere to get temporary security credentials in IAM for workloads such as servers, containers, and applications that run outside of AWS. To use IAM Roles Anywhere, your workloads must use X.509 certificates. Your Cloud Administrator should provide the certificate and private key needed to configure IAM Roles Anywhere as your credential provider.

## Step 1: Configure IAM Roles Anywhere
<a name="config-ira"></a>

IAM Roles Anywhere provides a way to get temporary credentials for a workload or process that runs outside of AWS. A trust anchor is established with the certificate authority to get temporary credentials for the associated IAM role. The role sets the permissions your workload will have when your code authenticates with IAM Roles Anywhere.

For steps to set up the trust anchor, IAM role, and IAM Roles Anywhere profile, see [Creating a trust anchor and profile in AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html) in the *IAM Roles Anywhere User Guide*.

**Note**
A *profile* in the *IAM Roles Anywhere User Guide* refers to a unique concept within the IAM Roles Anywhere service. It's not related to the profiles within the shared AWS `config` file.

## Step 2: Use IAM Roles Anywhere
<a name="use-ira"></a>

To get temporary security credentials from IAM Roles Anywhere, use the credential helper tool provided by IAM Roles Anywhere. The credential tool implements the signing process for IAM Roles Anywhere.

For instructions to download the credential helper tool, see [Obtaining temporary security credentials from AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html) in the *IAM Roles Anywhere User Guide*.

To use temporary security credentials from IAM Roles Anywhere with AWS SDKs and the AWS CLI, you can configure `credential_process` setting in the shared AWS `config` file. The SDKs and AWS CLI support a process credential provider that uses `credential_process` to authenticate. The following shows the general structure to set `credential_process`.

```
credential_process = [path to helper tool] [command] [--parameter1 {{value}}] [--parameter2 {{value}}] [...]
```

The `credential-process` command of the helper tool returns temporary credentials in a standard JSON format that is compatible with the `credential_process` setting. Note that the command name contains a hyphen but the setting name contains an underscore. The command requires the following parameters:
+ `private-key` – The path to the private key that signed the request.
+ ` certificate` – The path to the certificate.
+ `role-arn` – The ARN of the role to get temporary credentials for.
+ `profile-arn` – The ARN of the profile that provides a mapping for the specified role.
+ `trust-anchor-arn` – The ARN of the trust anchor used to authenticate.

Your Cloud Administrator should provide the certificate and private key. All three ARN values can be copied from the AWS Management Console. The following example shows a shared `config` file that configures retrieving temporary credentials from the helper tool.

```
[profile {{dev}}]
credential_process = ./aws_signing_helper credential-process --certificate {{/path/to/certificate}} --private-key {{/path/to/private-key}} --trust-anchor-arn {{arn:aws:rolesanywhere:region:account:trust-anchor/TA_ID}} --profile-arn {{arn:aws:rolesanywhere:region:account:profile/PROFILE_ID}} --role-arn {{arn:aws:iam::account:role/ROLE_ID}}
```

 For optional parameters and additional helper tool details, see [IAM Roles Anywhere Credential Helper](https://github.com/aws/rolesanywhere-credential-helper#readme) on GitHub.

For details on the SDK configuration setting itself and the process credential provider, see [Process credential provider](feature-process-credentials.md) in this guide.

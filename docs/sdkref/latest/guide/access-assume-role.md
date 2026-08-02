---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html
---

# Assuming a role with AWS credentials to authenticate AWS SDKs and tools
<a name="access-assume-role"></a>

Assuming a role involves using a set of temporary security credentials to access AWS resources that you might not have access to otherwise. These temporary credentials consist of an access key ID, a secret access key, and a security token. To learn more about AWS Security Token Service (AWS STS) API requests, see [Actions](https://docs.aws.amazon.com/STS/latest/APIReference/API_Operations.html) in the *AWS Security Token Service API Reference*.

To set up your SDK or tool to assume a role, you must first create or identify a specific *role* to assume. IAM roles are uniquely identified by a role Amazon Resource Name ([ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)). Roles establish trust relationships with another entity. The trusted entity that uses the role might be an AWS service or another AWS account. To learn more about IAM roles, see [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the *IAM User Guide*.

After the IAM role is identified, if you are trusted by that role, you can configure your SDK or tool to use the permissions that are granted by the role.

**Note**
It is an AWS best practice to use Regional endpoints whenever possible and to configure your [AWS Region](feature-region.md).

## Assume an IAM role
<a name="credOrSourceAssumeRole"></a>

When assuming a role, AWS STS returns a set of temporary security credentials. These credentials are sourced from another profile or from the instance or container that your code is running in. Most commonly this type of assuming a role is used when you have AWS credentials for one account, but your application needs access to resources in another account.

### Step 1: Set up an IAM role
<a name="credOrSourceAssumeRole_step1"></a>

To set up your SDK or tool to assume a role, you must first create or identify a specific role to assume. IAM roles are uniquely identified using a role [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). Roles establish trust relationships with another entity, typically within your account or for cross-account access. To set this up, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

### Step 2: Configure the SDK or tool
<a name="credOrSourceAssumeRole_step2"></a>

Configure the SDK or tool to source credentials from `credential_source` or `source_profile`.

Use `credential_source` to source credentials from an Amazon ECS container, an Amazon EC2 instance, or from environment variables.

Use `source_profile` to source credentials from another profile. `source_profile` also supports role chaining, which is hierarchies of profiles where an assumed role is then used to assume another role.

When you specify this in a profile, the SDK or tool automatically makes the corresponding AWS STS [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API call for you. To retrieve and use temporary credentials by assuming a role, specify the following configuration values in the shared AWS `config` file. For more details on each of these settings, see the [Assume role credential provider settings](feature-assume-role-credentials.md#feature-assume-role-credentials-settings) section.
+ `role_arn` - From the IAM role you created in Step 1
+ Configure either `credential_source` or `source_profile`
+ (Optional) `duration_seconds`
+ (Optional) `external_id`
+ (Optional) `mfa_serial`
+ (Optional) `role_session_name`

The following examples show the configuration of both assume role options in a shared `config` file:

```
role_arn = arn:aws:iam::{{123456789012}}:role/{{my-role-name}}
credential_source = {{Ec2InstanceMetadata}}
```

```
[{{profile-with-user-that-can-assume-role}}]
aws_access_key_id={{AKIAIOSFODNN7EXAMPLE}}
aws_secret_access_key={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
aws_session_token={{IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}

[profile dev]
region = {{us-east-1}}
output = json
role_arn = arn:aws:iam::{{123456789012}}:role/{{my-role-name}}
source_profile = {{profile-with-user-that-can-assume-role}}
role_session_name = {{my_session}}
```

For details on all assume role credential provider settings, see [Assume role credential provider](feature-assume-role-credentials.md) in this guide.

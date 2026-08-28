---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/config-files.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Config files and named profiles
<a name="config-files"></a>

This page covers how the SDK reads shared AWS configuration files and how to use named profiles to manage different environments. It includes the following topics:
+ [Shared config files](#shared-config-files) explains which files the SDK reads and their format.
+ [Using named profiles](#using-named-profiles) shows how to switch between different configurations without changing your code.

## Shared config files
<a name="shared-config-files"></a>

The SDK searches the shared AWS configuration files when looking for configuration values. These are the same files used by the AWS CLI and other AWS SDKs, so the SDK automatically reads any settings you configured there. The SDK reads from two files:

| File | Default location | Env override |
| --- | --- | --- |
| Config | \~/.aws/config | AWS\_CONFIG\_FILE |
| Credentials | \~/.aws/credentials | AWS\_SHARED\_CREDENTIALS\_FILE |

Both files use INI-style format. The config file requires the `[profile ...]` prefix (except for `[default]`); the credentials file uses bare section names. You can create multiple profiles (logical groups of configuration) by creating sections named `[profile profile-name]`.

```
# ~/.aws/config
[default]
region = us-west-2
retry_mode = standard
max_attempts = 3

[profile production]
region = us-east-1
retry_mode = standard
max_attempts = 10
```

```
# ~/.aws/credentials
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

## Using named profiles
<a name="using-named-profiles"></a>

A named profile is a collection of settings stored in the shared AWS config file under a specific name. With profiles, you can maintain separate configurations for different environments (such as development, staging, and production) and switch between them without changing your code.

By default, the SDK uses the `[default]` profile. To use a different profile, pass the `profile` parameter to `resolve()`:

```
config = await AsyncBedrockRuntimeConfig.resolve(profile="production")
```

Or set the `AWS_PROFILE` environment variable:

```
export AWS_PROFILE=production
```

Example config file with multiple profiles:

```
# ~/.aws/config
[default]
region = us-east-1
retry_mode = standard

[profile production]
region = us-west-2
retry_mode = standard
max_attempts = 10

[profile staging]
region = eu-west-1
endpoint_url = https://staging.internal.example.com
```

If the requested profile doesn't exist in the config file, a `ProfileNotFoundError` is raised with a message indicating where the profile name came from:

```
config = await AsyncBedrockRuntimeConfig.resolve(profile="typo")
# raises ProfileNotFoundError: Profile 'typo' from profile argument was not found in config file.
```

```
export AWS_PROFILE=typo
```

```
config = await AsyncBedrockRuntimeConfig.resolve()
# raises ProfileNotFoundError: Profile 'typo' from AWS_PROFILE environment variable was not found in config file.
```

The implicit `"default"` profile is exempt from this check. If no config file exists, the SDK simply uses defaults and environment variables without error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

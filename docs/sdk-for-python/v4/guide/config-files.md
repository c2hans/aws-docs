---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/config-files.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Config files and named profiles

This page covers how the SDK reads shared AWS configuration files and how to use named profiles to manage different environments. It includes the following topics:
+ [Shared config files](#shared-config-files) explains which files the SDK reads and their format.
+ [Using named profiles](#using-named-profiles) shows how to switch between different configurations without changing your code.

## Shared config files
<a name="shared-config-files"></a>

The SDK reads configuration values from the shared AWS configuration files. The AWS CLI and other AWS SDKs use the same files, so the SDK reads settings that you already configured for those tools. The SDK reads the following two files:

| File | Default location | Env override |
| --- | --- | --- |
| Config | \~/.aws/config | AWS\_CONFIG\_FILE |
| Credentials | \~/.aws/credentials | AWS\_SHARED\_CREDENTIALS\_FILE |

Both files use INI format, with one section for each profile. A profile is a named group of settings. In the config file, the section name for a profile other than `[default]` starts with `profile`, for example `[profile production]`. In the credentials file, the section name is the profile name alone, for example `[production]`.

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

With named profiles, you can keep separate configurations for different environments, such as development, staging, and production. You can switch between them without changing your code.

By default, the SDK uses the `[default]` profile. To use a different profile, pass the `profile` argument to `resolve()`:

```
from aws_sdk_bedrock_runtime import BedrockRuntimeConfig

config = BedrockRuntimeConfig.resolve(profile="production")
```

Or set the `AWS_PROFILE` environment variable:

```
export AWS_PROFILE=production
```

If the requested profile doesn't exist in the config file, `resolve()` raises a `ProfileNotFoundError`. The error message says where the profile name came from:

```
config = BedrockRuntimeConfig.resolve(profile="typo")
# raises ProfileNotFoundError: Profile 'typo' from profile argument was not found in config file.
```

```
export AWS_PROFILE=typo
```

```
config = BedrockRuntimeConfig.resolve()
# raises ProfileNotFoundError: Profile 'typo' from AWS_PROFILE environment variable was not found in config file.
```

The SDK doesn't apply this check to the implicit `default` profile. If no config file exists, the SDK uses environment variables and defaults without an error.

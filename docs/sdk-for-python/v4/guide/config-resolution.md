---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/config-resolution.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration resolution
<a name="config-resolution"></a>

This page covers how the AWS SDK for Python v4 resolves configuration values. It includes the following topics:
+ [Explicit resolution](#explicit-resolution) shows how to resolve configuration before you create a client and pass it to the client.
+ [Resolution order](#resolution-order) describes the order of precedence that the SDK uses to determine where each value comes from.
+ [Provenance tracking](#provenance-tracking) explains how to inspect the source of any resolved value.
+ [Overriding values](#overriding-values) shows how to set values at resolution time or change them after resolution.
+ [Service-specific configuration](#service-specific-configuration) covers fields that have service-specific sources.

Configuration resolution has the following characteristics:
+ **Explicit or automatic resolution**. You resolve a configuration by calling `resolve()` on the service's config class. If you don't, the client resolves one the first time you call an operation.
+ **Source tracking**. Every resolved value records whether it came from an override, an environment variable, a config file, or a default. Call `source_of()` to check the source of a field.
+ **Early validation**. The SDK rejects invalid values during resolution, before you call an operation.

## Explicit resolution
<a name="explicit-resolution"></a>

To resolve configuration before you create a client, or to customize values, call `resolve()` and pass the config object to the client. You can't construct a config object directly. Calling `BedrockRuntimeConfig()` raises a `ConfigError`:

```
# This raises ConfigError
config = BedrockRuntimeConfig()

# This is correct
config = BedrockRuntimeConfig.resolve()
```

The following example resolves configuration with overrides and passes it to a client:

```
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    ContentBlockText,
    ConverseOutputMessage,
)
from smithy_aws_core.identity import EnvironmentCredentialsResolver

def main() -> None:
    config = BedrockRuntimeConfig.resolve(
        region="us-west-2",
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    )
    with BedrockRuntimeClient(config=config) as client:
        response = client.converse(
            model_id="global.amazon.nova-2-lite-v1:0",
            messages=[
                {"role": "user", "content": [{"text": "What is 2 + 2?"}]}
            ],
        )
        if isinstance(response.output, ConverseOutputMessage):
            for block in response.output.value.content:
                if isinstance(block, ContentBlockText):
                    print(block.value)

if __name__ == "__main__":
    main()
```

For an asynchronous client, import `AsyncBedrockRuntimeConfig` from `aws_sdk_bedrock_runtime` and use `await AsyncBedrockRuntimeConfig.resolve()`. It takes the same arguments. The rest of this page applies to both config classes.

## Resolution order
<a name="resolution-order"></a>

The SDK resolves each config field from the following sources, in order of precedence. The first source that provides a value wins.

1. Explicit override (passed to `resolve()`)

1. Environment variable

1. Config file profile

1. Default

### 1. Explicit override
<a name="resolution-explicit-override"></a>

Values that you pass to `resolve()` take precedence over all other sources. Use an override to set a value in code regardless of the environment or config files:

```
config = BedrockRuntimeConfig.resolve(
    region="us-west-2",
    max_attempts=10,
)
```

### 2. Environment variable
<a name="resolution-environment-variable"></a>

If you don't pass an override, the SDK checks the standard AWS environment variables.

```
export AWS_REGION=us-west-2
export AWS_RETRY_MODE=standard
export AWS_MAX_ATTEMPTS=5
export AWS_ENDPOINT_URL=https://endpoint.example.com
```

```
config = BedrockRuntimeConfig.resolve()
config.region   # "us-west-2"
```

### 3. Config file (profile)
<a name="resolution-config-file"></a>

If neither an override nor an environment variable provides a value, the SDK reads the shared AWS configuration files, `~/.aws/config` and `~/.aws/credentials`. It reads the active profile, which is `[default]` unless you set `AWS_PROFILE` or pass `profile=` to `resolve()`:

```
# ~/.aws/config
[default]
region = us-east-1
retry_mode = standard
max_attempts = 3
endpoint_url = https://endpoint.example.com
sdk_ua_app_id = my-application
```

```
config = BedrockRuntimeConfig.resolve()
config.region   # "us-east-1"
```

### 4. Default
<a name="resolution-default"></a>

If no other source provides a value, the SDK uses the field's default. Defaults vary by field:

```
# Empty environment, no config file
config = BedrockRuntimeConfig.resolve(region="us-east-1")
config.retry_mode  # "standard"
```

**Note**
`region` has no default. Resolution fails with `ConfigValidationError` if no source provides it.

## Provenance tracking
<a name="provenance-tracking"></a>

The SDK tracks the origin of every resolved configuration value. Call `source_of()` with a field name to find out whether its value came from an explicit override, an environment variable, a config file profile, or a default.

```
# With AWS_REGION=us-west-2 set in the environment
# and ~/.aws/config containing:
#   [default]
#   retry_mode = standard

config = BedrockRuntimeConfig.resolve()

config.source_of("region")       # env
config.source_of("retry_mode")   # profile
config.source_of("max_attempts") # default
```

`source_of()` returns one of the following sources:

| Source | Meaning |
| --- | --- |
| override | You passed the value to resolve() or set it after resolution. |
| env | The value came from an environment variable. |
| profile | The value came from the shared config or credentials file. |
| default | No source provided a value, so the field uses its default. |

Use `source_of()` to debug configuration, for example, to find out where a Region came from. If you write a library or plugin, you can also use it to check whether a user set a value explicitly.

## Overriding values
<a name="overriding-values"></a>

### At resolution time
<a name="override-at-resolution"></a>

Values that you pass to `resolve()` skip the other sources, as shown in [1. Explicit override](#resolution-explicit-override). The SDK validates them immediately. Passing an invalid value raises `ConfigValidationError`:

```
config = BedrockRuntimeConfig.resolve(region="bad!")
# raises ConfigValidationError: Invalid value for 'region': 'bad!'.
# Must be a valid AWS region identifier.
```

### After resolution
<a name="override-after-resolution"></a>

You can change fields after resolution. The source changes to `override`. The SDK validates the new value:

```
config = BedrockRuntimeConfig.resolve(region="us-east-1")
config.region = "us-east-2"
config.source_of("region")  # override
config.region = "bad!"      # raises ConfigValidationError
```

**Note**
You can't change the static credential fields (`aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`) after resolution.

## Service-specific configuration
<a name="service-specific-configuration"></a>

The `endpoint_uri` field also has service-specific sources, such as the `AWS_ENDPOINT_URL_BEDROCK_RUNTIME` environment variable. These sources set a custom endpoint for one service without affecting other services. For the order in which the SDK checks them, see [Set a custom endpoint](config-endpoints.md#endpoints-custom-endpoint).

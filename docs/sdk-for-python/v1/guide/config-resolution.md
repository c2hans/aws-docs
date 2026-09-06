---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/config-resolution.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration resolution
<a name="config-resolution"></a>

This page covers how the AWS SDK for Python resolves configuration values. It includes the following topics:
+ [Explicit resolution](#explicit-resolution) shows how to resolve configuration upfront and pass it to a client.
+ [Resolution order](#resolution-order) describes the precedence chain the SDK uses to determine where each value comes from.
+ [Provenance tracking](#provenance-tracking) explains how to inspect the source of any resolved value.
+ [Overriding values](#overriding-values) shows how to set values at resolution time or mutate them after resolution.
+ [Service-specific configuration](#service-specific-configuration) covers endpoint resolution for individual services.

The config resolution system guarantees the following:
+ **Async-first**. All resolution happens asynchronously, either explicitly via `resolve()` or automatically on the first operation call.
+ **Transparent sourcing**. Every resolved value tracks where it came from (environment, config file, override, or default), queryable at any time via `source_of()`.
+ **Early validation**. Invalid values are rejected immediately during resolution, not when the first API call is made. If your configuration is invalid, you will know it right away.

## Explicit resolution
<a name="explicit-resolution"></a>

If you want to resolve configuration upfront or customize values before creating a client, you can explicitly call `resolve()` and pass the resulting config object to the client. Config objects cannot be created directly. Calling `AsyncBedrockRuntimeConfig()` raises an error, and all construction must go through `resolve()`:

```
# This raises ConfigError
config = AsyncBedrockRuntimeConfig()

# This is the correct way
config = await AsyncBedrockRuntimeConfig.resolve()
```

You can also pass values directly to `resolve()` to override what would otherwise be resolved from environment variables or config files:

```
config = await AsyncBedrockRuntimeConfig.resolve(
    region="us-west-2",
    max_attempts=5,
)
```

The following example shows how to explicitly resolve configuration with an override and pass it to a client:

```
import asyncio
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import Message, ContentBlockText, ConverseInput
from smithy_aws_core.identity import EnvironmentCredentialsResolver

async def main():
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-west-2",
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver()
    )
    async with AsyncBedrockRuntimeClient(config=config) as client:

        response = await client.converse(
            ConverseInput(
                model_id="global.amazon.nova-2-lite-v1:0",
                messages=[Message(role="user", content=[ContentBlockText(value="What is 2 + 2?")])],
            )
        )

        print(response.output.value.content[0].value)

asyncio.run(main())
```

## Resolution order
<a name="resolution-order"></a>

Each config field is resolved using the following precedence. The first source that provides a value wins.

1. Explicit override (passed to `resolve()`)

1. Environment variable

1. Config file profile

1. Default

### 1. Explicit override
<a name="resolution-explicit-override"></a>

This is the highest-priority source. Values passed directly to `resolve()` always take precedence over all other sources. Use this when you want to hardcode a value regardless of what's in the environment or config files:

```
config = await AsyncBedrockRuntimeConfig.resolve(
    region="us-west-2",
    max_attempts=10,
)
```

### 2. Environment variable
<a name="resolution-environment-variable"></a>

If no explicit override is provided, the SDK checks for standard AWS environment variables.

```
export AWS_REGION=us-west-2
export AWS_RETRY_MODE=standard
export AWS_MAX_ATTEMPTS=5
export AWS_ENDPOINT_URL=https://custom.endpoint.com
```

```
config = await AsyncBedrockRuntimeConfig.resolve()
config.region   # "us-west-2"
```

### 3. Config file (profile)
<a name="resolution-config-file"></a>

If no override or environment variable is found, the SDK reads from the shared AWS configuration files. Values are read from `~/.aws/config` and `~/.aws/credentials`. The SDK reads the active profile (defaulting to `[default]` unless `AWS_PROFILE` is set or `profile=` is passed):

```
# ~/.aws/config
[default]
region = us-east-1
retry_mode = standard
max_attempts = 3
endpoint_url = https://my-endpoint.com
sdk_ua_app_id = my-application
```

```
config = await AsyncBedrockRuntimeConfig.resolve()
config.region   # "us-east-1"
```

### 4. Default
<a name="resolution-default"></a>

If no other source provides a value, the SDK falls back to built-in defaults. These are the lowest-priority source and vary per field:

```
# Empty environment, no config file
config = await AsyncBedrockRuntimeConfig.resolve(region="us-east-1")
config.retry_mode  # "standard"
```

**Note**
`region` has no default. Resolution fails with `ConfigValidationError` if no source provides it.

## Provenance tracking
<a name="provenance-tracking"></a>

The SDK tracks the origin of every resolved configuration value. You can call `source_of()` on any field to find out whether its value came from an explicit override, an environment variable, a config file profile, or a built-in default. This is useful for debugging configuration issues or understanding which source is providing a given value.

```
# With AWS_REGION=us-west-2 set in the environment
# and ~/.aws/config containing:
#   [default]
#   retry_mode = standard

config = await AsyncBedrockRuntimeConfig.resolve()

config.source_of("region")       # env
config.source_of("retry_mode")   # profile
config.source_of("max_attempts") # default
```

Available sources:

| Source | Meaning |
| --- | --- |
| override | Value was explicitly provided to resolve() or set after resolution |
| env | Value came from an environment variable |
| profile | Value came from the config/credentials file |
| default | No source provided the value; using built-in default |

This is useful for debugging ("where did this region come from?") and for libraries or plugins that need to know whether a user explicitly configured a value or it was auto-resolved.

## Overriding values
<a name="overriding-values"></a>

### At resolution time
<a name="override-at-resolution"></a>

Pass keyword arguments to `resolve()` to set values that skip the resolution chain entirely:

```
config = await AsyncBedrockRuntimeConfig.resolve(
    region="eu-west-1",
    max_attempts=5,
    retry_mode="standard",
)
```

These overrides are validated immediately. Passing an invalid value raises `ConfigValidationError`:

```
config = await AsyncBedrockRuntimeConfig.resolve(region="bad!")
# raises ConfigValidationError: Invalid value for 'region': 'bad!'.
# Must be a valid AWS region identifier.
```

### After resolution
<a name="override-after-resolution"></a>

Fields can be mutated after resolution. The source updates to `override` and validation runs on the new value:

```
config = await AsyncBedrockRuntimeConfig.resolve(region='us-east-1')
config.region = "us-east-2"
config.source_of("region")  # override
config.region = "bad!"      # raises ConfigValidationError
```

**Note**
Static credential fields (`aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`) cannot be modified after resolution.

## Service-specific configuration
<a name="service-specific-configuration"></a>

### Service-specific endpoint resolution
<a name="service-specific-endpoint-resolution"></a>

When resolving `endpoint_uri`, service-specific configs (like `AsyncBedrockRuntimeConfig`) use an extended precedence chain. With this extended precedence chain, you can set a custom endpoint for one service without affecting other services. The SDK checks the following sources in order, and the first one that provides a value wins:

1. `AWS_ENDPOINT_URL_BEDROCK_RUNTIME` (service-specific env var)

1. `AWS_ENDPOINT_URL` (global env var)

1. Services section in config file (service-specific config)

1. `endpoint_url` in profile (global config)

Example `~/.aws/config` with a services section:

```
[default]
region = us-east-1
services = my-services

[services my-services]
bedrock_runtime =
  endpoint_url = https://bedrock-runtime.us-east-1.amazonaws.com
s3 =
  endpoint_url = https://s3.custom.local
```

```
config = await AsyncBedrockRuntimeConfig.resolve()
config.endpoint_uri   # "https://bedrock-runtime.us-east-1.amazonaws.com" (resolved from the services section)
```

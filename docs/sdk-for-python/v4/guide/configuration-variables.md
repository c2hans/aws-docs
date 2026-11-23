---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/configuration-variables.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration variables

This page lists the configuration fields that the AWS SDK for Python v4 supports, with their default values and examples. Synchronous and asynchronous config classes have the same fields. Some fields exist only on clients for services that support the feature.

## account\_id\_endpoint\_mode
<a name="config-account-id-endpoint-mode"></a>

Controls whether the client sends requests to account-based endpoints. These endpoints include your AWS account ID in the host name, such as `https://111122223333.ddb.us-east-1.amazonaws.com`. Only clients for services that support account-based endpoints have this field. For more information, see [Account-based endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

| Detail | Value |
| --- | --- |
| Env var | AWS\_ACCOUNT\_ID\_ENDPOINT\_MODE |
| Profile key | account\_id\_endpoint\_mode |
| Default | "preferred" |
| Valid values | "preferred", "disabled", or "required". Values are case-insensitive. Other values raise ConfigValidationError. |

For how each mode chooses the endpoint, see [Use account-based endpoints](config-endpoints.md#endpoints-account-id).

```bash
# Environment variable
export AWS_ACCOUNT_ID_ENDPOINT_MODE=disabled
```

```ini
# Config file
[default]
account_id_endpoint_mode = disabled
```

```python
# Explicit override
from aws_sdk_dynamodb import DynamoDBConfig

config = DynamoDBConfig.resolve(region="us-east-1", account_id_endpoint_mode="disabled")
```

## aws\_credentials\_identity\_resolver
<a name="config-aws-credentials-identity-resolver"></a>

The identity resolver that supplies AWS credentials for signing requests. Set this field only to use a specific resolver instead of the default credential resolver chain. Use a resolver that matches the client mode. For more information, see [Credential providers](credential-providers.md).

| Detail | Value |
| --- | --- |
| Default | None (the client uses the default credential resolver chain). For more details, see [Default credential resolver chain](credential-providers.md#credproviders-default-chain). |

To provide static credentials directly, see [Configure static credentials](credential-providers.md#credproviders-static).

## endpoint\_resolver
<a name="config-endpoint-resolver"></a>

The resolver that determines the endpoint for each request. By default, each client uses a resolver that evaluates the service's endpoint rules. Set this field to bypass the rules or to use your own resolver. For more information, see [Endpoint configuration](config-endpoints.md).

| Detail | Value |
| --- | --- |
| Default | A resolver that evaluates the service's endpoint rules |

To send every request to `endpoint_uri` without evaluating the endpoint rules, use `StaticEndpointResolver`. To write your own resolver, see [Use a custom endpoint resolver](config-endpoints.md#endpoints-custom-resolver).

```python
# Explicit override
from aws_sdk_bedrock_runtime import BedrockRuntimeConfig
from smithy_core.endpoints import StaticEndpointResolver

config = BedrockRuntimeConfig.resolve(
    region="us-west-2",
    endpoint_uri="http://localhost:5678",
    endpoint_resolver=StaticEndpointResolver(),
)
```

## endpoint\_uri
<a name="config-endpoint-uri"></a>

A custom endpoint for requests, such as a local test server. The client passes this value to the service's endpoint rules, which use it as the endpoint.

| Detail | Value |
| --- | --- |
| Env var | AWS\_ENDPOINT\_URL\_<SERVICE\_ID> (service-specific), AWS\_ENDPOINT\_URL (global) |
| Profile key | endpoint\_url in the profile or in the service's entry in a services section |
| Default | None (the client resolves the endpoint from the service's endpoint rules) |

The endpoint rules don't allow FIPS or dual-stack endpoints with a custom endpoint. If you set `use_fips_endpoint` or `use_dualstack_endpoint` to `True` along with `endpoint_uri`, the request fails with an `EndpointResolutionError`. To use a custom endpoint without the endpoint rules, see [endpoint\_resolver](#config-endpoint-resolver).

The SDK also checks a service-specific environment variable and a service-specific config file setting for this field. For the order in which the SDK checks these sources, see [Set a custom endpoint](config-endpoints.md#endpoints-custom-endpoint).

```bash
# Global environment variable (applies to all services)
export AWS_ENDPOINT_URL=http://localhost:4566

# Service-specific environment variable
export AWS_ENDPOINT_URL_BEDROCK_RUNTIME=http://localhost:5000
```

```ini
# Config file
[default]
endpoint_url = http://localhost:4566
```

## interceptors
<a name="config-interceptors"></a>

A list of interceptors that the client calls at defined points during each request. Interceptors can inspect or modify requests and responses. Synchronous and asynchronous clients use the same interceptors. For more information, see [Customizing SDK behavior with plugins and interceptors](using-extensions.md).

| Detail | Value |
| --- | --- |
| Default | [] (empty list) |

## max\_attempts
<a name="config-max-attempts"></a>

The maximum number of attempts for a single request, including the initial attempt. For example, a value of 5 means that the SDK retries a request up to 4 times.

| Detail | Value |
| --- | --- |
| Env var | AWS\_MAX\_ATTEMPTS |
| Profile key | max\_attempts |
| Default | None (the retry strategy uses its own default of 3 attempts, or 4 attempts for DynamoDB clients) |
| Valid values | Positive integer (>= 1) |

```bash
# Environment variable
export AWS_MAX_ATTEMPTS=5
```

```ini
# Config file
[default]
max_attempts = 5
```

## region
<a name="config-region"></a>

The AWS Region to send requests to. The service's endpoint rules use the Region to choose the endpoint, including the partition, such as the China Regions or AWS GovCloud (US).

| Detail | Value |
| --- | --- |
| Env vars | AWS\_REGION, AWS\_DEFAULT\_REGION |
| Profile key | region |
| Default | None |
| Valid values | AWS Region identifiers like us-east-1, eu-west-1, ap-southeast-1 |

```bash
# Environment variable
export AWS_REGION=us-west-2
```

```ini
# Config file
[default]
region = us-west-2
```

```python
# Explicit override
from aws_sdk_bedrock_runtime import BedrockRuntimeConfig

config = BedrockRuntimeConfig.resolve(region="us-west-2")
```

## retry\_mode
<a name="config-retry-mode"></a>

A string that represents the type of retries the SDK performs. For more information, see [Retries](config-retries.md).

| Detail | Value |
| --- | --- |
| Env var | AWS\_RETRY\_MODE |
| Profile key | retry\_mode |
| Default | "standard" |
| Valid values | "standard" or "adaptive". A "legacy" value from an environment variable or config file maps to "standard" with a warning. |

Passing `"legacy"` to `resolve()` raises `ConfigValidationError`.

```bash
# Environment variable
export AWS_RETRY_MODE=standard
```

```ini
# Config file
[default]
retry_mode = standard
```

## retry\_strategy
<a name="config-retry-strategy"></a>

A retry strategy object. When you set this field, the SDK ignores `retry_mode` and `max_attempts`. Use it when you need full control over retry behavior. For an example, see [Configuring retries](config-retries.md#configuring-retries).

| Detail | Value |
| --- | --- |
| Default | None (the SDK builds a strategy from retry\_mode and max\_attempts) |

## sdk\_ua\_app\_id
<a name="config-sdk-ua-app-id"></a>

An identifier for your application. The SDK appends it to the `User-Agent` header so that you can identify your application's requests in AWS service logs.

| Detail | Value |
| --- | --- |
| Env var | AWS\_SDK\_UA\_APP\_ID |
| Profile key | sdk\_ua\_app\_id |
| Default | None |
| Valid values | Any string. The SDK logs a warning for values longer than 50 characters. |

```bash
# Environment variable
export AWS_SDK_UA_APP_ID=my-web-app
```

```ini
# Config file
[default]
sdk_ua_app_id = my-web-app
```

## transport
<a name="config-transport"></a>

The HTTP client that the SDK uses to send requests. Use an HTTP client that matches the client mode. For details, including the optional `AWSCRTHTTPClient` for asynchronous clients and custom HTTP clients, see [HTTP configuration](http-configuration.md).

| Detail | Value |
| --- | --- |
| Default | Urllib3HTTPClient from smithy\_http.urllib3 for synchronous clients, and AIOHTTPClient from smithy\_http.aio.aiohttp for asynchronous clients. |

## use\_dualstack\_endpoint
<a name="config-use-dualstack-endpoint"></a>

Whether to send requests to a dual-stack endpoint, which accepts both IPv4 and IPv6 traffic. Clients for services without dual-stack endpoints don't have this field. For more information, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

| Detail | Value |
| --- | --- |
| Env var | AWS\_USE\_DUALSTACK\_ENDPOINT |
| Profile key | use\_dualstack\_endpoint |
| Default | None (the endpoint rules treat it as False) |
| Valid values | True or False in code. In environment variables and config files, true or false in any case. Other values raise ConfigValidationError. |

If the Region's partition doesn't support dual-stack endpoints, or if you also set `endpoint_uri`, the request fails with an `EndpointResolutionError`.

```bash
# Environment variable
export AWS_USE_DUALSTACK_ENDPOINT=true
```

```ini
# Config file
[default]
use_dualstack_endpoint = true
```

```python
# Explicit override
from aws_sdk_dynamodb import DynamoDBConfig

config = DynamoDBConfig.resolve(region="us-east-1", use_dualstack_endpoint=True)
```

## use\_fips\_endpoint
<a name="config-use-fips-endpoint"></a>

Whether to send requests to a FIPS endpoint. FIPS endpoints use cryptographic modules validated under the Federal Information Processing Standard (FIPS) 140. Clients for services without FIPS endpoints don't have this field. For more information, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

| Detail | Value |
| --- | --- |
| Env var | AWS\_USE\_FIPS\_ENDPOINT |
| Profile key | use\_fips\_endpoint |
| Default | None (the endpoint rules treat it as False) |
| Valid values | True or False in code. In environment variables and config files, true or false in any case. Other values raise ConfigValidationError. |

If the Region's partition doesn't support FIPS endpoints, or if you also set `endpoint_uri`, the request fails with an `EndpointResolutionError`.

```bash
# Environment variable
export AWS_USE_FIPS_ENDPOINT=true
```

```ini
# Config file
[default]
use_fips_endpoint = true
```

```python
# Explicit override
from aws_sdk_dynamodb import DynamoDBConfig

config = DynamoDBConfig.resolve(region="us-east-1", use_fips_endpoint=True)
```

## user\_agent\_extra
<a name="config-user-agent-extra"></a>

An additional string appended to the `User-Agent` header.

| Detail | Value |
| --- | --- |
| Default | None |

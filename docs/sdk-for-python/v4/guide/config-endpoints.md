---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/config-endpoints.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Endpoint configuration

An *endpoint* is the URL that a service client sends requests to, such as `https://dynamodb.us-east-1.amazonaws.com`. Each service client in the AWS SDK for Python v4 includes the endpoint rules of its AWS service. For each request, the client evaluates these rules with the Region, the client configuration, and values from the operation input to determine the endpoint.

The rules handle the differences between services and Regions. For example, they select the correct domain in partitions such as the China Regions and AWS GovCloud (US). They also select FIPS and dual-stack endpoints when you turn them on. For services that support account-based endpoints, they route requests to those endpoints. Most applications only need to set a Region.

This page includes the following topics:
+ [Set a custom endpoint](#endpoints-custom-endpoint)
+ [Use FIPS and dual-stack endpoints](#endpoints-fips-dualstack)
+ [Use account-based endpoints](#endpoints-account-id)
+ [Amazon S3 endpoint settings](#endpoints-s3)
+ [Bypass the endpoint rules](#endpoints-static-resolver)
+ [Use a custom endpoint resolver](#endpoints-custom-resolver)

## Set a custom endpoint
<a name="endpoints-custom-endpoint"></a>

To send requests to a different endpoint, such as a local test server, set the `endpoint_uri` field. The following example sends DynamoDB requests to a local test server.

```python
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig

config = DynamoDBConfig.resolve(
    region="us-east-1",
    endpoint_uri="http://localhost:8000",
)
with DynamoDBClient(config=config) as client:
    response = client.list_tables()
    print(response.table_names)
```

You can also set the endpoint outside your code. If you don't pass `endpoint_uri` to `resolve()`, the SDK checks the following sources in order and uses the first value that it finds:

1. The service-specific environment variable `AWS_ENDPOINT_URL_<SERVICE_ID>`, for example `AWS_ENDPOINT_URL_DYNAMODB`.

1. The `AWS_ENDPOINT_URL` environment variable, which applies to all services.

1. The `endpoint_url` setting for the service in a `services` section of the shared `config` file.

1. The `endpoint_url` setting in the profile.

To form the service-specific names, the SDK takes the service ID and replaces spaces and hyphens with underscores. The environment variable uses the uppercase form, such as `AWS_ENDPOINT_URL_BEDROCK_RUNTIME`. The `services` section uses the lowercase form, such as `bedrock_runtime`.

For example, each of the following settings sends DynamoDB requests to a local endpoint. The first is an environment variable. The second is a `services` section in the shared config file.

```bash
export AWS_ENDPOINT_URL_DYNAMODB=http://localhost:8000
```

```ini
# ~/.aws/config
[default]
region = us-east-1
services = local-services

[services local-services]
dynamodb =
  endpoint_url = http://localhost:8000
```

For more information about these environment variables and settings, see [Service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html) in the *AWS SDKs and Tools Reference Guide*. The SDK doesn't support the `ignore_configured_endpoint_urls` setting or the `AWS_IGNORE_CONFIGURED_ENDPOINT_URLS` environment variable that the reference guide describes. For the field reference, see [endpoint\_uri](configuration-variables.md#config-endpoint-uri).

A custom endpoint still goes through the endpoint rules. For most services, the rules use your endpoint as it is. They reject combinations that they don't support, such as a custom endpoint with FIPS turned on. To skip the rules, see [Bypass the endpoint rules](#endpoints-static-resolver).

## Use FIPS and dual-stack endpoints
<a name="endpoints-fips-dualstack"></a>

Many AWS services offer FIPS endpoints and dual-stack endpoints. FIPS endpoints use cryptographic modules validated under the Federal Information Processing Standard (FIPS) 140. Dual-stack endpoints accept both IPv4 and IPv6 traffic. To use them, turn on the following settings. Both settings are off by default.

| Endpoint type | Config field | Environment variable | Shared `config` file setting |
| --- | --- | --- | --- |
| FIPS | use\_fips\_endpoint | AWS\_USE\_FIPS\_ENDPOINT | use\_fips\_endpoint |
| Dual-stack | use\_dualstack\_endpoint | AWS\_USE\_DUALSTACK\_ENDPOINT | use\_dualstack\_endpoint |

In environment variables and the shared `config` file, use `true` or `false` in any letter case. Any other value raises `ConfigValidationError` when the configuration is resolved.

```python
config = DynamoDBConfig.resolve(
    region="us-east-1",
    use_fips_endpoint=True,
    use_dualstack_endpoint=True,
)
```

```ini
# ~/.aws/config
[default]
region = us-east-1
use_fips_endpoint = true
use_dualstack_endpoint = true
```

Not every service offers FIPS or dual-stack endpoints in every Region. If the endpoint doesn't exist, the request fails. A service's config has these fields only if the service's endpoint rules support them. For example, the config of a service without dual-stack endpoints has no `use_dualstack_endpoint` field. For more information, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

## Use account-based endpoints
<a name="endpoints-account-id"></a>

Some services, such as Amazon DynamoDB and Amazon Kinesis, can route requests to an endpoint that includes your AWS account ID, such as `https://111122223333.ddb.us-east-1.amazonaws.com`. Clients for these services have an `account_id_endpoint_mode` field that controls this routing. It accepts the following values:

`preferred` (default)
The client uses an account-based endpoint when the credentials include an account ID. Otherwise, it uses the regional endpoint, such as `https://dynamodb.us-east-1.amazonaws.com`.

`disabled`
The client always uses the regional endpoint.

`required`
The client always uses an account-based endpoint. If the credentials don't include an account ID, the operation raises `EndpointResolutionError`.

Credentials include an account ID when their source provides one. For example, the SDK reads the account ID from the `AWS_ACCOUNT_ID` environment variable, from the `aws_account_id` setting in a profile, or from the `AccountId` value that a `credential_process` command returns.

You can also set the mode with the `AWS_ACCOUNT_ID_ENDPOINT_MODE` environment variable or the `account_id_endpoint_mode` setting in the shared `config` file. Values aren't case sensitive. Any other value raises `ConfigValidationError`.

```python
config = DynamoDBConfig.resolve(
    region="us-east-1",
    account_id_endpoint_mode="disabled",
)
```

Account-based endpoints change the host name that your application connects to. If your network allows only specific host names, for example through firewall or proxy rules, allow the account-based host names or set the mode to `disabled`. For more information, see [Account-based endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

## Amazon S3 endpoint settings
<a name="endpoints-s3"></a>

The Amazon S3 client has the following additional endpoint fields. When `use_arn_region` is unset, the client uses the Region in the ARN. The other fields are off by default.

| Config field | Description | Environment variable and shared `config` file setting |
| --- | --- | --- |
| force\_path\_style | Puts the bucket name in the URL path instead of the host name, for example https://s3.us-east-1.amazonaws.com/amzn-s3-demo-bucket/. | None. Set it in code. |
| use\_accelerate\_endpoint | Sends requests to Amazon S3 Transfer Acceleration endpoints. | None. Set it in code. |
| use\_arn\_region | Uses the Region in a resource ARN, such as an access point ARN, instead of the client's Region. Set it to False to reject ARNs whose Region differs from the client's Region. | AWS\_S3\_USE\_ARN\_REGION, s3\_use\_arn\_region |
| disable\_multi\_region\_access\_points | Turns off the client's use of Multi-Region Access Points. | AWS\_S3\_DISABLE\_MULTIREGION\_ACCESS\_POINTS, s3\_disable\_multiregion\_access\_points |
| disable\_s3\_express\_session\_auth | Turns off session authentication for S3 Express One Zone directory buckets. The client signs those requests with standard Signature Version 4 instead. | AWS\_S3\_DISABLE\_EXPRESS\_SESSION\_AUTH, s3\_disable\_express\_session\_auth |

Use `force_path_style` with a custom endpoint that doesn't support bucket names in the host name.

```python
from aws_sdk_s3 import S3Config

config = S3Config.resolve(
    region="us-east-1",
    endpoint_uri="http://localhost:9000",
    force_path_style=True,
)
```

For more information about the Amazon S3 client, see [Amazon S3](services-s3.md).

## Bypass the endpoint rules
<a name="endpoints-static-resolver"></a>

To send every request to `endpoint_uri` without evaluating the endpoint rules, set the `endpoint_resolver` field to a `StaticEndpointResolver` from `smithy_core.endpoints`. The client then ignores `region`, `use_fips_endpoint`, `use_dualstack_endpoint`, and `account_id_endpoint_mode` when it chooses the endpoint. `StaticEndpointResolver` works with both synchronous and asynchronous clients.

```python
from aws_sdk_dynamodb import DynamoDBConfig
from smithy_core.endpoints import StaticEndpointResolver

config = DynamoDBConfig.resolve(
    region="us-east-1",
    endpoint_uri="http://localhost:8000",
    endpoint_resolver=StaticEndpointResolver(),
)
```

If `endpoint_uri` isn't set, `StaticEndpointResolver` raises `EndpointResolutionError`.

## Use a custom endpoint resolver
<a name="endpoints-custom-resolver"></a>

To decide the endpoint yourself, implement an endpoint resolver and pass it as the `endpoint_resolver` field. The resolver's `resolve_endpoint` method receives an `EndpointResolverParams` object and returns an `Endpoint`. The parameters include the operation in `params.operation` and its input in `params.input`. A custom resolver replaces the endpoint rules. The client doesn't apply its endpoint settings to the endpoint that your resolver returns. These settings include `endpoint_uri`, `region`, `use_fips_endpoint`, `use_dualstack_endpoint`, and `account_id_endpoint_mode`.

Asynchronous clients also accept a synchronous resolver. Implement an asynchronous resolver only if `resolve_endpoint` must await other code.

------
#### [ Synchronous client ]

Implement `smithy_core.interfaces.EndpointResolver`.

```python
from typing import Any

from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
from smithy_core import URI
from smithy_core.endpoints import Endpoint, EndpointResolverParams
from smithy_core.interfaces import EndpointResolver

class CustomEndpointResolver(EndpointResolver):
    def resolve_endpoint(self, params: EndpointResolverParams[Any]) -> Endpoint:
        return Endpoint(uri=URI(host="dynamodb.example.com"))

def create_client() -> DynamoDBClient:
    config = DynamoDBConfig.resolve(
        region="us-east-1",
        endpoint_resolver=CustomEndpointResolver(),
    )
    return DynamoDBClient(config=config)
```

------
#### [ Asynchronous client ]

Implement `smithy_core.aio.interfaces.AsyncEndpointResolver`.

```python
from typing import Any

from aws_sdk_dynamodb import AsyncDynamoDBClient, AsyncDynamoDBConfig
from smithy_core import URI
from smithy_core.aio.interfaces import AsyncEndpointResolver
from smithy_core.endpoints import Endpoint, EndpointResolverParams

class CustomAsyncEndpointResolver(AsyncEndpointResolver):
    async def resolve_endpoint(
        self, params: EndpointResolverParams[Any]
    ) -> Endpoint:
        return Endpoint(uri=URI(host="dynamodb.example.com"))

async def create_client() -> AsyncDynamoDBClient:
    config = await AsyncDynamoDBConfig.resolve(
        region="us-east-1",
        endpoint_resolver=CustomAsyncEndpointResolver(),
    )
    return AsyncDynamoDBClient(config=config)
```

------

`URI` uses the `https` scheme by default. To set another scheme, a port, or a path, pass the `scheme`, `port`, or `path` arguments.

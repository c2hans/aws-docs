---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-extensions.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Customizing SDK behavior with plugins and interceptors
<a name="using-extensions"></a>

When you invoke an operation, the SDK processes it through its request pipeline. The pipeline automatically handles stages such as serialization, signing, sending an HTTP request, and deserialization. However, some applications need to observe or adjust that behavior. Plugins and interceptors customize different parts of this process.
+ A *plugin* is a setup function that receives the configuration object before the pipeline is created. Use a plugin to change configuration, such as the Region, or to register other custom configurations.
+ An *interceptor* is an object whose hook methods are called by the pipeline while an operation runs. Use an interceptor to observe or modify requests and responses at defined stages, such as before serialization, before transmission, or after execution.

This page shows how to write both, when to scope them to a client versus a single operation, and which lifecycle hooks to choose.

## Customizing configuration with plugins
<a name="using-extensions-plugins"></a>

To define a plugin, write a callable that accepts the generated service configuration and returns `None`. The SDK applies a client plugin directly to the client's configuration. It applies an operation plugin to a copy of that configuration, so the changes affect only that invocation.

The following example defines `use_region`, which returns a plugin that sets the Region in a DynamoDB `AsyncDynamoDBConfig`. Passing the plugin to the client establishes the Region used by that client.

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig, Plugin
from aws_sdk_dynamodb.models import ListTablesInput

def use_region(region: str) -> Plugin:
    def configure(config: AsyncDynamoDBConfig) -> None:
        config.region = region

    return configure

config = await AsyncDynamoDBConfig.resolve()
client = AsyncDynamoDBClient(
    config=config,
    plugins=[use_region("us-east-1")],
)
```

The following call passes another `use_region` plugin to `list_tables`. The SDK applies it to the operation's copy of the configuration, changing the Region only for this call. Later calls continue to use the client's configured Region.

```
async with client:
    response = await client.list_tables(
        input=ListTablesInput(limit=25),
        plugins=[use_region("us-west-2")],
    )
```

## Hooking into request processing with interceptors
<a name="using-extensions-interceptors"></a>

An interceptor implements hook methods that the request pipeline calls at defined stages. The following interceptor logs when an SDK operation starts and whether the completed execution succeeded or failed. It supports every operation because it doesn't depend on a service-specific input or output type.

```
import logging
from typing import Any

from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from smithy_core.interceptors import (
    InputContext,
    Interceptor,
    OutputContext,
)

logger = logging.getLogger(__name__)

class ExecutionLogger(Interceptor[Any, Any, Any, Any]):
    def read_before_execution(
        self, context: InputContext[Any]
    ) -> None:
        logger.info("Starting SDK operation")

    def read_after_execution(
        self, context: OutputContext[Any, Any, Any, Any]
    ) -> None:
        if isinstance(context.response, Exception):
            logger.warning("SDK operation failed")
        else:
            logger.info("SDK operation completed")
```

### Registering an interceptor on a client
<a name="using-extensions-interceptors-client"></a>

To run an interceptor for every operation invoked by a client, include the interceptor when you resolve the configuration. The following example doesn't define or pass a plugin.

```
config = await AsyncDynamoDBConfig.resolve(
    region="us-east-1",
    interceptors=[ExecutionLogger()],
)
async with AsyncDynamoDBClient(config=config) as logged_client:
    response = await logged_client.list_tables(
        input=ListTablesInput(limit=25)
    )
```

The client copies this configuration for each operation, so each operation pipeline includes the registered interceptor. An interceptor registered at this scope must support every operation that the client can invoke.

### Registering an interceptor for one operation
<a name="using-extensions-interceptors-operation"></a>

An operation doesn't accept an `interceptors` argument. To register an interceptor for one invocation, define an operation plugin that adds it to the copied configuration used by that invocation.

```
def add_execution_logger(config: AsyncDynamoDBConfig) -> None:
    config.interceptors.append(ExecutionLogger())

response = await client.list_tables(
    input=ListTablesInput(limit=25),
    plugins=[add_execution_logger],
)
```

In this example, `add_execution_logger` is the plugin and `ExecutionLogger` is the interceptor. The plugin runs before the pipeline is created and registers the interceptor in the operation's configuration copy. The interceptor then runs while that pipeline processes this call. Later calls that don't receive the plugin don't use this interceptor.

## Choosing lifecycle hooks carefully
<a name="using-extensions-hooks"></a>

The `Interceptor` base class in the `smithy_core.interceptors` module defines the full set of hook methods; see the [interceptors module](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-core/src/smithy_core/interceptors.py) on GitHub. Each hook runs at one stage of the operation:
+ **Execution:** `read_before_execution`, `modify_before_completion`, and `read_after_execution`
+ **Serialization:** `modify_before_serialization`, `read_before_serialization`, and `read_after_serialization`
+ **Retries and attempts:** `modify_before_retry_loop`, `read_before_attempt`, `modify_before_attempt_completion`, and `read_after_attempt`
+ **Signing:** `modify_before_signing`, `read_before_signing`, and `read_after_signing`
+ **Transmission:** `modify_before_transmit`, `read_before_transmit`, and `read_after_transmit`
+ **Deserialization:** `modify_before_deserialization`, `read_before_deserialization`, and `read_after_deserialization`

Follow these rules when choosing a hook:
+ `read_*` hooks observe their context and must not modify request or response objects.
+ `modify_*` hooks return a replacement request, response, transport request, or transport response of the same type.
+ Execution hooks run once for an operation invocation. Attempt hooks can run more than once when the retry strategy makes another attempt.
+ Interceptors run in configuration order. An exception raised by an interceptor can cause the operation to fail.

Do not log credentials, authorization headers, or sensitive request and response data from an interceptor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

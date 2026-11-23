---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-extensions.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Customizing SDK behavior with plugins and interceptors

When you invoke an operation, the SDK processes it through its request pipeline. The pipeline handles stages such as serialization, signing, sending an HTTP request, and deserialization. Some applications need to observe or adjust that behavior. Plugins and interceptors customize different parts of this process.
+ A *plugin* is a setup function that receives the configuration object before the SDK creates the pipeline. Use a plugin to change configuration, such as the Region, or to register other custom configurations.
+ An *interceptor* is an object with hook methods that the pipeline calls while an operation runs. Use an interceptor to observe or modify requests and responses at defined stages, such as before serialization, before transmission, or after execution.

Synchronous and asynchronous clients support the same kinds of plugins and interceptors. Interceptor hooks are synchronous methods, so one interceptor class works with both client types. The examples on this page use a synchronous client.

This page shows how to write both, when to scope them to a client or to a single operation, and which lifecycle hooks to choose.

## Customizing configuration with plugins
<a name="using-extensions-plugins"></a>

To define a plugin, write a callable that accepts the generated service configuration and returns `None`. The SDK applies a client plugin once, when it sets up the client's configuration. It applies an operation plugin to a copy of the client's configuration, so the changes affect only that invocation.

The following example defines `use_region`, which returns a plugin that sets the Region in a `DynamoDBConfig`. Passing the plugin to the client sets the Region that the client uses.

```python
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
from aws_sdk_dynamodb.config import Plugin

def use_region(region: str) -> Plugin:
    def configure(config: DynamoDBConfig) -> None:
        config.region = region

    return configure

config = DynamoDBConfig.resolve(region="eu-west-1")
client = DynamoDBClient(
    config=config,
    plugins=[use_region("us-east-1")],
)
```

For an asynchronous client, write the plugin for `AsyncDynamoDBConfig` and import `Plugin` from `aws_sdk_dynamodb.aio.config`.

Every operation accepts a `plugins` keyword argument. The following call passes another `use_region` plugin to `list_tables`. The SDK applies it to the operation's copy of the configuration, which changes the Region only for this call. Later calls continue to use the client's configured Region.

```python
with client:
    response = client.list_tables(
        limit=25,
        plugins=[use_region("us-west-2")],
    )
```

## Hooking into request processing with interceptors
<a name="using-extensions-interceptors"></a>

An interceptor implements hook methods that the request pipeline calls at defined stages. The following interceptor logs when an SDK operation starts and whether the completed execution succeeded or failed. It supports every operation because it doesn't depend on a service-specific input or output type.

```python
import logging
from typing import Any

from aws_sdk_dynamodb import DynamoDBConfig
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

An asynchronous client calls the same hook methods on its event loop. A hook that blocks, for example by making a network call, also blocks the event loop.

### Registering an interceptor on a client
<a name="using-extensions-interceptors-client"></a>

To run an interceptor for every operation invoked by a client, include the interceptor when you resolve the configuration.

```python
config = DynamoDBConfig.resolve(
    region="us-east-1",
    interceptors=[ExecutionLogger()],
)
with DynamoDBClient(config=config) as logged_client:
    response = logged_client.list_tables(limit=25)
```

Every operation that the client invokes runs the registered interceptor, so an interceptor registered at this scope must support every operation that the client can invoke.

### Registering an interceptor for one operation
<a name="using-extensions-interceptors-operation"></a>

An operation doesn't accept an `interceptors` argument. To register an interceptor for one invocation, define an operation plugin that adds the interceptor to the copied configuration that the invocation uses.

```python
def add_execution_logger(config: DynamoDBConfig) -> None:
    config.interceptors.append(ExecutionLogger())

config = DynamoDBConfig.resolve(region="us-east-1")
with DynamoDBClient(config=config) as client:
    response = client.list_tables(
        limit=25,
        plugins=[add_execution_logger],
    )
```

In this example, `add_execution_logger` is the plugin and `ExecutionLogger` is the interceptor. The plugin runs before the SDK creates the pipeline and registers the interceptor in the operation's configuration copy. The interceptor then runs while that pipeline processes this call. Later calls that don't receive the plugin don't use this interceptor.

## Choosing lifecycle hooks carefully
<a name="using-extensions-hooks"></a>

The `Interceptor` base class in the `smithy_core.interceptors` module defines every hook method. For the documentation of each hook, see the [interceptors module](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-core/src/smithy_core/interceptors.py) on GitHub. The following table groups the hooks by the stage of the operation in which they run.

| Stage | Hooks |
| --- | --- |
| Execution | read\_before\_execution, modify\_before\_completion, and read\_after\_execution |
| Serialization | modify\_before\_serialization, read\_before\_serialization, and read\_after\_serialization |
| Retries and attempts | modify\_before\_retry\_loop, read\_before\_attempt, modify\_before\_attempt\_completion, and read\_after\_attempt |
| Signing | modify\_before\_signing, read\_before\_signing, and read\_after\_signing |
| Transmission | modify\_before\_transmit, read\_before\_transmit, and read\_after\_transmit |
| Deserialization | modify\_before\_deserialization, read\_before\_deserialization, and read\_after\_deserialization |

Follow these rules when you choose a hook:
+ `read_*` hooks observe their context and must not modify request or response objects.
+ `modify_*` hooks return a replacement request, response, transport request, or transport response of the same type.
+ Execution hooks run once for an operation invocation. Attempt hooks can run more than once when the retry strategy makes another attempt.
+ Interceptors run in configuration order. An exception raised by an interceptor can cause the operation to fail.

Do not log credentials, authorization headers, or sensitive request and response data from an interceptor.

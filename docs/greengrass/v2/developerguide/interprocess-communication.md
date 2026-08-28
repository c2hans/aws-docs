---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html
---

# Use the AWS IoT Device SDK to communicate with the Greengrass nucleus, other components, and AWS IoT Core
<a name="interprocess-communication"></a>

Components running on your core device can use the AWS IoT Greengrass Core interprocess communication (IPC) library in the AWS IoT Device SDK to communicate with the AWS IoT Greengrass nucleus and other Greengrass components. To develop and run custom components that use IPC, you must use the AWS IoT Device SDK to connect to the AWS IoT Greengrass Core IPC service and perform IPC operations.

The IPC interface supports two types of operations:
+ **Request/response**

  Components send a request to the IPC service and receive a response that contains the result of the request.
+ **Subscription**

  Components send a subscription request to the IPC service and expect a stream of event messages in response. Components provide a subscription handler that handles event messages, errors, and stream closure. The AWS IoT Device SDK includes a handler interface with the correct response and event types for each IPC operation. For more information, see [Subscribe to IPC event streams](#ipc-subscribe-operations).

**Topics**
+ [IPC client versions](#ipc-client-versions)
+ [Supported SDKs for interprocess communication](#ipc-requirements)
+ [Connect to the AWS IoT Greengrass Core IPC service](#ipc-service-connect)
+ [Authorize components to perform IPC operations](#ipc-authorization-policies)
+ [Subscribe to IPC event streams](#ipc-subscribe-operations)
+ [IPC best practices](#ipc-best-practices)
+ [Publish/subscribe local messages](ipc-publish-subscribe.md)
+ [Publish/subscribe AWS IoT Core MQTT messages](ipc-iot-core-mqtt.md)
+ [Interact with component lifecycle](ipc-component-lifecycle.md)
+ [Interact with component configuration](ipc-component-configuration.md)
+ [Retrieve secret values](ipc-secret-manager.md)
+ [Interact with local shadows](ipc-local-shadows.md)
+ [Manage local deployments and components](ipc-local-deployments-components.md)
+ [Authenticate and authorize client devices](ipc-client-device-auth.md)

## IPC client versions
<a name="ipc-client-versions"></a>

In later versions of the Java and Python SDKs, AWS IoT Greengrass provides an improved version of the IPC client, called IPC client V2. IPC client V2:
+ Reduces the amount of code that you need to write to use IPC operations and helps avoid common errors that can occur with IPC client V1.
+ Calls subscription handler callbacks in a separate thread, so you can now run blocking code, including additional IPC function calls, in subscription handler callbacks. IPC client V1 uses the same thread to communicate with the IPC server and call subscription handler callbacks.
+ Lets you call subscription operations using Lambda expressions (Java) or functions (Python). IPC client V1 requires you to define subscription handler classes.
+ Provides synchronous and asynchronous versions of each IPC operation. IPC client V1 provides only asynchronous versions of each operation.

We recommend that you use IPC client V2 to take advantage of these improvements. However, many examples in this documentation and in some online content demonstrate only how to use IPC client V1. You can use the following examples and tutorials to see sample components that use IPC client V2:
+ [PublishToTopic examples](ipc-publish-subscribe.md#ipc-operation-publishtotopic-examples)
+ [SubscribeToTopic examples](ipc-publish-subscribe.md#ipc-operation-subscribetotopic-examples)
+ [Tutorial: Develop a Greengrass component that defers component updates](defer-component-updates-tutorial.md)
+ [Tutorial: Interact with local IoT devices over MQTT](client-devices-tutorial.md)

Currently, the AWS IoT Device SDK for C\+\+ v2 supports only IPC client V1.

For components written in C, C\+\+, or Rust, the [AWS IoT Greengrass Component SDK](https://github.com/aws-greengrass/aws-greengrass-component-sdk) provides lightweight bindings for a subset of Greengrass IPC operations. Its small footprint also makes it suitable for resource-constrained devices. You can also use the AWS IoT Device SDK for C\+\+ v2, which supports IPC client V1. For more information, see [Use AWS IoT Greengrass Component SDK (C, C\+\+, Rust)](#ipc-component-sdk).

## Supported SDKs for interprocess communication
<a name="ipc-requirements"></a>

The AWS IoT Greengrass Core IPC libraries are included in the following SDKs.

| SDK | Minimum version | Usage |
| --- | --- | --- |
| [AWS IoT Greengrass Component SDK](https://github.com/aws-greengrass/aws-greengrass-component-sdk) (C, C\+\+, Rust) | v1.0.0 | See [Use AWS IoT Greengrass Component SDK (C, C\+\+, Rust)](#ipc-component-sdk) |
| [AWS IoT Device SDK for Java v2](https://github.com/aws/aws-iot-device-sdk-java-v2) | v1.6.0 | See [Use AWS IoT Device SDK for Java v2 (IPC client V2)](#ipc-java-v2) |
| [AWS IoT Device SDK for Python v2](https://github.com/aws/aws-iot-device-sdk-python-v2) | v1.9.0 | See [Use AWS IoT Device SDK for Python v2 (IPC client V2)](#ipc-python-v2) |
| [AWS IoT Device SDK for C\+\+ v2](https://github.com/aws/aws-iot-device-sdk-cpp-v2) | v1.17.0 | See [Use AWS IoT Device SDK for C\+\+ v2](#ipc-cpp) |
| [AWS IoT Device SDK for JavaScript v2](https://github.com/aws/aws-iot-device-sdk-js-v2) | v1.12.0 | See [Use AWS IoT Device SDK for JavaScript v2 (IPC client V1)](#ipc-nodejs) |

## Connect to the AWS IoT Greengrass Core IPC service
<a name="ipc-service-connect"></a>

To use interprocess communication in your custom component, you must create a connection to an IPC server socket that the AWS IoT Greengrass Core software runs. Complete the following tasks to download and use the AWS IoT Device SDK or the AWS IoT Greengrass Component SDK in the language of your choice.

### Use AWS IoT Greengrass Component SDK (C, C\+\+, Rust)
<a name="ipc-component-sdk"></a>

The [AWS IoT Greengrass Component SDK](https://github.com/aws-greengrass/aws-greengrass-component-sdk) provides C, C\+\+, and Rust bindings for Greengrass IPC operations. Its small footprint also makes it suitable for resource-constrained devices.

**To use the AWS IoT Greengrass Component SDK**

1. Download or clone the [AWS IoT Greengrass Component SDK](https://github.com/aws-greengrass/aws-greengrass-component-sdk) (v1.0.0 or later).

1. Follow the installation instructions in the [README](https://github.com/aws-greengrass/aws-greengrass-component-sdk#getting-started) for your language (C, C\+\+, or Rust).

1. Use the IPC client in your component code. For examples, see the IPC operation pages in this guide, which include AWS IoT Greengrass Component SDK code examples in the C, C\+\+ (Component SDK), and Rust tabs.

### Use AWS IoT Device SDK for Java v2 (IPC client V2)
<a name="ipc-java-v2"></a>

**To use the AWS IoT Device SDK for Java v2 (IPC client V2)**

1. Download the [AWS IoT Device SDK for Java v2](https://github.com/aws/aws-iot-device-sdk-java-v2) (v1.6.0 or later).

1. <a name="use-ipc-java-component-install-step"></a>Do one of the following to run your custom code in your component:
   + Build your component as a JAR file that includes the AWS IoT Device SDK, and run this JAR file in your component recipe.
   + Define the AWS IoT Device SDK JAR as a component artifact, and add that artifact to the classpath when you run your application in your component recipe.

1. Use the following code to create the IPC client.

   ```
   try (GreengrassCoreIPCClientV2 ipcClient = GreengrassCoreIPCClientV2.builder().build()) {
       // Use client.
   } catch (Exception e) {
       LOGGER.log(Level.SEVERE, "Exception occurred when using IPC.", e);
       System.exit(1);
   }
   ```

### Use AWS IoT Device SDK for Python v2 (IPC client V2)
<a name="ipc-python-v2"></a>

**To use the AWS IoT Device SDK for Python v2 (IPC client V2)**

1. Download the [AWS IoT Device SDK for Python](https://github.com/aws/aws-iot-device-sdk-python-v2) (v1.9.0 or later).

1. <a name="use-ipc-python-component-install-step"></a>Add the SDK's [installation steps](https://github.com/aws/aws-iot-device-sdk-python-v2#installation) to the install lifecycle in your component's recipe.

1. Create a connection to the AWS IoT Greengrass Core IPC service. Use the following code to create the IPC client.

   ```
   from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

   try:
       ipc_client = GreengrassCoreIPCClientV2()
       # Use IPC client.
   except Exception:
       print('Exception occurred when using IPC.', file=sys.stderr)
       traceback.print_exc()
       exit(1)
   ```

### Use AWS IoT Device SDK for C\+\+ v2
<a name="ipc-cpp"></a>

<a name="iot-device-sdk-cpp-v2-build-requirements-intro"></a>To build the AWS IoT Device SDK v2 for C\+\+, a device must have the following tools:<a name="iot-device-sdk-cpp-v2-build-requirements"></a>
+ C\+\+ 11 or later
+ CMake 3.1 or later
+ One of the following compilers:
  + GCC 4.8 or later
  + Clang 3.9 or later
  + MSVC 2015 or later

**To use the AWS IoT Device SDK for C\+\+ v2**

1. Download the [AWS IoT Device SDK for C\+\+ v2](https://github.com/aws/aws-iot-device-sdk-cpp-v2) (v1.17.0 or later).

1. Follow the [installation instructions in the README](https://github.com/aws/aws-iot-device-sdk-cpp-v2#Installation) to build the AWS IoT Device SDK for C\+\+ v2 from source.

1. In your C\+\+ build tool, link the Greengrass IPC library, `AWS::GreengrassIpc-cpp`, that you built in the previous step. The following `CMakeLists.txt` example links the Greengrass IPC library to a project that you build with CMake.

   ```
   cmake_minimum_required(VERSION 3.1)
   project (greengrassv2_pubsub_subscriber)

   file(GLOB MAIN_SRC
           "*.h"
           "*.cpp"
           )
   add_executable(${PROJECT_NAME} ${MAIN_SRC})

   set_target_properties(${PROJECT_NAME} PROPERTIES
           LINKER_LANGUAGE CXX
           CXX_STANDARD 11)
   find_package(aws-crt-cpp PATHS ~/sdk-cpp-workspace/build)
   find_package(EventstreamRpc-cpp PATHS ~/sdk-cpp-workspace/build)
   find_package(GreengrassIpc-cpp PATHS ~/sdk-cpp-workspace/build)
   target_link_libraries(${PROJECT_NAME} AWS::GreengrassIpc-cpp)
   ```

1. In your component code, create a connection to the AWS IoT Greengrass Core IPC service to create an IPC client (`Aws::Greengrass::GreengrassCoreIpcClient`). You must define an IPC connection lifecycle handler that handles IPC connection, disconnection, and error events. The following example creates an IPC client and an IPC connection lifecycle handler that prints when the IPC client connects, disconnects, and encounters errors.

   ```
   #include <iostream>

   #include <aws/crt/Api.h>
   #include <aws/greengrass/GreengrassCoreIpcClient.h>

   using namespace Aws::Crt;
   using namespace Aws::Greengrass;

   class IpcClientLifecycleHandler : public ConnectionLifecycleHandler {
       void OnConnectCallback() override {
           std::cout << "OnConnectCallback" << std::endl;
       }

       void OnDisconnectCallback(RpcError error) override {
           std::cout << "OnDisconnectCallback: " << error.StatusToString() << std::endl;
           exit(-1);
       }

       bool OnErrorCallback(RpcError error) override {
           std::cout << "OnErrorCallback: " << error.StatusToString() << std::endl;
           return true;
       }
   };

   int main() {
       // Create the IPC client.
       ApiHandle apiHandle(g_allocator);
       Io::EventLoopGroup eventLoopGroup(1);
       Io::DefaultHostResolver socketResolver(eventLoopGroup, 64, 30);
       Io::ClientBootstrap bootstrap(eventLoopGroup, socketResolver);
       IpcClientLifecycleHandler ipcLifecycleHandler;
       GreengrassCoreIpcClient ipcClient(bootstrap);
       auto connectionStatus = ipcClient.Connect(ipcLifecycleHandler).get();
       if (!connectionStatus) {
           std::cerr << "Failed to establish IPC connection: " << connectionStatus.StatusToString() << std::endl;
           exit(-1);
       }

       // Use the IPC client to create an operation request.

       // Activate the operation request.
       auto activate = operation.Activate(request, nullptr);
       activate.wait();

       // Wait for Greengrass Core to respond to the request.
       auto responseFuture = operation.GetResult();
       if (responseFuture.wait_for(std::chrono::seconds(timeout)) == std::future_status::timeout) {
           std::cerr << "Operation timed out while waiting for response from Greengrass Core." << std::endl;
           exit(-1);
       }

       // Check the result of the request.
       auto response = responseFuture.get();
       if (response) {
           std::cout << "Successfully published to topic: " << topic << std::endl;
       } else {
           // An error occurred.
           std::cout << "Failed to publish to topic: " << topic << std::endl;
           auto errorType = response.GetResultType();
           if (errorType == OPERATION_ERROR) {
               auto *error = response.GetOperationError();
               std::cout << "Operation error: " << error->GetMessage().value() << std::endl;
           } else {
               std::cout << "RPC error: " << response.GetRpcError() << std::endl;
           }
           exit(-1);
       }

       return 0;
   }
   ```

1. To run your custom code in your component, build your code as a binary artifact, and run the binary artifact in your component recipe. Set the artifact's `Execute` permission to `OWNER` to enable the AWS IoT Greengrass Core software to run the binary artifact.

   Your component recipe's `Manifests` section might look similar to the following example.

------
#### [ JSON ]

   ```
   {
     {{...}}
     "Manifests": [
       {
         "Lifecycle": {
           "Run": "{artifacts:path}/greengrassv2_pubsub_subscriber"
         },
         "Artifacts": [
           {
             "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.PubSubSubscriberCpp/1.0.0/greengrassv2_pubsub_subscriber",
             "Permission": {
               "Execute": "OWNER"
             }
           }
         ]
       }
     ]
   }
   ```

------
#### [ YAML ]

   ```
   {{...}}
   Manifests:
     - Lifecycle:
         Run: {artifacts:path}/greengrassv2_pubsub_subscriber
       Artifacts:
         - URI: s3://amzn-s3-demo-bucket/artifacts/com.example.PubSubSubscriberCpp/1.0.0/greengrassv2_pubsub_subscriber
           Permission:
             Execute: OWNER
   ```

------

### Use AWS IoT Device SDK for JavaScript v2 (IPC client V1)
<a name="ipc-nodejs"></a>

<a name="iot-device-sdk-nodejs-build-requirements-intro"></a>To build the AWS IoT Device SDK for JavaScript v2 for use with NodeJS, a device must have the following tools:<a name="iot-device-sdk-nodejs-build-requirements"></a>
+ NodeJS 10.0 or later
  + Run `node -v` to check the Node version.
+ CMake 3.1 or later

**To use the AWS IoT Device SDK for JavaScript v2 (IPC client V1)**

1. Download the [AWS IoT Device SDK for JavaScript v2](https://github.com/aws/aws-iot-device-sdk-js-v2) (v1.12.10 or later).

1. Follow the [installation instructions in the README](https://github.com/aws/aws-iot-device-sdk-js-v2/tree/v1.12.1#installation) to build the AWS IoT Device SDK for JavaScript v2 from source.

1. Create a connection to the AWS IoT Greengrass Core IPC service. Complete the following steps to create the IPC client and establish a connection.

1. Use the following code to create the IPC client.

   ```
   import * as greengrascoreipc from 'aws-iot-device-sdk-v2';

   let client = greengrascoreipc.createClient();
   ```

1. Use the following code to establish a connection from your component to the Greengrass nucleus.

   ```
   await client.connect();
   ```

## Authorize components to perform IPC operations
<a name="ipc-authorization-policies"></a>

To allow your custom components to use some IPC operations, you must define *authorization policies* that allow the component to perform the operation on certain resources. Each authorization policy defines a list of operations and a list of resources that the policy allows. For example, the publish/subscribe messaging IPC service defines publish and subscribe operations for topic resources. You can use the `*` wildcard to allow access to all operations or all resources.

You define authorization policies with the `accessControl` configuration parameter, which you can set in the component recipe or when you deploy the component. The `accessControl` object maps IPC service identifiers to lists of authorization policies. You can define multiple authorization policies for each IPC service to control access. Each authorization policy has a policy ID, which must be unique among all components.

**Tip**
To create unique policy IDs, you can combine the component name, IPC service name, and a counter. For example, a component named `com.example.HelloWorld` might define two publish/subscribe authorization policies with the following IDs:
`com.example.HelloWorld:pubsub:1`
`com.example.HelloWorld:pubsub:2`

Authorization policies use the following format. This object is the `accessControl` configuration parameter.

------
#### [ JSON ]

```
{
  "{{IPC service identifier}}": {
    "{{policyId}}": {
      "policyDescription": "{{description}}",
      "operations": [
        "{{operation1}}",
        "{{operation2}}"
      ],
      "resources": [
        "{{resource1}}",
        "{{resource2}}"
      ]
    }
  }
}
```

------
#### [ YAML ]

```
{{IPC service identifier}}:
  {{policyId}}:
    policyDescription: {{description}}
    operations:
      - {{operation1}}
      - {{operation2}}
    resources:
      - {{resource1}}
      - {{resource2}}
```

------

### Wildcards in authorization policies
<a name="ipc-authorization-policy-wildcards"></a>

You can use the `*` wildcard in the `resources` element of IPC authorization policies to allow access to multiple resources in a single authorization policy.
+ In all versions of the [Greengrass nucleus](greengrass-nucleus-component.md), you can specify a single `*` character as a resource to allow access to all resources.
+ In [Greengrass nucleus](greengrass-nucleus-component.md) v2.6.0 and later, you can specify the `*` character in a resource to match any combination of characters. For example, you can specify `factory/1/devices/Thermostat*/status` to allow access to a status topic for all thermostat devices in a factory, where each device's name begins with `Thermostat`.

When you define authorization policies for the AWS IoT Core MQTT IPC service, you can also use MQTT wildcards (`+` and `#`) to match multiple resources. For more information, see [MQTT wildcards in AWS IoT Core MQTT IPC authorization policies](ipc-iot-core-mqtt.md#ipc-iot-core-mqtt-authorization-mqtt-wildcards).

### Recipe variables in authorization policies
<a name="ipc-authorization-policy-recipe-variables"></a>

If you use [Greengrass nucleus](greengrass-nucleus-component.md) v2.6.0 or later, and you set the Greengrass nucleus' [interpolateComponentConfiguration](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration-interpolate-component-configuration) configuration option to `true`, you can use the `{iot:thingName}` [recipe variable](component-recipe-reference.md#recipe-variables) in authorization policies. When you need an authorization policy that includes the core device's name, such as for MQTT topics or device shadows, you can use this recipe variable to configure a single authorization policy for a group of core devices. For example, you can allow a component access to the following resource for shadow IPC operations.

```
$aws/things/{iot:thingName}/shadow/
```

### Special characters in authorization policies
<a name="ipc-authorization-policy-special-characters"></a>

To specify a literal `*` or `?` character in an authorization policy, you must use an escape sequence. The following escape sequences instruct the AWS IoT Greengrass Core software to use the literal value instead of the character's special meaning. For example, the `*` character is a [wildcard](#ipc-authorization-policy-wildcards) that matches any combination of characters.

| Literal character | Escape sequence | Notes |
| --- | --- | --- |
| `*` | `${*}` |  |
| `?` | `${?}` | AWS IoT Greengrass doesn't currently support the `?` wildcard, which matches any single character. |
| `$` | `${$}` | Use this escape sequence to match a resource that contains `${`. For example, to match a resource named `${resourceName}`, you must specify `${$}{resourceName}`. Otherwise, to match a resource that contains `$`, you can use a literal `$`, such as to allow access to a topic that begins with `$aws`. |

### Authorization policy examples
<a name="ipc-authorization-policy-examples"></a>

You can reference the following authorization policy examples to help you configure authorization policies for your components.

**Example component recipe with an authorization policy**
The following example component recipe includes an `accessControl` object defines an authorization policy. This policy authorizes the `com.example.HelloWorld` component to publish to the `test/topic` topic.

```
{
  "RecipeFormatVersion": "2020-01-25",
  "ComponentName": "com.example.HelloWorld",
  "ComponentVersion": "1.0.0",
  "ComponentDescription": "A component that publishes messages.",
  "ComponentPublisher": "Amazon",
  "ComponentConfiguration": {
    "DefaultConfiguration": {
      "accessControl": {
        "aws.greengrass.ipc.pubsub": {
          "com.example.HelloWorld:pubsub:1": {
            "policyDescription": "Allows access to publish to test/topic.",
            "operations": [
              "aws.greengrass#PublishToTopic"
            ],
            "resources": [
              "test/topic"
            ]
          }
        }
      }
    }
  },
  "Manifests": [
    {
      "Lifecycle": {
        "Run": "java -jar {artifacts:path}/HelloWorld.jar"
      }
    }
  ]
}
```

```
---
RecipeFormatVersion: '2020-01-25'
ComponentName: com.example.HelloWorld
ComponentVersion: '1.0.0'
ComponentDescription: A component that publishes messages.
ComponentPublisher: Amazon
ComponentConfiguration:
  DefaultConfiguration:
    accessControl:
      aws.greengrass.ipc.pubsub:
        "com.example.HelloWorld:pubsub:1":
          policyDescription: Allows access to publish to test/topic.
          operations:
            - "aws.greengrass#PublishToTopic"
          resources:
            - "test/topic"
Manifests:
  - Lifecycle:
      Run: |-
        java -jar {artifacts:path}/HelloWorld.jar
```

**Example component configuration update with an authorization policy**
The following example configuration update in a deployment specifies to configure a component with an `accessControl` object that defines an authorization policy. This policy authorizes the `com.example.HelloWorld` component to publish to the `test/topic` topic.
**Configuration to merge**

```
{
  "accessControl": {
    "aws.greengrass.ipc.pubsub": {
      "com.example.HelloWorld:pubsub:1": {
        "policyDescription": "Allows access to publish to test/topic.",
        "operations": [
          "aws.greengrass#PublishToTopic"
        ],
        "resources": [
          "test/topic"
        ]
      }
    }
  }
}
```
The following command creates a deployment to a core device.

```
aws greengrassv2 create-deployment --cli-input-json file://hello-world-deployment.json
```
The `hello-world-deployment.json` file contains the following JSON document.

```
{
  "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore",
  "deploymentName": "Deployment for MyGreengrassCore",
  "components": {
    "com.example.HelloWorld": {
      "componentVersion": "1.0.0",
      "configurationUpdate": {
        "merge": "{\"accessControl\":{\"aws.greengrass.ipc.pubsub\":{\"com.example.HelloWorld:pubsub:1\":{\"policyDescription\":\"Allows access to publish to test/topic.\",\"operations\":[\"aws.greengrass#PublishToTopic\"],\"resources\":[\"test/topic\"]}}}}"
      }
    }
  }
}
```
The following [Greengrass CLI](greengrass-cli-component.md) command creates a local deployment on a core device.

```
sudo greengrass-cli deployment create \
  --recipeDir recipes \
  --artifactDir artifacts \
  --merge "com.example.HelloWorld=1.0.0" \
  --update-config hello-world-configuration.json
```
The `hello-world-configuration.json` file contains the following JSON document.

```
{
  "com.example.HelloWorld": {
    "MERGE": {
      "accessControl": {
        "aws.greengrass.ipc.pubsub": {
          "com.example.HelloWorld:pubsub:1": {
            "policyDescription": "Allows access to publish to test/topic.",
            "operations": [
              "aws.greengrass#PublishToTopic"
            ],
            "resources": [
              "test/topic"
            ]
          }
        }
      }
    }
  }
}
```

## Subscribe to IPC event streams
<a name="ipc-subscribe-operations"></a>

You can use IPC operations to subscribe to streams of events on a Greengrass core device. To use a subscribe operation, define a *subscription handler* and create a request to the IPC service. Then, the IPC client runs the subscription handler's functions each time that the core device streams an event message to your component.

You can close a subscription to stop processing event messages. To do so, call `closeStream()` (Java), `close()` (Python), or `Close()` (C\+\+) on the subscription operation object that you used to open the subscription.

The AWS IoT Greengrass Core IPC service supports the following subscribe operations:
+ [SubscribeToTopic](ipc-publish-subscribe.md#ipc-operation-subscribetotopic)
+ [SubscribeToIoTCore](ipc-iot-core-mqtt.md#ipc-operation-subscribetoiotcore)
+ [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates)
+ [SubscribeToConfigurationUpdate](ipc-component-configuration.md#ipc-operation-subscribetoconfigurationupdate)
+ [SubscribeToValidateConfigurationUpdates](ipc-component-configuration.md#ipc-operation-subscribetovalidateconfigurationupdates)

**Topics**
+ [Define subscription handlers](#ipc-define-subscription-handlers)
+ [Example subscription handlers](#ipc-subscription-handler-examples)

### Define subscription handlers
<a name="ipc-define-subscription-handlers"></a>

To define a subscription handler, define callback functions that handle event messages, errors, and stream closure. If you use IPC client V1, you must define these functions in a class. If you use IPC client V2, which is available in later versions of the Java and Python SDKs, you can define these functions without creating a subscription handler class.

------
#### [ Java ]

If you use IPC client V1, you must implement the generic `software.amazon.awssdk.eventstreamrpc.StreamResponseHandler<{{StreamEventType}}>` interface. {{StreamEventType}} is the type of event message for the subscription operation. Define the following functions to handle event messages, errors, and stream closure.

If you use IPC client V2, you can define these functions outside of a subscription handler class or use [lambda expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html).

`void onStreamEvent({{StreamEventType}} event)`
The callback that the IPC client calls when it receives an event message, such as an MQTT message or a component update notification.

`boolean onStreamError(Throwable error)`
The callback that the IPC client calls when a stream error occurs.
<a name="ipc-subscription-handler-on-stream-error-return-value"></a>Return true to close the subscription stream as a result of the error, or return false to keep the stream open.

`void onStreamClosed()`
The callback that the IPC client calls when the stream closes.

------
#### [ Python ]

If you use IPC client V1, you must extend the stream response handler class that corresponds to the subscription operation. The AWS IoT Device SDK includes a subscription handler class for each subscription operation. {{StreamEventType}} is the type of event message for the subscription operation. Define the following functions to handle event messages, errors, and stream closure.

If you use IPC client V2, you can define these functions outside of a subscription handler class or use [lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).

`def on_stream_event(self, event: {{StreamEventType}}) -> None`
The callback that the IPC client calls when it receives an event message, such as an MQTT message or a component update notification.

`def on_stream_error(self, error: Exception) -> bool`
The callback that the IPC client calls when a stream error occurs.
<a name="ipc-subscription-handler-on-stream-error-return-value"></a>Return true to close the subscription stream as a result of the error, or return false to keep the stream open.

`def on_stream_closed(self) -> None`
The callback that the IPC client calls when the stream closes.

------
#### [ C\+\+ (IPC client V1) ]

Implement a class that derives from the stream response handler class that corresponds to the subscription operation. The AWS IoT Device SDK includes a subscription handler base class for each subscription operation. {{StreamEventType}} is the type of event message for the subscription operation. Define the following functions to handle event messages, errors, and stream closure.

`void OnStreamEvent({{StreamEventType}} *event)`
The callback that the IPC client calls when it receives an event message, such as an MQTT message or a component update notification.

`bool OnStreamError(OperationError *error)`
The callback that the IPC client calls when a stream error occurs.
<a name="ipc-subscription-handler-on-stream-error-return-value"></a>Return true to close the subscription stream as a result of the error, or return false to keep the stream open.

`void OnStreamClosed()`
The callback that the IPC client calls when the stream closes.

------
#### [ JavaScript ]

Implement a class that derives from the stream response handler class that corresponds to the subscription operation. The AWS IoT Device SDK includes a subscription handler base class for each subscription operation. {{StreamEventType}} is the type of event message for the subscription operation. Define the following functions to handle event messages, errors, and stream closure.

`on(event: 'ended', listener: StreamingOperationEndedListener)`
The callback that the IPC client calls when the stream closes.

`on(event: 'streamError', listener: StreamingRpcErrorListener)`
The callback that the IPC client calls when a stream error occurs.
<a name="ipc-subscription-handler-on-stream-error-return-value"></a>Return true to close the subscription stream as a result of the error, or return false to keep the stream open.

`on(event: 'message', listener: (message: InboundMessageType) => void)`
The callback that the IPC client calls when it receives an event message, such as an MQTT message or a component update notification.

------

### Example subscription handlers
<a name="ipc-subscription-handler-examples"></a>

The following example demonstrates how to use the [SubscribeToTopic](ipc-publish-subscribe.md#ipc-operation-subscribetotopic) operation and a subscription handler to subscribe to local publish/subscribe messages.

------
#### [ Java (IPC client V2) ]

**Example: Subscribe to local publish/subscribe messages**  <a name="ipc-operation-subscribetotopic-example-java-v2"></a>

```
package com.aws.greengrass.docs.samples.ipc;

import software.amazon.awssdk.aws.greengrass.GreengrassCoreIPCClientV2;
import software.amazon.awssdk.aws.greengrass.SubscribeToTopicResponseHandler;
import software.amazon.awssdk.aws.greengrass.model.*;

import java.nio.charset.StandardCharsets;
import java.util.Optional;

public class SubscribeToTopicV2 {

    public static void main(String[] args) {
        String topic = args[0];
        try (GreengrassCoreIPCClientV2 ipcClient = GreengrassCoreIPCClientV2.builder().build()) {
            SubscribeToTopicRequest request = new SubscribeToTopicRequest().withTopic(topic);
            GreengrassCoreIPCClientV2.StreamingResponse<SubscribeToTopicResponse,
                    SubscribeToTopicResponseHandler> response =
                    ipcClient.subscribeToTopic(request, SubscribeToTopicV2::onStreamEvent,
                            Optional.of(SubscribeToTopicV2::onStreamError),
                            Optional.of(SubscribeToTopicV2::onStreamClosed));
            SubscribeToTopicResponseHandler responseHandler = response.getHandler();
            System.out.println("Successfully subscribed to topic: " + topic);

            // Keep the main thread alive, or the process will exit.
            try {
                while (true) {
                    Thread.sleep(10000);
                }
            } catch (InterruptedException e) {
                System.out.println("Subscribe interrupted.");
            }

            // To stop subscribing, close the stream.
            responseHandler.closeStream();
        } catch (Exception e) {
            if (e.getCause() instanceof UnauthorizedError) {
                System.err.println("Unauthorized error while publishing to topic: " + topic);
            } else {
                System.err.println("Exception occurred when using IPC.");
            }
            e.printStackTrace();
            System.exit(1);
        }
    }

    public static void onStreamEvent(SubscriptionResponseMessage subscriptionResponseMessage) {
        try {
            BinaryMessage binaryMessage = subscriptionResponseMessage.getBinaryMessage();
            String message = new String(binaryMessage.getMessage(), StandardCharsets.UTF_8);
            String topic = binaryMessage.getContext().getTopic();
            System.out.printf("Received new message on topic %s: %s%n", topic, message);
        } catch (Exception e) {
            System.err.println("Exception occurred while processing subscription response " +
                    "message.");
            e.printStackTrace();
        }
    }

    public static boolean onStreamError(Throwable error) {
        System.err.println("Received a stream error.");
        error.printStackTrace();
        return false; // Return true to close stream, false to keep stream open.
    }

    public static void onStreamClosed() {
        System.out.println("Subscribe to topic stream closed.");
    }
}
```

------
#### [ Python (IPC client V2) ]

**Example: Subscribe to local publish/subscribe messages**  <a name="ipc-operation-subscribetotopic-example-python-v2"></a>

```
import sys
import time
import traceback

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    SubscriptionResponseMessage,
    UnauthorizedError
)

def main():
    args = sys.argv[1:]
    topic = args[0]

    try:
        ipc_client = GreengrassCoreIPCClientV2()
        # Subscription operations return a tuple with the response and the operation.
        _, operation = ipc_client.subscribe_to_topic(topic=topic, on_stream_event=on_stream_event,
                                                     on_stream_error=on_stream_error, on_stream_closed=on_stream_closed)
        print('Successfully subscribed to topic: ' + topic)

        # Keep the main thread alive, or the process will exit.
        try:
            while True:
                time.sleep(10)
        except InterruptedError:
            print('Subscribe interrupted.')

        # To stop subscribing, close the stream.
        operation.close()
    except UnauthorizedError:
        print('Unauthorized error while subscribing to topic: ' +
              topic, file=sys.stderr)
        traceback.print_exc()
        exit(1)
    except Exception:
        print('Exception occurred', file=sys.stderr)
        traceback.print_exc()
        exit(1)

def on_stream_event(event: SubscriptionResponseMessage) -> None:
    try:
        message = str(event.binary_message.message, 'utf-8')
        topic = event.binary_message.context.topic
        print('Received new message on topic %s: %s' % (topic, message))
    except:
        traceback.print_exc()

def on_stream_error(error: Exception) -> bool:
    print('Received a stream error.', file=sys.stderr)
    traceback.print_exc()
    return False  # Return True to close stream, False to keep stream open.

def on_stream_closed() -> None:
    print('Subscribe to topic stream closed.')

if __name__ == '__main__':
    main()
```

------
#### [ C\+\+ (IPC client V1) ]

**Example: Subscribe to local publish/subscribe messages**  <a name="ipc-operation-subscribetotopic-example-cpp"></a>

```
#include <iostream>

#include </crt/Api.h>
#include <aws/greengrass/GreengrassCoreIpcClient.h>

using namespace Aws::Crt;
using namespace Aws::Greengrass;

class SubscribeResponseHandler : public SubscribeToTopicStreamHandler {
    public:
        virtual ~SubscribeResponseHandler() {}

    private:
        void OnStreamEvent(SubscriptionResponseMessage *response) override {
            auto jsonMessage = response->GetJsonMessage();
            if (jsonMessage.has_value() && jsonMessage.value().GetMessage().has_value()) {
                auto messageString = jsonMessage.value().GetMessage().value().View().WriteReadable();
                // Handle JSON message.
            } else {
                auto binaryMessage = response->GetBinaryMessage();
                if (binaryMessage.has_value() && binaryMessage.value().GetMessage().has_value()) {
                    auto messageBytes = binaryMessage.value().GetMessage().value();
                    std::string messageString(messageBytes.begin(), messageBytes.end());
                    // Handle binary message.
                }
            }
        }

        bool OnStreamError(OperationError *error) override {
            // Handle error.
            return false; // Return true to close stream, false to keep stream open.
        }

        void OnStreamClosed() override {
            // Handle close.
        }
};

class IpcClientLifecycleHandler : public ConnectionLifecycleHandler {
    void OnConnectCallback() override {
        // Handle connection to IPC service.
    }

    void OnDisconnectCallback(RpcError error) override {
        // Handle disconnection from IPC service.
    }

    bool OnErrorCallback(RpcError error) override {
        // Handle IPC service connection error.
        return true;
    }
};

int main() {
    ApiHandle apiHandle(g_allocator);
    Io::EventLoopGroup eventLoopGroup(1);
    Io::DefaultHostResolver socketResolver(eventLoopGroup, 64, 30);
    Io::ClientBootstrap bootstrap(eventLoopGroup, socketResolver);
    IpcClientLifecycleHandler ipcLifecycleHandler;
    GreengrassCoreIpcClient ipcClient(bootstrap);
    auto connectionStatus = ipcClient.Connect(ipcLifecycleHandler).get();
    if (!connectionStatus) {
        std::cerr << "Failed to establish IPC connection: " << connectionStatus.StatusToString() << std::endl;
        exit(-1);
    }

    String topic("my/topic");
    int timeout = 10;

    SubscribeToTopicRequest request;
    request.SetTopic(topic);

    //SubscribeResponseHandler streamHandler;
    auto streamHandler = MakeShared<SubscribeResponseHandler>(DefaultAllocator());
    auto operation = ipcClient.NewSubscribeToTopic(streamHandler);
    auto activate = operation->Activate(request, nullptr);
    activate.wait();

    auto responseFuture = operation->GetResult();
    if (responseFuture.wait_for(std::chrono::seconds(timeout)) == std::future_status::timeout) {
        std::cerr << "Operation timed out while waiting for response from Greengrass Core." << std::endl;
        exit(-1);
    }

    auto response = responseFuture.get();
    if (!response) {
        // Handle error.
        auto errorType = response.GetResultType();
        if (errorType == OPERATION_ERROR) {
            auto *error = response.GetOperationError();
            (void)error;
            // Handle operation error.
        } else {
            // Handle RPC error.
        }
        exit(-1);
    }

    // Keep the main thread alive, or the process will exit.
    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(10));
    }

    operation->Close();
    return 0;
}
```

------
#### [ JavaScript ]

**Example: Subscribe to local publish/subscribe messages**  <a name="ipc-operation-subscribetotopic-example-nodejs"></a>

```
import * as greengrasscoreipc from "aws-iot-device-sdk-v2/dist/greengrasscoreipc";
import {SubscribeToTopicRequest, SubscriptionResponseMessage} from "aws-iot-device-sdk-v2/dist/greengrasscoreipc/model";
import {RpcError} from "aws-iot-device-sdk-v2/dist/eventstream_rpc";

class SubscribeToTopic {
    private ipcClient : greengrasscoreipc.Client
    private readonly topic : string;

    constructor() {
        // define your own constructor, e.g.
        this.topic = "<define_your_topic>";
        this.subscribeToTopic().then(r => console.log("Started workflow"));
    }

    private async subscribeToTopic() {
        try {
            this.ipcClient = await getIpcClient();

            const subscribeToTopicRequest : SubscribeToTopicRequest = {
                topic: this.topic,
            }

            const streamingOperation = this.ipcClient.subscribeToTopic(subscribeToTopicRequest, undefined); // conditionally apply options

            streamingOperation.on("message", (message: SubscriptionResponseMessage) => {
                // parse the message depending on your use cases, e.g.
                if(message.binaryMessage && message.binaryMessage.message) {
                    const receivedMessage = message.binaryMessage?.message.toString();
                }
            });

            streamingOperation.on("streamError", (error : RpcError) => {
                // define your own error handling logic
            })

            streamingOperation.on("ended", () => {
                // define your own logic
            })

            await streamingOperation.activate();

            // Keep the main thread alive, or the process will exit.
            await new Promise((resolve) => setTimeout(resolve, 10000))
        } catch (e) {
            // parse the error depending on your use cases
            throw e
        }
    }
}

export async function getIpcClient(){
    try {
        const ipcClient = greengrasscoreipc.createClient();
        await ipcClient.connect()
            .catch(error => {
                // parse the error depending on your use cases
                throw error;
            });
        return ipcClient
    } catch (err) {
        // parse the error depending on your use cases
        throw err
    }
}

// starting point
const subscribeToTopic = new SubscribeToTopic();
```

------
#### [ Rust ]

**Example: Subscribe to local publish/subscribe messages**

```
use gg_sdk::{Sdk, SubscribeToTopicPayload};
use std::{thread, time::Duration};

fn main() {
    let sdk = Sdk::init();
    sdk.connect().expect("Failed to establish IPC connection");

    let topic = "my/topic";

    let callback = |topic: &str, payload: SubscribeToTopicPayload| match payload
    {
        SubscribeToTopicPayload::Binary(message) => {
            let message = String::from_utf8_lossy(message);
            println!("Received new message on topic {topic}: {message}");
        }
        SubscribeToTopicPayload::Json(_) => {
            println!("Received new message on topic {topic}: (JSON message)");
        }
    };

    let _sub = sdk
        .subscribe_to_topic(topic, &callback)
        .expect("Failed to subscribe to topic");

    println!("Successfully subscribed to topic: {topic}");

    // Keep the main thread alive, or the process will exit.
    loop {
        thread::sleep(Duration::from_secs(10));
    }
}
```

------
#### [ C ]

**Example: Subscribe to local publish/subscribe messages**

```
#include <assert.h>
#include <gg/error.h>
#include <gg/ipc/client.h>
#include <gg/object.h>
#include <gg/sdk.h>
#include <gg/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

static void on_subscription_response(
    void *ctx, GgBuffer topic, GgObject payload, GgIpcSubscriptionHandle handle
) {
    (void) ctx;
    (void) handle;

    if (gg_obj_type(payload) == GG_TYPE_BUF) {
        GgBuffer message = gg_obj_into_buf(payload);
        printf(
            "Received new message on topic %.*s: %.*s\n",
            (int) topic.len,
            topic.data,
            (int) message.len,
            message.data
        );
    } else {
        assert(gg_obj_type(payload) == GG_TYPE_MAP);
        printf(
            "Received new message on topic %.*s: (JSON message)\n",
            (int) topic.len,
            topic.data
        );
    }
}

int main(void) {
    gg_sdk_init();

    GgError err = ggipc_connect();
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to establish IPC connection.\n");
        exit(-1);
    }

    GgBuffer topic = GG_STR("my/topic");

    GgIpcSubscriptionHandle handle;
    err = ggipc_subscribe_to_topic(
        topic, on_subscription_response, NULL, &handle
    );
    if (err != GG_ERR_OK) {
        fprintf(
            stderr,
            "Failed to subscribe to topic: %.*s\n",
            (int) topic.len,
            topic.data
        );
        exit(-1);
    }

    printf(
        "Successfully subscribed to topic: %.*s\n", (int) topic.len, topic.data
    );

    // Keep the main thread alive, or the process will exit.
    while (1) {
        sleep(10);
    }

    // To stop subscribing, close the stream.
    ggipc_close_subscription(handle);
}
```

------
#### [ C\+\+ (Component SDK) ]

**Example: Subscribe to local publish/subscribe messages**

```
#include <gg/ipc/client.hpp>
#include <gg/object.hpp>
#include <unistd.h>
#include <cassert>
#include <iostream>

class ResponseHandler : public gg::ipc::LocalTopicCallback {
    void operator()(
        std::string_view topic,
        gg::Object payload,
        gg::ipc::Subscription &handle
    ) override {
        (void) handle;
        if (payload.index() == GG_TYPE_BUF) {
            std::cout << "Received new message on topic " << topic << ": "
                      << get<gg::Buffer>(payload) << "\n";
        } else {
            assert(payload.index() == GG_TYPE_MAP);
            std::cout << "Received new message on topic " << topic
                      << ": (JSON message)\n";
        }
    }
};

int main() {
    auto &client = gg::ipc::Client::get();

    auto error = client.connect();
    if (error) {
        std::cerr << "Failed to establish IPC connection.\n";
        exit(-1);
    }

    std::string_view topic = "my/topic";

    static ResponseHandler handler;
    error = client.subscribe_to_topic(topic, handler);
    if (error) {
        std::cerr << "Failed to subscribe to topic: " << topic << "\n";
        exit(-1);
    }

    std::cout << "Successfully subscribed to topic: " << topic << "\n";

    // Keep the main thread alive, or the process will exit.
    while (1) {
        sleep(10);
    }
}
```

------

## IPC best practices
<a name="ipc-best-practices"></a>

The best practices for using IPC in custom components differ between IPC client V1 and IPC client V2. Follow the best practices for the IPC client version that you use.

------
#### [ IPC client V2 ]

The IPC client V2 runs callback functions in a separate thread, so compared to IPC client V1, there are fewer guidelines for you to follow when you use IPC and write subscription handler functions.
+ <a name="ipc-best-practice-reuse-one-client"></a>**Reuse one IPC client**

  After you create an IPC client, keep it open and reuse it for all IPC operations. Creating multiple clients uses extra resources and can result in resource leaks.
+ **Handle exceptions**

  The IPC client V2 logs uncaught exceptions in subscription handler functions. You should catch exceptions in your handler functions to handle errors that occur in your code.

------
#### [ IPC client V1 ]

The IPC client V1 uses a single thread that communicates with the IPC server and calls subscription handlers. You must consider this synchronous behavior when you write subscription handler functions.
+ <a name="ipc-best-practice-reuse-one-client"></a>**Reuse one IPC client**

  After you create an IPC client, keep it open and reuse it for all IPC operations. Creating multiple clients uses extra resources and can result in resource leaks.
+ **Run blocking code asynchronously**

  The IPC client V1 can't send new requests or process new event messages while the thread is blocked. You should run blocking code in a separate thread that you run from the handler function. Blocking code includes `sleep` calls, loops that continuously run, and synchronous I/O requests that take time to complete.
+ **Send new IPC requests asynchronously**

  The IPC client V1 can't send a new request from within subscription handler functions, because the request blocks the handler function if you wait for a response. You should send IPC requests in a separate thread that you run from the handler function.
+ **Handle exceptions**

  The IPC client V1 doesn't handle uncaught exceptions in subscription handler functions. If your handler function throws an exception, the subscription closes, and the exception doesn't appear in your component logs. You should catch exceptions in your handler functions to keep the subscription open and log errors that occur in your code.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

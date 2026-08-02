---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-component-configuration.html
---

# Interact with component configuration
<a name="ipc-component-configuration"></a>

The component configuration IPC service lets you do the following:
+ Get and set component configuration parameters.
+ Subscribe to component configuration updates.
+ Validate component configuration updates before the nucleus applies them.

**Topics**
+ [Minimum SDK versions](#ipc-component-configuration-sdk-versions)
+ [GetConfiguration](#ipc-operation-getconfiguration)
+ [UpdateConfiguration](#ipc-operation-updateconfiguration)
+ [SubscribeToConfigurationUpdate](#ipc-operation-subscribetoconfigurationupdate)
+ [SubscribeToValidateConfigurationUpdates](#ipc-operation-subscribetovalidateconfigurationupdates)
+ [SendConfigurationValidityReport](#ipc-operation-sendconfigurationvalidityreport)

## Minimum SDK versions
<a name="ipc-component-configuration-sdk-versions"></a>

The following table lists the minimum versions of the SDKs that you can use to interact with component configuration.

| SDK | Minimum version |
| --- | --- |
| [AWS IoT Greengrass Component SDK (C, C\+\+, Rust)](https://github.com/aws-greengrass/aws-greengrass-component-sdk) | v1.0.0 |
| [AWS IoT Device SDK for Java v2](https://github.com/aws/aws-iot-device-sdk-java-v2) | v1.2.10 |
| [AWS IoT Device SDK for Python v2](https://github.com/aws/aws-iot-device-sdk-python-v2) | v1.5.3 |
| [AWS IoT Device SDK for C\+\+ v2](https://github.com/aws/aws-iot-device-sdk-cpp-v2) | v1.17.0 |
| [AWS IoT Device SDK for JavaScript v2](https://github.com/aws/aws-iot-device-sdk-js-v2) | v1.12.0 |

## GetConfiguration
<a name="ipc-operation-getconfiguration"></a>

Gets a configuration value for a component on the core device. You specify the key path for which to get a configuration value.

### Request
<a name="ipc-operation-getconfiguration-request"></a>

This operation's request has the following parameters:

`componentName` (Python: `component_name`)  <a name="ipc-configuration-request-component-name"></a>
(Optional) The name of the component.
Defaults to the name of the component that makes the request.

`keyPath` (Python: `key_path`)
The key path to the configuration value. Specify a list where each entry is the key for a single level in the configuration object. For example, specify `["mqtt", "port"]` to get the value of `port` in the following configuration.

```
{
  "mqtt": {
    "port": 443
  }
}
```
To get the component's complete configuration, specify an empty list.

### Response
<a name="ipc-operation-getconfiguration-response"></a>

This operation's response has the following information:

`componentName` (Python: `component_name`)  <a name="ipc-configuration-response-component-name"></a>
The name of the component.

`value`
The requested configuration as an object.

### Examples
<a name="ipc-operation-getconfiguration-examples"></a>

The following examples demonstrate how to call this operation in custom component code.

------
#### [ Rust ]

**Example: Get configuration**

```
use core::mem::MaybeUninit;
use gg_sdk::{Sdk, UnpackedObject};

fn main() {
    let sdk = Sdk::init();
    sdk.connect().expect("Failed to establish IPC connection");

    // Get a configuration value at key path ["mqtt", "port"]
    let mut buf = [MaybeUninit::uninit(); 1024];

    let value = sdk
        .get_config(&["mqtt", "port"], None, &mut buf)
        .expect("Failed to get configuration");

    if let UnpackedObject::I64(port) = value.unpack() {
        println!("Configuration value: {port}");
    }
}
```

------
#### [ C ]

**Example: Get configuration**

```
#include <gg/error.h>
#include <gg/ipc/client.h>
#include <gg/object.h>
#include <gg/sdk.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    gg_sdk_init();

    GgError err = ggipc_connect();
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to establish IPC connection.\n");
        exit(-1);
    }

    // Get a configuration value at key path ["mqtt", "port"]
    uint8_t response_mem[1024];
    GgObject value;

    err = ggipc_get_config(
        GG_BUF_LIST(GG_STR("mqtt"), GG_STR("port")),
        NULL, // component_name (NULL = current component)
        GG_BUF(response_mem),
        &value
    );
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to get configuration.\n");
        exit(-1);
    }

    if (gg_obj_type(value) == GG_TYPE_I64) {
        printf("Configuration value: %" PRId64 "\n", gg_obj_into_i64(value));
    } else if (gg_obj_type(value) == GG_TYPE_BUF) {
        GgBuffer buf = gg_obj_into_buf(value);
        printf("Configuration value: %.*s\n", (int) buf.len, buf.data);
    } else {
        printf("Configuration value is of unexpected type.\n");
    }
}
```

------
#### [ C\+\+ (Component SDK) ]

**Example: Get configuration**

```
#include <gg/ipc/client.hpp>
#include <iostream>

int main() {
    auto &client = gg::ipc::Client::get();

    auto error = client.connect();
    if (error) {
        std::cerr << "Failed to establish IPC connection.\n";
        exit(-1);
    }

    // Get a configuration value at key path ["mqtt", "port"]
    std::array key_path = { gg::Buffer { "mqtt" }, gg::Buffer { "port" } };
    int64_t value = 0;

    error = client.get_config(key_path, std::nullopt, value);
    if (error) {
        std::cerr << "Failed to get configuration.\n";
        exit(-1);
    }

    std::cout << "Configuration value: " << value << "\n";
}
```

------

## UpdateConfiguration
<a name="ipc-operation-updateconfiguration"></a>

Updates a configuration value for this component on the core device.

### Request
<a name="ipc-operation-updateconfiguration-request"></a>

This operation's request has the following parameters:

`keyPath` (Python: `key_path`)
(Optional) The key path to the container node (the object) to update. Specify a list where each entry is the key for a single level in the configuration object. For example, specify the key path `["mqtt"]` and the merge value `{ "port": 443 }` to set the value of `port` in the following configuration.

```
{
  "mqtt": {
    "port": 443
  }
}
```
The key path must specify a container node (an object) in the configuration. If the node doesn't exist in the component's configuration, this operation creates it and sets its value to the object in `valueToMerge`.
Defaults to the root of the configuration object.

`timestamp`
The current Unix epoch time in milliseconds. This operation uses this timestamp to resolve concurrent updates to the key. If the key in the component configuration has a greater timestamp than the timestamp in the request, then the request fails.

`valueToMerge` (Python: `value_to_merge`)
The configuration object to merge at the location that you specify in `keyPath`. For more information, see [Update component configurations](update-component-configurations.md).

### Response
<a name="ipc-operation-updateconfiguration-response"></a>

This operation doesn't provide any information in its response.

### Examples
<a name="ipc-operation-updateconfiguration-examples"></a>

The following examples demonstrate how to call this operation in custom component code.

------
#### [ Rust ]

**Example: Update configuration**

```
use gg_sdk::Sdk;

fn main() {
    let sdk = Sdk::init();
    sdk.connect().expect("Failed to establish IPC connection");

    // Update configuration value at key path ["mqtt", "port"] to 443
    sdk.update_config(&["mqtt", "port"], None, 443)
        .expect("Failed to update configuration");

    println!("Successfully updated configuration.");
}
```

------
#### [ C ]

**Example: Update configuration**

```
#include <gg/error.h>
#include <gg/ipc/client.h>
#include <gg/object.h>
#include <gg/sdk.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    gg_sdk_init();

    GgError err = ggipc_connect();
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to establish IPC connection.\n");
        exit(-1);
    }

    // Update configuration value at key path ["mqtt", "port"] to 443
    err = ggipc_update_config(
        GG_BUF_LIST(GG_STR("mqtt"), GG_STR("port")),
        NULL, // timestamp (NULL = current time)
        gg_obj_i64(443)
    );
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to update configuration.\n");
        exit(-1);
    }

    printf("Successfully updated configuration.\n");
}
```

------
#### [ C\+\+ (Component SDK) ]

**Example: Update configuration**

```
#include <gg/ipc/client.hpp>
#include <iostream>

int main() {
    auto &client = gg::ipc::Client::get();

    auto error = client.connect();
    if (error) {
        std::cerr << "Failed to establish IPC connection.\n";
        exit(-1);
    }

    // Update configuration value at key path ["mqtt", "port"] to 443
    std::array key_path = { gg::Buffer { "mqtt" }, gg::Buffer { "port" } };

    error = client.update_config(key_path, 443);
    if (error) {
        std::cerr << "Failed to update configuration.\n";
        exit(-1);
    }

    std::cout << "Successfully updated configuration.\n";
}
```

------

## SubscribeToConfigurationUpdate
<a name="ipc-operation-subscribetoconfigurationupdate"></a>

Subscribe to receive notifications when a component's configuration updates. When you subscribe to a key, you receive a notification when any child of that key updates.

<a name="ipc-subscribe-operation-note"></a>This operation is a subscription operation where you subscribe to a stream of event messages. To use this operation, define a stream response handler with functions that handle event messages, errors, and stream closure. For more information, see [Subscribe to IPC event streams](interprocess-communication.md#ipc-subscribe-operations).

**Event message type:** `ConfigurationUpdateEvents`

### Request
<a name="ipc-operation-subscribetoconfigurationupdate-request"></a>

This operation's request has the following parameters:

`componentName` (Python: `component_name`)  <a name="ipc-configuration-request-component-name"></a>
(Optional) The name of the component.
Defaults to the name of the component that makes the request.

`keyPath` (Python: `key_path`)
The key path to the configuration value for which to subscribe. Specify a list where each entry is the key for a single level in the configuration object. For example, specify `["mqtt", "port"]` to get the value of `port` in the following configuration.

```
{
  "mqtt": {
    "port": 443
  }
}
```
To subscribe to updates for all values in the component's configuration, specify an empty list.

### Response
<a name="ipc-operation-subscribetoconfigurationupdate-response"></a>

This operation's response has the following information:

`messages`
The stream of notification messages. This object, `ConfigurationUpdateEvents`, contains the following information:
`configurationUpdateEvent` (Python: `configuration_update_event`)
The configuration update event. This object, `ConfigurationUpdateEvent`, contains the following information:
`componentName` (Python: `component_name`)  <a name="ipc-configuration-response-component-name"></a>
The name of the component.
`keyPath` (Python: `key_path`)
The key path to the configuration value that updated.

### Examples
<a name="ipc-operation-subscribetoconfigurationupdate-examples"></a>

The following examples demonstrate how to call this operation in custom component code.

------
#### [ Rust ]

**Example: Subscribe to configuration updates**

```
use gg_sdk::Sdk;
use std::{thread, time::Duration};

fn main() {
    let sdk = Sdk::init();
    sdk.connect().expect("Failed to establish IPC connection");

    // Subscribe to configuration updates for key path ["mqtt"]
    let callback = |component_name: &str, key_path: &[&str]| {
        println!(
            "Received configuration update for component: {component_name}"
        );
        println!("Key path: {key_path:?}");
    };

    let _sub = sdk
        .subscribe_to_configuration_update(None, &["mqtt"], &callback)
        .expect("Failed to subscribe to configuration updates");

    println!("Successfully subscribed to configuration updates.");

    // Keep the main thread alive, or the process will exit.
    loop {
        thread::sleep(Duration::from_secs(10));
    }
}
```

------
#### [ C ]

**Example: Subscribe to configuration updates**

```
#include <gg/error.h>
#include <gg/ipc/client.h>
#include <gg/object.h>
#include <gg/sdk.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

static void on_subscription_response(
    void *ctx,
    GgBuffer component_name,
    GgList key_path,
    GgIpcSubscriptionHandle handle
) {
    (void) ctx;
    (void) handle;

    printf(
        "Received configuration update for component: %.*s\n",
        (int) component_name.len,
        component_name.data
    );

    printf("Key path: [");
    for (size_t i = 0; i < key_path.len; i++) {
        if (i > 0) {
            printf(", ");
        }
        GgObject *obj = &key_path.items[i];
        if (gg_obj_type(*obj) == GG_TYPE_BUF) {
            GgBuffer key = gg_obj_into_buf(*obj);
            printf("\"%.*s\"", (int) key.len, key.data);
        }
    }
    printf("]\n");
}

int main(void) {
    gg_sdk_init();

    GgError err = ggipc_connect();
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to establish IPC connection.\n");
        exit(-1);
    }

    // Subscribe to configuration updates for key path ["mqtt"]
    GgIpcSubscriptionHandle handle;
    err = ggipc_subscribe_to_configuration_update(
        NULL, // component_name (NULL = current component)
        GG_BUF_LIST(GG_STR("mqtt")),
        on_subscription_response,
        NULL,
        &handle
    );
    if (err != GG_ERR_OK) {
        fprintf(stderr, "Failed to subscribe to configuration updates.\n");
        exit(-1);
    }

    printf("Successfully subscribed to configuration updates.\n");

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

**Example: Subscribe to configuration updates**

```
#include <gg/ipc/client.hpp>
#include <unistd.h>
#include <iostream>

class ResponseHandler : public gg::ipc::ConfigurationUpdateCallback {
    void operator()(
        std::string_view component_name,
        gg::List key_path,
        gg::ipc::Subscription &handle
    ) override {
        (void) handle;
        std::cout << "Received configuration update for component: "
                  << component_name << "\n";
        std::cout << "Key path: [";
        for (size_t i = 0; i < key_path.size(); i++) {
            if (i > 0) {
                std::cout << ", ";
            }
            std::cout << "\"" << get<gg::Buffer>(key_path[i]) << "\"";
        }
        std::cout << "]\n";
    }
};

int main() {
    auto &client = gg::ipc::Client::get();

    auto error = client.connect();
    if (error) {
        std::cerr << "Failed to establish IPC connection.\n";
        exit(-1);
    }

    // Subscribe to configuration updates for key path ["mqtt"]
    std::array key_path = { gg::Buffer { "mqtt" } };

    static ResponseHandler handler;
    error = client.subscribe_to_configuration_update(
        key_path, std::nullopt, handler
    );
    if (error) {
        std::cerr << "Failed to subscribe to configuration updates.\n";
        exit(-1);
    }

    std::cout << "Successfully subscribed to configuration updates.\n";

    // Keep the main thread alive, or the process will exit.
    while (1) {
        sleep(10);
    }
}
```

------

## SubscribeToValidateConfigurationUpdates
<a name="ipc-operation-subscribetovalidateconfigurationupdates"></a>

Subscribe to receive notifications before this component's configuration updates. This lets components validate updates to their own configuration. Use the [SendConfigurationValidityReport](#ipc-operation-sendconfigurationvalidityreport) operation to tell the nucleus whether or not the configuration is valid.

**Important**
Local deployments don't notify components of updates.

<a name="ipc-subscribe-operation-note"></a>This operation is a subscription operation where you subscribe to a stream of event messages. To use this operation, define a stream response handler with functions that handle event messages, errors, and stream closure. For more information, see [Subscribe to IPC event streams](interprocess-communication.md#ipc-subscribe-operations).

**Event message type:** `ValidateConfigurationUpdateEvents`

### Request
<a name="ipc-operation-subscribetovalidateconfigurationupdates-request"></a>

This operation's request doesn't have any parameters.

### Response
<a name="ipc-operation-subscribetovalidateconfigurationupdates-response"></a>

This operation's response has the following information:

`messages`
The stream of notification messages. This object, `ValidateConfigurationUpdateEvents`, contains the following information:
`validateConfigurationUpdateEvent` (Python: `validate_configuration_update_event`)
The configuration update event. This object, `ValidateConfigurationUpdateEvent`, contains the following information:
`deploymentId` (Python: `deployment_id`)
The ID of the AWS IoT Greengrass deployment that updates the component.
`configuration`
The object that contains the new configuration.

## SendConfigurationValidityReport
<a name="ipc-operation-sendconfigurationvalidityreport"></a>

Tell the nucleus whether or not a configuration update to this component is valid. The deployment fails if you tell the nucleus that the new configuration isn't valid. Use the [SubscribeToValidateConfigurationUpdates](#ipc-operation-subscribetovalidateconfigurationupdates) operation to subscribe to validate configuration updates.

If a component doesn't respond to a validate configuration update notification, the nucleus waits the amount of time that you specify in the deployment's configuration validation policy. After that timeout, the nucleus proceeds with the deployment. The default component validation timeout is 20 seconds. For more information, see [Create deployments](create-deployments.md) and the [DeploymentConfigurationValidationPolicy](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentConfigurationValidationPolicy.html) object that you can provide when you call the [CreateDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html) operation.

### Request
<a name="ipc-operation-sendconfigurationvalidityreport-request"></a>

This operation's request has the following parameters:

`configurationValidityReport` (Python: `configuration_validity_report`)
The report that tells the nucleus whether or not the configuration update is valid. This object, `ConfigurationValidityReport`, contains the following information:
`status`
The validity status. This enum, `ConfigurationValidityStatus`, has the following values:
+ `ACCEPTED` – The configuration is valid and the nucleus can apply it to this component.
+ `REJECTED` – The configuration isn't valid and the deployment fails.
`deploymentId` (Python: `deployment_id`)
The ID of the AWS IoT Greengrass deployment that requested the configuration update.
`message`
(Optional) A message that reports why the configuration isn't valid.

### Response
<a name="ipc-operation-sendconfigurationvalidityreport-response"></a>

This operation doesn't provide any information in its response.

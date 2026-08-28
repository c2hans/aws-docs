---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/elpg-provisioning.html
---

# 11 Provisioning
<a name="elpg-provisioning"></a>

All ExpressLink modules will be equipped with a pre-provisioned hardware root of trust (on chip or external secure element, secure enclave, TPM, iSIM). This will provide the necessary unique identifier (UID) of the module, a key pair (public, private) and will hold a certificate that is signed by a CA shared with AWS as part of ExpressLink program. This certificate will be used to transfer the module public key to the AWS endpoint upon activation.

## 11.1 ExpressLink Modules Activation
<a name="elpg-provisioning-module-activation"></a>

Upon first use, or following a complete factory reset, each ExpressLink module is ready to establish a connection according to the model's specific connectivity capabilities (Wi-Fi, Cellular, ...). In case of Wi-Fi modules, this is possible only after the end-user has provided the module with the proper Wi-Fi credentials for a local, compatible Wi-Fi Access Point (router).

### 11.1.1 ExpressLink Staging Account Authentication
<a name="elpg-provisioning-staging-account"></a>

Each ExpressLink module is ready to establish a connection with a default AWS IoT ExpressLink staging account. The connection is mutually authenticated using the ExpressLink birth certificate (and an AWS server certificate) and upgraded to a secure socket connection (Mutual TLS).

### 11.1.2 ExpressLink Staging Account Endpoint
<a name="elpg-provisioning-staging-account-endpoint"></a>

During the qualification process, AWS assigns each ExpressLink manufacturing partner a dedicated staging account and the associated, unique AWS endpoint (URL).

**11.1.2.1**   The assigned staging account endpoint is set as the "factory default" for the Endpoint configuration parameter (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)).

### 11.1.3 ExpressLink Birth Certificate
<a name="elpg-provisioning-birth-certificate"></a>

Each ExpressLink device must be provided with an X.509 certificate that conforms to the following specification:
+ **11.1.3.1**   The Serial Number must contain the device Unique ID (a unique, nonsequential 128-bit or larger number) also assigned as the ExpressLink module ThingName configuration.
+ **11.1.3.2**   The certificate signature is provided by a Certificate Authority that has been registered by the vendor with AWS IoT Core for the exclusive use of the vendor ExpressLink modules.
+ **11.1.3.3**   The expiration date is set to no less than 10 years from the device certificate issue.

### 11.1.4 ExpressLink staging account device registration
<a name="elpg-provisioning-staging-account-registration"></a>

Using the staging account endpoint, the ExpressLink module proceeds to login to the AWS IoT Core MQTT broker. If successful, an automated process (JITP or similar) creates a thing and associated policies using an ExpressLink template and appends it to the staging account registry.

### 11.1.5 ExpressLink MQTT Login signature
<a name="elpg-provisioning-mqtt-login-signature"></a>

The ExpressLink module presents an "MQTT login string" formatted as follows (as a single line string):

```
?SDK=RTOS &SDKVersion=x.y.z &Platform=ExpressLink &Metadata=( Vendor=<vendor-name>; Model=<model-name>; FWversion=X.Y.Z; TechSpec=0.9.1; CustomName=<custom-product-name>)
```

This string is logged by AWS IoT Core and allows the collection of meta data that is used to assess the effective usage of ExpressLink modules, provide diagnostic information and measure the successful completion of the onboarding process.
+ **SDK**: is the RTOS used by the ExpressLink module (for example, "FreeRTOS").
+ **SDKVersion**: is the semantic version of the RTOS kernel used (for example, "v10.4.2").
+ **Platform**: must match the string "ExpressLink".
+ **Metadata**: provides further detail as a list of additional key-value pairs using the following grammar `(<key>=<value>; *)`. The Metadata value string enclosed in parentheses is formatted as follows:
  + **11.1.5.1**   Keys and values are expressed using ASCII alphanumeric characters (0-9, A-Z, a-z), including the dash (-), period (.) and space.
  + **11.1.5.2**   Leading/trailing spaces are ignored and automatically trimmed from keys and values.
  + **11.1.5.3**   The following key/value pairs are required:
    + **Vendor**: manufacturer of the module.
    + **Model**: uniquely identifies the specific model. NOTE: Vendor and Model combine to form the persistent configuration parameter "About" (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)) with a max length of 64 characters.
    + **FWversion**: semantic version of the manufacturer module firmware (for example, "1.1.13"). Also see the persistent configuration parameter "Version" in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2).
    + **TechSpec:** semantic version of the module technical specifications target (for example, "0.9.1"). Also see the persistent configuration parameter "TechSpec" in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2).
    + **CustomName**: a custom field as configured by the host processor (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)). Also see the persistent configuration parameter "CustomName" in that same table.
  + **11.1.5.4**   The Metadata string (contained in parentheses) will not exceed a maximum length of 256 characters. Should the concatenation of the prescribed key/value pairs exceed this maximum value, it will be right-truncated at the expense of the CustomName value.
  + Example of Metadata:

    ```
    (Vendor=ABC; Model= A-1234; FWversion = X.Y.Z; TechSpec =0.9.1; CustomName = Toaster 3000 )
    ```

    Note the uneven use of spaces in the example above is interpreted correctly by trimming leading and trailing spaces as per 11.1.5.2.

## 11.2 ExpressLink Evaluation Kits Quick Connect Flow
<a name="elpg-provisioning-evaluation-kits"></a>

ExpressLink Evaluation Kits are able to use the ExpressLink staging account to deliver a fast, out-of-box experience. As soon as connected they are able to publish data to an ExpressLink MQTT topic ("data") and subscribe to any ExpressLink MQTT topic ("state"). AWS provides a simple web application (Quick Connect) to all ExpressLink users to visualize the data published by the Host processor (using animated graphs) and to send customizable commands back to their Host processors.

<a name="elpg-figure5"></a>![Figure 5 - ExpressLink Evaluation Kit Quick Connect flow](http://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/images/eval-kit-quick-connect.png)

Developers are also able to register their ExpressLink modules to their private developer's accounts and proceed to application development with a few simple, manual steps, including:
+ extracting the device certificate
+ uploading it to their private accounts
+ updating the ExpressLink endpoint

### 11.2.1 Workshop Default Wi-Fi Credentials (Optional)
<a name="elpg-provisioning-default-wifi"></a>

To reduce the number of configuration steps and time required to establish a Wi-Fi connection, a default set of Wi-Fi credentials can be provided in the configuration dictionary at factory reset.

Using default Wi-Fi credentials can be convenient in workshop, classroom or seminar environments to avoid several (10\+) users attempting to simultaneously use a CONFMODE (Bluetooth) connection. This greatly simplifies the room set up.

If implemented, the manufacturer documents such credentials in the module datasheet.

## 11.3 ExpressLink Production Onboarding Flow
<a name="elpg-provisioning-onboarding"></a>

Onboarding is the process of creating a "thing" corresponding to each physical device in the customer account registry in order to provide access to the account's IoT core services. Each thing must be associated with a valid certificate and access policy document.

In a production flow, ExpressLink customers can use any of a number of automated onboarding techniques as required by their application, including:
+ Pre-registration, where the modules' certificates are obtained before assembly and uploaded to the customer account in advance.
+ End of (assembly) Line registration, where module certificates are collected after product assembly and individually uploaded to the customer's AWS account.
+ End of Line batch registration, where module certificates are collected after product assembly and shipped in batches to the customer for upload into the AWS account.
+ Just in Time Registration, where the device onboards to the customer account at first connection. (This requires pre-registration of the module manufacturer's CA to the customer account.)
+ Late-binding, where the end product user performs the product onboarding (often simultaneously with the user's own registration, although the two steps should not be confused).

### 11.3.1 ExpressLink late binding flow example
<a name="elpg-provisioning-late-binding"></a>

A late binding onboarding flow can be initiated by the end-user after purchasing the finished product when they connect it for the first time and register the product. The end-user can be directed to a web application devised by the OEM/customer (for example, a toaster manufacturer) that will guide the user through the following steps:

1. Enter Wi-Fi credentials (only for Wi-Fi modules)– this is required to access the AWS cloud. To accomplish this, the host can activate a CONFMODE for credential entry or the host can directly manipulate the configuration dictionary (SSID, Passphrase).

1. Access the ExpressLink staging account for the first time.

1. Claim the ExpressLink module (identified by ThingName) from the staging account.

1. Transfer the certificate to the OEM account registry (thing creation).

1. Update the ExpressLink module Endpoint (to point to the OEM account).

1. Disconnect and reconnect the ExpressLink Device to the OEM account.

Steps 1 and 2 are facilitated by the staging account assigned to each manufacturer and managed by AWS. Steps 3 and 4 require the customer to implement a claim mechanism that interacts with the AWS managed staging account. Step 5 is facilitated by a specific device feature as described in [11.3.2 ExpressLink onboarding states and transitions](#elpg-provisioning-onboarding-states).

Additional steps to register the user, create an end-user (application) account, collect user identifiable information (user name and password) and bind it to the ExpressLink thing are left to the OEM application.

### 11.3.2 ExpressLink onboarding states and transitions
<a name="elpg-provisioning-onboarding-states"></a>

The configuration parameter Endpoint (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)) controls the onboarding state of the device. The device is in the *staging* state when the Endpoint parameter (string) matches the factory default value that corresponds to an AWS-managed staging account assigned to each manufacturer. The device is in the *onboarded* state when the Endpoint parameter has been modified to point to a customer account (endpoint) by a host that directly updated the configuration dictionary using a CONF command (see [6.2.1 CONF KEY=*{value}*   »Assignment«](elpg-configuration-dictionary.md#elpg-assignment-conf)) or by means of the following remote update process:

**11.3.2.1**   When (and only when) in the *staging* state, a connected ExpressLink module automatically subscribes ONLY to the endpoint-update topic: **{{ThingName}}/expresslink\_config**. Then, when it receives a message on the update topic with the following format: **{"Endpoint" : "value"}**, the module updates the Endpoint configuration parameter with the requested new value.

**11.3.2.2**   The host can retrieve the MSG event produced (GET0) and use it to implement additional optional features, such as to alert the user of the device of a successful onboarding (registration).

**11.3.2.3**   The module will also automatically disconnect. The related CONLOST event will inform the host that it must re-establish a new connection, this time to the newly assigned endpoint.

**11.3.2.4**   The host can query the state of the module using the CONNECT? command and inspecting the second numerical parameter provided in the response (see [4.7.1 CONNECT?   »Request the connection status«](elpg-commands.md#elpg-connectq-command)) without having to inspect the contents of the Endpoint configuration parameter (or knowing or assuming the default Endpoint value to compare against).

**11.3.2.5**   When (and only when) in the *onboarded* state, a connected ExpressLink module subscribes automatically to several AWS-reserved topics as required to support OTA and other core ExpressLink functionality. In the same way, features dependent on the AWS IoT Device Defender and AWS IoT Device Shadow services are supported only when a module is in the *onboarded* state.

<a name="elpg-figure6"></a>![Figure 6 - ExpressLink onboarding states diagram](http://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/images/image5.png)

Once onboarded, all ExpressLink modules behave as fully owned devices and connect to the customer/OEM account as the ExpressLink things are transferred to the chosen OEM registry. It is the responsibility of the OEM to manage the product life cycle, use the OTA services to apply module updates (with images provided by the ExpressLink module vendor) and apply host processor application updates as needed.

### 11.3.3 Handling onboarding failures
<a name="elpg-provisioning-onboarding-failures"></a>

The onboarding process can fail at various points due to end-user, host application, or network errors. We envision the following scenarios:
+ Onboarding process failure: if the OEM misconfigures the account policies this would prevent the device certificate from being moved into the target account. The AWS IoT API will report this type of error to OEM developers during testing.
+ Onboarding process failure: if the ExpressLink claim and removal from the staging account fails this would leave it in the staging account while a new thing is created in the OEM account and the ExpressLink module is redirected to the new endpoint. Staging account periodic cleaning and fraud detection sweeps will clear the anomaly in a short time.
+ Endpoint Update failure: if the device does not receive the ExpressLink endpoint update message it remains in the staging account and fails to connect to the target OEM account within a given amount of time. The binding process (web application) can be designed to timeout and guide the user to repeat the procedure until successful.
+ Accidental product factory reset: in this case, the ExpressLink device will rejoin the staging account as soon as connectivity is regained, and the onboarding process can be restarted at any time. The OEM application will be able to detect that an already registered device is re-applying to onboarding and could possibly help to restore the product status and/or report the error to developers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

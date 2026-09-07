---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-provisioning.html
---

# 10 Provisioning
<a name="elpg-provisioning"></a>

All ExpressLink modules will be equipped with a pre-provisioned hardware root of trust (on chip or external secure element, secure enclave, TPM, iSIM). This will provide the necessary unique identifier (UID) of the module, a key pair (public, private) and will hold a certificate that is signed by a CA shared with AWS as part of ExpressLink program. This certificate will be used to transfer the module public key to the AWS endpoint upon activation.

## 10.1 ExpressLink Modules Activation
<a name="elpg-provisioning-module-activation"></a>

Upon first use, or following a complete factory reset, each ExpressLink module is ready to establish a connection according to the model's specific connectivity capabilities (Wi-Fi, Cellular, ...). In case of Wi-Fi modules, this is possible only after the end-user has provided the module with the proper Wi-Fi credentials for a local, compatible Wi-Fi Access Point (router).

### 10.1.1 ExpressLink Staging Account Authentication
<a name="elpg-provisioning-staging-account"></a>

Each ExpressLink module is ready to establish a connection with a default AWS IoT ExpressLink staging account. The connection is mutually authenticated using the ExpressLink birth certificate (and an AWS server certificate) and upgraded to a secure socket connection (Mutual TLS).

### 10.1.2 ExpressLink Staging Account Endpoint
<a name="elpg-provisioning-staging-account-endpoint"></a>

During the qualification process, AWS assigns each ExpressLink manufacturing partner a dedicated staging account and the associated, unique AWS endpoint (URL).

**10.1.2.1**   The assigned staging account endpoint is set as the "factory default" for the Endpoint configuration parameter (see [Table 2 - Configuration dictionary persistent keys](elpg-configuration-dictionary.md#elpg-table2)).

### 10.1.3 ExpressLink Birth Certificate
<a name="elpg-provisioning-birth-certificate"></a>

Each ExpressLink device must be provided with an X.509 certificate that conforms to the following specification:
+ **10.1.3.1**   The Serial Number must contain the device Unique ID (a unique, nonsequential 128-bit or larger number) also assigned as the ExpressLink module ThingName configuration.
+ **10.1.3.2**   The certificate signature is provided by a Certificate Authority that has been registered by the vendor with AWS IoT Core for the exclusive use of the vendor ExpressLink modules.
+ **10.1.3.3**   The expiration date is set to no less than 10 years from the device certificate issue.

### 10.1.4 ExpressLink staging account device registration
<a name="elpg-provisioning-staging-account-registration"></a>

Using the staging account endpoint, the ExpressLink module proceeds to login to the AWS IoT Core MQTT broker. If successful, an automated process (JITP or similar) creates a thing and associated policies using an ExpressLink template and appends it to the staging account registry.

## 10.2 ExpressLink Evaluation Kits Quick Connect Flow
<a name="elpg-provisioning-evaluation-kits"></a>

ExpressLink Evaluation Kits are able to use the ExpressLink staging account to deliver a fast, out-of-box experience. As soon as connected they are able to publish data to an ExpressLink MQTT topic ("data") and subscribe to any ExpressLink MQTT topic ("state"). AWS provides a simple web application (Quick Connect) to all ExpressLink users to visualize the data published by the Host processor (using animated graphs) and to send customizable commands back to their Host processors.

Developers are also able to register their ExpressLink modules to their private developer's accounts and proceed to application development with a few simple, manual steps, including:
+ extracting the device certificate
+ uploading it to their private accounts
+ updating the ExpressLink endpoint

### 10.2.1 Workshop Default Wi-Fi Credentials (Optional)
<a name="elpg-provisioning-default-wifi"></a>

To reduce the number of configuration steps and time required to establish a Wi-Fi connection, a default set of Wi-Fi credentials can be provided in the configuration dictionary at factory reset.

Using default Wi-Fi credentials can be convenient in workshop, classroom or seminar environments to avoid several (10\+) users attempting to simultaneously use a CONFMODE (Bluetooth) connection. This greatly simplifies the room set up.

If implemented, the manufacturer documents such credentials in the module datasheet.

## 10.3 ExpressLink Production Onboarding Flow
<a name="elpg-provisioning-onboarding"></a>

Onboarding is the process of creating a "thing" corresponding to each physical device in the customer account registry in order to provide access to the account's IoT core services. Each thing must be associated with a valid certificate and access policy document.

In a production flow, ExpressLink customers can use any of a number of automated onboarding techniques as required by their application, including:
+ Pre-registration, where the modules' certificates are obtained before assembly and uploaded to the customer account in advance.
+ End of (assembly) Line registration, where module certificates are collected after product assembly and individually uploaded to the customer's AWS account.
+ End of Line batch registration, where module certificates are collected after product assembly and shipped in batches to the customer for upload into the AWS account.
+ Just in Time Registration, where the device onboards to the customer account at first connection. (This requires pre-registration of the module manufacturer's CA to the customer account.)

### 10.3.1 ExpressLink onboarding states and transitions
<a name="elpg-provisioning-onboarding-states"></a>

**10.3.1.1**   At first activation or following a factory reset, all ExpressLink devices default to the Evaluation and Test state where they connect to the manufacturer's staging account. The configuration parameter Endpoint (see [Table 2 - Configuration dictionary persistent keys](elpg-configuration-dictionary.md#elpg-table2)) controls this behavior. When (and only when) in the Evaluation and Test state, ExpressLink modules must automatically subscribe to the endpoint-update topic: **<ThingName>/expresslink\_config**. When it receives a message on the update topic with the following format: **{"Endpoint" : "value"}**, the module will update the Endpoint configuration parameter with the requested new value.

**10.3.1.2**   The host can retrieve the MSG event produced (GET0) and use it to implement additional optional features, such as to alert the user of the device of a successful onboarding (registration).

**10.3.1.3**   The module will also automatically disconnect. The related CONLOST event will inform the host that it must re-establish a new connection, this time to the newly assigned endpoint.

**10.3.1.4**   The host can query the state of the module using the CONNECT? command and inspecting the second numerical parameter provided in the response (see [3.7.1 CONNECT? ⁞  Request the connection status](elpg-commands.md#elpg-connectq-command)) without having to inspect the contents of the Endpoint configuration parameter (or knowing/assuming the default Endpoint value to compare against).

<a name="elpg-figure6"></a>![Figure 6 - ExpressLink onboarding states diagram](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/images/image5.png)

Once onboarded, all ExpressLink modules behave as fully owned devices and connect to the customer/OEM account as the ExpressLink things are transferred to the chosen OEM registry. It is the responsibility of the OEM to manage the product life cycle, use the OTA services to apply module updates (with images provided by the ExpressLink module vendor) and apply host processor application updates as needed.

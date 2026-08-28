---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/cfg-dt-dp.html
---

# Create a device pool in IDT for FreeRTOS
<a name="cfg-dt-dp"></a>

Devices to be tested are organized in device pools. Each device pool consists of one or more identical devices. You can configure IDT for FreeRTOS to test a single device in a pool or multiple devices in a pool. To accelerate the qualification process, IDT for FreeRTOS can test devices with the same specifications in parallel. It uses a round-robin method to execute a different test group on each device in a device pool.

You can add one or more devices to a device pool by editing the `devices` section of the `device.json` template in the `configs` folder.

**Note**
All devices in the same pool must be of same technical specification and SKU.

To enable parallel builds of the source code for different test groups, IDT for FreeRTOS copies the source code to a results folder inside the IDT for FreeRTOS extracted folder. The source code path in your build or flash command must be referenced using either the `testdata.sourcePath` or `sdkPath` variable. IDT for FreeRTOS replaces this variable with a temporary path of the copied source code. For more information see, [IDT for FreeRTOS variables](dt-vars.md).

The following is an example `device.json` file used to create a device pool with multiple devices.

```
[
    {
        "id": "{{pool-id}}",
        "sku": "{{sku}}",
        "features": [
            {
                "name": "WIFI",
                "value": "Yes | No"
            },
            {
                "name": "Cellular",
                "value": "Yes | No"
            },
            {
                "name": "OTA",
                "value": "Yes | No",
                "configs": [
                    {
                        "name": "OTADataPlaneProtocol",
                        "value": "HTTP | MQTT"
                    }
                ]
            },
            {
                "name": "BLE",
                "value": "Yes | No"
            },
            {
                "name": "TCP/IP",
                "value": "On-chip | Offloaded | No"
            },
            {
                "name": "TLS",
                "value": "Yes | No"
            },
            {
                "name": "PKCS11",
                "value": "RSA | ECC | Both | No"
            },
            {
                "name": "KeyProvisioning",
                "value": "Import | Onboard | No"
            }
        ],

        "devices": [
          {
            "id": "{{device-id}}",
            "connectivity": {
              "protocol": "uart",
              "serialPort": "/dev/tty{{*}}"
            },
            ***********Remove the section below if the device does not support onboard key generation***************
            "secureElementConfig" : {
              "publicKeyAsciiHexFilePath": "{{absolute-path-to/public-key-txt-file: contains-the-hex-bytes-public-key-extracted-from-onboard-private-key}}",
              "secureElementSerialNumber": "{{secure-element-serialNo-value}}",
              "preProvisioned"           : "Yes | No"
            },
            **********************************************************************************************************
            "identifiers": [
              {
                "name": "serialNo",
                "value": "{{serialNo-value}}"
              }
            ]
          }
        ]
    }
]
```

The following attributes are used in the `device.json` file:

**`id`**
A user-defined alphanumeric ID that uniquely identifies a pool of devices. Devices that belong to a pool must be of the same type. When a suite of tests is running, devices in the pool are used to parallelize the workload.

**`sku`**
An alphanumeric value that uniquely identifies the board you are testing. The SKU is used to track qualified boards.
If you want to list your board in AWS Partner Device Catalog, the SKU you specify here must match the SKU that you use in the listing process.

**`features`**
An array that contains the device's supported features. AWS IoT Device Tester uses this information to select the qualification tests to run.
Supported values are:
**`TCP/IP`**
Indicates if your board supports a TCP/IP stack and whether it is supported on-chip (MCU) or offloaded to another module. TCP/IP is required for qualification.
**`WIFI`**
Indicates if your board has Wi-Fi capabilities. Must be set to `No` if `Cellular` is set to `Yes`.
**`Cellular`**
Indicates if your board has cellular capabilities. Must be set to `No` if `WIFI` is set to `Yes`. When this feature is set to `Yes`, the FullSecureSockets test will be executed using AWS t2.micro EC2 instances and this may incur additional costs to your account. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).
**`TLS`**
Indicates if your board supports TLS. TLS is required for qualification.
**`PKCS11`**
Indicates the public key cryptography algorithm that the board supports. PKCS11 is required for qualification. Supported values are `ECC`, `RSA`, `Both` and `No`. `Both` indicates the board supports both the `ECC` and `RSA` algorithms.
**`KeyProvisioning`**
Indicates the method of writing a trusted X.509 client certificate onto your board. Valid values are `Import`, `Onboard` and `No`. Key provisioning is required for qualification.
+ Use `Import` if your board allows the import of private keys. IDT will create a private key and build this to the FreeRTOS source code.
+ Use `Onboard` if your board supports on-board private key generation (for example, if your device has a secure element, or if you prefer to generate your own device key pair and certificate). Make sure you add a `secureElementConfig` element in each of the device sections and put the absolute path to the public key file in the `publicKeyAsciiHexFilePath` field.
+ Use `No` if your board does not support key provisioning.
**`OTA`**
Indicates if your board supports over-the-air (OTA) update functionality. The `OtaDataPlaneProtocol` attribute indicates which OTA dataplane protocol the device supports. The attribute is ignored if the OTA feature is not supported by the device. When `"Both"` is selected, the OTA test execution time is prolonged due to running both MQTT, HTTP, and mixed tests.
Starting with IDT v4.1.0, `OtaDataPlaneProtocol` accepts only `HTTP` and `MQTT` as supported values.
**`BLE`**
Indicates if your board supports Bluetooth Low Energy (BLE).

**`devices.id`**
A user-defined unique identifier for the device being tested.

**`devices.connectivity.protocol`**
The communication protocol used to communicate with this device. Supported value: `uart`.

**`devices.connectivity.serialPort`**
The serial port of the host computer used to connect to the devices being tested.

**`devices.secureElementConfig.PublicKeyAsciiHexFilePath`**
The absolute path to the file that contains the hex bytes public key extracted from onboard private key.
Example format:

```
3059 3013 0607 2a86 48ce 3d02 0106 082a
8648 ce3d 0301 0703 4200 04cd 6569 ceb8
1bb9 1e72 339f e8cf 60ef 0f9f b473 33ac
6f19 1813 6999 3fa0 c293 5fae 08f1 1ad0
41b7 345c e746 1046 228e 5a5f d787 d571
dcb2 4e8d 75b3 2586 e2cc 0c
```
If your public key is in .der format, you can hex encode the public key directly to generate the hex file.
Example command for .der public key to generate hex file:

```
xxd -p pubkey.der > outFile
```
If your public key is in .pem format, you can extract the base64 encoded part, decode it into binary format, and then hex encode it to generate the hex file.
For example, use these commands to generate a hex file for a .pem public key:

1. Take out the base64 encoded part of the key (strip the header and footer ) and store it in a file, for example name it `base64key`, run this command to convert it to .der format:

   ```
   base64 —decode base64key > pubkey.der
   ```

1. Run the `xxd` command to convert it to hex format.

   ```
   xxd -p pubkey.der > outFile
   ```

**`devices.secureElementConfig.SecureElementSerialNumber`**
(Optional) The serial number of the secure element. Provide this field when the serial number is printed out along with the device public key when you run the FreeRTOS demo/test project.

**`devices.secureElementConfig.preProvisioned`**
(Optional) Set to "Yes" if the device has a pre-provisioned secure element with locked-down credentials, that cannot import, create, or destroy objects. This configuration takes effect only when `features` has `KeyProvisioning` set to "Onboard", along with `PKCS11` set to "ECC".

**`identifiers`**
(Optional) An array of arbitrary name-value pairs. You can use these values in the build and flash commands described in the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

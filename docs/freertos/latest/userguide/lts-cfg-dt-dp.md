---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-cfg-dt-dp.html
---

# Create a device pool in IDT for FreeRTOS
<a name="lts-cfg-dt-dp"></a>

Devices to be tested are organized in device pools. Each device pool consists of one or more identical devices. You can configure IDT for FreeRTOS to test a single device, or multiple devices in a pool. To accelerate the qualification process, IDT for FreeRTOS can test devices with the same specifications in parallel. It uses a round-robin method to execute a different test group on each device in a device pool.

The `device.json` file has an array in its top level. Each array attribute is a new device pool. Each device pool has a devices array attribute, which has multiple devices declared. In the template, there is a device pool and only one device in that device pool. You can add one or more devices to a device pool by editing the `devices` section of the `device.json` template in the `configs` folder.

**Note**
All devices in the same pool must be of the same technical specification and SKU. To enable parallel builds of the source code for different test groups, IDT for FreeRTOS copies the source code to a results folder inside the IDT for FreeRTOS extracted folder. You must reference the source code path in your build or flash command using the `testdata.sourcePath` variable. IDT for FreeRTOS replaces this variable with a temporary path of the copied source code. For more information, see [IDT for FreeRTOS variables](lts-dt-vars.md).

The following is an example `device.json` file was used to create a device pool with multiple devices.

```
[
    {
        "id": "pool-id",
        "sku": "sku",
        "features": [
           {
              "name": "Wifi",
              "value": "Yes | No"
           },
           {
              "name": "Cellular",
              "value": "Yes | No"
           },
           {
              "name": "BLE",
              "value": "Yes | No"
          },
          {
             "name": "PKCS11",
             "value": "RSA | ECC | Both"
          },
          {
              "name": "OTA",
              "value": "Yes | No",
              "configs": [
              {
                  "name": "OTADataPlaneProtocol",
                  "value": "MQTT | HTTP | None"
              }
            ]
          },
          {
             "name": "KeyProvisioning",
             "value": "Onboard | Import | Both | No"
          }
        ],
        "devices": [
          {
            "id": "device-id",
            "connectivity": {
              "protocol": "uart",
              "serialPort": "/dev/tty*"
            },
            "secureElementConfig" : {
              "publicKeyAsciiHexFilePath": "absolute-path-to/public-key-txt-file: contains-the-hex-bytes-public-key-extracted-from-onboard-private-key",
              "publiDeviceCertificateArn": "arn:partition:iot:region:account-id:resourcetype:resource:qualifier",
              "secureElementSerialNumber": "secure-element-serialNo-value",
              "preProvisioned"           : "Yes | No",
              "pkcs11JITPCodeVerifyRootCertSupport": "Yes | No"
            },
            "identifiers": [
              {
                "name": "serialNo",
                "value": "serialNo-value"
              }
            ]
          }
        ]
    }
]
```

The following attributes are used in the `device.json` file:

** `id` **
A user-defined alphanumeric ID that uniquely identifies a pool of devices. Devices that belong to a pool must be of the same type. When a suite of tests is running, devices in the pool are used to parallelize the workload.

** `sku` **
An alphanumeric value that uniquely identifies the board you are testing. The SKU is used to track qualified boards.
If you want to list your board in AWS Partner Device Catalog, the SKU you specify here must match the SKU that you use in the listing process.

** `features` **
An array that contains the device's supported features. AWS IoT Device Tester uses this information to select the qualification tests to run.
Supported values are:
** `Wifi` **
Indicates if your board has Wi-Fi capabilities.
** `Cellular` **
Indicates if your board has cellular capabilities.
** `PKCS11` **
Indicates the public key cryptography algorithm that the board supports. PKCS11 is required for qualification. Supported values are `ECC`, `RSA`, and `Both`. `Both` indicates the board supports both `ECC` and `RSA`.
** `KeyProvisioning` **
Indicates the method of writing a trusted X.509 client certificate onto your board.

Valid values are `Import`, `Onboard`, `Both` and `No`. `Onboard`, `Both`, or `No` key provisioning is required for qualification. `Import` alone is not a valid option for qualification.
+ Use `Import` only if your board allows the import of private keys. Selecting `Import` is not a valid configuration for qualification and should be used only for testing purposes, specifically with PKCS11 test cases. `Onboard`, `Both` or `No` is required for qualification.
+ Use `Onboard` if your board supports on-board private keys (for example, if your device has a secure element, or if you prefer to generate your own device key pair and certificate). Make sure you add a `secureElementConfig` element in each of the device sections and put the absolute path to the public key file in the `publicKeyAsciiHexFilePath` field.
+ Use `Both` if your board supports both importing private keys and on-board key generation for key provisioning.
+ Use `No` if your board doesn't support key provisioning. `No`is only a valid option when your device is also pre-provisioned.
** `OTA` **
Indicates if your board supports over-the-air (OTA) update functionality. The `OtaDataPlaneProtocol` attribute indicates which OTA dataplane protocol the device supports. OTA with either HTTP or MQTT dataplane protocol is required for qualification. To skip running OTA tests while testing, set the OTA feature to `No` and the `OtaDataPlaneProtocol` attribute to `None`. This will not be a qualification run.
** `BLE` **
Indicates if your board supports Bluetooth Low Energy (BLE).

** `devices.id` **
A user-defined unique identifier for the device being tested.

** `devices.connectivity.serialPort` **
The serial port of the host computer used to connect to the devices being tested.

** `devices.secureElementConfig.PublicKeyAsciiHexFilePath` **
Required if your board is NOT `pre-provisioned` or `PublicDeviceCertificateArn` is not provided. Since `Onboard`is a required type of Key Provisioning, this field is currently required for the FullTransportInterfaceTLS test group. If your device is `pre-provisioned`, `PublicKeyAsciiHexFilePath` is optional and need not be included.
The following block is an absolute path to the file that contains the hex bytes public key extracted from `Onboard` private key.

```
3059 3013 0607 2a86 48ce 3d02 0106 082a
8648 ce3d 0301 0703 4200 04cd 6569 ceb8
1bb9 1e72 339f e8cf 60ef 0f9f b473 33ac
6f19 1813 6999 3fa0 c293 5fae 08f1 1ad0
41b7 345c e746 1046 228e 5a5f d787 d571
dcb2 4e8d 75b3 2586 e2cc 0c
```
If your public key is in .der format, you can hex encode the public key directly to generate the hex file.
To generate the hex file from a .der public key, enter the following **xxd** command:

```
xxd -p pubkey.der > outFile
```
If your public key is in .pem format, you can extract the base64 encoded headers and footers and decode it into binary format. Then, you hex encode the binary string to generate the hex file.
To generate a hex file for a .pem public key, do the following:

1. Run the following **base64** command to remove the base64 header and footer from the public key. The decoded key, named `base64key`, is then output to the file `pubkey.der`:

   ```
   base64 —decode base64key > pubkey.der
   ```

1. Run the following **xxd** command to convert `pubkey.der` to hex format. The resulting key is saved as `{{outFile}}`

   ```
   xxd -p pubkey.der > {{outFile}}
   ```

** `devices.secureElementConfig.PublicDeviceCertificateArn` **
The ARN of the certificate from your secure element that is uploaded to AWS IoT Core. For information about uploading your certificate to AWS IoT Core, see [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) in the *AWS IoT Developer Guide*.

** `devices.secureElementConfig.SecureElementSerialNumber` **
(Optional) The serial number of the secure element. The serial number is optionally used to create device certificates for JITR key provisioning.

** `devices.secureElementConfig.preProvisioned` **
(Optional) Set to "Yes" if the device has a pre-provisioned secure element with locked-down credentials, that cannot import, create, or destroy objects. If this attribute is set to **Yes**, you must provide the corresponding pkcs11 labels.

** `devices.secureElementConfig.pkcs11JITPCodeVerifyRootCertSupport` **
(Optional) Set to **Yes** if the device’s corePKCS11 implementation supports storage for JITP. This will enable the JITP `codeverify` test when testing core PKCS 11, and requires code verification key, JITP certificate, and root certificate PKCS 11 labels to be provided.

** `identifiers` **
(Optional) An array of arbitrary name-value pairs. You can use these values in the build and flash commands described in the next section.

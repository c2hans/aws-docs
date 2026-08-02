---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/config-settings-device.html
---

# Configure settings for testing devices
<a name="config-settings-device"></a>

Build, flash, and test settings are made in the `configs/userdata.json` file. We support Echo Server configuration by loading both the client and server certificates and keys in the `customPath`. For more information, see [Setting up an echo server](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-echo-server.html) in the *FreeRTOS Porting Guide*. The following JSON example shows how you can configure IDT for FreeRTOS to test multiple devices:

```
{
    "sourcePath": "{{/absolute-path-to/freertos}}",
    "vendorPath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}",
    // ***********The sdkConfiguration block below is needed if you are not using the default, unmodified FreeRTOS repo.
    // In other words, if you are using the default, unmodified FreeRTOS repo then remove this block***************
    "sdkConfiguration": {
        "name": "{{sdk-name}}",
        "version": "{{sdk-version}}",
        "path": "{{/absolute-path-to/sdk}}"
    },
    "buildTool": {
        "name": "{{your-build-tool-name}}",
        "version": "{{your-build-tool-version}}",
        "command": [
            "{{{{config.idtRootPath}}/relative-path-to/build-parallel.sh}} {{testData.sourcePath}} {{enableTests}}"
        ]
    },
    "flashTool": {
        "name": "{{your-flash-tool-name}}",
        "version": "{{your-flash-tool-version}}",
        "command": [
            "/{{{{config.idtRootPath}}/relative-path-to/flash-parallel.sh}} {{testData.sourcePath}} {{device.connectivity.serialPort}} {{buildImageName}}"
        ],
        "buildImageInfo" : {
            "testsImageName": "{{tests-image-name}}",
            "demosImageName": "{{demos-image-name}}"
        }
    },
    "testStartDelayms": 0,
    "clientWifiConfig": {
        "wifiSSID": "{{ssid}}",
        "wifiPassword": "{{password}}",
        "wifiSecurityType": "eWiFiSecurityOpen | eWiFiSecurityWEP | eWiFiSecurityWPA | eWiFiSecurityWPA2 | eWiFiSecurityWPA3"
    },
    "testWifiConfig": {
        "wifiSSID": "{{ssid}}",
        "wifiPassword": "{{password}}",
        "wifiSecurityType": "eWiFiSecurityOpen | eWiFiSecurityWEP | eWiFiSecurityWPA | eWiFiSecurityWPA2 | eWiFiSecurityWPA3"
    },
    //**********
    //This section is used to start echo server based on server certificate generation method,
    //When certificateGenerationMethod is set as Automatic specify the eccCurveFormat to generate certifcate and key based on curve format,
    //When certificateGenerationMethod is set as Custom specify the certificatePath and PrivateKeyPath to be used to start echo server
    //**********
    "echoServerCertificateConfiguration": {
      "certificateGenerationMethod": "Automatic | Custom",
      "customPath": {
          "clientCertificatePath":"{{/path/to/clientCertificate}}",
          "clientPrivateKeyPath": "{{/path/to/clientPrivateKey}}",
          "serverCertificatePath":"{{/path/to/serverCertificate}}",
          "serverPrivateKeyPath": "{{/path/to/serverPrivateKey}}"
      },
    "eccCurveFormat": "P224 | P256 | P384 | P521"
    },
    "echoServerConfiguration": {
        "securePortForSecureSocket": {{33333}}, // Secure tcp port used by SecureSocket test. Default value is 33333. Ensure that the port configured isn't blocked by the firewall or your corporate network
        "insecurePortForSecureSocket": {{33334}}, // Insecure tcp port used by SecureSocket test. Default value is 33334. Ensure that the port configured isn't blocked by the firewall or your corporate network
        "insecurePortForWiFi": {{33335}} // Insecure tcp port used by Wi-Fi test. Default value is 33335. Ensure that the port configured isn't blocked by the firewall or your corporate network
    },
    "otaConfiguration": {
        "otaFirmwareFilePath": "{{testData.sourcePath}}/{{relative-path-to/ota-image-generated-in-build-process}}",
        "deviceFirmwareFileName": "{{ota-image-name-on-device}}",
        "otaDemoConfigFilePath": "{{testData.sourcePath}}/{{relative-path-to/ota-demo-config-header-file}}",
        "codeSigningConfiguration": {
            "signingMethod": "AWS | Custom",
            "signerHashingAlgorithm": "SHA1 | SHA256",
            "signerSigningAlgorithm": "RSA | ECDSA",
            "signerCertificate": "arn:{{partition}}:{{service}}:{{region}}:{{account-id}}:{{resource}}:{{qualifier}} | /{{absolute-path-to/signer-certificate-file}}",
            "signerCertificateFileName": "{{signerCertificate-file-name}}",
            "compileSignerCertificate": boolean,
            // ***********Use signerPlatform if you choose aws for signingMethod***************
            "signerPlatform": "AmazonFreeRTOS-Default | AmazonFreeRTOS-TI-CC3220SF",
            "untrustedSignerCertificate": "arn:{{partition}}:{{service}}:{{region}}:{{account-id}}:{{resourcetype}}:{{resource}}:{{qualifier}}",
            // ***********Use signCommand if you choose custom for signingMethod***************
            "signCommand": [
                "/{{absolute-path-to}}/sign.sh {{inputImageFilePath}} {{outputSignatureFilePath}}"
            ]
        }
    },
    // ***********Remove the section below if you're not configuring CMake***************
    "cmakeConfiguration": {
        "boardName": "{{board-name}}",
        "vendorName": "{{vendor-name}}",
        "compilerName": "{{compiler-name}}",
        "frToolchainPath": {{"/path/to/freertos/toolchain}}",
        "cmakeToolchainPath": "{{/path/to/cmake/toolchain}}"
    },
    "freertosFileConfiguration": {
        "required": [
            {
                "configName": "pkcs11Config",
                "filePath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}/aws_tests/config_files/core_pkcs11_config.h"
            },
            {
                "configName": "pkcs11TestConfig",
                "filePath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}/aws_tests/config_files/iot_test_pkcs11_config.h"
            }
        ],
        "optional": [
            {
                "configName": "otaAgentTestsConfig",
                "filePath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}/aws_tests/config_files/ota_config.h"
            },
            {
                "configName": "otaAgentDemosConfig",
                "filePath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}/aws_demos/config_files/ota_config.h"
            },
            {
                "configName": "otaDemosConfig",
                "filePath": "{{testData.sourcePath}}/vendors/{{vendor-name}}/boards/{{board-name}}/aws_demos/config_files/ota_demo_config.h"
            }
        ]
    }
}
```

The following lists the attributes used in `userdata.json`:

**`sourcePath`**
The path to the root of the ported FreeRTOS source code. For parallel testing with an SDK, the `sourcePath` can be set using the `{{userData.sdkConfiguration.path}}` place holder. For example:

```
{ "sourcePath":"{{userData.sdkConfiguration.path}}/{{freertos}}" }
```

**`vendorPath`**
The path to the vendor specific FreeRTOS code. For serial testing, the `vendorPath` can be set as an absolute path. For example:

```
{ "vendorPath":"C:/{{path-to-freertos}}/vendors/espressif/boards/{{esp32}}" }
```
For parallel testing, the `vendorPath` can be set using the `{{testData.sourcePath}}` place holder. For example:

```
{ "vendorPath":"{{testData.sourcePath}}/vendors/espressif/boards/esp32" }
```
The `vendorPath` variable is only necessary when running without an SDK, it can be removed otherwise.
When running tests in parallel without an SDK, the `{{testData.sourcePath}}` placeholder must be used in the `vendorPath`, `buildTool`, `flashTool` fields. When running test with a single device, absolute paths must be used in the `vendorPath`, `buildTool`, `flashTool` fields. When running with an SDK, the `{{sdkPath}}` placeholder must be used in the `sourcePath`, `buildTool`, and `flashTool` commands.

**`sdkConfiguration`**
If you are qualifying FreeRTOS with any modifications to files and folder structure beyond what is required for porting, then you will need to configure your SDK information in this block. If you're not qualifying with a ported FreeRTOS inside of an SDK, then you should omit this block entirely.
**`sdkConfiguration.name`**
The name of the SDK you're using with FreeRTOS. If you're not using an SDK, then the entire `sdkConfiguration` block should be omitted.
**`sdkConfiguration.version`**
The version of the SDK you're using with FreeRTOS. If you're not using an SDK, then the entire `sdkConfiguration` block should be omitted.
**`sdkConfiguration.path`**
The absolute path to your SDK directory that contains your FreeRTOS code. If you're not using an SDK, then the entire `sdkConfiguration` block should be omitted.

**`buildTool`**
The full path to your build script (.bat or .sh) that contains the commands to build your source code. All references to the source code path in the build command must be replaced by the AWS IoT Device Tester variable `{{testdata.sourcePath}}` and references to the SDK path should be replaced by `{{sdkPath}}`. Use the `{{config.idtRootPath}}` placeholder to reference the absolute or relative IDT path.

**`testStartDelayms`**
Specifies how many milliseconds the FreeRTOS test runner will wait before starting to run tests. This can be useful if the device under test begins outputting important test information before IDT has a chance to connect and start logging due to network or other latency. The max allowed value is 30000 ms (30 seconds). This value is applicable to FreeRTOS test groups only, and not applicable to other test groups that do not utilize the FreeRTOS test runner, such as the OTA tests.

**`flashTool`**
Full path to your flash script (.sh or .bat) that contains the flash commands for your device. All references to the source code path in the ﬂash command must be replaced by the IDT for FreeRTOS variable `{{testdata.sourcePath}}` and all references to your SDK path must be replaced by the IDT for FreeRTOS variable `{{sdkPath}}`.Use the `{{config.idtRootPath}}` placeholder to reference the absolute or relative IDT path.
**`buildImageInfo`**
**`testsImageName`**
The name of the file produced by the build command when building tests from the `{{freertos-source}}/tests` folder.
**`demosImageName`**
The name of the file produced by the build command when building tests from the `{{freertos-source}}/demos` folder.

**`clientWifiConfig`**
The client Wi-Fi configuration. The Wi-Fi library tests require an MCU board to connect to two access points. (The two access points can be the same.) This attribute configures the Wi-Fi settings for the first access point. Some of the Wi-Fi test cases expect the access point to have some security and not to be open. Please make sure both access points are on the same subnet as the host computer running IDT.
**`wifi_ssid`**
The Wi-Fi SSID.
**`wifi_password`**
The Wi-Fi password.
**`wifiSecurityType`**
The type of Wi-Fi security used. One of the values:
+ `eWiFiSecurityOpen`
+ `eWiFiSecurityWEP`
+ `eWiFiSecurityWPA`
+ `eWiFiSecurityWPA2`
+ `eWiFiSecurityWPA3`
If your board does not support Wi-Fi, you must still include the `clientWifiConfig` section in your `device.json` file, but you can omit values for these attributes.

**`testWifiConfig`**
The test Wi-Fi configuration. The Wi-Fi library tests require an MCU board to connect to two access points. (The two access points can be the same.) This attribute configures the Wi-Fi setting for the second access point. Some of the Wi-Fi test cases expect the access point to have some security and not to be open. Please make sure both access points are on the same subnet as the host computer running IDT.
**`wifiSSID`**
The Wi-Fi SSID.
**`wifiPassword`**
The Wi-Fi password.
**`wifiSecurityType`**
The type of Wi-Fi security used. One of the values:
+ `eWiFiSecurityOpen`
+ `eWiFiSecurityWEP`
+ `eWiFiSecurityWPA`
+ `eWiFiSecurityWPA2`
+ `eWiFiSecurityWPA3`
If your board does not support Wi-Fi, you must still include the `testWifiConfig` section in your `device.json` file, but you can omit values for these attributes.

**`echoServerCertificateConfiguration`**
The configurable echo server certificate generation placeholder for secure socket tests. This field is required.
**`certificateGenerationMethod`**
Specifies whether the server certificate is generated automatically or provided manually.
**`customPath`**
If `certificateGenerationMethod` is "Custom", `certificatePath` and `privateKeyPath` are required.
**`certificatePath`**
Specifies the filepath for the server certificate.
**`privateKeyPath`**
Specifies the filepath for the private key.
**`eccCurveFormat`**
Specifies the curve format supported by the board. Required when `PKCS11` is set to "ecc" in `device.json`. Valid values are "P224", "P256", "P384", or "P521".

**`echoServerConfiguration`**
The configurable echo server ports for WiFi and secure sockets tests. This field is optional.
**`securePortForSecureSocket`**
The port which is used to setup an echo server with TLS for the secure sockets test. The default value is 33333. Ensure the port configured is not blocked by a firewall or your corporate network.
**`insecurePortForSecureSocket`**
The port which is used to setup echo server without TLS for the secure sockets test. The default value used in the test is 33334. Ensure the port configured is not blocked by a firewall or your corporate network.
**`insecurePortForWiFi`**
The port which is used to setup echo server without TLS for WiFi test. The default value used in the test is 33335. Ensure the port configured is not blocked by a firewall or your corporate network.

**`otaConfiguration`**
The OTA configuration. [Optional]
**`otaFirmwareFilePath`**
The full path to the OTA image created after the build. For example, `{{testData.sourcePath}}/{{relative-path/to/ota/image/from/source/root}}`.
**`deviceFirmwareFileName`**
The full file path on the MCU device where the OTA firmware is located. Some devices do not use this field, but you still must provide a value.
**`otaDemoConfigFilePath`**
The full path to `aws_demo_config.h`, found in `{{afr-source}}/vendors/vendor/boards/board/aws_demos/config_files/`. These files are included in the porting code template that FreeRTOS provides.
**`codeSigningConfiguration`**
The code signing configuration.
**`signingMethod`**
The code signing method. Possible values are `AWS` or `Custom`.
For the Beijing and Ningxia Regions, use `Custom`. `AWS` code signing isn't supported in these Regions.
**`signerHashingAlgorithm`**
The hashing algorithm supported on the device. Possible values are `SHA1` or `SHA256`.
**`signerSigningAlgorithm`**
The signing algorithm supported on the device. Possible values are `RSA` or `ECDSA`.
**`signerCertificate`**
The trusted certificate used for OTA.
For AWS code signing method, use the Amazon Resource Name (ARN) for the trusted certificate uploaded to the AWS Certificate Manager.
For Custom code signing method, use the absolute path to the signer certificate file.
For more information about creating a trusted certificate, see [Create a code-signing certificate](ota-code-sign-cert.md).
**`signerCertificateFileName`**
The file name of the code signing certificate on the device. This value must match the file name that you provided when you ran the `aws acm import-certificate` command.
For more information, see [Create a code-signing certificate](ota-code-sign-cert.md).
**`compileSignerCertificate`**
Set to `true` if the code signer signature verification certificate isn't provisioned or flashed, so it must be compiled into the project. AWS IoT Device Tester fetches the trusted certificate and compiles it into `aws_codesigner_certifiate.h`.
**`untrustedSignerCertificate`**
The ARN or filepath for a second certificate used in some OTA tests as an untrusted certificate. For more information about creating a certificate, see [ Create a code-signing certificate](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert.html).
**`signerPlatform`**
The signing and hashing algorithm that AWS Code Signer uses while creating the OTA update job. Currently, the possible values for this field are `AmazonFreeRTOS-TI-CC3220SF` and `AmazonFreeRTOS-Default`.
+ Choose `AmazonFreeRTOS-TI-CC3220SF` if `SHA1` and `RSA`.
+ Choose `AmazonFreeRTOS-Default` if `SHA256` and `ECDSA`.
If you need `SHA256` \| `RSA` or `SHA1` \| `ECDSA` for your configuration, contact us for further support.
Configure `signCommand` if you chose `Custom` for `signingMethod`.
**`signCommand`**
The command used to perform custom code signing. You can find the template in the `/configs/script_templates` directory.
Two placeholders `{{inputImageFilePath}}` and `{{outputSignatureFilePath}}` are required in the command. `{{inputImageFilePath}}` is the file path of the image built by IDT to be signed. `{{outputSignatureFilePath}}` is the file path of the signature which will be generated by the script.

**`cmakeConfiguration`**
CMake configuration [Optional]
To execute CMake test cases, you must provide the board name, vendor name, and either the `frToolchainPath` or `compilerName`. You may also provide the `cmakeToolchainPath` if you have a custom path to the CMake toolchain.
**`boardName`**
The name of the board under test. The board name should be the same as the folder name under `{{path/to/afr/source/code}}/vendors/{{vendor}}/boards/{{board}}`.
**`vendorName`**
The vendor name for the board under test. The vendor should be the same as the folder name under `{{path/to/afr/source/code}}/vendors/{{vendor}}`.
**`compilerName`**
The compiler name.
**`frToolchainPath`**
The fully-qualified path to the compiler toolchain
**`cmakeToolchainPath` **
The fully-qualified path to the CMake toolchain. This field is optional

**`freertosFileConfiguration`**
The configuration of the FreeRTOS files that IDT modifies before running tests.
**`required`**
This section specifies required tests whose config files you have moved, for example, PKCS11, TLS, and so on.
**`configName`**
The name of the test that is being configured.
**`filePath`**
The absolute path to the configuration files within the `{{freertos}}` repo. Use the `{{testData.sourcePath}}` variable to define the path.
**`optional`**
This section specifies optional tests whose config files you have moved, for example OTA, WiFi, and so on.
**`configName`**
The name of the test that is being configured.
**`filePath`**
The absolute path to the configuration files within the `{{freertos}}` repo. Use the `{{testData.sourcePath}}` variable to define the path.

**Note**
To execute CMake test cases, you must provide the board name, vendor name, and either the `afrToolchainPath` or `compilerName`. You may also provide `cmakeToolchainPath` if you have a custom path to the CMake toolchain.

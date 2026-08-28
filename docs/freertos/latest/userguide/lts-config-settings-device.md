---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-config-settings-device.html
---

# Configure settings for testing devices
<a name="lts-config-settings-device"></a>

Build, flash, and test settings are made in the `configs/userdata.json` file. The following JSON example shows how you can configure IDT for FreeRTOS to test multiple devices:

```
{
    "sourcePath": "</path/to/freertos>",
    "retainModifiedSourceDirectories": true | false,
    "freeRTOSVersion": "<freertos-version>",
    "freeRTOSTestParamConfigPath": "{{testData.sourcePath}}/path/from/source/path/to/test_param_config.h",
    "freeRTOSTestExecutionConfigPath": "{{testData.sourcePath}}/path/from/source/path/to/test_execution_config.h",
    "buildTool": {
        "name": "your-build-tool-name",
        "version": "your-build-tool-version",
        "command": [
            "<build command> -any-additional-flags {{testData.sourcePath}}"
        ]
    },
    "flashTool": {
        "name": "your-flash-tool-name",
        "version": "your-flash-tool-version",
        "command": [
            "<flash command> -any-additional-flags {{testData.sourcePath}} -any-additional-flags"
        ]
    },
    "testStartDelayms": 0,
    "echoServerConfiguration": {
      "keyGenerationMethod": "EC | RSA",
      "serverPort": 9000
    },
    "otaConfiguration": {
        "otaE2EFirmwarePath": "{{testData.sourcePath}}/relative-path-to/ota-image-generated-in-build-process",
        "otaPALCertificatePath": "/path/to/ota/pal/certificate/on/device",
        "deviceFirmwarePath" : "/path/to/firmware/image/name/on/device",
        "codeSigningConfiguration": {
            "signingMethod": "AWS | Custom",
            "signerHashingAlgorithm": "SHA1 | SHA256",
            "signerSigningAlgorithm": "RSA | ECDSA",
            "signerCertificate": "arn:partition:service:region:account-id:resource:qualifier | /absolute-path-to/signer-certificate-file",
            "untrustedSignerCertificate": "arn:partition:service:region:account-id:resourcetype:resource:qualifier",
            "signerCertificateFileName": "signerCertificate-file-name",
            "compileSignerCertificate": true | false,
            // ***********Use signerPlatform if you choose AWS for signingMethod***************
            "signerPlatform": "AmazonFreeRTOS-Default | AmazonFreeRTOS-TI-CC3220SF"
            ]
         }
    },
    **********
    This section is used for PKCS #11 labels of private key, public key, device certificate, code verification key, JITP certificate, and root certificate.
    When configuring PKCS11, you set up labels and you must provide the labels of the device certificate, public key,
    and private key for the key generation type (EC or RSA) it was created with. If your device supports PKCS11 storage of JITP certificate,
    code verification key, and root certificate, set 'pkcs11JITPCodeVerifyRootCertSupport' to 'Yes' in device.json and provide the corresponding labels.
    **********
    "pkcs11LabelConfiguration":{
        "pkcs11LabelDevicePrivateKeyForTLS": "<device-private-key-label>",
        "pkcs11LabelDevicePublicKeyForTLS": "<device-public-key-label>",
        "pkcs11LabelDeviceCertificateForTLS": "<device-certificate-label>",
        "pkcs11LabelPreProvisionedECDevicePrivateKeyForTLS": "<preprovisioned-ec-device-private-key-label>",
        "pkcs11LabelPreProvisionedECDevicePublicKeyForTLS": "<preprovisioned-ec-device-public-key-label>",
        "pkcs11LabelPreProvisionedECDeviceCertificateForTLS": "<preprovisioned-ec-device-certificate-label>",
        "pkcs11LabelPreProvisionedRSADevicePrivateKeyForTLS": "<preprovisioned-rsa-device-private-key-label>",
        "pkcs11LabelPreProvisionedRSADevicePublicKeyForTLS": "<preprovisioned-rsa-device-public-key-label>",
        "pkcs11LabelPreProvisionedRSADeviceCertificateForTLS": "<preprovisioned-rsa-device-certificate-label>",
        "pkcs11LabelCodeVerifyKey": "<code-verification-key-label>",
        "pkcs11LabelJITPCertificate": "<JITP-certificate-label>",
        "pkcs11LabelRootCertificate": "<root-certificate-label>"
     }
  }
```

The following lists the attributes used in `userdata.json`:

**  `sourcePath` **
The path to the root of the ported FreeRTOS source code.

**  `retainModifiedSourceDirectories` **
(Optional) Checks if to retain the modified source directories used during building and flashing for debugging purposes. If set to `true`, the modified source directories are named retainedSrc and found within the results log folders in each test group run. If not included, the field defaults to `false`.

**  `freeRTOSTestParamConfigPath` **
The path to `test_param_config.h` file for FreeRTOS-Libraries-Integration-Tests integration. This file must use the `{{testData.sourcePath}}` placeholder variable to make it relative to the source code root. AWS IoT Device Tester uses the parameters in this file to configure the tests.

**  `freeRTOSTestExecutionConfigPath` **
The path to `test_execution_config.h` file for FreeRTOS-Libraries-Integration-Tests integration. This file must use the `{{testData.sourcePath}}` placeholder variable to make it relative to the repository root. AWS IoT Device Tester uses this file to control which tests must run.

**  `freeRTOSVersion` **
The version of FreeRTOS including the patch version used in your implementation. See [Supported versions of AWS IoT Device Tester for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html) for the FreeRTOS versions compatible with AWS IoT Device Tester for FreeRTOS.

**  `buildTool` **
The command to build your source code. All references to the source code path in the build command must be replaced by the AWS IoT Device Tester variable `{{testData.sourcePath}}`. Use the `{{config.idtRootPath}}` placeholder to reference a build script relative to the AWS IoT Device Tester root path.

**  `flashTool` **
The command to flash an image to your device. All references to the source code path in the ﬂash command must be replaced by the AWS IoT Device Tester variable `{{testData.sourcePath}}`. Use the `{{config.idtRootPath}}` placeholder to reference a flash script relative to the AWS IoT Device Tester root path.
The new integration tests structure with FRQ 2.0 doesn't require path variables such as `{{enableTests}}` and `{{buildImageName}}`. The OTA End to End tests are run with the config templates provided in the [ FreeRTOS-Libraries-Integration-Tests](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/config_template/) GitHub repository. If the files in the GitHub repository are present in your parent source project, the source code isn't changed between tests. If a different build image for OTA End to End is needed, you must build this image in the build script and specify it in the `userdata.json` file specified under `otaConfiguration`.

**  `testStartDelayms` **
Specifies how many milliseconds the FreeRTOS test runner will wait before starting to run tests. This can be useful if the device under test begins to output important test information before IDT has a chance to connect and start logging due to network or other latency issues. This value is applicable to FreeRTOS test groups only, and not to other test groups that do not utilize the FreeRTOS test runner, such as the OTA tests. If you receive an error related to **expected 10 but received 5**, this field should be set to 5000.

**  `echoServerConfiguration` **
The configuration to setup the echo server for the TLS test. This field is required.
** `keyGenerationMethod` **
The echo server is configured with this option. The options are EC, or RSA.
** `serverPort` **
The port number on which the echo server runs.

**  `otaConfiguration` **
The configuration for OTA PAL and OTA E2E tests. This field is required.
**`otaE2EFirmwarePath`**
Path to the OTA bin image that IDT uses for the OTA End to End tests.
** `otaPALCertificatePath` **
The path to the certificate for OTA PAL test on device. This is used to verify the signature. For example, **ecdsa-sha256-signer.crt.pem**.
** `deviceFirmwarePath` **
The path to the hard coded name for the firmware image to boot. If your device does NOT use the file system for firmware boot, specify this field as `'NA'`. If your device uses the file system for firmware boot, specify the path or name to the firmware boot image.
** `codeSigningConfiguration` **
** `signingMethod` **
The code signing method. Possible values are AWS or Custom.
For the Beijing and Ningxia Regions, use Custom. AWS code signing is not supported in that region.
** `signerHashingAlgorithm` **
The hashing algorithm supported on the device. Possible values are `SHA1` or `SHA256`.
** `signerSigningAlgorithm` **
The signing algorithm supported on the device. Possible values are `RSA` or `ECDSA`.
** `signerCertificate` **
The trusted certificate used for OTA. For the AWS code signing method, use the Amazon Resource Name (ARN) for the trusted certificate uploaded to the AWS Certificate Manager. For the Custom code signing method, use the absolute path to the signer certificate file. For information about creating a trusted certificate, see [ Create a code-signing certificate](https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert.html).
** `untrustedSignerCertificate` **
The ARN or filepath for a second certificate used in some OTA tests as an untrusted certificate. For information about creating a certificate, see [ Create a code-signing certificate](https://docs.aws.amazon.com//freertos/latest/userguide/ota-code-sign-cert.html).
** `signerCertificateFileName` **
The file name of the code signing certificate on the device. This value must match the file name that you provided when you ran the `aws acm import-certificate` command.
** `compileSignerCertificate` **
Boolean value that determines the status of the signature verification certificate. Valid values are `true` and `false`.
Set this value to **true** if the code signer signature verification certificate is not provisioned or flashed. It must be compiled into the project. AWS IoT Device Tester fetches the trusted certificate and compiles it into `aws_codesigner_certificate.h`.
** `signerPlatform` **
The signing and hashing algorithm that AWS Code Signer uses while creating the OTA update job. Currently, the possible values for this field are `AmazonFreeRTOS-TI-CC3220SF` and `AmazonFreeRTOS-Default`.
+ Choose `AmazonFreeRTOS-TI-CC3220SF` if `SHA1` and `RSA`.
+ Choose `AmazonFreeRTOS-Default` if `SHA256` and `ECDSA`.
+ If you need `SHA256` \| `RSA` or `SHA1` \| `ECDSA` for your configuration, contact us for further support.
+ Configure `signCommand` if you chose `Custom` for `signingMethod`.
** `signCommand` **
Two placeholders `{{inputImageFilePath}}` and `{{outputSignatureFilePath}}` are required in the command. `{{inputImageFilePath}}` is the file path of the image built by IDT to be signed. `{{outputSignatureFilePath}} `is the file path of the signature which will be generated by the script.

**  `pkcs11LabelConfiguration` **
PKCS11 label configuration requires at least one set of labels of device certificate label, public key label, and private key label to run the PKCS11 test groups. The required PKCS11 labels are based on your device configuration in the `device.json` file. If pre-provisioned is set to **Yes** in `device.json`, then the required labels must be one of the below depending on what's chosen for the PKCS11 feature.
+ `PreProvisionedEC`
+ `PreProvisionedRSA`
If pre-provisioned is set to **No** in `device.json`, then the required labels are:
+ `pkcs11LabelDevicePrivateKeyForTLS`
+ `pkcs11LabelDevicePublicKeyForTLS`
+ `pkcs11LabelDeviceCertificateForTLS`
The following three labels are required only if you select **Yes** for `pkcs11JITPCodeVerifyRootCertSupport` in your `device.json` file.
+ `pkcs11LabelCodeVerifyKey`
+ `pkcs11LabelRootCertificate`
+ `pkcs11LabelJITPCertificate`
The values for these fields should match the values defined in the [FreeRTOS Porting Guide](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-pkcs.html).
** `pkcs11LabelDevicePrivateKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the private key. For devices with onboard and import support of key provisioning, this label is used for testing. This label may be different than the one defined for the pre-provisioned case. If you have key provisioning set to **No** and pre-provisioned set to **Yes**, in `device.json`, this will be undefined.
** `pkcs11LabelDevicePublicKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the public key. For devices with onboard and import support of key provisioning, this label is used for testing. This label may be different than the one defined for pre-provisioned case. If you have key provisioning set to **No** and pre-provisioned set to **Yes**, in `device.json`, this will be undefined.
** `pkcs11LabelDeviceCertificateForTLS` **
(Optional) This label is used for the PKCS \#11 label of the device certificate. For devices with onboard and import support of key provisioning, this label will be used for testing. This label may be different than the one defined for pre-provisioned case. If you have key provisioning set to **No** and pre-provisioned set to **Yes**, in `device.json`, this will be undefined.
** `pkcs11LabelPreProvisionedECDevicePrivateKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the private key. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an EC key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedRSADevicePrivateKeyForTLS`, or both must be provided. This label may be different than the one defined for onboard and import cases.
** `pkcs11LabelPreProvisionedECDevicePublicKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the public key. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an EC key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedRSADevicePublicKeyForTLS`, or both must be provided. This label may be different than the one defined for onboard and import cases.
** `pkcs11LabelPreProvisionedECDeviceCertificateForTLS` **
(Optional) This label is used for the PKCS \#11 label of the device certificate. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an EC key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedRSADeviceCertificateForTLS`, or both must be provided. This label may be different than the one defined for onboard and import cases.
** `pkcs11LabelPreProvisionedRSADevicePrivateKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the private key. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an RSA key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedECDevicePrivateKeyForTLS`, or both must be provided.
** `pkcs11LabelPreProvisionedRSADevicePublicKeyForTLS` **
(Optional) This label is used for the PKCS \#11 label of the public key. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an RSA key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedECDevicePublicKeyForTLS`, or both must be provided.
** `pkcs11LabelPreProvisionedRSADeviceCertificateForTLS` **
(Optional) This label is used for the PKCS \#11 label of the device certificate. For devices with secure elements or hardware limitations, this will have a different label to preserve AWS IoT credentials. If your device supports pre-provisioning with an RSA key, provide this label. When preProvisioned is set to **Yes** in `device.json`, this label, `pkcs11LabelPreProvisionedECDeviceCertificateForTLS`, or both must be provided.
** `pkcs11LabelCodeVerifyKey` **
(Optional) This label is used for the PKCS \#11 label of the code verification key. If your device has PKCS \#11 storage support of the JITP certificate, code verification key, and root certificate, provide this label. When `pkcs11JITPCodeVerifyRootCertSupport` in `device.json` is set to **Yes**, this label must be provided.
** `pkcs11LabelJITPCertificate` **
(Optional) This label is used for the PKCS \#11 label of the JITP certificate. If your device has PKCS \#11 storage support of the JITP certificate, code verification key, and root certificate, provide this label. When `pkcs11JITPCodeVerifyRootCertSupport` in `device.json` is set to **Yes**, this label must be provided.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

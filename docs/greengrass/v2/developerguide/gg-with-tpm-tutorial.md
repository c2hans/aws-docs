---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-with-tpm-tutorial.html
---

# Tutorial: Secure Greengrass Nucleus with Trusted Platform Module (TPM)
<a name="gg-with-tpm-tutorial"></a>

**Note**
The mechanism in this tutorial is supported only with [Install AWS IoT Greengrass Core software with manual resource provisioning](manual-installation.md).

These tutorials contain instructions on how to use the TPM2 chip as an Hardware Security Module(HSM) to create a private key and CSR. Which is used to [Create the thing certificate](manual-installation.md#create-thing-certificate).

These tutorials show you how to enhance device security by configuring AWS IoT Greengrass Core software (Greengrass Nucleus) with a Trusted Platform Module (TPM) using the PKCS\#11 interface. This TPM integration ensures that private keys and certificates used for device identity and connecting to AWS IoT Core are securely stored in tamper-proof hardware, preventing extraction for impersonation or other malicious activities.

When you complete this integration, your Greengrass core device will use TPM-protected private keys for its identity and communication with AWS IoT services.

For more information about security on Greengrass devices, see [Security in AWS IoT Greengrass](security.md).

## Prerequisites
<a name="prerequisites"></a>

To complete this tutorial, you need the following:
+ A Linux-compatible device with TPM 2.0 hardware or firmware TPM 2.0.
+ Instructions in this tutorial are defined for Ubuntu 24.04 LTS.
  + Any Linux distribution that can support the [Linux TPM2 Software Stack](https://tpm2-software.github.io/) can support this mechanism.
+ A developer machine with AWS CLI installed and configured with permissions to:
  + Create and manage AWS IoT resources
  + Create and manage IAM roles and policies
+ Java Runtime Environment (JRE) version 8 or later installed on your device.
+ The following software packages installed on your device:
  + curl
  + jq
+ Root or sudo privileges on the device.

## Step 1: Install TPM2 tools and dependencies
<a name="tpm_step1"></a>

In this step, you install the necessary TPM2 software tools and libraries.

1. Update your package manager and install the TPM2 tools and dependencies by running the following command.

   ```
   sudo apt-get update && sudo apt-get install tpm2-tools \
   tpm2-abrmd \
   tpm2-tss-engine-tools \
   gnutls-bin \
   libtpm2-pkcs11-1 \
   libtpm2-pkcs11-tools \
   libtpm2-pkcs11-1-dev \
   python3-tpm2-pkcs11-tools \
   libengine-pkcs11-openssl \
   libtss2-tcti-tabrmd0
   ```

1. Install the OpenSSL TPM2 provider packages on Ubuntu 24.04 that use OpenSSL engine 3.

   ```
   sudo apt-get install tpm2-openssl
   ```

## Step 2: Initialize PKCS\#11 store and create a slot
<a name="tpm_step2"></a>

1. Create a directory to store data.

   ```
   sudo mkdir -p /etc/tpm2_pkcs11
   ```

1. Set the storage location as an environment variable. For more information about the store hierarchy, see [Initialization](https://github.com/tpm2-software/tpm2-pkcs11/blob/master/docs/INITIALIZING.md#initialization).

   ```
   export TPM2_PKCS11_STORE=/etc/tpm2_store
   ```

1. Initialize the TPM2 token with the primary object.

   ```
   sudo tpm2_ptool init
   ```

   The options available are the following:
`hierarchy-auth HIERARCHY_AUTH`
The authorization password for adding a primary object to the hierarchy.
`primary-auth PRIMARY_AUTH`
Authorization value for existing primary key object.
Default is an empty auth value.
`primary-handle [PRIMARY_HANDLE]`
Use an existing primary key object.
Default: `0x81000001`
`transient-parents`
Use a transient primary object of a given template.
Values: `tpm2-tools-default`,`tpm2-tools-ecc-default`,`tss2-engine-key`
`path PATH`
The location of the store directory. If specified, the directory must exist. If not specified, it performs a search by looking at environment variable `TPM2_PKCS11_STORE`. If that environment variable is not set, it will look at `/etc/tpm2_pkcs11`. If that directory is not found or can't be created, it defaults to the current working directory.

## Step 3: Create a token and a key
<a name="tpm_step3"></a>

1. Create a PKCS\#11 token.

   ```
   sudo tpm2_ptool addtoken —pid=1 —userpin={{USERPIN}} —sopin={{SOPIN}} —label=greengrass
   ```

   The available options are the following:
`--pid PID`
The primary object id to associate with this token.
`--sopin SOPIN`
The Administrator pin. This pin is used for object recovery.
`--userpin USERPIN`
The user pin. This pin is used for authentication for object use.
`--label LABEL`
A unique label to identify the profile in use, must be unique.
`--hierarchy-auth HIERARCHY_AUTH`

1. Create an ECC key object.

   ```
   sudo tpm2_ptool addkey —algorithm=ecc256 —label=greengrass —userpin=****** —key-label=greenkey
   ```
`--label LABEL`
The tokens label to import the key too.
`--key-label KEY_LABEL`
The label of the key imported. Defaults to an integer value.
`--id ID`
The key id. Defaults to a random 8 bytes of hex.
`--attr-always-authenticate`
Sets the CKA\_ALWAYS\_AUTHENTICATE attribute to CK\_TRUE.
`--hierarchy-auth HIERARCHY_AUTH`
The hierarchyauth, required for transient pobjects.
`--sopin SOPIN`
The Administrator pin.
`--userpin USERPIN`
The User pin.
`--algorithm`
{rsa1024,rsa2048,rsa3072,rsa4096,aes128,aes256,ecc224,ecc256,ecc384,ecc521,hmac:sha1,hmac:sha256,hmac:sha384,hmac:sha512}
 The type of the key.

1. Export the TPM2-TSS object from the token to capture the authentication data.

   ```
   yaml_ecc0=$(sudo tpm2_ptool export —label="greengrass" —key-label="greenkey" —userpin="******")
   ```

   Example output:

   ```
   > echo $yaml_ecc0
   object-auth: 706c1cad8a5238871b30149705255926
   primary-object:
     auth: ''
     hierarchy: owner
     is_transient: false
   ```
**Note**
You will also find a file named `greenkey.pem` which is the TSS2 Private Key in the directory where you ran this command. Use this to generate the CSR with the tpm2 openssl provider. The TSS2 PRIVATE KEY file is protected by the TPM and cannot be used on another machine. For more information about TSS2 keys with OpenSSL, see [Storing the Private or Public Key](https://github.com/tpm2-software/tpm2-openssl/blob/master/docs/keys.md#storing-the-private-or-a-public-key).

1. Capture the authentication data for the TSS private key.

   ```
   auth_ecc0=$(echo "$yaml_ecc0" | grep "object-auth" | cut -d' ' -f2-)
   ```

## Step 4: Generate Certificate Signing Request(CSR)
<a name="step4"></a>

In this step, you'll use the TPM2-protected private key to generate a CSR.

1. Generate a CSR using the TPM2 provider.

   ```
   sudo openssl req -new -provider tpm2 -provider base -key greenkey.pem -passin "pass:$auth_ecc0" -out "$H"$HOSTNAME".csr
   ```

   When prompted, provide the required information for your CSR, including:
   + Country Name (2 letter code)
   + State or Province Name
   + Locality Name
   + Organization Name
   + Organizational Unit Name
   + Common Name
   + Email Address

   Alternatively, you can supply an OpenSSL config file for unattended generation. For more information, see [OpenSSL Documentation](https://docs.openssl.org/3.0/man1/openssl-req/#standard-commands).

1. If you're not generating the CSR on the same machine, copy the generated CSR to a machine that has AWS credentials configured.

## Step 5: Create the thing certificate
<a name="step5"></a>

Create an AWS IoT thing certificate. For more information about how to create a thing certificate, see [Create the thing certificate](manual-installation.md#create-thing-certificate).

## Step 6: Import thing certificate to TPM
<a name="step6"></a>

1. Copy the thing certificate to the device.

1. Add the thing certificate to the Greengrass token.

   ```
   sudo tpm2_ptool addcert --label=greengrass --key-label=greenkey device.pem.crt
   ```

   The available options are the following:
`--help`
Show this help message and exit.
`--label LABEL`
The profile label to remove.
`--key-label KEY_LABEL`
The associated private key label.
`--key-id KEY_ID`
The associated private key id in hex.
`cert`
The x509 PEM certificate to add.

## Step 7: Capture the PKCS\#11 object URL
<a name="step7"></a>

We will use the `p11tool` provided from the `gnutls-bin` package to get the PKCS\#11 token URL and object URLs.

1. Capture the token URL for the Greengrass token.

   ```
   TOKEN=sudo p11tool --list-token-urls | grep "token=greengrass"
   ```

1. Get the object URLs for the Greengrass token. Use the same pin you used in Step 3.

   ```
   sudo p11tool --login --list-all "${TOKEN}"
   ```

   Example output:

   ```
   Token 'greengrass' with URL 'pkcs11:model=SLB9672%00%00%00%00%00%00%00%00%00;manufacturer=Infineon;serial=0000000000000000;token=greengrass' requires user PIN
   Enter PIN:
   WARNING: Needed CKA_VALUE but didn't find encrypted blob
   Object 0:
           URL: pkcs11:model=SLB9672%00%00%00%00%00%00%00%00%00;manufacturer=Infineon;serial=0000000000000000;token=greengrass;id=%39%32%37%65%61%64%61%39%31%32%35%31%61%35%37%31;object=greenkey;type=private
           Type: Private key (EC/ECDSA-SECP256R1)
           Label: greenkey
           Flags: CKA_PRIVATE; CKA_NEVER_EXTRACTABLE; CKA_SENSITIVE;
           ID: 39:32:37:65:61:64:61:39:31:32:35:31:61:35:37:31

   Object 1:
           URL: pkcs11:model=SLB9672%00%00%00%00%00%00%00%00%00;manufacturer=Infineon;serial=0000000000000000;token=greengrass;id=%39%32%37%65%61%64%61%39%31%32%35%31%61%35%37%31;object=greenkey;type=public
           Type: Public key (EC/ECDSA-SECP256R1)
           Label: greenkey
           ID: 39:32:37:65:61:64:61:39:31:32:35:31:61:35:37:31

   Object 2:
           URL: pkcs11:model=SLB9672%00%00%00%00%00%00%00%00%00;manufacturer=Infineon;serial=0000000000000000;token=greengrass;id=%39%32%37%65%61%64%61%39%31%32%35%31%61%35%37%31;object=greenkey;type=cert
           Type: X.509 Certificate (EC/ECDSA-SECP256R1)
           Expires: Fri Dec 31 18:59:59 2049
           Label: greenkey
           ID: 39:32:37:65:61:64:61:39:31:32:35:31:61:35:37:31
   ```

1. Capture the object URL for the private key and the certificate.

## Step 8: Configure and install Greengrass with TPM2 support
<a name="step8"></a>

1. Configure the thing certificate. For more information see [Configure the thing certificate](https://docs.aws.amazon.com/greengrass/v2/developerguide/manual-installation.html#configure-thing-certificate).

1. Complete the instructions to Install the AWS IoT Greengrass Core software with the private key and certificate in an HSM in [Install the AWS IoT Greengrass Core software](manual-installation.md#run-greengrass-core-v2-installer-manual). Then, use the following steps to configure your installation to leverage TPM2 through PKCS\#11 interface.

1. Verify you have the PKCS\#11 provider component downloaded and saved in your Greengrass installer location.

1. Use a text editor to create a configuration file named `config.yaml` to provide to the installer. For example, on a Linux-based system, you can run the following command to use GNU `nano` to create the file.

   ```
   nano GreengrassInstaller/config.yaml
   ```

1. Copy the following YAML content into the file. This partial configuration file specifies system parameters, Greengrass nucleus parameters, and PKCS\#11 provider parameters.

   ```
   ---
   system:
     certificateFilePath: "pkcs11:model=SW%20%20%20TPM%00%00%00%00%00%00%00%00;manufacturer=IBM;serial=0000000000000000;token=greengrass;id=%34%35;object=greenkey;type=cert"
     privateKeyPath: "pkcs11:model=SW%20%20%20TPM%00%00%00%00%00%00%00%00;manufacturer=IBM;serial=0000000000000000;token=greengrass;id=%34%35;object=greenkey;type=private"
     rootCaPath: "/greengrass/v2/AmazonRootCA1.pem"
     rootpath: "/greengrass/v2"
     thingName: "myThing"
   services:
     aws.greengrass.Nucleus:
       componentType: "NUCLEUS"
       version: "2.14.0"
       configuration:
         awsRegion: "us-east-1"
         iotRoleAlias: "GreengrassCoreTokenExchangeRoleAlias"
         iotDataEndpoint: "device-data-prefix-ats.iot.us-west-2.amazonaws.com"
         iotCredEndpoint: "device-credentials-prefix.credentials.iot.us-west-2.amazonaws.com"
     aws.greengrass.crypto.Pkcs11Provider:
       configuration:
         name: "tpm2_pkcs11"
         library: "/usr/lib/x86_64-linux-gnu/pkcs11/libtpm2_pkcs11.so"
         slot: 1
         userPin: "123456"
   ```

1. Edit the file with the parameters specific for your installation.

   1. Update certificateFilePath and privateKeyPath with the Update certificateFilePath and privateKeyPath with the PKCS\#11 URL captured in Step 7.

   1. Update your iotDataEndpoint and iotCredEndpoint based on your AWS IoT endpoint.

   1. In the `aws.greengrass.crypto.Pkcs11Provider` configuration, update the library based on your platform.
**Note**
The example shown is for X86\_64. The file path will be similar for ARM64 device.

1. Complete the Greengrass installation steps in [Install the AWS IoT Greengrass Core software](manual-installation.md#run-greengrass-core-v2-installer-manual).

## Step 9: Verify the installation
<a name="step9"></a>

In this step, you'll verify that Greengrass is running properly with TPM2 integration.

1. Check the Greengrass service status.

   ```
   sudo systemctl status greengrass.service
   ```

1. View the Greengrass logs to ensure there are no errors.

   ```
   sudo tail -f /greengrass/v2/logs/greengrass.log
   ```

1. Verify that your device appears as connected in the [AWS IoT console](https://console.aws.amazon.com/iot).

   1. Sign in to the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass).

   1. Under **Manage**, expand **Greengrass devices**, and choose **Core devices**.

   1. Confirm your device is connected. The device status will show `HEALTHY` if it is connected. For more information, see [Check Greengrass core device status](device-status.md).

## Troubleshooting
<a name="troubleshoot"></a>

If you encounter issues during the setup or operation of your TPM2-enabled Greengrass device, try the following troubleshooting steps.
+ Check the main Greengrass log file.

  ```
  sudo tail -f /greengrass/v2/logs/greengrass.log
  ```
+ Verify PKCS\#11 provider configuration.

  ```
  sudo cat /greengrass/v2/config/effectiveConfig.yaml
  ```
+ Ensure the TPM2 service is running.

  ```
  sudo systemctl status tpm2-abrmd.service
  ```
+ Verify that the TPM2 key is accessible.

  ```
  sudo pkcs11-tool —module /usr/lib/x86_64-linux-gnu/pkcs11/libtpm2_pkcs11.so -l -p 123456 —list-objects
  ```
+ If your OS is set up with full disk encryption with TPM2 storage root keys such as Clevis or systemd-cryptenroll, verify you aren't using the same persistent handle used by these tools. Using the same persistent handle might affect your disk encryption mechanism. To check all created and used persistent handles, run the following command

  ```
  sudo tpm2_getcap handles-persistent
  ```

## Next steps
<a name="next-steps"></a>

Now that you've successfully integrated your Greengrass core device with TPM2, you can:
+ Deploy components to your secure Greengrass device. For more information, see [Deploy AWS IoT Greengrass components to devices](manage-deployments.md)
+ Set up additional Greengrass devices with TPM2 integration.

For more information about security on Greengrass devices, see [Security in AWS IoT Greengrass](security.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

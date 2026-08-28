---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-lite-with-tpm-tutorial.html
---

# Tutorial: Secure AWS IoT Greengrass Nucleus Lite with Trusted Platform Module (TPM)
<a name="gg-lite-with-tpm-tutorial"></a>

This tutorial explains how to enable and configure Trusted Platform Module (TPM) support for AWS IoT Greengrass nucleus lite. TPM provides hardware-based root of trust for secure key storage. This security feature protects cryptographic operations and sensitive credentials, enhancing device security and integrity.

When you complete this integration, your AWS IoT Greengrass core device will use TPM-protected private keys for its identity and communication with AWS IoT services.

For more information about security on AWS IoT Greengrass devices, see [Security in AWS IoT Greengrass](security.md).

## Prerequisites
<a name="lite-tpm-prerequisites"></a>

To complete this tutorial, you need the following:
+ A Linux-compatible device with TPM 2.0 hardware or [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html)
+ A developer machine with Greengrass Nucleus Lite installed. For more information, see [Install the AWS IoT Greengrass Core software (console)](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-v2-console.html).
+ Instructions in this tutorial are defined for Ubuntu 24.04 LTS.
+ Any Linux distribution that can support the [Linux TPM2 Software Stack](https://tpm2-software.github.io/) can support this mechanism.
+ A developer machine with [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured with permissions to:
  + Create and manage AWS IoT resources
  + Create and manage IAM roles and policies
+ Root or sudo privileges on the device.

This tutorial contains instructions on how to use the TPM2 chip as a Hardware Security Module (HSM) to create a private key and CSR which is used to create the AWS IoT thing certificate.

## Step 1: Set up a NitroTPM instance
<a name="lite-tpm-step1"></a>

1. Set up a NitroTPM instance. For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-support-on-ami.html).

1. Launch final instance using the custom AMI created in the previous step.
**Important**
When connecting with SSH, use the `ubuntu` user instead of `root`.

1. Check that the TPM device is present and working by running the following command:

   ```
   ls -la /dev/tpm*
   ```

   You should see `/dev/tpm0` and `/dev/tpmrm0` devices.

## Step 2: Install and configure TPM tools
<a name="lite-tpm-step2"></a>

1. Install the required packages by running the following command:

   ```
   sudo apt update
   sudo apt install tpm2-openssl tpm2-tools tpm2-abrmd libtss2-tcti-tabrmd0
   ```

1. Verify the TPM device's permissions by running the following command:

   ```
   ls -l /dev/tpm0    # Should be owned by tss:root with permissions 0660
   ls -l /dev/tpmrm0  # Should be owned by tss:tss with permissions 0660
   ```

## Step 3: Configure the OpenSSL TPM2 provider
<a name="lite-tpm-step3"></a>

1. Edit the OpenSSL configuration file:

   ```
   sudo vi /etc/ssl/openssl.cnf
   ```

1. Add the following configuration:

   ```
   [openssl_init]
   providers = provider_sect

   [provider_sect]
   default = default_sect
   tpm2 = tpm2_sect

   [default_sect]
   activate = 1

   [tpm2_sect]
   identity = tpm2
   module = /usr/local/lib64/tpm2.so
   activate = 1
   ```

1. Adjust the module path as necessary. You can find the correct path using:

   ```
   find /usr -name "tpm2.so"
   ```

## Step 4: Generate persistent TPM keys
<a name="lite-tpm-step4"></a>

1. Create a primary key by running the following command:

   ```
   sudo tpm2_createprimary -C o -c primary.ctx
   ```

1. Create an ECC key object by running the following command:

   ```
   sudo tpm2_create -C primary.ctx -g sha256 -G ecc256 -r device.priv -u device.pub
   ```

1. Load the key by running the following command:

   ```
   sudo tpm2_load -C primary.ctx -r device.priv -u device.pub -c device.ctx
   ```

1. Make the key persistent by running the following command:

   ```
   sudo tpm2_evictcontrol -C o -c device.ctx 0x81000002
   ```

   This creates a persistent key with the handle (like `0x81000002`).

## Step 5: Generate Certificate Signing Request (CSR)
<a name="lite-tpm-step5"></a>

In this step, you'll use the TPM2-protected private key to generate a Certificate Signing Request (CSR).

1. Generate a CSR using the TPM key:

   ```
   openssl req -new -provider tpm2 -key "handle:0x81000002" \
       -out device.csr \
       -subj "/CN=TPMThing"
   ```

1. Replace `0x81000002` with your chosen handle value and `TPMThing` with your desired thing name.

## Step 6: Create the certificate from CSR
<a name="lite-tpm-step6"></a>

1. On your development computer, create a folder where you downloaded the certificate for the AWS IoT thing.

   ```
   mkdir greengrass-v2-certs
   ```

1. Use the CSR file to create and download the certificate for the AWS IoT thing to your development computer.

   ```
   aws iot create-certificate-from-csr \
     --set-as-active \
     --certificate-signing-request file://{{path_to_device.csr}} \
     --certificate-pem-outfile greengrass-v2-certs/device.pem.crt
   ```

   If the request succeeds, the response looks similar to the following example:

   ```
   {
   "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificateId": "aa0b7958770878eabe251d8a7ddd547f4889c524c9b574ab9fbf65f32248b1d4",
     "certificatePem": "-----BEGIN CERTIFICATE-----
   MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w
    0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZ
    WF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIw
    EAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5
    jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh
    MCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb
    WF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx
    HzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE
    BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI
    k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ
    ITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr
    AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auN
    KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6Guo
    EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw
    3rrszlaEXAMPLE=
   -----END CERTIFICATE-----"
   }
   ```

## Step 7: Set up Greengrass Nucleus Lite with TPM support
<a name="lite-tpm-step7"></a>

To enable TPM support in Greengrass Nucleus Lite, make the following changes:

1. Configure user permissions by adding the `ggcore` user to the `tss` group for TPM access:

   ```
   sudo usermod -a -G tss ggcore
   ```

1. Update the credentials directory by completing the following steps:
   + Remove the private key file from the credentials directory.
     + Since we are using persistent TPM keys, no private key file needs to be copied.
   + Copy the new `device.pem.crt` into that credentials directory.

1. Edit `config.yaml` with the following TPM-specific configuration:

   ```
   system:
       privateKeyPath: "handle:0x81000002" # Use your chosen handle
       certificateFilePath: "" # Replace with the path of device.pem.crt
       ...
   ```

1. Reboot your Greengrass Nucleus Lite by running the following command:

   ```
   systemctl restart greengrass-lite.target
   ```

## Troubleshooting
<a name="lite-tpm-troubleshooting"></a>

If you encounter issues during the setup or operation of your TPM2-enabled AWS IoT Greengrass device, try the following troubleshooting steps:

**TPM device is not found (when using NitroTPM)**

If `/dev/tpm0` is not present, do the following steps:

1. Verify you're using a NitroTPM-supported instance type.

1. Ensure the AMI was created with `--tpm-support v2.0`.

1. Verify that the instance was launched from the custom AMI.

**Permission denied errors**

If you encounter TPM access errors, do the following:

1. Verify that the user is in the `tss` group: `groups $USER`.

1. Check the TPM device's permissions using the following command:

   ```
   ls -l /dev/tpm*
   ```

1. Verify you logged out and logged back in after adding to the `tss` group.

**OpenSSL provider issues**

If TPM provider is not found, do the following:

1. Verify `tpm2.so` path in the `/etc/ssl/openssl.cnf`.

1. Check provider installation by running the following command:

   ```
   openssl list -providers
   ```

1. Verify the `tpm2-openssl` package is properly installed.

## Next steps
<a name="lite-tpm-next-steps"></a>

Now that you've successfully integrated your AWS IoT Greengrass core device with TPM2, you can:
+ Deploy components to your secure AWS IoT Greengrass device
+ Set up additional AWS IoT Greengrass devices with TPM2 integration

For more information about security on AWS IoT Greengrass devices, see [Security in AWS IoT Greengrass](security.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

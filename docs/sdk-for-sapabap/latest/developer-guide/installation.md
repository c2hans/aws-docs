---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/installation.html
---

# Installing AWS SDK for SAP ABAP
<a name="installation"></a>

**Topics**
+ [Download SDK for SAP ABAP](#download)
+ [Verify SDK for SAP ABAP file – *optional*](#verification)
+ [AWS SDK Transports](#transports)

## Download SDK for SAP ABAP
<a name="download"></a>

Download the SDK from **[https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/abapsdk-LATEST.zip](https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/abapsdk-LATEST.zip)**.

```
curl "https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/abapsdk-LATEST.zip" -o "abapsdk-LATEST.zip"
```

When the download is complete, we recommend that you unzip the downloaded file into a directory, such as `/tmp/awssdk`.

## Verify SDK for SAP ABAP file – *optional*
<a name="verification"></a>

This optional step of validating the signature of your SDK file helps you confirm that your SDK has not been tampered with. Use the following steps to verify your SDK file.

1. Download the SDK SIGNATURE file with the following command.

   ```
   curl "https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/abapsdk-LATEST.sig" -o "abapsdk-LATEST.sig"
   ```

1. Copy the following public key, and save it to a file named `abapsdk-signing-key.pem`.

   ```
   -----BEGIN PUBLIC KEY-----
   MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmS3oN3wKBh4HJOGaOtye
   15RR5909nuw0JxOvEDCT7O9wUrXS3mjgEw6b6hvr2dLdoFr+eH4ewT5bVl6U3gDv
   051sTdEJJpfLEWJJZZNK3v9fGWKyXgYe+ifmsPmf4lhNd2auzpvIy2UrlSYijCRB
   BWZFW+Ux0OkILz+8vCFSXMZ6Z0qtLIlZFbGrn6A5adbwwzfOqkg9BUEZK0wB6TAi
   ZTnkMdBZGCBM9K2MRKKMxtrxUn+TFcAYyh5pM9tUAb2q4XE5m7092UnZG7ur/QYl
   1FSZwAhQmk8hUPgUaqOOQRC6z3TRzIGKOA/DI0cUPJMzFR4LCxEJkgh4rkRaU9V2
   O7DthUpj8b7QcQaiOpnMpBf3zWLgbjNmX0hB0Eprg8/nVRHspf3zuiscJ2lMPkz0
   cHOR3lMNsMLzm+d/gVkLt31R/JwAcFCkXTWvR8/VOWNGZZXdVUbefrfI/k7fP60B
   bzUrIlN4poq16rc4Tk5Derg+wQ7rOWjXkXop2kiCMjbYo0ol0kS/At64PLjpz8dH
   Zg25o79U9EJln+lpqZ297Ks+HoctOv2GPbeeh0s7+N0fRTyOr81EZIURLPKLVQUw
   otVRzNDgLOA7eA667NrmegZfHCmqEwK9tXakZUHAcMzRPyhALc/HtmovxdStN9h1
   JC4exOGqstAv1fX5QaTbMSECAwEAAQ==
   -----END PUBLIC KEY-----
   ```

1. Verify the downloaded SDK ZIP file with the following command. The command requires `openssl` that is part of many Linux distributions.

   ```
   openssl dgst -sha256 -verify abapsdk-signing-key.pem -keyform PEM -signature abapsdk-LATEST.sig abapsdk-LATEST.zip
   ```

1. Verify that the output of the preceding command is `Verified OK`.

1. If the output is `Verification Failure`, repeat the preceding steps. If you continue to receive a failed output, don't install the SDK and contact Support.

## AWS SDK Transports
<a name="transports"></a>

**Topics**
+ [Contents](#contents)
+ [Importing](#importing)
+ [Namespace](#namespace)

### Contents
<a name="contents"></a>

The installation of SDK for SAP ABAP is completed through ABAP Transports. You must import these transports into your development or sandbox environment.

Each SDK for SAP ABAP release completely replaces the previous one.  There is no need to apply incremental transports.  The transports are bundled in a ZIP file. The following is the structure of the ZIP file.

```
transports/
transports/core/
transports/core/Knnnnnn.AWS
transports/core/Rnnnnnn.AWS
transports/tla1/
transports/tla1/Knnnnnn.AWS
transports/tla1/Rnnnnnn.AWS
transports/tla2/
transports/tla2/Knnnnnn.AWS
transports/tla2/Rnnnnnn.AWS
.
.
.
```

The `transports` folder contains a `core` subfolder. The `core` subfolder contains the core runtime transports and a subfolder for each module, named by the three letter abbreviation of the module. For a complete module list of the TLAs, see [AWS SDK for SAP ABAP - Module List](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/tla.html).

AWS SDK transports are workbench requests. Depending on the configuration of your TMS routes, the SDK may not automatically forward to your quality assurance and production queues after importing into the previous system. You must manually add them to the queue of each system.

When your project is ready for the next phase, AWS SDK can be imported along with separate transports containing your own `Z` code with business functionality. If you are using a change control system, such as SAP Change Request Management (ChaRM), consult your ChaRM administrator for correct handling of third-party transports.

### Importing
<a name="importing"></a>

**Topics**
+ [Key pointers](#importing-key-pointers)
+ [Time to import](#importing-time)

AWS SDK transports are client-independent. The core transport is mandatory and contains the SDK runtime code, the API for AWS Security Token Service, and the API for Amazon Simple Storage Service.  The remaining SDK modules are each delivered in a separate transport. To keep the size of the SDK small in your system, each SDK module is optional. You can install additional modules later, if required for your business logic.

For example, if you want to use the APIs for Amazon S3 and Amazon Translate, import the `core` transport (containing core runtime, Amazon S3, and AWS STS modules) and the `xl8` transport (containing the module for Amazon Translate) transports.

To see a complete list of SDK for SAP ABAP APIs, see [SDK for SAP ABAP - API Reference Guide](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html).

The following are key pointers when importing AWS SDK transports.
+ Each transport is delivered as `Knnnnnn.AWS` and `Rnnnnnn.AWS`
  + `Knnnnnn.AWS` must be copied to `/usr/sap/trans/cofiles`
  + `Rnnnnnn.AWS` must be copied to `/usr/sap/trans/data`.
+ When importing transports, you must select the **Ignore Invalid Component Version** found at *Import Transport Request* > *Options* > *Import Options*.
+ All desired transports can be imported simultaneously.
+ If importing the transports separately, the `core` transport must be imported first.
+ The release level of all the transports must be identical.

**Time to import**

AWS SDK transports may take many minutes to import. The transports are successful if STMS shows a green (`RC=0`) or yellow (`RC=4`) light.
+ A red light (`RC=8`) indicates that the import had a syntax error.
  + Select **Request** → **Display** → **Logs to examine the import error**.
  + During the import, if an error is thrown because of a missing interface `IF_SYSTEM_UUID_RFC4122_STATIC`, then ensure that SAP Note 2619546 is applied to the system. For more information, see [Notes](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#parameters).
  + If the cause of the error is unknown, contact Support.
+ A red lightning bolt (`RC=12`) indicates that the transport files have not been correctly loaded into `/usr/sap/trans` or do not have the necessary permissions.

#### Key pointers
<a name="importing-key-pointers"></a>

The following are key pointers when importing AWS SDK transports.
+ Each transport is delivered as `Knnnnnn.AWS` and `Rnnnnnn.AWS`
  + `Knnnnnn.AWS` must be copied to `/usr/sap/trans/cofiles`
  + `Rnnnnnn.AWS` must be copied to `/usr/sap/trans/data`.
+ When importing transports, you must select the **Ignore Invalid Component Version** found at *Import Transport Request* > *Options* > *Import Options*.
+ All desired transports can be imported simultaneously.
+ If importing the transports separately, the `core` transport must be imported first.
+ The release level of all the transports must be identical.

#### Time to import
<a name="importing-time"></a>

AWS SDK transports may take many minutes to import. The transports are successful if STMS shows a green (`RC=0`) or yellow (`RC=4`) light.
+ A red light (`RC=8`) indicates the import had a syntax error.
  + Select **Request** → **Display** → **Logs to examine the import error**.
  + During the import, if an error is thrown due to a missing interface `IF_SYSTEM_UUID_RFC4122_STATIC`, then ensure that SAP Note 2619546 is applied to the system. For more information, see [Notes](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#parameters).
  + If the cause of the error is unknown, contact Support.
+ A red lightning bolt (`RC=12`) indicates the transport files have not been correctly loaded into `/usr/sap/trans` or do not have the necessary permissions.

### Namespace
<a name="namespace"></a>

SDK for SAP ABAP uses the `/AWS1/` namespace and does not modify SAP objects or any other objects in your system with the following exception.
+ AWS `auth` objects are in an **Auth Object Class**. Auth Object Classes are limited to four characters and do not support namespaces. SDK for SAP ABAP uses Auth Object Class is `YAW1`. If you already have an auth object class `YAW1` in transaction `SU21`, contact Support before installation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html
---

# SAP prerequisites
<a name="prerequisites"></a>

The following prerequisites for installing the SDK are applicable when your SAP systems are hosted on AWS.

**Topics**
+ [Prerequisites for AWS SDK for SAP ABAP](#sdk)
+ [Prerequisites for AWS SDK for SAP ABAP - BTP edition](#sdk-btp)

## Prerequisites for AWS SDK for SAP ABAP
<a name="sdk"></a>

The following are the prerequisites for AWS SDK for SAP ABAP.

**Topics**
+ [Basis release](#basis)
+ [Kernel release](#kernel)
+ [Parameters](#parameters)
+ [Notes](#notes)
+ [Outbound connectivity](#outbound-connectivity)
+ [HTTPS connectivity](#https-connectivity)
+ [Access to Amazon EC2 instance metadata](#instance-metadata)

### Basis release
<a name="basis"></a>

SDK for SAP ABAP is compatible with SAP NetWeaver 7.4 and higher. SDK for SAP ABAP doesn't touch any SAP application tables. It is completely agnostic about the applications, such as SAP Enterprise Resource Planning and SAP Landscape Transformation Replication Server.

The minimum supported SP-Level for `SAP_BASIS 740` is `SP 0008`. For more information, see [SAP Note 1856171 - Supporting form fields of the same name in CL\_HTTP\_ENTITY](https://launchpad.support.sap.com/#/notes/1856171) (requires SAP portal access). Based on your business requirements, you can choose a higher SP-Level, as shown in the following image.

![An example of the Installed Software Component Versions tab in the portal.](http://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/sp-level.png)

There is no minimum SP-Level requirement for `SAP_BASIS 750` and higher releases.

### Kernel release
<a name="kernel"></a>

SDK for SAP ABAP and tools that use the Internet Communication Manager (ICM) for HTTP connectivity, rely on the SAP kernel for its cryptographic, HTTP, XML, and JSON capabilities. We recommend using the latest kernel release that is compatible with your SAP NetWeaver platform. The minimum requirement is kernel release **741**. For more information, see [SAP Note 2083594 - SAP Kernel Versions and SAP Kernel Patch Levels](https://launchpad.support.sap.com/#/notes/2083594) (requires SAP portal access).

If you are using kernel release 741 or 742, the following patch levels are required:
+  741 patchno 212
+  742 patchno 111

### Parameters
<a name="parameters"></a>

Your SAP system must support Server Name Indication (SNI) as described in the following SAP Notes (requires SAP portal access).
+ [SAP Note 2124480 - ICM/Web Dispatcher: TLS Extension Server Name Indication (SNI) as client](https://launchpad.support.sap.com/#/notes/2124480)
+ [SAP Note 2582368 - SapSSL update for client-side sending of TLS extension SNI by saphttp, sapkprotp, sldreg ](https://launchpad.support.sap.com/#/notes/2582368)

Configure the following parameter in the `DEFAULT.PFL` file.

```
icm/HTTPS/client_sni_enabled = TRUE
```

### Notes
<a name="notes"></a>

Apply the following SAP Note to your system.
+ [https://launchpad.support.sap.com/\#/notes/0001856171](https://launchpad.support.sap.com/#/notes/0001856171)
+ [https://launchpad.support.sap.com/\#/notes/0002619546](https://launchpad.support.sap.com/#/notes/0002619546)

### Outbound connectivity
<a name="outbound-connectivity"></a>

SDK for SAP ABAP is an HTTPS client. The SAP system sends HTTPS messages outbound. There is no requirement of an inbound connectivity.

### HTTPS connectivity
<a name="https-connectivity"></a>

All AWS API calls are made with encrypted HTTPS channels. The SAP system must be set up to trust AWS certificates to establish an outbound HTTPS connection.

1. Go to [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/).

1. Under **Root CAs**, download all the certificates using the *PEM* link.

1. Import these certificates in `STRUST` of your `SSL Client (Standard) PSE` on each of your SAP systems, as shown in the following image.
![An example of the certificate list in the SSL client standard PSE.](http://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/https.png)

### Access to Amazon EC2 instance metadata
<a name="instance-metadata"></a>

ABAP system makes unencrypted HTTP connections to localhost (http://169.254.169.254) to enable Amazon EC2 instance metadata. The HTTP channel is used only to retrieve AWS credentials from the local server. The HTTP traffic stays within the host.

The metadata allows an SAP system in AWS to securely authenticate itself without storing a secret key in the SAP Secure Store. This feature is applicable only to SAP systems hosted on Amazon EC2.

Configure the `DEFAULT.PFL` file with the following parameter to enable your SAP system to make an unencrypted outbound HTTP connection.

```
icm/server_port_<xx> = PROT=HTTP,PORT=8000,TIMEOUT=60,PROCTIMEOUT=600
```

Use the following parameter to enable the outbound HTTP connection without enabling the inbound connection.

```
icm/server_port_<xx> = PROT=HTTP,PORT=0,TIMEOUT=60,PROCTIMEOUT=600
```

Verify that your SAP system is configured for outbound HTTP connections with the following steps:

1. Run **SMICM** transaction.

1. Go to **Active Services**.

1. Verify that you see a **green check mark** in the HTTP row, under *Active* column, as shown in the following image.
![An example of a green checkmark for the HTTP protocol on the Active Services list.](http://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/http.png)

## Prerequisites for AWS SDK for SAP ABAP - BTP edition
<a name="sdk-btp"></a>

The following are the only prerequisites for AWS SDK for SAP ABAP - BTP edition.

**Topics**
+ [SAP Landscape Portal – BTP edition](#landscape-portal)
+ [SAP Credential Store – BTP edition](#credential-store)

### SAP Landscape Portal – BTP edition
<a name="landscape-portal"></a>

This prerequisite is only applicable for AWS SDK for SAP ABAP - BTP edition.

SAP Landscape Portal is the only supported mechanism to install add-ons in an SAP BTP environment. Ensure that you are subscribed to use this service. For more information, see [Landscape Portal](https://help.sap.com/docs/btp/sap-business-technology-platform/landscape-portal).

### SAP Credential Store – BTP edition
<a name="credential-store"></a>

This prerequisite is only applicable for AWS SDK for SAP ABAP - BTP edition.

In the developer preview, secret access key authentication is the only supported mechanism for authenticating AWS SDK for SAP ABAP - BTP edition. The SDK reads the credentials from the Credential Store, and stores the secret access key securely.

You must meet the following prerequisites.
+ Subscription to Credential Store.
+ Credential Store assigned as an entitlement to your BTP sub-account. See [Initial setup](https://help.sap.com/docs/credential-store/sap-credential-store/initial-setup) for more details.
+ A service instance with standard plan for Credential Store. See [Create a service instance](https://help.sap.com/docs/credential-store/sap-credential-store/create-service-instance) for more details.

For more information, see [Using SAP Credential Store](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/credential-store.html).

The SAP Credential Store service runs in SAP BTP outside of the ABAP BTP system. See [SAP Credential Store](https://help.sap.com/docs/credential-store) for more details.

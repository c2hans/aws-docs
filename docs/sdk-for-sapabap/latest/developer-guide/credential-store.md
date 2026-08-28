---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/credential-store.html
---

# Using SAP Credential Store
<a name="credential-store"></a>

SAP Credential Store is used in SAP Business Technology Platform to securely store credentials for secret access key authentication to AWS. You must have a subscription to use the service.

The following instructions assume that you have already configured an SDK profile. For more information, see [Configuring AWS SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/configuring.html).

Before commencing the configuration, ensure that you meet the prerequisites. For more information, see [SAP Credential Store](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#credential-store).

**Topics**
+ [Configuration steps](#configuration)
+ [Using SAP Credential Store with the SDK](#connection)

## Configuration steps
<a name="configuration"></a>

**Topics**
+ [Step 1: Configure settings for authentication](#authentication)
+ [Step 2: Create a service key](#service-key)
+ [Step 3: Convert service key into `.p12` format](#conversion)
+ [Step 4: Connect to SAP BTP, ABAP environment](#connection)

### Step 1: Configure settings for authentication
<a name="authentication"></a>

Use the following steps to configure the Credential Store settings for authentication.

1. Navigate to the **Settings** tab of the SAP Credential Store instance.

1. Select **Edit Configurations**:
   + Choose **Mutual TLS** as the Default Authentication Type.
   + Select **Disabled** for Payload Encryption Status. The payload is encrypted in transit with HTTPS. However, the payload cannot currently be double-encrypted.

1. Select **Save**.

### Step 2: Create a service key
<a name="service-key"></a>

Use the following steps to create a service key for Credential Store.

1. In the left pane of the SAP Credential Store application, navigate to **Service Keys**.

1. Select **Create Service Key**.

1. Enter a name for the service key, and select **Create**.

The service key is created on the basis of the chosen authentication type. Download the service key, and keep it secure for later usage.

### Step 3: Convert service key into `.p12` format
<a name="conversion"></a>

A client certificate in the `.p12` format is required to create an outbound user for communication system. Use the following steps to generate a `.p12` certificate from the certificate details provided in the Credential Store Service key.

1. Download the **SAP Cloud Root CA** certificate (required by SAP) from [SAP Trust Center Services](https://support.sap.com/en/offerings-programs/support-services/trust-center-services.html).

1. Open the SAP Cloud Root CA certificate in any text file format. At the end of the file, press Enter, and copy-paste the certificate from the certificate field of the service key. Replace new line characters `\n` with actual new line (Enter), and save the entire certificate in `.cer` file format.

1. Copy the key from the key field of the service key. This private key must be treated as sensitive data. Paste it in a text file, and replace new line characters `\n` with actual new line (Enter). Save the private key in a text file.

1. With the certificate and private key generated in the previous steps, run the following command to generate a `.p12` certificate.

   ```
   openssl pkcs12 -export -out <.p12_{{filename}}> -inkey <private_key.key> -in <certificate.cer>
   ```

   The command required verification of the export password. Retain the password for further use.

Delete the `.key` text file saved in your private key.

### Step 4: Connect to SAP BTP, ABAP environment
<a name="connection"></a>

Configure SAP BTP, ABAP environment to connect with SAP Credential Store.

**Topics**
+ [Communication system](#system)
+ [Communication arrangement](#arrangement)

#### Communication system
<a name="system"></a>

Use the following steps to create a communication system that enables communication from SAP BTP, ABAP environment to SAP Credential Store.

1. Open the Fiori launchpad of the ABAP environment system.

1. Select the **Communication Systems** tile to open the application.

1. Select **New**.

1. Enter a name and ID for the communication system, and select **Create**. For example, you can name the system `ZSAP_CREDSTORE`.

1. Enter other required information:
   + **Host name**: Copy the host name from the Service Key URL. For example, if the URL is `https://credstore.mesh.cf.us10.hana.ondemand.com/api/v1/credentials`, then the host name is `credstore.mesh.cf.us10.hana.ondemand.com`.
   + **Users for Outbound Communication**: Select `+` to add a new user.

     1. Select **SSL Client Certificate** as the Authentication mechanism.

     1. Select **Upload New Certificate**:
        + Browse the `.p12` certificate generated in the preceding step.
        + Enter a description.
        + Enter the export password that was used to generate the `.p12` certificate.
        + Select **Upload**.

     1. Select **Create** to create an outbound user.

1. Select **Save**.

1. Delete the service key downloaded in the previous step.

#### Communication arrangement
<a name="arrangement"></a>

Use the following steps to create a communication arrangement to provide a communication scenario for outbound communication.

1. Open the Fiori launchpad of the ABAP environment system.

1. Select the **Communication Arrangements** tile to open the application.

1. Select **New**.

1. Select communication scenario `/AWS1/CRED_COMM_SCENARIO`, and enter a name for the communication arrangement. For example, `Z_AWS_SDK_TO_SAP_CREDSTORE`.

1. Select **Create**.

1. In the Communication System field, browse for the the Communication System created in the previous step. Other information is auto-populated post selection of the system.

1. Select **Save**.

1. Select **Check Connection** to test your connection.

Once this setup is complete, the ABAP environment can use the communication arrangement to use the SAP Credential Store service via outbound service (HTTP).

## Using SAP Credential Store with the SDK
<a name="connection"></a>

**Topics**
+ [Step 1: Create a namespace and credential(s)](#create-namespace)
+ [Step 2: Configure Custom Business Configuration application](#business-configuration)

### Step 1: Create a namespace and credential(s)
<a name="create-namespace"></a>

Create a namespace and credential in SAP Credential Store with SAP Help – [Create, Edit, and Delete a Credential](https://help.sap.com/docs/credential-store/sap-credential-store/create-edit-and-delete-credential).

Enter the following details to create a credential of type **Key**.
+ **Namespace** – Enter a name for the namespace, and group related credentials together.
+ **Name** – Enter a name for the key. We recommend `aws-0123456789012-username`, where:
  + `0123456789012` is the AWS account ID to which the credential grants access
  + `username` is the IAM user name to which the credential belongs
+ **Value** – Enter a base-64 encoded secret access key. Use the following command to base-64 encode your secret access key.

  ```
  xargs echo -n | base64 # just press enter, do not enter arguments on the command line
  MySecretAccessKey
  Ctrl-D
  ```

  The command reads the secret access key from standard input, and passes it to base64 without a trailing newline. It outputs the base-64 encoded secret access key to the screen. Clear or close your terminal after copying the value into SAP Credential Store.
+ **Username** – Enter your access key ID.
+ Select **Create**.

A new namespace with one credential is created, and credentials can be added, deleted or modified within this namespace.

Follow the principle of least privilege to manage access to the credentials stored in the namespace.

### Step 2: Configure Custom Business Configuration application
<a name="business-configuration"></a>

Use the following steps to configure Custom Business Configuration application to define the credential to use for authentication by the SDK.

1. Open the Fiori launchpad of the ABAP environment system.

1. Browse **Custom Business Configuration** tile to open the application.

1. Open **SDK Profile** Business Configuration.

1. Select the SDK profile for which authentication settings must be configured for SAP Credential Store.

1. In the **Authentication and Settings** tab for the selected profile, select **Edit**, and enter the following details:
   + **Authentication Method** – Select **Credentials from SAP Credential Store**.
   + **Namespace** – Enter the namespace created in SAP Credential Store. For more information, see [Step 1: Create a namespace and credential(s)](#create-namespace).
   + **Key Name** – Enter the name of the created key credential. For more information, see [Step 1: Create a namespace and credential(s)](#create-namespace).
   + **Communication Arrangement** – Enter the name of the created communication arrangement. For more information, see [Communication arrangement](#arrangement).

1. Select **Apply** to go to the **AWS SDK Profile** screen.

1. Select **Select Transport** to select the transport using the value help.

1. Select **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

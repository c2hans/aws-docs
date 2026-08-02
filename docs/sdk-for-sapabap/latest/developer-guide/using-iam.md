---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/using-iam.html
---

# Using certificates with IAM Roles Anywhere
<a name="using-iam"></a>

SAP system can be authenticated on AWS by using certificated-based authentication with AWS Identity and Access Management Roles Anywhere. You must setup the certificate in `STRUST`, and configure the SDK profile in `/AWS1/IMG`.

## Prerequisites
<a name="using-iam-prerequisites"></a>

The following prerequisites must be met before commencing setup for certification.
+ The X.509 certificate issued by your certificate authority (CA) must meet the following requirements.
  + The signing certificate must be a v3 certificate.
  + The chain must not exceed 5 certificates.
  + The certificate must support RSA or ECDSA algorithms.
+ Register your CA with IAM Roles Anywhere as a trust anchor, and create a profile to specify the roles/policies for IAM Roles Anywhere. For more information, see [Creating a trust anchor and profile in AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html).
+ IAM roles for SAP users must be created by the IAM administrator. The roles must have permissions to call the required AWS services. For more information, see [Best practices for IAM Security](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html).
+ Create authorization to run `/AWS1/IMG` transaction. For more information, see [Authorizations for configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html#configuration-authorizations).

## Procedure
<a name="using-iam-procedure"></a>

Follow along these instructions to setup certificate-based authentication.

**Topics**
+ [Step 1 – Define an SSF application by using SAP's Secure Store and Forward (SSF)](#step1)
+ [Step 2 – Set SSF parameters](#step2)
+ [Step 3 – Create the PSE and certificate request](#step3)
+ [Step 4 – Import certificate response into the relevant PSE](#step4)
+ [Step 5 – Configuring SDK profile to use IAM Roles Anywhere](#step5)

### Step 1 – Define an SSF application by using SAP's Secure Store and Forward (SSF)
<a name="step1"></a>

1. Run transaction code `SE16` to define an SSF application.

1. Enter `SSFAPPLIC` table name, and select **New Entries**.

1. Enter a name for the SSF application in the `APPLIC` filed, a description in the `DESCRIPT` filed, and select `Selected (X)` option for the remaining fields.

### Step 2 – Set SSF parameters
<a name="step2"></a>

1. Run the `/n/AWS1/IMG` to launch AWS SDK for SAP ABAP Implementation Guide (IMG).

1. Select **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises Systems**.

1. Run the **Set SSF Parameters** IMG activity.

1. Select **New Entries**, and choose the SSF application created in the previous step. Select **Save**.

1. Modify the hash algorithm to **SHA256**, and the encryption algorithm to **AES256-CBC**. Retain the other settings as default, and select **Save**.

### Step 3 – Create the PSE and certificate request
<a name="step3"></a>

1. Run the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises systems**.

1. Run the `Create PSE for SSF Application` IMG activity.

1. Select **Edit** for the `STRUST` transaction.

1. Right-select the SSF application created in [Step 1 – Define an SSF application by using SAP's Secure Store and Forward (SSF)](#step1), and choose **Create**. Retain all other default settings, and select **Continue**.

1. Select **Create Certificate Request**. See the following image. Retain the default options, and select **Continue**. Copy or export the generated certificate request, and provide it to your CA. Your CA verifies the request, and responds with a signed public-key certificate.
![The icon for Create Certificate Request for the SSF AWS IAM Roles Anywhere Signing Certificate.](http://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/using-iam-image1.png)

   The signing process varies based on your CA, and the technology used by them. See [Issuing private end-entity certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html) with AWS Private Certificate Authority for an example.

### Step 4 – Import certificate response into the relevant PSE
<a name="step4"></a>

1. Run the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises systems**.

1. Run the `Create PSE for SSF Application` IMG activity.

1. Select **Edit** for the `STRUST` transaction.

1. Choose the SSF application, and then select **Import Certificate Response** located in the PSE section below the subject. Either copy and paste the certificate response into text box or import the file from the file system. Select **Continue** > **Save**.

1. The certificate details can be viewed by selecting the subject twice. The information is displayed in the certificate section.

### Step 5 – Configuring SDK profile to use IAM Roles Anywhere
<a name="step5"></a>

1. Run the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Application Configurations**.

1. Create a new SDK profile, and name it.

1. Choose IAM Roles Anywhere as the authentication method.
   + In the left pane, select **Authentication and Settings**.
   + Create a new entry, and enter the information for your SAP system, and AWS Region.
   + Select **IAM Roles Anywhere** for the authentication method, and select **Save**.
   + Select **Enter Details**, and in the pop-up window, choose the SSF application created in [Step 1 – Define an SSF application by using SAP's Secure Store and Forward (SSF)](#step1). Enter the **Trust Anchor ARN**, and **Profile ARN** that were created in [Prerequisites](#using-iam-prerequisites). See the following image. Select **Continue**.
![An example of the Amazon Resource Names (ARN) for the trust anchor and profile.](http://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/images/using-iam-image2.png)

1. In the left pane, select **IAM Role Mapping**. Enter a name, and provide the IAM role's ARN provided by your IAM administrator.

For more information, see [Application configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/application-configuration.html).

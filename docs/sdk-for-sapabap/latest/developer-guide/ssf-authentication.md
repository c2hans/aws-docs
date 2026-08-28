---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/ssf-authentication.html
---

# Using Secret Access Key Authentication with SSF Encryption
<a name="ssf-authentication"></a>

On-premises SAP systems (or systems running in other clouds) can be authenticated on AWS by using secret access key authentication with AWS Identity and Access Management. SAP's [Secure Store and Forward Mechanism](https://help.sap.com/docs/ABAP_PLATFORM_NEW/cf1026f0534f408e849ee7feed288a66/53251a355d0c4d78e10000009b38f83b.html) (SSF) is used to encrypt and securely store AWS credentials (Access Key ID and a Secret Access Key) of an IAM user. The SAP system logs into AWS using an IAM user, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for information.

## Prerequisites
<a name="ssf-authentication-prerequisites"></a>

The following prerequisites must be met before commencing the configuration:
+ IAM roles for SAP users must be created by the IAM administrator. The roles must have permissions to call the required AWS services. For more information, see [Best practices for IAM Security](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html).
+ Create authorization to run `/AWS1/IMG` transaction. For more information, see [Authorizations for configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html#configuration-authorizations).

## Procedure
<a name="ssf-authentication-procedure"></a>

Follow along these instructions to configure SSF-encrypted credential storage:

**Topics**
+ [Step 1 – Define an SSF application for Credential Storage](#ssf-step1)
+ [Step 2 – Set the encryption parameters for the SSF application](#ssf-step2)
+ [Step 3 – Create PSE for SSF Application](#ssf-step3)
+ [Step 4 – Assign an SSF application to the AWS SDK for SAP ABAP](#ssf-step4)
+ [Step 5 – Configure SDK profile to use SSF-encrypted credentials](#ssf-step5)

### Step 1 – Define an SSF application for Credential Storage
<a name="ssf-step1"></a>

1. Execute transaction code `SE16` to define an SSF application.

1. Enter `SSFAPPLIC` table name, and select **New Entries**.

1. Enter following details:
   + **APPLIC**: `ZAWS1` (name for the SSF application).
   + **DESCRIPT**: `SSF Encryption for the AWS SDK for SAP ABAP` (description).
   + Choose `Selected(X)` option for the remaining fields.

1. Select Save.

### Step 2 – Set the encryption parameters for the SSF application
<a name="ssf-step2"></a>

1. Execute the transaction code `/n/AWS1/IMG` to launch the Implementation Guide (IMG) for AWS SDK for SAP ABAP.

1. Expand the IMG node **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises systems**.

1. Execute the **Set SSF Parameters** IMG activity.

1. Select **New Entries**, and choose the SSF application created in the previous step. Select **Save**.

1. Modify the hash algorithm to **SHA256** (or higher), and the encryption algorithm to **AES256-CBC**. Retain the other settings as default, and select **Save**.

These encryption settings will be used to securely encrypt AWS credentials.

### Step 3 – Create PSE for SSF Application
<a name="ssf-step3"></a>

1. Execute the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises systems**.

1. Execute the IMG activity **Create PSE for SSF Application**, which will direct you to the `STRUST transaction`. Select **Edit**.

1. Right-select the SSF application created in [Step 1 – Define an SSF application for Credential Storage](#ssf-step1), and choose **Create**. Retain all other default settings, and select **Continue**. Ensure you choose `RSA` and not DSA as the algorithm.

### Step 4 – Assign an SSF application to the AWS SDK for SAP ABAP
<a name="ssf-step4"></a>

1. Execute the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Technical Prerequisites** > **Additional Settings for On-Premises systems**.

1. Execute the IMG activity **Assign an SSF application to the AWS SDK for SAP ABAP**.

1. Select **New Entries** and enter the SSF application created in [Step 1 – Define an SSF application for Credential Storage](#ssf-step1). Select **Save**.

### Step 5 – Configure SDK profile to use SSF-encrypted credentials
<a name="ssf-step5"></a>

1. Execute the `/n/AWS1/IMG` transaction, and select **AWS SDK for SAP ABAP Settings** > **Application Configurations**.

1. Execute the IMG activity **SDK Profile**.

1. Select **New Entries**. Enter profile name and description. Select **Save**.

1. Highlight the entry that you created and click on the **Authentication And Settings tree** branch.

1. Select **New Entries** and enter following details:
   + **SID**: The system ID of the SAP system.
   + **Client**: The client of the SAP system.
   + **Scenario ID**: Select the `DEFAULT` scenario created by your Basis administrator.
   + **AWS Region**: AWS Region that you want to make calls to.
   + **Authentication Method**: Select `Credentials from SSF Storage` from the dropdown and select **Save**. Select **Set Credentials** and enter the Access Key ID and Secret Access Key of the IAM user.
   + **Disable IAM roles**: Keep this as default i.e. unchecked.
   + Select **Save**.

1. Click on the IAM Role Mapping tree branch. Select **New Entries**. Enter sequence number, name for logical IAM role and IAM Role ARN provided by the AWS IAM Administrator. Select **Save**.

For more information, see [Application configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/application-configuration.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/install-certificate-authority.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Install Certificate Authority
<a name="install-certificate-authority"></a>

 For a DC to support Smart Card authentication, each DC must have a certificate issued by a trusted CA. This CA can be either a trusted third-party authority or a local Active Directory Certificate authority. Use the following directions to install Active Directory Certificate Services (ADCS) and create a new local enterprise CA.

 **To install ACDS and create a new local enterprise CA**:

1.  Log on as a member of both the “Enterprise Admins” group and the root domain's “Domain Admins” group.

1.  In Server Manager, select **Manage**, and then select **Add Roles and Features**. The Add Roles and Features Wizard opens.

1.  In **Select Installation Type**, ensure that **Role-Based or feature-based installation** is selected, and then select **Next**.

1.  **Select destination server**, ensure that **Select a server from the server pool** is selected. In **Server Pool**, ensure that the **local computer** is selected. Choose **Next**.

1.  In **Select Server Roles**, in **Roles**, select **Active Directory Certificate Services**. When you are prompted to add required features, select **Add Features**, and then select **Next**.

1.  In **Select features**, select **Next**.

1.  In **Active Directory Certificate Services**, read the provided information, and then select **Next**.

1.  In **Confirm installation selections**, select **Install**. Do not close the wizard during the installation process.

1.  When installation is complete, select **Configure Active Directory Certificate Services on the destination server**. The AD CS Configuration wizard opens. Read the credentials information and, if needed, provide the credentials for an account that is a member of the Enterprise Admins group. Choose **Next**.

1.  In **Role Services**, select **Certification Authority**, and then select **Next**.

1.  On the **Setup Type** page, verify that **Enterprise CA** is selected, and then choose **Next**.

1.  On the **Specify the type of the CA** page, verify that **Root CA** is selected, and then choose **Next**.

1.  On the **Specify the type of the private key** page, verify that **Create a new private key** is selected, and then choose **Next**.

1.  On the **Cryptography for CA** page, keep the default settings for **CSP** (**RSA\#Microsoft Software Key Storage Provider**) and **hash algorithm** (SHA256), and determine the best key character length for your deployment. Large key character lengths provide optimal security; however, they can impact server performance and might not be compatible with legacy applications. It is recommended that you keep the default setting of 2048. Choose **Next**.

1.  On the **CA Name** page, keep the suggested common name for the CA or change the name according to your requirements. Ensure that you are certain the CA name is compatible with your naming conventions and purposes, because you cannot change the CA name after you have installed AD CS. Choose **Next**.

1.  On the **Validity Period** page, in **Specify the validity period**, type the number and select a time value (**Years**, **Months**, **Weeks**, or **Days**). The default setting of five years is recommended. Choose **Next**.

1.  On the **CA Database** page, in **Specify the database locations**, specify the folder location for the certificate database and the certificate database log. If you specify locations other than the default locations, ensure that the folders are secured with access control lists (ACLs) that prevent unauthorized users or computers from accessing the CA database and log files. Choose **Next**.

1.  In **Confirmation**, choose **Configure** to apply your selections, and then choose **Close**.

 **Alternatively, use the following PowerShell snippet to install and configure ADCS**:

1.  Install the ADCS Certificate Authority Windows Feature:

   ```
   Install-WindowsFeature ADCS-Cert-Authority -IncludeManagementTools
   ```

1.  Create the Enterprise Root CA.

```
      Install-ADcsCertificationAuthority `
      -CAType EnterpriseRootCa `
      -CACommonName `
      -CADistinguishedNameSuffix $domainDistinguishedName `
      -CryptoProviderName "RSA#Microsoft Software Key Storage
      Provider" `
      -KeyLength 2048 `
      -HashAlgorithmName "SHA256"
```

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/publish-dod-pki-certificates-to-the-active-directory-ntauth-store-using-installroot.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Publish DoD PKI certificates to the Active Directory NTAuth store using InstallRoot
<a name="publish-dod-pki-certificates-to-the-active-directory-ntauth-store-using-installroot"></a>

 Active Directory has an additional certificate store called NTAuth. The certificates that get installed in the Active Directory NTAuth store then get replicated to the local NTAuth store on the Domain Controllers. The Domain Controllers must have the intermediate and root CA certificates installed in their local NTAuth store to allow for smart card authentication using the certificates on the DoD CAC. These steps will install the CA certificates into the Active Directory NTAuth store using InstallRoot. InstallRoot version 4.1 or newer is required to install CA certificates into the NTAuth store.

 **To install the CA certificates into the NTAuth store**:

1.  Right-click the **InstallRoot** utility and choose **run as administrator** when launching InstallRoot.
**Note**
 Active Directory Enterprise Administrator rights are required to successfully load the CA certificates into the NTAuth certificate store.

1.  Choose the **Certificate** tab.

1.  Expand the **Install DoD Certificates group** by choosing the **▼ symbol**.

1.  Highlight the **top certificate** (DoD Root CA2).

1.  Choose **PEM Export** and select a directory to store the exported certificate (for example, c:\\certs).

1.  Open an **elevated command prompt** using **Run as administrator**, and navigate to the directory where the certificate was stored in the previous step.

1.  Run this command:

   ```
         certutil -dspublish -f "DoD_Root_CA_2__0x05__DoD_Root_CA_2.cer" NTAuthCA
   ```

    Repeat step 4 through step 7 for the remaining DoD Root CAs.

    The following figure shows the certificate successfully installed into the NTAuth store.
![A screenshot showing the code publishing the certificate into the NTAuth certificate store.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard8.png)

   * Publish certificate into the NTAuth certificate store *

1.  In the **InstallRoot** utility, choose the **Store** tab.

1.  Choose the **Active Directory NTAuth** icon.

1.  A pop-up window appears with a security warning stating that any actions in the NTAuth store impact the entire domain. Choose **OK**.

1.  A new store called NTAuth is created. Choose the **Active Directory NTAuth** tab.

1.  Confirm there is a green check mark beside **Install DoD Certificates**.
![A screenshot showing DoD certificate installation.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard9.png)

   * InstallRoot install DoD certificates*

1.  Choose the **Home** tab.

1.  Choose the **Install Certificates** button. You may receive a prompt that configuration changes have been made and would you like to save those changes. Choose **Yes** to proceed.

1.  A summary window displays the results. After checking the results, choose **OK**, then exit InstallRoot.

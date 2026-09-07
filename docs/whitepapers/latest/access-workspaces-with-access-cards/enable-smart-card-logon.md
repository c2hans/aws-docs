---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/enable-smart-card-logon.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enable smart card logon
<a name="enable-smart-card-logon"></a>

The Microsoft implementation for certificate-based authentication to AD requires a unique identifier called the User Principal Name (UPN) to be present in the Subject Alternative Name (SAN) field of the user’s certificate. The DoD implements this value in the user’s email signature certificate.

The UPN consists of two parts: the *generic name* and the *domain identifier suffix*. The DoD generic name is formatted as the individual’s Electronic Data Interchange – Personnel Identifier (EDI-PI). The EDI-PI is appended with the domain identifier suffix: “@mil” for NIPRNet. This unique value (User\_EDI-PI@mil) must match the UPN value listed in the user’s account in AD for authentication to succeed.

**Note**
 Microsoft has updated their security best practices to implement strong attribution in Active Directory authentication using the altSecurityIdentities attributes for Users authenticating with certificates (for example, CAC Cards).
 For more information, go to [ Certificate-based authentication changes on Windows domain controllers](https://support.microsoft.com/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16).

## Alternative User Principal Name suffix
<a name="alternative-user-principal-name-suffix"></a>

 AD must be configured to accept the DoD-specific alternative UPN suffix. This is a one-time action that must be performed using **Active Directory Domains and Trusts**.

1.  Open **Server Manager**. At the top of the dashboard, select **Tools** > **Active Directory Domains and Trusts**.

1.  Right-click the **Active Directory Domains and Trusts** root node and select **Properties**.

1.  In the **Alternative UPN Suffix** text box insert *mil* and choose **Add**.

1.  Choose **OK**. Close the **Active Directory Domains and Trusts** window.

## Users
<a name="user-accounts"></a>

 To map a user’s certificate to their AD account using the standard method of mapping (UPN), the certificate must contain two things:
+  An Enhanced Key Usage (EKU) of “Smart Card Logon” or no EKU, and a Key Usage of “Digital Signature”.
+  A UPN value in the SAN attribute of the certificate. This UPN must be in the form of *xxxxx@domain\_suffix*.

 Their account User Logon Name must be renamed to match the UPN in the certificate. Existing users can be modified easily in Active Directory Users and Computers, and new users can be configured properly from the start using the existing new user wizard.

### To remap existing users who currently authenticate via username/password:
<a name="to-remap-existing-users-who-currently-authenticate-via-usernamepassword"></a>

1.  Open **Server Manager**. At the top of the dashboard, select **Tools** > **Active Directory Users and Computers**.

1.  Navigate to a user who will be migrated to smart card logon.

1.  Right-click the user and select **Properties**.

1.  Choose the **Account** tab. Note the user’s logon name and UPN suffix.

1.  Change the **User Logon Name** to match the **UPN** of this user.

1.  Select the **@mil extension** from the **domain suffix** drop-down box to match the domain suffix in the user’s certificate UPN value. Do not change the User logon name (pre-Windows 2000) fields.
![A screenshot showing the selection of the user's domain suffix](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard13.png)

   * Select user's domain suffix to match UPN value *

1.  If your organizational policy requires users to log on with smart cards only (no username/password allowed), scroll down to the **Account options** section and choose **Smart card is required for interactive logon**.

1.  Choose **OK** to save the modifications.

### To strongly map users in Active Directory using altSecurityIdentities
<a name="to-strongly-map-users-using-altsecurityidentities"></a>

1.  Open Server Manager, then choose **Tools**, **Active Directory Users and Computers**.

1.  Choose **View**, **Advanced Features**.

1.  Navigate to a user who will be migrated to smart card logon.

1.  Right-click the user, then select **Properties**.

1.  Choose **Attribute Editor**, find **altSecurityIdentities**, then select **Edit**.

1.  In **Values to add**, add the strong attribution value for the user in this format: *X509IssuerSerialNumber*. An example of a strong mapping value might be **X509:<I>IssuerName<SR>1234567890**.

    In the following screenshot, the mapping value is **X509:<I>DC=com,DC=contoso,CN=CONTOSO-DC-CA<SR>1200000000AC11000000002B**.
![A screenshot that shows adding a strong mapping value example.](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/add-strong-mapping-value.png)
**Note**
 There are some fields associated with the certificate, such as Issuer, Subject, and Serial Number, that are reported in a *forward* format. Because of this, they will need to be reversed when you add them to the mapping string of the altSecurityIdentities attribute. For example, when adding the *X509IssuerSerialNumber* mapping to a user to be authenticated, search for the `Issuer` and `Serial Number` fields of the certificate you intend to map to the user and reverse the order in which they are given. To find these values, find the certificate to map the user, double-click the file and choose **Details**.
See the following sample output:
 `Issuer: CN=CONTOSO-DC-CA, DC=contoso, DC=com`
 `SerialNumber: 2B0000000011AC0000000012`
 Then, update the user’s altSecurityIdentities attribute in Active Directory with the following string: **X509:<I>DC=com,DC=contoso,CN=CONTOSO-DC-CA<SR>1200000000AC11000000002B**
 Here are some other examples of strong attribution according to the Microsoft documentation:

![A screenshot that shows example strong mapping values.](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/strong-mapping-value-examples.png)

1.  Select **OK**, then **Apply**.

### Manually Creating New Users
<a name="manually-creating-new-users"></a>

1.  Open **Server Manager**. At the top of the dashboard, choose **Tools**, **Active Directory Users and Computers**.

1.  Navigate to the OU container that will hold the new user. Right-click the container and choose **New**, **User**.

1.  Enter the user’s information, similar to the screen shot below. Enter the user’s real name information, but for the **User Logon Name**, enter the EDI-PI of the user with the appropriate domain suffix: EDIPI@mil domain suffix

1.  Form the **User Logon Name** (pre-Windows 2000) as it would conform to the proper username convention of your network. Choose **Next**.
![A screenshot showing the creation of a new user with domain suffix and UPN value.](https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard14.png)

   *Create new user with domain suffix and UPN value *

1.  Enter the appropriate temporary password for the user, selecting the standard options for your domain. Choose **Next**.

1.  Choose **Finish**.

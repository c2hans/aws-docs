---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/import-the-issuing-ca-certificate-into-the-enterprise-ntauth-store.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Import the issuing CA certificate into the Enterprise NTAuth store
<a name="import-the-issuing-ca-certificate-into-the-enterprise-ntauth-store"></a>

 In a command prompt, type the following command, and then press **ENTER**:

```
 certutil -dspublish -f ca_name.cer NTAuthCA
```

 The following figure shows the successful import of the certificate into the NTAuth store.

![A screenshot showing the import of the issuing CA certificate into the Enterprise NTAuth store](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard11.png)

 *Import the issuing CA certificate into Enterprise NTAuth store *

The contents of the NTAuth store are cached in the following registry location:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EnterpriseCertificates\NTAuth\Certificates
```

This registry key is automatically updated to reflect the certificates that are published to the NTAuth store in the AD configuration container. This behavior occurs when Group Policy settings are updated and when the client-side extension that is responsible for autoenrollment runs. In certain scenarios, such as AD replication latency or when the “Do not enroll certificates automatically” policy setting is enabled, the registry is not updated. In these scenarios, you can run the following command manually to insert the certificate into the registry location:

```
certutil -enterprise -addstore NTAuth issuing_ca_name.cer
```

 The following figure shows the successful insert of the certificate into the registry location.

![A screenshot showing the import of the issuing CA certificate into Enterprise NTAuth store.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard12.png)

* Import the issuing CA certificate into Enterprise NTAuth store *

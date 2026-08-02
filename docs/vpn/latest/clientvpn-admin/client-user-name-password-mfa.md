---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-user-name-password-mfa.html
---

# Troubleshooting AWS Client VPN: Client software returns user name and password errors — Active Directory authentication
<a name="client-user-name-password-mfa"></a>

**Problem**
I use Active Directory authentication for my Client VPN endpoint and I used to be able to connect my clients to the Client VPN successfully. But now, clients are getting invalid user name and password errors.

**Possible causes**
If you use Active Directory authentication and if you enabled multi-factor authentication (MFA) after you distributed the client configuration file, the file does not contain the necessary information to prompt users to enter their MFA code. Users are prompted to enter their user name and password only, and authentication fails.

**Solution**
Download a new client configuration file and distribute it to your clients. Verify that the new file contains the following line.

```
static-challenge "Enter MFA code " 1
```

For more information, see [AWS Client VPN endpoint configuration file export](cvpn-working-endpoint-export.md). Test the MFA configuration for your Active Directory without using the Client VPN endpoint to verify that MFA is working as expected.

---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/resolve-host-name.html
---

# Troubleshooting AWS Client VPN: Unable to resolve the Client VPN endpoint DNS name
<a name="resolve-host-name"></a>

**Problem**
I am unable to resolve the Client VPN endpoint's DNS name.

There are several possible causes for this problem. Review the following causes and apply the corresponding solution.

**Cause 1: The client does not prepend the required random string**
The Client VPN endpoint configuration file includes a parameter called `remote-random-hostname`. This parameter forces the client to prepend a random string to the DNS name to prevent DNS caching. Some clients do not recognize this parameter and therefore, they do not prepend the required random string to the DNS name.

**Solution**
Open the Client VPN endpoint configuration file using your preferred text editor. Locate the line that specifies the Client VPN endpoint DNS name, and prepend a random string to it so that the format is {{random\_string.displayed\_DNS\_name}}. For example:
+ Original DNS name: `cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`
+ Modified DNS name: `asdfa.cvpn-endpoint-0102bc4c2eEXAMPLE.clientvpn.us-west-2.amazonaws.com`

**Cause 2: The SAML identity provider signing certificate has expired**
If your Client VPN endpoint uses federated authentication (SAML 2.0), name resolution can fail and return `NXDOMAIN` ("Non-existent domain") when the signing certificate in your identity provider (IdP) metadata expires. When the certificate in the uploaded IAM SAML identity provider metadata is no longer valid, AWS Client VPN stops publishing the DNS record for the endpoint, so resolution fails before a connection is attempted. The endpoint can still report a state of `available`, which makes this cause easy to overlook.

**Solution**
To resolve an expired SAML signing certificate, do the following:

1. Confirm that the endpoint uses SAML-based (federated) authentication.

1. In your identity provider, generate new metadata that contains a valid, unexpired signing certificate.

1. Update the IAM SAML identity provider with the refreshed metadata document. For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the *IAM User Guide*.

1. Allow time for the endpoint DNS record to be republished, and then retry resolution. The change often takes effect within a few minutes, but in some situations it can take up to 4 hours to complete, because modifications to a Client VPN endpoint take effect up to 4 hours after the service accepts the request. For more information, see [Modify an AWS Client VPN endpoint](cvpn-working-endpoint-modify.md).

To avoid recurrence, track the expiration date of the SAML signing certificate and rotate the IdP metadata before it expires.

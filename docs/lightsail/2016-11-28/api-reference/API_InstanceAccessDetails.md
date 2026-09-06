---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceAccessDetails.html
---

# InstanceAccessDetails
<a name="API_InstanceAccessDetails"></a>

The parameters for gaining temporary access to one of your Amazon Lightsail instances.

## Contents
<a name="API_InstanceAccessDetails_Contents"></a>

 ** certKey **   <a name="Lightsail-Type-InstanceAccessDetails-certKey"></a>
For SSH access, the public key to use when accessing your instance For OpenSSH clients (command line SSH), you should save this value to `tempkey-cert.pub`.
Type: String
Required: No

 ** expiresAt **   <a name="Lightsail-Type-InstanceAccessDetails-expiresAt"></a>
For SSH access, the date on which the temporary keys expire.
Type: Timestamp
Required: No

 ** hostKeys **   <a name="Lightsail-Type-InstanceAccessDetails-hostKeys"></a>
Describes the public SSH host keys or the RDP certificate.
Type: Array of [HostKeyAttributes](API_HostKeyAttributes.md) objects
Required: No

 ** instanceName **   <a name="Lightsail-Type-InstanceAccessDetails-instanceName"></a>
The name of this Amazon Lightsail instance.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** ipAddress **   <a name="Lightsail-Type-InstanceAccessDetails-ipAddress"></a>
The public IP address of the Amazon Lightsail instance.
Type: String
Pattern: `([0-9]{1,3}\.){3}[0-9]{1,3}`
Required: No

 ** ipv6Addresses **   <a name="Lightsail-Type-InstanceAccessDetails-ipv6Addresses"></a>
The IPv6 address of the Amazon Lightsail instance.
Type: Array of strings
Pattern: `([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}`
Required: No

 ** password **   <a name="Lightsail-Type-InstanceAccessDetails-password"></a>
For RDP access, the password for your Amazon Lightsail instance. Password will be an empty string if the password for your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.
If you create an instance using any key pair other than the default (`LightsailDefaultKeyPair`), `password` will always be an empty string.
If you change the Administrator password on the instance, Lightsail will continue to return the original password value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.
Type: String
Required: No

 ** passwordData **   <a name="Lightsail-Type-InstanceAccessDetails-passwordData"></a>
For a Windows Server-based instance, an object with the data you can use to retrieve your password. This is only needed if `password` is empty and the instance is not new (and therefore the password is not ready yet). When you create an instance, it can take up to 15 minutes for the instance to be ready.
Type: [PasswordData](API_PasswordData.md) object
Required: No

 ** privateKey **   <a name="Lightsail-Type-InstanceAccessDetails-privateKey"></a>
For SSH access, the temporary private key. For OpenSSH clients (command line SSH), you should save this value to `tempkey`).
Type: String
Required: No

 ** protocol **   <a name="Lightsail-Type-InstanceAccessDetails-protocol"></a>
The protocol for these Amazon Lightsail instance access details.
Type: String
Valid Values: `ssh | rdp`
Required: No

 ** username **   <a name="Lightsail-Type-InstanceAccessDetails-username"></a>
The user name to use when logging in to the Amazon Lightsail instance.
Type: String
Required: No

## See Also
<a name="API_InstanceAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceAccessDetails)

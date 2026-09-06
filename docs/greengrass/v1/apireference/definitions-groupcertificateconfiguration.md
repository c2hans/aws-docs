---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupcertificateconfiguration.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GroupCertificateConfiguration
<a name="definitions-groupcertificateconfiguration"></a>

```
{
"GroupId": "string",
"CertificateAuthorityExpiryInMilliseconds": "string",
"CertificateExpiryInMilliseconds": "string"
}
```

GroupCertificateConfiguration
Information about a group certificate configuration.
type: object

GroupId
The ID of the group certificate configuration.
type: string

CertificateAuthorityExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate authority expires.
type: string

CertificateExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate expires.
type: string

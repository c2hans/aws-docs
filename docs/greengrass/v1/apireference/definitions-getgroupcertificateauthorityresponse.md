---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getgroupcertificateauthorityresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetGroupCertificateAuthorityResponse
<a name="definitions-getgroupcertificateauthorityresponse"></a>

```
{
"PemEncodedCertificate": "string",
"GroupCertificateAuthorityArn": "string",
"GroupCertificateAuthorityId": "string"
}
```

GetGroupCertificateAuthorityResponse
Information about a certificate authority for a group.
type: object

PemEncodedCertificate
The PEM encoded certificate for the group.
type: string

GroupCertificateAuthorityArn
The ARN of the certificate authority for the group.
type: string

GroupCertificateAuthorityId
The ID of the certificate authority for the group.
type: string

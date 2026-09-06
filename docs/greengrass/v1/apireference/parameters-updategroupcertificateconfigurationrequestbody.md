---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-updategroupcertificateconfigurationrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateGroupCertificateConfigurationRequestBody
<a name="parameters-updategroupcertificateconfigurationrequestbody"></a>

```
{
"CertificateExpiryInMilliseconds": "string"
}
```

UpdateGroupCertificateConfigurationRequestBody
in: body
required: true
schema: [UpdateGroupCertificateConfigurationRequest](definitions-updategroupcertificateconfigurationrequest.md)

updateGroupCertificateConfigurationRequest
type: object
required: ["CertificateExpiryInMilliseconds"]

CertificateExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate expires.
type: string

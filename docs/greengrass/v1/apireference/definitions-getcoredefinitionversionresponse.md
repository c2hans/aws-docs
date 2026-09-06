---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getcoredefinitionversionresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetCoreDefinitionVersionResponse
<a name="definitions-getcoredefinitionversionresponse"></a>

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Cores": [
    {
      "Id": "string",
      "ThingArn": "string",
      "CertificateArn": "string",
      "SyncShadow": true
    }
  ]
},
"NextToken": "string"
}
```

GetCoreDefinitionVersionResponse
type: object

Arn
The ARN of the core definition version.
type: string

Id
The ID of the core definition version.
type: string

Version
The version of the core definition version.
type: string

CreationTimestamp
The time, in milliseconds since the epoch, when the core definition version was created.
type: string

Definition
Information about a core definition version.
type: object

Cores
A list of cores in the core definition version.
type: array
items: [Core](definitions-core.md)

Core
Information about a core.
type: object
required: ["Id", "ThingArn", "CertificateArn"]

Id
A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string

ThingArn
The ARN of the thing that is the core.
type: string

CertificateArn
The ARN of the certificate associated with the core.
type: string

SyncShadow
If true, the core's local shadow is synced with the cloud automatically.
type: boolean

NextToken
The token for the next set of results, or `null` if there are no more results.
type: string

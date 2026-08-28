---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-versions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Versions
<a name="definitions-versions"></a>

```
{
"Versions": [
  {
    "Arn": "string",
    "Id": "string",
    "Version": "string",
    "CreationTimestamp": "string"
  }
]
}
```

Versions
type: object

Versions
A list of versions.
type: array
items: [VersionInformation](definitions-versioninformation.md)

VersionInformation
Information about a version.
type: object

Arn
The ARN of the version.
type: string

Id
The ID of the parent definition that the version is associated with.
type: string

Version
The ID of the version.
type: string

CreationTimestamp
The time, in milliseconds since the epoch, when the version was created.
type: string

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

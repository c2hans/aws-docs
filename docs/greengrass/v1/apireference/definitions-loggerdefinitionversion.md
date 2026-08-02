---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-loggerdefinitionversion.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# LoggerDefinitionVersion
<a name="definitions-loggerdefinitionversion"></a>

```
{
"Loggers": [
  {
    "Id": "string",
    "Type": "FileSystem|AWSCloudWatch",
    "Component": "GreengrassSystem|Lambda",
    "Level": "DEBUG|INFO|WARN|ERROR|FATAL",
    "Space": 0
  }
]
}
```

LoggerDefinitionVersion
Information about a logger definition version.
type: object

Loggers
A list of loggers.
type: array
items: [Logger](definitions-logger.md)

Logger
Information about a logger
type: object
required: ["Id", "Type", "Component", "Level"]

Id
A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string

Type
type: string
enum: ["FileSystem", "AWSCloudWatch"]

Component
type: string
enum: ["GreengrassSystem", "Lambda"]

Level
type: string
enum: ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]

Space
The amount of file space, in KB, to use if the local file system is used for logging purposes.
type: integer

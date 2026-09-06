---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-errordetails.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ErrorDetails
<a name="definitions-errordetails"></a>

```
[
{
  "DetailedErrorCode": "string",
  "DetailedErrorMessage": "string"
}
]
```

ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)

ErrorDetail
Details about the error.
type: object

DetailedErrorCode
A detailed error code.
type: string

DetailedErrorMessage
A detailed error message.
type: string

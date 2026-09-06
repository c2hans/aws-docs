---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-listdeploymentsrequest.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListDeploymentsRequest
<a name="definitions-listdeploymentsrequest"></a>

```
{
"MaxResults": 0,
"NextToken": "string"
}
```

ListDeploymentsRequest
type: object

MaxResults
The maximum number of results to be returned per request.
in: query
type: integer
min: 1
max: 250

NextToken
The token to retrieve the next set of results.
in: query
type: string

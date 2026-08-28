---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourceaccesspolicy.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ResourceAccessPolicy
<a name="definitions-resourceaccesspolicy"></a>

```
{
"ResourceId": "string",
"Permission": "ro|rw"
}
```

ResourceAccessPolicy
A policy used by the function to access a resource.
type: object
required: ["ResourceId"]

ResourceId
The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)
type: string

Permission
The type of permission a function has to access a resource.
type: string
enum: ["ro", "rw"]

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-permission-model-structure.html
---

# Permission model structure
<a name="next-gen-api-permission-model-structure"></a>

```
{
  "invokerRoleName": "string",
  "crossAccountRoles": [
    {
      "crossAccountRoleArn": "string",
      "externalId": "string"
    }
  ]
}
```

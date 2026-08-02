---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-migration-step1.html
---

# Identify the application to migrate
<a name="next-gen-migration-step1"></a>

Use the AWS Resilience Hub v1 API to find the application ARN you want to migrate.

```
# List your v1 applications
aws resiliencehub list-apps
```

Note the ARN of the application you want to migrate. You use this ARN in the next step.

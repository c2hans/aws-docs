---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-authentication.html
---

# Making API requests and authentication
<a name="next-gen-api-authentication"></a>

**Endpoint**

```
https://resiliencehub.{region}.amazonaws.com
```

**API version**

Next generation Resilience Hub APIs use the `/v3` path prefix. All requests must be signed with AWS Signature Version 4 (SigV4).

**Authentication**

All API calls require valid AWS credentials. Next generation Resilience Hub uses AWS IAM for authorization. Ensure your IAM policy grants the necessary `resiliencehub:*` actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

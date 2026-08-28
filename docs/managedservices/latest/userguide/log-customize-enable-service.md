---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-enable-service.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Enabling logging for supported services
<a name="log-customize-enable-service"></a>

Some services do not have logging enabled by default and require explicit enablement.

To enable logging for CloudFront, OpenSearch, Amazon RDS and Route53, submit an RFC with the Management \| Other \| Other \| Create change type (ct-1e1xtak34nx76) with the following values, replacing {{variables}} as appropriate:

```
Subject: Enable logging for {{SERVICE_NAME}}
Description: Service ARN: {{SERVICE_ARN}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

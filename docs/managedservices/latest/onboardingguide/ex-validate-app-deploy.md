---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-validate-app-deploy.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Validate the Application Deployment
<a name="ex-validate-app-deploy"></a>

Navigate to the endpoint (ELB CName) of the previously-created load balancer, with the WordPress deployed path: /WordPress. For example:

```
http://stack-{{ID-FOR-ELB}}.us-east-1.elb.amazonaws.com/WordPress
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

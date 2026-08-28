---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-control-examples.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF Fraud Control account takeover prevention (ATP) examples
<a name="waf-atp-control-examples"></a>

This section shows example configurations that satisfy common use cases for the AWS WAF Fraud Control account takeover prevention (ATP) implementations.

Each example provides a description of the use case and then shows the solution in JSON listings for the custom configured rules.

**Note**
You can retrieve JSON listings like the ones shown in these examples through the console protection pack (web ACL) JSON download or rule JSON editor, or through the `getWebACL` operation in the APIs and the command line interface.

**Topics**
+ [ATP example: Simple configuration](waf-atp-control-example-basic.md)
+ [ATP example: Custom handling for missing and compromised credentials](waf-atp-control-example-user-agent-exception.md)
+ [ATP example: Response inspection configuration](waf-atp-control-example-response-inspection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

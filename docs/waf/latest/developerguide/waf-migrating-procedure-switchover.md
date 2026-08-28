---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure-switchover.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Migrating a protection pack (web ACL): switchover
<a name="waf-migrating-procedure-switchover"></a>

After you've verified your new protection pack (web ACL) settings, you can start to use it in place of your AWS WAF Classic protection pack (web ACL).

**To begin using your new AWS WAF protection pack (web ACL)**

1. Associate the AWS WAF protection pack (web ACL) with the resources that you want to protect, following the guidance at [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md). This automatically disassociates the resources from the old protection pack (web ACL).

   The switch can take from a few seconds to a number of minutes to propagate. During this time, some requests might be processed by the old protection pack (web ACL) and others by the new protection pack (web ACL). Your resources will be protected throughout the switch, but you might notice inconsistencies in request handling until it's complete.

1. Configure logging for the new protection pack (web ACL), following the guidance at [Logging AWS WAF protection pack (web ACL) traffic](logging.md).

1. (Optional) If your AWS WAF Classic protection pack (web ACL) is no longer associated with any resources, consider removing it entirely from AWS WAF Classic. For information, see [Deleting a Web ACL](classic-web-acl-deleting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

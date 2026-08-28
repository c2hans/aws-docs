---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/understanding-cts.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# What are change types?
<a name="understanding-cts"></a>

Change type refers to the action that an AWS Managed Services (AMS) request for change (RFC) performs and encompasses the change action itself, and the type of change – manual vs automated. AMS has a large collection of change types not used by other Amazon web services. You use these change types when submitting a request for change (RFC) to deploy, or manage, or gain access to, resources.

**Topics**
+ [Automated and manual CTs](ug-automated-or-manual.md)
+ [CT approval requirements](constrained-unconstrained-ctis.md)
+ [Change type versions](ct-versions.md)
+ [Create change types](ct-creates.md)
+ [Update change types](ct-updates.md)
+ [Internal-only change types](ct-internals.md)
+ [Change type schemas](ct-schemas.md)
+ [Managing permissions for change types](ct-permissions.md)
+ [Redacting sensitive information from change types](ct-redaction.md)
+ [Finding a change type, using the query option](ug-find-ct-ex-section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

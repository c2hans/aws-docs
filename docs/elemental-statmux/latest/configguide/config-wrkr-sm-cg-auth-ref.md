---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/configguide/config-wrkr-sm-cg-auth-ref.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# User Authentication Reference
<a name="config-wrkr-sm-cg-auth-ref"></a>

Enabling user authentication provides you more control over your AWS Elemental systems. Authentication helps secure your nodes while also allowing you to do the following:
+ Track node activity on a per-user basis.
+ Limit accidental access to a node by allowing distinct login credentials for each node. This way, an operator with access to multiple nodes must enter the credentials for a specific node prior to sending any commands.

Whether or not you enable authentication, we recommend that all of your nodes are installed behind a customer firewall or on a private network.

The following sections provide more information about user authentication.

**Topics**
+ [Supported Types of User Authentication](auth-ref-type-auth.md)
+ [Authentication User Types](auth-ref-type-user.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

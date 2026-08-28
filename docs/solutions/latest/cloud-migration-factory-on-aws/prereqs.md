---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/prereqs.html
---

# Prerequisites
<a name="prereqs"></a>

## Source server permissions
<a name="prereqs-domain"></a>

A domain user with local admin permissions to the in-scope source servers targeted for migration is required for Windows and Linux (sudo permissions) servers. If source servers are not in a domain, other users may be used, including an LDAP user with sudo/administrator permissions or a local sudo/administrator user. Before launching this solution, verify that you have the necessary permissions or have coordinated with the appropriate person in your organization with permissions.

## AWS Application Migration Service (AWS MGN)
<a name="aws-application-migration-service-aws-mgn"></a>

If you use AWS MGN for this solution, you must first initialize the AWS MGN service in every target account and region before launching the target account stack, refer to [Initializing Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html) in the *Application Migration Service User Guide* for more details.

## Private deployment
<a name="private-deploy"></a>

If you have chosen to deploy a **Private** instance of CMF, deploy a web server in your environment before proceeding with the CMF solution deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

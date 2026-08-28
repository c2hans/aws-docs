---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AccessPoliciesStatus.html
---

# AccessPoliciesStatus
<a name="API_AccessPoliciesStatus"></a>

## Description
<a name="API_AccessPoliciesStatus_Description"></a>

The configured access rules for the domain's document and search endpoints, and the current status of those rules.

## Contents
<a name="API_AccessPoliciesStatus_Contents"></a>

 **Options**
Access rules for a domain's document or search service endpoints. For more information, see [Configuring Access for a Search Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html) in the *Amazon CloudSearch Developer Guide*. The maximum size of a policy document is 100 KB.
Type: String
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

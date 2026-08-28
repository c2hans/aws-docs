---
source_url: https://docs.aws.amazon.com/singlesignon/latest/developerguide/making-api-requests.html
---

# Making API Requests
<a name="making-api-requests"></a>

IAM Identity Center SCIM implementation supports the bearer HTTP authentication scheme. An access token (also known as a bearer token) must be passed in the HTTP Authorization header of each request to your SCIM endpoint. See [Considerations for using automatic provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html#auto-provisioning-considerations) in the *IAM Identity Center User Guide* for instructions on generating and retrieving your access token.

Other authentication schemes described in the SCIM specifications are not supported at this time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center SCIM Implementation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

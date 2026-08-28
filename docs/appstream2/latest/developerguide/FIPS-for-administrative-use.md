---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/FIPS-for-administrative-use.html
---

# FIPS Endpoints for Administrative Use
<a name="FIPS-for-administrative-use"></a>

To specify a FIPS endpoint when you run an AWS CLI command for WorkSpaces Applications, use the `endpoint-url` parameter. The following example uses the WorkSpaces Applications FIPS endpoint in the US West (Oregon) Region to retrieve a list of all stacks in the Region:

```
aws appstream describe-stacks --endpoint-url https://appstream2-fips.us-west-2.amazonaws.com
```

To specify a FIPS endpoint for WorkSpaces Applications API operations, use the procedure in your AWS SDK for specifying a custom endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

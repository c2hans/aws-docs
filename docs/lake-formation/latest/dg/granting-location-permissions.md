---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/granting-location-permissions.html
---

# Granting data location permissions
<a name="granting-location-permissions"></a>

Data location permissions in AWS Lake Formation enable principals to create and alter Data Catalog resources that point to designated registered Amazon S3 locations. Data location permissions work in addition to Lake Formation data permissions to secure information in your data lake.

Lake Formation does not use the AWS Resource Access Manager (AWS RAM) service for data location permission grants, so you don't need to accept resource share invitations for data location permissions.

You can grant data location permissions by using the Lake Formation console, API, or AWS Command Line Interface (AWS CLI).

**Note**
For a grant to succeed, you must first register the data location with Lake Formation.

**See Also:**
[Underlying data access control](access-control-underlying-data.md#data-location-permissions)

**Topics**
+ [Granting data location permissions (same account)](granting-location-permissions-local.md)
+ [Granting data location permissions (external account)](granting-location-permissions-external.md)
+ [Granting permissions on a data location shared with your account](regranting-locations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

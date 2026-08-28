---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/unregister-location.html
---

# Deregistering an Amazon S3 location
<a name="unregister-location"></a>

You can deregister an Amazon Simple Storage Service (Amazon S3) location if you no longer want it to be managed by Lake Formation. Deregistering a location does not affect Lake Formation data location permissions that are granted on that location. You can reregister a location that you deregistered, and the data location permissions remain in effect. You can use a different role to reregister the location.

**To deregister a location (console)**

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Sign in as the data lake administrator or as a user with the `lakeformation:RegisterResource` IAM permission.

1. In the navigation pane, under **Administration**, choose **Data lake locations**.

1. Select a location, and on the **Actions** menu, choose **Remove**.

1. When prompted for confirmation, choose **Remove**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

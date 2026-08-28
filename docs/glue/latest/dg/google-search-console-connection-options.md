---
source_url: https://docs.aws.amazon.com/glue/latest/dg/google-search-console-connection-options.html
---

# Google Search Console connection options
<a name="google-search-console-connection-options"></a>

The following are connection options for Google Search Console:
+ `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Google Search Console.
+ `API_VERSION`(String) - (Required) Used for Read. Google Search Console Rest API version you want to use.
+ `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+ `FILTER_PREDICATE`(String) - Default: "start\_end\_date between <30 days ago from current date> AND <yesterday: that is, 1 day ago from the current date>". Used for Read. It should be in the Spark SQL format.
+ `QUERY`(String) - Default: "start\_end\_date between <30 days ago from current date> AND <yesterday: that is, 1 day ago from the current date>" Used for Read. Full Spark SQL query.
+ `INSTANCE_URL`(String) - Used for Read. A valid Google Search Console instance URL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

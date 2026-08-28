---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-06-18-config-search.html
---

# Release: Elastic Beanstalk console adds environment configuration option search on June 18, 2019
<a name="release-2019-06-18-config-search"></a>

The Elastic Beanstalk console adds a new table view to environment configuration. You can search for options by name or value.

**Release date:** June 18, 2019

## Changes
<a name="release-2019-06-18-config-search.changes"></a>

The environment configuration page in the Elastic Beanstalk console has several configuration categories, each with a group of options. Previously, the page showed a summary for each category on a configuration card (the **Grid View**). Finding the right category to edit when you needed to change a particular option was a challenge.

Starting with today's release, the Elastic Beanstalk console adds an alternative **Table View**, which shows all configuration options in a table, grouped by category. You can search for an option by its name or value by entering search terms into a search box. As you type, the list gets shorter and shows only options that match your search terms.

![Table view of the configuration overview page of the Elastic Beanstalk console, showing an option search](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/images/2019-06-13-config-search.cfg-table-search.png)

For more information about configuring environment options, see [AWS Elastic Beanstalk Environment Configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

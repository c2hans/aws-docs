---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/analyze-data.html
---

# Analyze data in a collaboration
<a name="analyze-data"></a>

In AWS Clean Rooms, you can analyze data by running queries or jobs.

A *query* is a method to access and analyze configured tables in a collaboration, using a supported set of functions, classes, and variables. The currently supported query language in AWS Clean Rooms is SQL. There are 3 ways to run a query in AWS Clean Rooms: Write SQL code, use an approved SQL analysis template, or use the Analysis builder UI.

A *job* is a method to access and analyze configured tables in a collaboration using a supported set of functions, classes, and variables. The currently supported type of job in AWS Clean Rooms is PySpark. There is one way to run a job in AWS Clean Rooms: by using an approved PySpark analysis template.

The following topics describe how to analyze data in AWS Clean Rooms by running SQL queries or PySpark jobs.

**Topics**
+ [Running SQL queries](running-sql-queries.md)
+ [Running PySpark jobs](run-jobs.md)
+ [Using an intermediate table in analyses](use-intermediate-table.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

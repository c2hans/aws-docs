---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/understanding-materialized-views.html
---

# Understanding materialized views
<a name="understanding-materialized-views"></a>

## Views
<a name="views"></a>

A view is a virtual table that's based on the result set of a SQL `SELECT` query. The virtual table contains the data retrieved from the query expression, but the result isn't stored on disk. When you use views, you always get the most up-to-date data because the query pulls the data from the original tables every single time that you run the query. You can create a view from one or more base tables or views. You can also query a view the same way that you query the original base tables.

The following example query shows how to create a view:

```
CREATE VIEW tickets_view
AS
   select e.eventname,
          sum(s.price) as total_sales
   from sales s
   join event e
       on e.eventid = s.eventid
   group by e.eventname;
```

The following example query shows how to query a view:

```
select eventname,
       total_sales
from ticket_view
where eventname = 'Gotterburg';
```

## Materialized views
<a name="materialized-views"></a>

A materialized view is a database object that contains the results of a query. For example, a materialized view can be any of the following:
+ A local copy of data located remotely
+ A subset of the rows or columns of a table or join result
+ A summary using an aggregate function

## Comparison of view types
<a name="view-type-comparison"></a>

The following table summarizes the differences between a view and materialized view.

|
|
| Key | View | Materialized view |
| --- |--- |--- |
| Definition | A virtual table that doesn't store any data, but instead runs a defined SQL query to get data from one or more tables in a database | A virtual table that's defined by an editable SQL query, but the result of the query gets stored on disk |
| Storage | Result of the query expression is not stored on disk—only the query expression is stored on disk | Query expression and the result of the query expression both stored on disk |
| Run | The query that defines the view runs every time the view is referenced in a query | The result of the query is stored on disk, and the query expression doesn't run every time a user tries to fetch the data from a materialized view |
| Data recency | Always provides the latest updated value from the base tables | Doesn't provide the latest updated value if that value gets changed in the database |
| Cost | No storage cost | Has a storage cost |
| Design | To create a standard view, you must:<br />·         Have access to the underlying tables<br />·         Use a standard `SELECT` statement | To create a materialized view, you must:<br />·         Have access to the underlying tables<br />·         Use a standard `SELECT` statement<br />Optionally, you can specify the following:<br />·         Whether the materialized view is included in automated and manual cluster snapshots, which are stored in Amazon Simple Storage Service (Amazon S3)<br />·         How the data in the materialized view is distributed and sorted<br />·         Whether the materialized view should be automatically refreshed with the latest changes from its base tables |
| Usage | When data is accessed or updated infrequently | When data is accessed or updated frequently |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

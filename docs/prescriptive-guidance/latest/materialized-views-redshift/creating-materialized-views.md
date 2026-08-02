---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/creating-materialized-views.html
---

# Creating materialized views
<a name="creating-materialized-views"></a>

You can create a materialized view based on one or more of the following:
+ Amazon Redshift tables
+ External tables that you can create by using [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) or a [federated query](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html)
+ Other materialized views

When you create a materialized view, Amazon Redshift runs the user-specified SQL statement to gather the data from the base table or tables. Then, Amazon Redshift stores the result set.

The following illustration provides an overview of a materialized view called `mv_total_orders`. This view is defined by a SQL query that uses two base tables: customer and order.

![SQL query with two base tables](http://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/images/guide-img/fd96a9bf-2877-4487-8c53-466d142e055c/images/45279be2-b622-466b-b80e-1889ef956cb7.png)

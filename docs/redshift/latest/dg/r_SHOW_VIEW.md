---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_VIEW.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# SHOW VIEW
<a name="r_SHOW_VIEW"></a>

Shows the definition of a view, including for materialized views and late-binding views. You can use the output of the SHOW VIEW statement to recreate the view.

## Syntax
<a name="r_SHOW_VIEW-synopsis"></a>

```
SHOW VIEW [schema_name.]view_name
```

## Parameters
<a name="r_SHOW_VIEW-parameters"></a>

 *schema\_name*
(Optional) The name of the related schema.

 *view\_name*
The name of the view to show.

## Examples
<a name="r_SHOW_VIEW-examples"></a>

 Following is the view definition for the view `LA_Venues_v`.

```
create view LA_Venues_v as select * from venue where venuecity='Los Angeles';
```

Following is an example of the SHOW VIEW command and output for the view defined preceding.

```
show view LA_Venues_v;
```

```
SELECT venue.venueid,
venue.venuename,
venue.venuecity,
venue.venuestate,
venue.venueseats
FROM venue WHERE ((venue.venuecity)::text = 'Los Angeles'::text);
```

Following is the view definition for the view `public.Sports_v` in the schema `public`.

```
create view public.Sports_v as select * from category where catgroup='Sports';
```

Following is an example of the SHOW VIEW command and output for the view defined preceding.

```
show view public.Sports_v;
```

```
SELECT category.catid,
category.catgroup,
category.catname,
category.catdesc
FROM category WHERE ((category.catgroup)::text = 'Sports'::text);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

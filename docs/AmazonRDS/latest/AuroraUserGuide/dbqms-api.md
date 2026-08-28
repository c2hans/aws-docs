---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/dbqms-api.html
---

# Database Query Metadata Service (DBQMS) API reference
<a name="dbqms-api"></a>

The Database Query Metadata Service (`dbqms`) is an internal-only service. It provides your recent and saved queries for the query editor on the AWS Management Console for multiple AWS services, including Amazon RDS.

**Topics**
+ [CreateFavoriteQuery](#CreateFavoriteQuery)
+ [CreateQueryHistory](#CreateQueryHistory)
+ [CreateTab](#CreateTab)
+ [DeleteFavoriteQueries](#DeleteFavoriteQueries)
+ [DeleteQueryHistory](#DeleteQueryHistory)
+ [DeleteTab](#DeleteTab)
+ [DescribeFavoriteQueries](#DescribeFavoriteQueries)
+ [DescribeQueryHistory](#DescribeQueryHistory)
+ [DescribeTabs](#DescribeTabs)
+ [GetQueryString](#GetQueryString)
+ [UpdateFavoriteQuery](#UpdateFavoriteQuery)
+ [UpdateQueryHistory](#UpdateQueryHistory)
+ [UpdateTab](#UpdateTab)

## CreateFavoriteQuery
<a name="CreateFavoriteQuery"></a>

Save a new favorite query. Each user can create up to 1000 saved queries. This limit is subject to change in the future.

## CreateQueryHistory
<a name="CreateQueryHistory"></a>

Save a new query history entry.

## CreateTab
<a name="CreateTab"></a>

Save a new query tab. Each user can create up to 10 query tabs.

## DeleteFavoriteQueries
<a name="DeleteFavoriteQueries"></a>

Delete one or more saved queries.

## DeleteQueryHistory
<a name="DeleteQueryHistory"></a>

Delete query history entries.

## DeleteTab
<a name="DeleteTab"></a>

Delete query tab entries.

## DescribeFavoriteQueries
<a name="DescribeFavoriteQueries"></a>

List saved queries created by a user in a given account.

## DescribeQueryHistory
<a name="DescribeQueryHistory"></a>

List query history entries.

## DescribeTabs
<a name="DescribeTabs"></a>

List query tabs created by a user in a given account.

## GetQueryString
<a name="GetQueryString"></a>

Retrieve full query text from a query ID.

## UpdateFavoriteQuery
<a name="UpdateFavoriteQuery"></a>

Update the query string, description, name, or expiration date.

## UpdateQueryHistory
<a name="UpdateQueryHistory"></a>

Update the status of query history.

## UpdateTab
<a name="UpdateTab"></a>

Update the query tab name and query string.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

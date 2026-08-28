---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/limits.html
---

# AWS Service Catalog default service quotas
<a name="limits"></a>

Your AWS account has the following default quotas for AWS Organizations, constraint, portfolio, product, provisioned product, regional, service action, and TagOptions.

## AWS Organizations
<a name="orgs"></a>
+  AWS Service Catalog delegated administrators per organization: 50

## Constraint quotas
<a name="constraint"></a>
+ Constraints per product per portfolio: 100

## Portfolio quotas
<a name="portfolio"></a>
+ Users, groups, and roles per portfolio: 100
+ Products per portfolio: 150
+ Tags per portfolio: 20
+ Shared accounts per portfolio: 5000
+ Tag values per tag key: 25

## Product quotas
<a name="product"></a>
+ Users, groups, and roles per product: 200
+ Product versions per product: 100
+ Tags per product: 20
+ Tag values per tag key: 25

## Provisioned product quotas
<a name="provisioned"></a>
+ Tags per provisioned product: 50

## Regional quotas
<a name="regional"></a>
+ Portfolios: 100
+ Products: 350

## Service action quotas
<a name="serv-action"></a>
+ Service actions per region: 200
+ Service action associations per product version: 25

## TagOptions quotas
<a name="tagoption"></a>
+ TagOptions per resource: 25
+ Values per TagOption: 25

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

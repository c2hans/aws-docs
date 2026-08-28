---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_SESSION_ARN.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# CURRENT\_SESSION\_ARN
<a name="r_CURRENT_SESSION_ARN"></a>

Returns the ARN of the currently authorized global user. Global users present with the same identity across Redshift accounts, clusters, and Serverless workgroups. Global users log in through IAM Identity Center, or through IAM-based session authentication. Data lake users are global AWS users.

This function is typically used in the context of using multi-dialect AWS Glue views. For more information about identity management with IAM Identity Center and Redshift, see [Connect Redshift with IAM Identity Center to give users a single sign-on experience](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html). For more information about multi-dialect Glue views [Creating views in the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html).

## Syntax
<a name="r_CURRENT_SESSION_ARN-synopsis"></a>

```
current_session_arn()
```

## Return type
<a name="r_CURRENT_SESSION_ARN-return-type"></a>

Returns a VARCHAR string of the globally authenticated user or a null value.

## Usage notes
<a name="r_CURRENT_SESSION_ARN-usage"></a>

Local users aren't supported and result in a null response.

## Example
<a name="r_CURRENT_SESSION_ARN-example"></a>

The following query returns the name of the current session ARN:

```
SELECT current_session_arn();

current_session_arn
--------------
arn:aws:iam::123456789012:user/user
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-lake-formation-permission-errors.html
---

# AWS Lake Formation permission errors
<a name="aws-lake-formation-permission-errors"></a>

This solution is configured to use IAM permissions for all AWS AWS Glue Data Catalog resources. If you had previously configured your AWS account to use Lake Formation for all new database and tables prior to deploying the solution you might see the following error when the Metric ETL Glue Job attempts to run for the first time:

```
AccessDeniedException: An error occurred (AccessDeniedException) when calling the GetTable operation: Insufficient Lake Formation permission(s)
```

To fix this error without reverting your account-wide permissions back to the default settings, you must grant the Glue Job IAM role permission to access the solution database and table resources.

1. To grant the `MetricsEtlJobRole` **Super** permissions to all tables within the solution database, see [Granting table permissions using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-table-permissions.html) in the *AWS Lake Formation Developer Guide*.

1. Re-run any failed Glue jobs, making sure to pass in the `--object_keys` parameter with the failed parameter values from previous runs.

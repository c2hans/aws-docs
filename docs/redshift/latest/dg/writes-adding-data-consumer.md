---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/writes-adding-data-consumer.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Adding data consumers to a datashare in Amazon Redshift
<a name="writes-adding-data-consumer"></a>

You can add one or more data consumers to the datashares on the console or with SQL. Data consumers can be namespaces that uniquely identified Amazon Redshift clusters or AWS accounts.

------
#### [ Console ]

You must explicitly choose to turn off or turn on sharing your datashare to clusters with public access.
+ Choose **Add namespaces to the datashare**. Namespaces are globally unique identifier (GUID) for Amazon Redshift cluster.
+ Choose **Add AWS accounts** to the datashare. The specified AWS accounts must have access permissions to the datashare.

------
#### [ SQL ]

With SQL, the administrator grants usage on the datashare to a specific namespace in the account. You can find the namespace ID as part of the ARN in the cluster details page, in the Amazon Redshift Serverless namespace details page, or by running the command `SELECT current_namespace;`. For more information, see [CURRENT\_NAMESPACE](https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_NAMESPACE.html).

```
GRANT USAGE ON DATASHARE my_datashare TO NAMESPACE '86b5169f-012a-234b-9fbb-e2e24359e9a8';
```

The following is an example of how to grant usage of a datashare to an AWS account.

```
GRANT USAGE ON DATASHARE salesshare TO ACCOUNT '123456789012';
```

The following is an example of how to grant usage of a datashare to a Lake Formation account.

```
GRANT USAGE ON DATASHARE salesshare TO ACCOUNT '123456789012' VIA DATA CATALOG;
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

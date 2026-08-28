---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/feature-store.html
---

# Feature Store
<a name="feature-store"></a>

Using [SageMaker Feature Store](https://aws.amazon.com/sagemaker/feature-store/) increases team productivity, because it decouples component boundaries (for example, storage versus usage). It also provides feature reusability across different data science teams within your organization.

## Use time travel queries
<a name="use-time-travel-queries"></a>

Time travel capabilities in Feature Store help reproduce model builds and support stronger governance practices. This can be useful when an organization wants to assess data lineage, similar to how version control tools such as Git assess code. Time travel queries also help organizations provide accurate data for compliance checks. For more information, see [Understanding the key capabilities of Amazon SageMaker Feature Store](https://aws.amazon.com/blogs/machine-learning/understanding-the-key-capabilities-of-amazon-sagemaker-feature-store/) on the AWS Machine Learning blog.

## Use IAM roles
<a name="use-iam-roles"></a>

Feature Store also helps improve security without affecting team productivity and innovation. You can use [AWS Identity and Access Management (IAM) roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to give or restrict granular access to specific features for specific users or groups.

For example, the following policy restricts access to a sensitive feature in Feature Store.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/12345678910/sagemaker/us-east-2/offline-store/doctor-appointments"
        }
    ]
}
```

For more information about data security and encryption using Feature Store, see [Security and access control](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-security.html) in the SageMaker documentation.

## Use unit testing
<a name="use-unit-testing"></a>

When data scientists create models based on some data, they often make assumptions about the distribution of the data, or they perform a thorough analysis to fully understand the data properties. When these models are deployed, they eventually become stale. When the dataset becomes outdated, data scientists, ML engineers, and (in some cases) automated systems retrain the model with new data that is fetched from an online or offline store.

However, the distribution of this new data might have changed, which could affect the current algorithm's performance. An automated way to check for these types of issues is to borrow the concept of *unit testing* from software engineering. Common things to test for include the percentage of missing values, the cardinality of categorical variables, and whether real valued columns adhere to some expected distribution by using a framework such as hypothesis test statistics ([*t*-test](https://en.wikipedia.org/wiki/Student%27s_t-test)). You might also want to validate the data schema, to make sure it hasn't changed and won't generate invalid input features silently.

Unit testing requires understanding the data and its domain so you can plan the exact assertions to perform as part of the ML project. For more information, see [Testing data quality at scale with PyDeequ](https://aws.amazon.com/blogs/big-data/testing-data-quality-at-scale-with-pydeequ/) on the AWS Big Data blog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

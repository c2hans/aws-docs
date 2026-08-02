---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/tagging-practices-to-avoid.html
---

# Tagging practices to avoid
<a name="tagging-practices-to-avoid"></a>

While there are practices to implement when tagging objects or infrastructure on AWS, there are also practices to avoid.

## Inconsistent tagging
<a name="inconsistent"></a>

As covered in the [Objectives](objectives.md) section, without tagging, you cannot achieve a high level of automation, cleanup, or monitoring. Similarly, with incomplete or inconsistent tags, the information required for automation or monitoring is not complete, leading to unreliable results.

Imagine a scenario where you use a tagging strategy to calculate the total costs for all projects. The strategy starts at the proof-of-concept phase (PoC) and ends at the production phase. Consider the following scenarios with tags applied to data and resources for project Sales Forecasting P1, D1, and Pr1 examples and for project Post-Sales Maintenance P2, D2, and Pr2 examples.

### Sales Forecasting
<a name="sales-forecasting.9bd6932d-d56c-5e72-839f-b2a3715b5693"></a>

Example P1: PoC project (domain and timestamp missing).

```
env: "poc"
project: "sales forecasting"
```

Example D1: Development phase (domain missing).

```
env: "dev"
project: "sales forecasting"
timestamp: 20210505T12:34:55
```

Example Pr1: Production phase (all values exist).

```
env: "prod"
project: "sales forecasting"
domain: "machine learning"
timestamp: 20210505T12:34:55
```

For project Sales Forecasting:
+ Example P1 does not mention what domain or timestamp the object was from.
+ Example D1 also does not mention the domain of project.
+ Example Pr1 has all the required data.

Examples P1 and D1 wil result in incorrect reporting or estimates for planning because the domains are not defined.

### Post-Sales Maintenance
<a name="post-sales-maintenance.f508c56a-89ae-53f6-b1fc-463255ba7fbd"></a>

Example P2: PoC project (all tags missing).

Example D2: Development phase (project missing).

```
env: "dev"
domain: "machine learning"
timestamp: 20210505T12:34:55
```

Example Pr2: Production phase (all values exist).

```
env: "prod"
project: "post sales maintenance"
domain: "machine learning"
timestamp: 20210505T12:34:55
```

For project Post Sales Maintenance:
+ Example P2 does not have any information, so it cannot be tracked.
+ Example D2 doesn't mention the project name, so it cannot be tracked.
+ Example Pr2 has all the required data.

Examples P2 and D2 will result in incorrect reporting, under planning, or underreporting because of missing or inconsistent tags.

Therefore, it's important to implement the tagging strategy consistently.

## Incorrect and sensitive data in tags
<a name="incorrect-sensitive"></a>

Tagging can be counterproductive if used with incorrect or sensitive or private information. Incorrect tags can produce misleading results. Using tags that include sensitive data, such as personally identifiable information (PII), can put the security of your customers and employees at risk.

### Incorrect information in tags
<a name="incorrect-information-in-tags.8735da7e-49f0-59e6-91ba-23f9e475206a"></a>

Imagine a scenario where you use a tagging strategy to calculate the total costs for each domain or department. You have just finished your data ingestion phase and are moving toward machine learning. The following example includes custom tags that have been copied from the previous phase of a project.

```
env: "development"
project: "sales prediction"
domain: "data ingestion"
timestamp: 20210505T12:34:55
```

The domain is incorrectly labeled as `data ingestion` from the previous project phase, instead of the correct domain, which is `machine learning`. Now, the reports for the `data ingestion` domain will show higher costs, time range, and resource allocation. The `machine learning` domain will show lower values for those reports. This will result in incorrect planning, budget allocation, and deadline estimates.

Having the correct tags is essential for a functional system.

### Sensitive information in tags
<a name="sensitive-information-in-tags.9e3bfea3-6cb0-5942-9c6d-6d30ae3f6ec0"></a>

AWS provides several tools for identifying PII in objects. These tools include [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) and [AWS Glue sensitive data detection](https://docs.aws.amazon.com/glue/latest/ug/detect-PII.html) to find data that can be used to identify individuals. However, it's important not to use PII or sensitive data in tags.

Consider the following example of a file in Amazon S3 that has PII redacted or anonymized.

```
{
  firstName: "67A1790DCA55B8803AD024EE28F616A2",
  lastName: "DRG54654DFHJGDYYRD",
  age: 21,
  city : "Frankfurt",
  probability_of_purchase: 48.858093,
  veggieName: "broccoli",
  creditcard: false
}
```

You can see that the customer first name and last name have been hashed. However, in this example, the record has the following custom tags.

```
owner: "Company XYZ"
about: "John Doe"
contact: "johnthegreat@email.com"
timestamp: 20210505T12:34:55
```

In this case, although the file itself contains no PII, the tags do contain sensitive information. This increases the probability of an information leak, because when you share or transfer a file or object, you also share or transfer its metadata. This also applies to other AWS resources, such as a database, tables, jobs, and functions.

Therefore it's extremely important to avoid using private information in tags. The same concept extends to crucial or nonpublic information.

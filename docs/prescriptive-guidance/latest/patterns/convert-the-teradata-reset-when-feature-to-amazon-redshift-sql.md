---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-the-teradata-reset-when-feature-to-amazon-redshift-sql.html
---

# Convert the Teradata RESET WHEN feature to Amazon Redshift SQL
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql"></a>

*Po Hong, Amazon Web Services*

## Summary
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-summary"></a>

**RESET WHEN** is a Teradata feature used in SQL analytical window functions. It is an extension to the ANSI SQL standard. **RESET WHEN** determines the partition over which an SQL window function operates based on some specified condition. If the condition evaluates to **TRUE**, a new, dynamic sub-partition is created inside the existing window partition. For more information about **RESET WHEN**, see the [Teradata documentation](https://docs.teradata.com/reader/1DcoER_KpnGTfgPinRAFUw/b7wL86OoMTPno6hrSPNdDg).

Amazon Redshift doesn’t support **RESET WHEN** in SQL window functions. To implement this functionality, you have to convert **RESET WHEN** to the native SQL syntax in Amazon Redshift, and use multiple, nested functions. This pattern demonstrates how you can use the Teradata **RESET WHEN** feature and how you can convert it to Amazon Redshift SQL syntax.

## Prerequisites and limitations
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-prereqs"></a>

**Prerequisites**
+ Basic knowledge of the Teradata data warehouse and its SQL syntax
+ Good understanding of Amazon Redshift and its SQL syntax

## Architecture
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-architecture"></a>

**Source technology stack**
+ Teradata data warehouse

**Target technology stack**
+ Amazon Redshift

**Architecture**

For a high-level architecture for migrating a Teradata database to Amazon Redshift, see the pattern [Migrate a Teradata database to Amazon Redshift using AWS SCT data extraction agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-teradata-database-to-amazon-redshift-using-aws-sct-data-extraction-agents.html). The migration doesn't automatically convert the Teradata **RESET WHEN** phrase to Amazon Redshift SQL. You can convert this Teradata extension by following the guidelines in the next section.

## Tools
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-tools"></a>

**Code**

To illustrate the concept of **RESET WHEN**, consider the following table definition in Teradata:

```
create table systest.f_account_balance
( account_id integer NOT NULL,
  month_id integer,
  balance integer )
unique primary index (account_id, month_id);
```

Run the following SQL code to insert sample data into the table:

```
BEGIN TRANSACTION;
Insert Into systest.f_account_balance values (1,1,60);
Insert Into systest.f_account_balance values (1,2,99);
Insert Into systest.f_account_balance values (1,3,94);
Insert Into systest.f_account_balance values (1,4,90);
Insert Into systest.f_account_balance values (1,5,80);
Insert Into systest.f_account_balance values (1,6,88);
Insert Into systest.f_account_balance values (1,7,90);
Insert Into systest.f_account_balance values (1,8,92);
Insert Into systest.f_account_balance values (1,9,10);
Insert Into systest.f_account_balance values (1,10,60);
Insert Into systest.f_account_balance values (1,11,80);
Insert Into systest.f_account_balance values (1,12,10);
END TRANSACTION;
```

The sample table has the following data:

|
|
| account\_id | month\_id | balance |
| --- |--- |--- |
| 1 | 1 | 60 |
| 1 | 2 | 99 |
| 1 | 3 | 94 |
| 1 | 4 | 90 |
| 1 | 5 | 80 |
| 1 | 6 | 88 |
| 1 | 7 | 90 |
| 1 | 8 | 92 |
| 1 | 9 | 10 |
| 1 | 10 | 60 |
| 1 | 11 | 80 |
| 1 | 12 | 10 |

For each account, let’s say that you want to analyze the sequence of consecutive monthly balance increases. When one month’s balance is less than, or equal to, the previous month’s balance, the requirement is to reset the counter to zero and restart.

*Teradata RESET WHEN use case*

To analyze this data, Teradata SQL uses a window function with a nested aggregate and a **RESET WHEN** phrase, as follows:

```
SELECT account_id, month_id, balance,
 ( ROW_NUMBER() OVER (PARTITION BY account_id ORDER BY month_id
RESET WHEN balance <= SUM(balance) over (PARTITION BY account_id ORDER BY month_id ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING) ) -1 ) as balance_increase
FROM systest.f_account_balance
ORDER BY 1,2;
```

Output:

|
|
|  account\_id | month\_id | balance | balance\_increase |
| --- |--- |--- |--- |
| 1 | 1 | 60 | 0 |
| 1 | 2 | 99 | 1 |
| 1 | 3 | 94 | 0 |
| 1 | 4 | 90 | 0 |
| 1 | 5 | 80 | 0 |
| 1 | 6 | 88 | 1 |
| 1 | 7 | 90 | 2 |
| 1 | 8 | 92 | 3 |
| 1 | 9 | 10 | 0 |
| 1 | 10 | 60 | 1 |
| 1 | 11 | 80 | 2 |
| 1 | 12 | 10 | 0 |

The query is processed as follows in Teradata:

1. The **SUM(balance)** aggregate function calculates the sum of all balances for a given account in a given month.

1. We check to see if a balance in a given month (for a given account) is greater than the balance of the previous month.

1. If the balance increased, we track a cumulative count value. If the **RESET WHEN** condition evaluates to **false**, which means that the balance has increased over successive months, we continue to increase the count.

1. The **ROW\_NUMBER()** ordered analytical function calculates the count value. When we reach a month whose balance is less than, or equal to, the balance of the previous month, the **RESET WHEN** condition evaluates to **true**. If so, we start a new partition and **ROW\_NUMBER()** restarts the count from 1. We use **ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING** to access the value of the previous row.

1. We subtract 1 to ensure that the count value starts with 0.

*Amazon Redshift equivalent SQL*

Amazon Redshift doesn’t support the **RESET WHEN** phrase in an SQL analytical window function.  To produce the same result, you must rewrite the Teradata SQL using Amazon Redshift native SQL syntax and nested sub-queries, as follows:

```
SELECT account_id, month_id, balance,
   (ROW_NUMBER() OVER(PARTITION BY account_id, new_dynamic_part ORDER BY month_id) -1) as balance_increase
FROM
( SELECT account_id, month_id, balance, prev_balance,
SUM(dynamic_part) OVER (PARTITION BY account_id ORDER BY month_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) As new_dynamic_part
FROM ( SELECT account_id, month_id, balance,
SUM(balance) over (PARTITION BY account_id ORDER BY month_id ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING) as prev_balance,
(CASE When balance <= prev_balance Then 1 Else 0 END) as dynamic_part
FROM systest.f_account_balance ) A
) B
ORDER BY 1,2;
```

Because Amazon Redshift doesn’t support nested window functions in the **SELECT** clause of a single SQL statement, you must use two nested sub-queries.
+ In the inner sub-query (alias A), a dynamic partition indicator (**dynamic\_part**) is created and populated. **dynamic\_part** is set to 1 if one month’s balance is less than or equal to the preceding month’s balance; otherwise, it’s set to 0.
+ In the next layer (alias B), a **new\_dynamic\_part** attribute is generated as the result of a **SUM** window function.
+ Finally, you add **new\_dynamic\_part** as a new partition attribute (**dynamic partition**) to the existing partition attribute (**account\_id**) and apply the same **ROW\_NUMBER()** window function as in Teradata (and minus one).

After these changes, Amazon Redshift SQL generates the same output as Teradata.

## Epics
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-epics"></a>

### Convert RESET WHEN to Amazon Redshift SQL
<a name="convert-reset-when-to-amazon-redshift-sql"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create your Teradata window function. | Use nested aggregates and the RESET WHEN phrase according to your needs. | SQL developer |
| Convert the code to Amazon Redshift SQL. | To convert your code, follow the guidelines in the "Tools" section of this pattern. | SQL developer |
| Run the code in Amazon Redshift. | Create your table, load data into the table, and run your code in Amazon Redshift. | SQL developer |

## Related resources
<a name="convert-the-teradata-reset-when-feature-to-amazon-redshift-sql-resources"></a>

**References**
+ [RESET WHEN Phrase](https://docs.teradata.com/reader/1DcoER_KpnGTfgPinRAFUw/b7wL86OoMTPno6hrSPNdDg) (Teradata documentation)
+ [RESET WHEN explanation](https://stackoverflow.com/questions/53344536/teradata-reset-when-partition-by-order-by) (Stack Overflow)
+ [Migrate to Amazon Redshift](https://aws.amazon.com/redshift/data-warehouse-migration/) (AWS website)
+ [Migrate a Teradata database to Amazon Redshift using AWS SCT data extraction agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-teradata-database-to-amazon-redshift-using-aws-sct-data-extraction-agents.html) (AWS Prescriptive Guidance)
+ [Convert the Teradata NORMALIZE temporal feature to Amazon Redshift SQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql.html) (AWS Prescriptive Guidance)

**Tools**
+ [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/)

**Partners**
+ [AWS Migration Competency Partners](https://aws.amazon.com/migration/partner-solutions/#delivery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

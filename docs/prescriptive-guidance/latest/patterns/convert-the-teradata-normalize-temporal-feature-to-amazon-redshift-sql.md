---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql.html
---

# Convert the Teradata NORMALIZE temporal feature to Amazon Redshift SQL
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql"></a>

*Po Hong, Amazon Web Services*

## Summary
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-summary"></a>

**NORMALIZE** is a Teradata extension to the ANSI SQL standard. When a SQL table includes a column that has a **PERIOD** data type, **NORMALIZE** combines values that meet or overlap in that column, to form a single period that consolidates multiple, individual period values. To use **NORMALIZE**, at least one column in the SQL **SELECT** list must be of Teradata's temporal **PERIOD** data type. For more information about **NORMALIZE**, see the [Teradata documentation](https://docs.teradata.com/reader/2_MC9vCtAJRlKle2Rpb0mA/MIGI5UMEwgERC3Un7tEZ6g).

Amazon Redshift doesn’t support **NORMALIZE**, but you can implement this functionality by using native SQL syntax and the **LAG** window function in Amazon Redshift. This pattern focuses on using the Teradata **NORMALIZE** extension with the **ON MEETS OR OVERLAPS** condition, which is the most popular format. It explains how this feature works in Teradata and how it can be converted into Amazon Redshift native SQL syntax.

## Prerequisites and limitations
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-prereqs"></a>

**Prerequisites**
+ Basic Teradata SQL knowledge and experience
+ Amazon Redshift knowledge and experience

## Architecture
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-architecture"></a>

**Source technology stack**
+ Teradata data warehouse

**Target technology stack**
+ Amazon Redshift

**Target architecture**

For a high-level architecture for migrating a Teradata database to Amazon Redshift, see the pattern [Migrate a Teradata database to Amazon Redshift using AWS SCT data extraction agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-teradata-database-to-amazon-redshift-using-aws-sct-data-extraction-agents.html). The migration doesn't automatically convert the Teradata **NORMALIZE** phrase to Amazon Redshift SQL. You can convert this Teradata extension by following the guidelines in this pattern.

## Tools
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-tools"></a>

**Code**

To illustrate the concept and functionality of **NORMALIZE**, consider the following table definition in Teradata:

```
CREATE TABLE systest.project
     (    emp_id        INTEGER,
          project_name  VARCHAR(20),
          dept_id       INTEGER,
          duration      PERIOD(DATE)
     );
```

Run the following SQL code to insert sample data into the table:

```
BEGIN TRANSACTION;

INSERT INTO systest.project VALUES (10, 'First Phase', 1000,  PERIOD(DATE '2010-01-10', DATE '2010-03-20') );
INSERT INTO systest.project VALUES (10, 'First Phase', 2000,  PERIOD(DATE '2010-03-20', DATE '2010-07-15') );

INSERT INTO systest.project VALUES (10, 'Second Phase', 2000,  PERIOD(DATE '2010-06-15', DATE '2010-08-18') );
INSERT INTO systest.project VALUES (20, 'First Phase', 2000,  PERIOD(DATE '2010-03-10', DATE '2010-07-20') );

INSERT INTO systest.project VALUES (20, 'Second Phase', 1000,  PERIOD(DATE '2020-05-10', DATE '2020-09-20') );

END TRANSACTION;
```

Results:

```
select * from systest.project order by 1,2,3;

 *** Query completed. 4 rows found. 4 columns returned.
 *** Total elapsed time was 1 second.

     emp_id  project_name              dept_id  duration
-----------  --------------------  -----------  ------------------------
         10  First Phase                  1000  ('10/01/10', '10/03/20')
         10  First Phase                  2000  ('10/03/20', '10/07/15')
         10  Second Phase                 2000  ('10/06/15', '10/08/18')
         20  First Phase                  2000  ('10/03/10', '10/07/20')
         20  Second Phase                 1000  ('20/05/10', '20/09/20')
```

*Teradata NORMALIZE use case*

Now add the Teradata **NORMALIZE** SQL clause to the **SELECT** statement:

```
SELECT NORMALIZE ON MEETS OR OVERLAPS emp_id, duration
FROM systest.project
ORDER BY 1,2;
```

This **NORMALIZE** operation is performed on a single column (`emp_id`). For `emp_id=10`, the three overlapping period values in duration coalesce into a single period value, as follows:

```
     emp_id  duration
-----------  ------------------------
         10  ('10/01/10', '10/08/18')
         20  ('10/03/10', '10/07/20')
         20  ('20/05/10', '20/09/20')
```

The following **SELECT** statement performs a **NORMALIZE** operation on `project_name` and `dept_id`. Note that the **SELECT** list contains only one **PERIOD** column, `duration`.

```
SELECT NORMALIZE project_name, dept_id, duration
FROM systest.project;
```

Output:

```
project_name              dept_id  duration
--------------------  -----------  ------------------------
First Phase                  1000  ('10/01/10', '10/03/20')
Second Phase                 1000  ('20/05/10', '20/09/20')
First Phase                  2000  ('10/03/10', '10/07/20')
Second Phase                 2000  ('10/06/15', '10/08/18')
```

*Amazon Redshift equivalent SQL*

Amazon Redshift currently doesn’t support the **PERIOD** data type in a table. Instead, you need to divide a Teradata **PERIOD** data field into two parts: `start_date, end_date`, as follows:

```
CREATE TABLE systest.project
     (    emp_id        INTEGER,
          project_name  VARCHAR(20),
          dept_id       INTEGER,
          start_date  DATE,
          end_date    DATE
     );
```

Insert sample data into the table:

```
BEGIN TRANSACTION;

INSERT INTO systest.project VALUES (10, 'First Phase', 1000,  DATE '2010-01-10', DATE '2010-03-20' );
INSERT INTO systest.project VALUES (10, 'First Phase', 2000,  DATE '2010-03-20', DATE '2010-07-15');

INSERT INTO systest.project VALUES (10, 'Second Phase', 2000,  DATE '2010-06-15', DATE '2010-08-18' );
INSERT INTO systest.project VALUES (20, 'First Phase', 2000,  DATE '2010-03-10', DATE '2010-07-20' );

INSERT INTO systest.project VALUES (20, 'Second Phase', 1000,  DATE '2020-05-10', DATE '2020-09-20' );

END TRANSACTION;
```

Output:

```
 emp_id | project_name | dept_id | start_date |  end_date
--------+--------------+---------+------------+------------
     10 | First Phase  |    1000 | 2010-01-10 | 2010-03-20
     10 | First Phase  |    2000 | 2010-03-20 | 2010-07-15
     10 | Second Phase |    2000 | 2010-06-15 | 2010-08-18
     20 | First Phase  |    2000 | 2010-03-10 | 2010-07-20
     20 | Second Phase |    1000 | 2020-05-10 | 2020-09-20
(5 rows)
```

To rewrite Teradata’s **NORMALIZE** clause, you can use the [LAG window function](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_LAG.html) in Amazon Redshift. This function returns the values for a row at a given offset above (before) the current row in the partition.

You can use the **LAG** function to identify each row that begins a new period by determining if a period meets or overlaps with the previous period (0 if yes and 1 if no). When this flag is cumulatively summed up, it provides a group identifier that can be used in the outer **Group By** clause to arrive at the desired result in Amazon Redshift.

Here’s a sample Amazon Redshift SQL statement that uses **LAG()**:

```
SELECT emp_id, start_date, end_date,
            (CASE WHEN start_date <= LAG(end_date) OVER (PARTITION BY emp_id ORDER BY start_date, end_date) THEN 0 ELSE 1 END) AS GroupStartFlag
FROM systest.project
ORDER BY 1,2;
```

Output:

```
 emp_id | start_date |  end_date  | groupstartflag
--------+------------+------------+----------------
     10 | 2010-01-10 | 2010-03-20 |              1
     10 | 2010-03-20 | 2010-07-15 |              0
     10 | 2010-06-15 | 2010-08-18 |              0
     20 | 2010-03-10 | 2010-07-20 |              1
     20 | 2020-05-10 | 2020-09-20 |              1
(5 rows)
```

The following Amazon Redshift SQL statement normalizes only on the `emp_id` column:

```
SELECT T2.emp_id, MIN(T2.start_date) as new_start_date, MAX(T2.end_date) as new_end_date
FROM
( SELECT T1.*, SUM(GroupStartFlag) OVER (PARTITION BY emp_id ORDER BY start_date ROWS UNBOUNDED PRECEDING) As GroupID
FROM ( SELECT emp_id, start_date, end_date,
            (CASE WHEN start_date <= LAG(end_date) OVER (PARTITION BY emp_id ORDER BY start_date, end_date) THEN 0 ELSE 1 END) AS GroupStartFlag
FROM systest.project ) T1
) T2
GROUP BY T2.emp_id, T2.GroupID
ORDER BY 1,2;
```

Output:

```
 emp_id | new_start_date | new_end_date
--------+----------------+------------------------------------
     10 | 2010-01-10     | 2010-08-18
     20 | 2010-03-10     | 2010-07-20
     20 | 2020-05-10     | 2020-09-20
(3 rows)
```

** **

The following Amazon Redshift SQL statement normalizes on both the `project_name` and `dept_id` columns:

```
SELECT T2.project_name, T2.dept_id, MIN(T2.start_date) as new_start_date, MAX(T2.end_date) as new_end_date
FROM
( SELECT T1.*, SUM(GroupStartFlag) OVER (PARTITION BY project_name, dept_id ORDER BY start_date ROWS UNBOUNDED PRECEDING) As GroupID
FROM ( SELECT project_name, dept_id, start_date, end_date,
            (CASE WHEN start_date <= LAG(end_date) OVER (PARTITION BY project_name, dept_id ORDER BY start_date, end_date) THEN 0 ELSE 1 END) AS GroupStartFlag
FROM systest.project ) T1
) T2
GROUP BY T2.project_name, T2.dept_id, T2.GroupID
ORDER BY 1,2,3;
```

Output:

```
 project_name | dept_id | new_start_date | new_end_date
--------------+---------+----------------+--------------
 First Phase  |    1000 | 2010-01-10     | 2010-03-20
 First Phase  |    2000 | 2010-03-10     | 2010-07-20
 Second Phase |    1000 | 2020-05-10     | 2020-09-20
 Second Phase |    2000 | 2010-06-15     | 2010-08-18
(4 rows)
```

## Epics
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-epics"></a>

### Convert NORMALIZE to Amazon Redshift SQL
<a name="convert-normalize-to-amazon-redshift-sql"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create your Teradata SQL code. | Use the NORMALIZE phrase according to your needs. | SQL developer |
| Convert the code to Amazon Redshift SQL. | To convert your code, follow the guidelines in the "Tools" section of this pattern. | SQL developer |
| Run the code in Amazon Redshift. | Create your table, load data into the table, and run your code in Amazon Redshift. | SQL developer |

## Related resources
<a name="convert-the-teradata-normalize-temporal-feature-to-amazon-redshift-sql-resources"></a>

**References**
+ [Teradata NORMALIZE temporal feature](https://docs.teradata.com/reader/2_MC9vCtAJRlKle2Rpb0mA/MIGI5UMEwgERC3Un7tEZ6g) (Teradata documentation)
+ [LAG window function](https://docs.aws.amazon.com/redshift/latest/dg/r_WF_LAG.html) (Amazon Redshift documentation)
+ [Migrate to Amazon Redshift](https://aws.amazon.com/redshift/data-warehouse-migration/) (AWS website)
+ [Migrate a Teradata database to Amazon Redshift using AWS SCT data extraction agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-teradata-database-to-amazon-redshift-using-aws-sct-data-extraction-agents.html) (AWS Prescriptive Guidance)
+ [Convert the Teradata RESET WHEN feature to Amazon Redshift SQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-the-teradata-reset-when-feature-to-amazon-redshift-sql.html) (AWS Prescriptive Guidance)

**Tools**
+ [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/)

**Partners**
+ [AWS Migration Competency Partners](https://aws.amazon.com/migration/partner-solutions/#delivery)

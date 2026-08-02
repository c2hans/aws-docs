---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-sql-capabilities.html
---

# SQL capabilities of AWS Clean Rooms Differential Privacy
<a name="dp-sql-capabilities"></a>

AWS Clean Rooms Differential Privacy uses a general-purpose query structure to support complex SQL queries. Custom analysis templates are validated against this structure to ensure that they can run on tables protected by differential privacy. The following table indicates which functions are supported. See [Query structure and syntax](analysis-rules-custom.md#dp-query-structure-syntax) for more information.

| Category | SQL constructs supported in the Spark analytics engine | Common table expressions (CTEs) | Final SELECT clause |
| --- |--- |--- |--- |
| Aggregate functions |    ANY\_VALUE function   APPROXIMATE PERCENTILE\_DISC function   AVG function   COUNT and COUNT DISTINCT functions    MAX function   MEDIAN function   MIN function   PERCENTILE\_CONT function   STDDEV\_SAMP and STDDEV\_POP functions   SUM and SUM DISTINCT functions   VAR\_SAMP and VAR\_POP functions    | Supported with the condition that CTEs using differential privacy protected tables must result in data with user-level records. You should write the SELECT expression in those CTEs using `SELECT userIdentifierColumn...' format. | Supported aggregations: AVG, COUNT, COUNT DISTINCT, STDDEV, and SUM. |
| CTEs | WITH clause, WITH clause subquery | Supported with the condition that CTEs using differential privacy protected tables must result in data with user-level records. You should write the SELECT expression in those CTEs using `SELECT userIdentifierColumn...' format. | N/A |
| Subqueries |    SELECT   HAVING   JOIN   JOIN condition   FROM   WHERE    | You can have any subquery that doesn't reference differential privacy relations in these constructs. You can have any subquery that references differential privacy relations in a FROM and JOIN clause only. |
| Join clauses |    INNER JOIN   LEFT JOIN    LEFT SEMI JOIN   LEFT ANTI JOIN    RIGHT JOIN   FULL JOIN   [JOIN] OR operator   CROSS JOIN    | Supported with the condition that only JOIN functions that are equi-joins on user identifier columns are supported and are mandatory when querying two or more tables with differential privacy turned on. Ensure that the mandatory equi-join conditions are correct. Confirm that the table owner has configured the same user identifier column in all tables so that the definition of a user remains consistent across tables.<br />CROSS JOIN functions are not supported when combining two or more relations with differential privacy turned on. |
| Set operators | UNION, UNION ALL, INTERSECT, EXCEPT \| MINUS (these are synonyms) | UNION, UNION ALL, INTERSECT, EXCEPT \| MINUS (these are synonyms) | Not supported |
| Window functions | Aggregate functions  AVG window function   COUNT window function   CUME\_DIST window function   DENSE\_RANK window function   FIRST\_VALUE window function   LAG window function   LAST\_VALUE window function   LEAD window function   MAX window functions   MEDIAN window functions   MIN window functions   NTH\_VALUE window function    STDDEV\_SAMP and STDDEV\_POP window function (STDDEV\_SAMP and STDDEV are synonyms)   SUM window functions   VAR\_SAMP and VAR\_POP window functions (VAR\_SAMP and VARIANCE are synonyms)  <br />Ranking functions  DENSE\_RANK window function   NTILE window function   PERCENT\_RANK window function   RANK window function   ROW\_NUMBER window function   | All are supported with the condition that the user identifier column in the window function's partition clause is required when you query a relation with differential privacy turned on. | Not supported |
| Conditional expressions |    CASE condition expression   COALESCE expression   GREATEST and LEAST functions   NVL and COALESCE functions   NVL2 function   NULLIF function    | All are supported | All are supported |
| Conditions |    Comparison condition   Logical conditions   Pattern-matching conditions   BETWEEN range conditions   Null condition    | EXISTS and IN can't be used because they require subqueries. All others are supported. | All are supported |
| Date-time functions |    Date and time functions in transactions   Concatenation operator   ADD\_MONTHS functions   CONVERT\_TIMEZONE function   CURRENT\_DATE function   DATEADD function   DATEDIFF function   DATE\_PART functions   DATE\_TRUNC function   EXTRACT function    TO\_TIMESTAMP function   Date parts for date or timestamp functions    | All are supported | All are supported |
| String functions |    \|\| (concatenation) operator   BTRIM function   CHAR\_LENGTH function   CHARACTER\_LENGTH function    CONCAT function   LEFT and RIGHT functions   LEN function   LENGTH function   LOWER function   LPAD and RPAD functions   LTRIM function   POSITION functions   REGEXP\_COUNT function   REGEXP\_INSTR function   REGEXP\_REPLACE function   REGEXP\_SUBSTR function   REPEAT function   REPLACE function    REVERSE function   RTRIM function    SPLIT\_PART function    SUBSTRING function    TRANSLATE function   TRIM functions   UPPER function    | All are supported | All are supported |
| Data type formatting functions |    CAST function   TO\_CHAR   TO\_DATE function   TO\_NUMBER   Datetime format strings   Numeric format strings    | All are supported | All are supported |
| Hash functions |     AES\_ENCRYPT   AES\_DECRYPT   ENCODE   DECODE    MD5 function    SHA1 function   SHA2 function     XX\_HASH64     | All are supported | All are supported |
| Mathematical operator symbols | \+, -, \*, /, %, and @ | All are supported | All are supported |
| Math functions |    ABS function   ACOS function   ASIN function   ATAN function   ATAN2 function   CBRT function   CEILING (or CEIL) function   COS function   COT function   DEGREES function    LTRIM function    EXP function   FLOOR function   LN function   LOG function   MOD function   PI function   POWER function   RADIANS function   RANDOM function   ROUND function   SIGN function   SIN function   SQRT functions   TRUNC function    | All are supported | All are supported |
| VARBYTE functions |      UNHEX,   UNBASE64   HEX    HLL\_SKETCH\_AGG,    HLL\_SKETCH\_ESTIMATE   HLL\_UNION   HLL\_UNION\_AGG     | All are supported | All are supported |
| JSON |      TO\_JSON   GET\_JSON\_OBJECT     | All are supported | All are supported |
| Array functions |      ARRAY\_CONTAINS   ARRAY\_DISTINCT   ARRAY\_EXCEPT   ARRAY\_INTERSECT   ARRAY\_JOIN   ARRAY\_REMOVE   ARRAY\_SORT   ARRAY\_UNION     | Not supported | Not supported |
| Extended GROUP BY | GROUPING SETS, ROLLUP, CUBE | Not supported | Not supported |
| Sort operation | ORDER BY | Supported with the condition that an ORDER BY clause is only supported in a window function's partition clause when querying tables with differential privacy turned on. | Supported |
| Row limits | LIMIT, OFFSET | Not supported in CTEs using differential privacy protected tables | All are supported |
| Table and column aliasing |   | Supported | Supported |
| Math functions on aggregate functions |   | Supported | Supported |
| Scalar functions within aggregate functions |   | Supported | Supported |

## Common alternatives for unsupported SQL constructs
<a name="common-alternatives"></a>

| Category | SQL construct | Alternative |
| --- |--- |--- |
| Window functions |    LISTAGG   PERCENTILE\_CONT   PERCENTILE\_DISC    | You can use the equivalent aggregate function with GROUP BY. |
| Mathematical operator symbols |    $column \|\|/ 2   $column \|/ 2   $column ^ 2    |    CBRT   SQRT   POWER($column, 2)    |
| Scalar functions |    SYSDATE   $column::integer   convert(type, $column)    |    CURRENT\_DATE   CAST $column AS integer   CAST $column AS type    |
| Literals | INTERVAL ‘1 SECOND' | INTERVAL '1' SECOND |
| Row limiting | TOP n | LIMIT n |
| Join |    USING   NATURAL    | ON clause should explicitly contain a join criterion. |

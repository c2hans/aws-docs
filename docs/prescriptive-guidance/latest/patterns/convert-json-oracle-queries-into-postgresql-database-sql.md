---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-json-oracle-queries-into-postgresql-database-sql.html
---

# Convert JSON Oracle queries into PostgreSQL database SQL
<a name="convert-json-oracle-queries-into-postgresql-database-sql"></a>

*Pinesh Singal and Lokesh Gurram, Amazon Web Services*

## Summary
<a name="convert-json-oracle-queries-into-postgresql-database-sql-summary"></a>

This migration process for moving from on-premises to the Amazon Web Services (AWS) Cloud uses the AWS Schema Conversion Tool (AWS SCT) to convert the code from an Oracle database into a PostgreSQL database. Most of the code is automatically converted by AWS SCT. However, JSON-related Oracle queries are not automatically converted.

Starting from Oracle 12.2 version, Oracle Database supports various JSON functions that help in converting JSON-based data into ROW-based data. However, AWS SCT doesn’t automatically convert JSON-based data into language that is supported by PostgreSQL.

This migration pattern primarily focuses on manually converting the JSON-related Oracle queries with functions such as `JSON_OBJECT`, `JSON_ARRAYAGG`, and `JSON_TABLE` from an Oracle database to a PostgreSQL database.

## Prerequisites and limitations
<a name="convert-json-oracle-queries-into-postgresql-database-sql-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An on-premises Oracle database instance (up and running)
+ An Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition database instance (up and running)

**Limitations **
+ JSON-related queries require a fixed `KEY` and `VALUE` format. Not using that format returns the wrong result.
+ If any change in JSON structure adds new `KEY` and `VALUE` pairs in the result section, the corresponding procedure or function must be changed in the SQL query.
+ Some JSON-related functions are supported in earlier versions of Oracle and PostgreSQL but with fewer capabilities.

**Product versions**
+ Oracle Database version 12.2 and later
+ Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible version 9.5 and later
+ AWS SCT latest version (tested using version 1.0.664)

## Architecture
<a name="convert-json-oracle-queries-into-postgresql-database-sql-architecture"></a>

**Source technology stack  **
+ An Oracle database instance with version 19c

**Target technology stack  **
+ An Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database instance with version 13

**Target architecture **

![Description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5e2c3b07-9ef5-417f-b049-bcea58f2c3ec/images/2ff8b00b-8849-4ef1-9be1-579f7b51be10.png)

1. Use AWS SCT with the JSON function code to convert the source code from Oracle to PostgreSQL.

1. The conversion produces PostgreSQL-supported migrated .sql files.

1. Manually convert the non-converted Oracle JSON function codes to PostgreSQL JSON function codes.

1. Run the .sql files on the target Aurora PostgreSQL-Compatible DB instance.

## Tools
<a name="convert-json-oracle-queries-into-postgresql-database-sql-tools"></a>

**AWS services**
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

**Other services**
+ [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments.
+ pgAdmin or DBeaver. [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects. [DBeaver](https://dbeaver.io/) is a universal database tool.

## Best practices
<a name="convert-json-oracle-queries-into-postgresql-database-sql-best-practices"></a>

Oracle query has type `CAST` as the default when using the `JSON_TABLE` function. A best practice is to use `CAST` in PostgreSQL too, using double greater-than characters (`>>`).

For more information, see *Postgres\_SQL\_Read\_JSON* in the *Additional information* section.

## Epics
<a name="convert-json-oracle-queries-into-postgresql-database-sql-epics"></a>

### Generate the JSON data in the Oracle and PostgreSQL databases
<a name="generate-the-json-data-in-the-oracle-and-postgresql-databases"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Store the JSON data in the Oracle database. | Create a table in the Oracle database, and store the JSON data in the `CLOB` column.  Use the *Oracle\_Table\_Creation\_Insert\_Script* that’s in the *Additional information* section. | Migration engineer |
| Store the JSON data in the PostgreSQL database. | Create a table in the PostgreSQL database, and store the JSON data in the `TEXT` column. Use the *Postgres\_Table\_Creation\_Insert\_Script* that’s in the *Additional information* section. | Migration engineer |

### Convert the JSON into ROW format
<a name="convert-the-json-into-row-format"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Convert the JSON data on the Oracle database. | Write an Oracle SQL query to read the JSON data into ROW format. For more details and example syntax, see *Oracle\_SQL\_Read\_JSON* in the *Additional information* section. | Migration engineer |
| Convert the JSON data on the PostgreSQL database. | Write a PostgreSQL query to read the JSON data into ROW format. For more details and example syntax, see *Postgres\_SQL\_Read\_JSON* in the *Additional information* section.  | Migration engineer |

### Manually convert the JSON data using the SQL query and report the output in JSON format
<a name="manually-convert-the-json-data-using-the-sql-query-and-report-the-output-in-json-format"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform aggregations and validation on the Oracle SQL query. | To manually convert the JSON data, perform a join, aggregation, and validation on the Oracle SQL query, and report the output in JSON format. Use the code under *Oracle\_SQL\_JSON\_Aggregation\_Join* in the *Additional information* section.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-json-oracle-queries-into-postgresql-database-sql.html) | Migration engineer |
| Perform aggregations and validation on the Postgres SQL query. | To manually convert the JSON data, perform a join, aggregation, and validation on the PostgreSQL query, and report the output in JSON format. Use the code under *Postgres\_SQL\_JSON\_Aggregation\_Join* in the *Additional information* section.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-json-oracle-queries-into-postgresql-database-sql.html) | Migration engineer |

### Convert the Oracle procedure into a PostgreSQL function that contains JSON queries
<a name="convert-the-oracle-procedure-into-a-postgresql-function-that-contains-json-queries"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Convert the JSON queries in the Oracle procedure into rows. | For the example Oracle procedure, use the previous Oracle query and the code under  *Oracle\_procedure\_with\_JSON\_Query* in the *Additional information* section. | Migration engineer |
| Convert the PostgreSQL functions that have JSON queries into row-based data. | For the example PostgreSQL functions, use the previous PostgreSQL query and the code that’s under *Postgres\_function\_with\_JSON\_Query* in the *Additional information* section. | Migration engineer |

## Related resources
<a name="convert-json-oracle-queries-into-postgresql-database-sql-resources"></a>
+ [Oracle JSON functions](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/adjsn/generation.html)
+ [PostgreSQL JSON functions](https://www.postgresql.org/docs/13/functions-json.html)
+ [Oracle JSON Functions Examples](https://oracle-base.com/articles/12c/sql-json-functions-12cr2)
+ [PostgreSQL JSON function examples](https://dba.stackexchange.com/questions/69655/select-columns-inside-json-agg)
+ [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

## Additional information
<a name="convert-json-oracle-queries-into-postgresql-database-sql-additional"></a>

To convert JSON code from the Oracle database to PostgreSQL database, use the following scripts, in order.

**1. Oracle\_Table\_Creation\_Insert\_Script**

```
create table aws_test_table(id number,created_on date default sysdate,modified_on date,json_doc clob);

REM INSERTING into EXPORT_TABLE
SET DEFINE OFF;
Insert into aws_test_table (ID,CREATED_ON,MODIFIED_ON,json_doc)
values (1,to_date('02-AUG-2022 12:30:14','DD-MON-YYYY HH24:MI:SS'),to_date('02-AUG-2022 12:30:14','DD-MON-YYYY HH24:MI:SS'),TO_CLOB(q'[{
  "metadata" : {
    "upperLastNameFirstName" : "ABC XYZ",
    "upperEmailAddress" : "abc@gmail.com",
    "profileType" : "P"
  },
  "data" : {
    "onlineContactId" : "032323323",
    "displayName" : "Abc, Xyz",
    "firstName" : "Xyz",
    "lastName" : "Abc",
    "emailAddress" : "abc@gmail.com",
    "productRegistrationStatus" : "Not registered",
    "positionId" : "0100",
    "arrayPattern" : " -'",
    "a]')
|| TO_CLOB(q'[ccount" : {
      "companyId" : "SMGE",
      "businessUnitId" : 7,
      "accountNumber" : 42000,
      "parentAccountNumber" : 32000,
      "firstName" : "john",
      "lastName" : "doe",
      "street1" : "retOdertcaShr ",
      "city" : "new york",
      "postalcode" : "XY ABC",
      "country" : "United States"
    },
    "products" : [
      {
        "appUserGuid" : "i0acc4450000001823fbad478e2eab8a0",
        "id" : "0000000046",
]')
|| TO_CLOB(q'[        "name" : "ProView",
        "domain" : "EREADER",
        "registrationStatus" : false,
        "status" : "11"
      }
    ]
  }
}]'));
Insert into aws_test_table (ID,CREATED_ON,MODIFIED_ON,json_doc) values (2,to_date('02-AUG-2022 12:30:14','DD-MON-YYYY HH24:MI:SS'),to_date('02-AUG-2022 12:30:14','DD-MON-YYYY HH24:MI:SS'),TO_CLOB(q'[{
  "metadata" : {
    "upperLastNameFirstName" : "PQR XYZ",
    "upperEmailAddress" : "pqr@gmail.com",
    "profileType" : "P"
  },
  "data" : {
    "onlineContactId" : "54534343",
    "displayName" : "Xyz, pqr",
    "firstName" : "pqr",
    "lastName" : "Xyz",
    "emailAddress" : "pqr@gmail.com",
    "productRegistrationStatus" : "Not registered",
    "positionId" : "0090",
    "arrayPattern" : " -'",
    "account" : {
      "companyId" : "CARS",
      "busin]')
|| TO_CLOB(q'[essUnitId" : 6,
      "accountNumber" : 42001,
      "parentAccountNumber" : 32001,
      "firstName" : "terry",
      "lastName" : "whitlock",
      "street1" : "UO  123",
      "city" : "TOTORON",
      "region" : "NO",
      "postalcode" : "LKM 111",
      "country" : "Canada"
    },
    "products" : [
      {
        "appUserGuid" : "ia744d7790000016899f8cf3f417d6df6",
        "id" : "0000000014",
        "name" : "ProView eLooseleaf",
      ]')
|| TO_CLOB(q'[  "domain" : "EREADER",
        "registrationStatus" : false,
        "status" : "11"
      }
    ]
  }
}]'));

commit;
```

**2. Postgres\_Table\_Creation\_Insert\_Script**

```
create table aws_test_pg_table(id int,created_on date ,modified_on date,json_doc text);
insert into aws_test_pg_table(id,created_on,modified_on,json_doc)
values(1,now(),now(),'{
  "metadata" : {
    "upperLastNameFirstName" : "ABC XYZ",
    "upperEmailAddress" : "abc@gmail.com",
    "profileType" : "P"
  },
  "data" : {
    "onlineContactId" : "032323323",
    "displayName" : "Abc, Xyz",
    "firstName" : "Xyz",
    "lastName" : "Abc",
    "emailAddress" : "abc@gmail.com",
    "productRegistrationStatus" : "Not registered",
    "positionId" : "0100",
    "arrayPattern" : " -",
    "account" : {
      "companyId" : "SMGE",
      "businessUnitId" : 7,
      "accountNumber" : 42000,
      "parentAccountNumber" : 32000,
      "firstName" : "john",
      "lastName" : "doe",
      "street1" : "retOdertcaShr ",
      "city" : "new york",
      "postalcode" : "XY ABC",
      "country" : "United States"
    },
    "products" : [
      {
        "appUserGuid" : "i0acc4450000001823fbad478e2eab8a0",
        "id" : "0000000046",
        "name" : "ProView",
        "domain" : "EREADER",
        "registrationStatus" : false,
        "status" : "11"
      }
    ]
  }
}');

insert into aws_test_pg_table(id,created_on,modified_on,json_doc)
values(2,now(),now(),'{
  "metadata" : {
    "upperLastNameFirstName" : "PQR XYZ",
    "upperEmailAddress" : "pqr@gmail.com",
    "profileType" : "P"
  },
  "data" : {
    "onlineContactId" : "54534343",
    "displayName" : "Xyz, pqr",
    "firstName" : "pqr",
    "lastName" : "Xyz",
    "emailAddress" : "a*b**@h**.k**",
    "productRegistrationStatus" : "Not registered",
    "positionId" : "0090",
    "arrayPattern" : " -",
    "account" : {
      "companyId" : "CARS",
      "businessUnitId" : 6,
      "accountNumber" : 42001,
      "parentAccountNumber" : 32001,
      "firstName" : "terry",
      "lastName" : "whitlock",
      "street1" : "UO  123",
      "city" : "TOTORON",
      "region" : "NO",
      "postalcode" : "LKM 111",
      "country" : "Canada"
    },
    "products" : [
      {
        "appUserGuid" : "ia744d7790000016899f8cf3f417d6df6",
        "id" : "0000000014",
        "name" : "ProView eLooseleaf",
        "domain" : "EREADER",
        "registrationStatus" : false,
        "status" : "11"
      }
    ]
  }
}');
```

**3. Oracle\_SQL\_Read\_JSON**

The following code blocks show how to convert Oracle JSON data into row format.

*Example query and syntax*

```
SELECT   JSON_OBJECT(
 'accountCounts' VALUE JSON_ARRAYAGG(
            JSON_OBJECT(
                'businessUnitId' VALUE business_unit_id,
                        'parentAccountNumber' VALUE parent_account_number,
                        'accountNumber' VALUE account_number,
                        'totalOnlineContactsCount' VALUE online_contacts_count,
                        'countByPosition' VALUE
                    JSON_OBJECT(
                        'taxProfessionalCount' VALUE tax_count,
                        'attorneyCount' VALUE attorney_count,
                        'nonAttorneyCount' VALUE non_attorney_count,
                        'clerkCount' VALUE clerk_count
                               ) ) ) ) FROM
    (SELECT   tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number,
            SUM(1) online_contacts_count,
            SUM(CASE WHEN tab_data.position_id = '0095' THEN  1 ELSE 0 END) tax_count,
            SUM(CASE    WHEN tab_data.position_id = '0100' THEN 1 ELSE 0 END) attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0090' THEN 1 ELSE 0 END) non_attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0050' THEN 1 ELSE 0 END) clerk_count
        FROM aws_test_table scco,JSON_TABLE ( json_doc, '$' ERROR ON ERROR         COLUMNS (
          parent_account_number NUMBER PATH
           '$.data.account.parentAccountNumber',
            account_number NUMBER PATH '$.data.account.accountNumber',
            business_unit_id NUMBER PATH '$.data.account.businessUnitId',
            position_id VARCHAR2 ( 4 ) PATH '$.data.positionId'    )
            ) AS tab_data
            INNER JOIN JSON_TABLE ( '{
        "accounts": [{
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }, {
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }]
      }', '$.accounts[*]' ERROR ON ERROR
      COLUMNS (
      parent_account_number PATH '$.parentAccountNumber',
      account_number PATH '$.accountNumber',
      business_unit_id PATH '$.businessUnitId')
      ) static_data
      ON ( static_data.parent_account_number = tab_data.parent_account_number
           AND static_data.account_number = tab_data.account_number
           AND static_data.business_unit_id = tab_data.business_unit_id )
        GROUP BY
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number );
```

The JSON document stores the data as collections. Each collection can have `KEY` and `VALUE` pairs. Every `VALUE` can have nested `KEY` and `VALUE` pairs. The following table provides information about reading the specific `VALUE` from the JSON document.

|
|
| KEY | HIERARCHY or PATH to be used to get the VALUE | VALUE |
| --- |--- |--- |
| `profileType` | `metadata` -> `profileType` | "P" |
| `positionId` | `data` -> `positionId` | "0100" |
| `accountNumber` | `data` -> account -> `accountNumber` | 42000 |

In the previous table, the `KEY` `profileType` is a `VALUE` of the `metadata` `KEY`. The `KEY` `positionId` is a `VALUE` of the `data` `KEY`. The `KEY` `accountNumber` is a `VALUE` of the `account` `KEY`, and the `account` `KEY` is a `VALUE` of the `data` `KEY`.

*Example JSON document*

```
{
  "metadata" : {
    "upperLastNameFirstName" : "ABC XYZ",
    "upperEmailAddress" : "abc@gmail.com",
"profileType" : "P"
  },
  "data" : {
    "onlineContactId" : "032323323",
    "displayName" : "Abc, Xyz",
    "firstName" : "Xyz",
    "lastName" : "Abc",
    "emailAddress" : "abc@gmail.com",
    "productRegistrationStatus" : "Not registered",
"positionId" : "0100",
    "arrayPattern" : " -",
    "account" : {
      "companyId" : "SMGE",
      "businessUnitId" : 7,
"accountNumber" : 42000,
      "parentAccountNumber" : 32000,
      "firstName" : "john",
      "lastName" : "doe",
      "street1" : "retOdertcaShr ",
      "city" : "new york",
      "postalcode" : "XY ABC",
      "country" : "United States"
    },
    "products" : [
      {
        "appUserGuid" : "i0acc4450000001823fbad478e2eab8a0",
        "id" : "0000000046",
        "name" : "ProView",
        "domain" : "EREADER",
        "registrationStatus" : false,
        "status" : "11"
      }
    ]
  }
}
```

*SQL query that is used to get the selected fields from the JSON document*

```
select parent_account_number,account_number,business_unit_id,position_id from aws_test_table aws,JSON_TABLE ( json_doc, '$' ERROR ON ERROR
COLUMNS (
parent_account_number NUMBER PATH '$.data.account.parentAccountNumber',
account_number NUMBER PATH '$.data.account.accountNumber',
business_unit_id NUMBER PATH '$.data.account.businessUnitId',
position_id VARCHAR2 ( 4 ) PATH '$.data.positionId'
)) as sc
```

In the previous query, `JSON_TABLE` is a built-in function in Oracle that converts the JSON data into row format. The JSON\_TABLE function expects parameters in JSON format.

Every item in `COLUMNS` has a predefined `PATH`, and there an appropriate `VALUE` for a given `KEY` is returned in row format.

*Result from the previous query*

|
|
| PARENT\_ACCOUNT\_NUMBER | ACCOUNT\_NUMBER | BUSINESS\_UNIT\_ID | POSITION\_ID |
| --- |--- |--- |--- |
| 32000 | 42000 | 7 | 0100 |
| 32001 | 42001 | 6 | 0090 |

**4. Postgres\_SQL\_Read\_JSON**

** ***Example query and syntax*

```
select *
from (
select (json_doc::json->'data'->'account'->>'parentAccountNumber')::INTEGER as parentAccountNumber,
(json_doc::json->'data'->'account'->>'accountNumber')::INTEGER as accountNumber,
(json_doc::json->'data'->'account'->>'businessUnitId')::INTEGER as businessUnitId,
(json_doc::json->'data'->>'positionId')::VARCHAR as positionId
from aws_test_pg_table) d ;
```

In Oracle, `PATH` is used to identify the specific `KEY` and `VALUE`. However, PostgreSQL uses a `HIERARCHY` model for reading `KEY` and `VALUE` from JSON. The same JSON data mentioned under `Oracle_SQL_Read_JSON` is used in the following examples.

*SQL query with type CAST not allowed*

(If you force type `CAST`, the query fails with a syntax error.)

```
select *
from (
select (json_doc::json->'data'->'account'->'parentAccountNumber') as parentAccountNumber,
(json_doc::json->'data'->'account'->'accountNumber')as accountNumber,
(json_doc::json->'data'->'account'->'businessUnitId') as businessUnitId,
(json_doc::json->'data'->'positionId')as positionId
from aws_test_pg_table) d ;
```

Using a single greater-than operator (`>`) will return the `VALUE` defined for that `KEY`. For example, `KEY`: `positionId`, and `VALUE`: `"0100"`.

Type `CAST` is not allowed when you use the single greater-than operator (`>`).

*SQL query with type CAST allowed*

```
select *
from (
select (json_doc::json->'data'->'account'->>'parentAccountNumber')::INTEGER as parentAccountNumber,
(json_doc::json->'data'->'account'->>'accountNumber')::INTEGER as accountNumber,
(json_doc::json->'data'->'account'->>'businessUnitId')::INTEGER as businessUnitId,
(json_doc::json->'data'->>'positionId')::varchar as positionId
from aws_test_pg_table) d ;
```

To use type `CAST`, you must use the double greater-than operator. If you use the single greater-than operator, the query returns the `VALUE` defined (for example, `KEY`: `positionId`, and `VALUE`: `"0100"`). Using the double greater-than operator (`>>`) will return the actual value defined for that `KEY` (for example, `KEY`: `positionId`, and `VALUE`: `0100`, without double quotation marks).

In the preceding case, `parentAccountNumber` is type `CAST` to `INT`, `accountNumber` is type `CAST` to `INT`, `businessUnitId` is type `CAST` to `INT`, and `positionId` is type `CAST` to `VARCHAR`.

The following tables show query results that explain role of the single greater-than operator (`>`) and the double greater-than operator (`>>`).

In the first table table, the query uses the single greater-than operator (`>`). Each column is in JSON type and can’t be converted into another data type.

|
|
| parentAccountNumber | accountNumber | businessUnitId | positionId |
| --- |--- |--- |--- |
| 2003565430 | 2003564830 | 7 | "0100" |
| 2005284042 | 2005284042 | 6 | "0090" |
| 2000272719 | 2000272719 | 1 | "0100" |

In the second table, the query uses the double greater-than operator (`>>`). Each column supports type `CAST` based on the column value. For example, `INTEGER` in this context.

|
|
| parentAccountNumber | accountNumber | businessUnitId | positionId |
| --- |--- |--- |--- |
| 2003565430 | 2003564830 | 7 | 0100 |
| 2005284042 | 2005284042 | 6 | 0090 |
| 2000272719 | 2000272719 | 1 | 0100 |

**5. Oracle\_SQL\_JSON\_Aggregation\_Join**

*Example query*

```
SELECT
    JSON_OBJECT(
        'accountCounts' VALUE JSON_ARRAYAGG(
            JSON_OBJECT(
                'businessUnitId' VALUE business_unit_id,
                        'parentAccountNumber' VALUE parent_account_number,
                        'accountNumber' VALUE account_number,
                        'totalOnlineContactsCount' VALUE online_contacts_count,
                        'countByPosition' VALUE
                    JSON_OBJECT(
                        'taxProfessionalCount' VALUE tax_count,
                        'attorneyCount' VALUE attorney_count,
                        'nonAttorneyCount' VALUE non_attorney_count,
                        'clerkCount' VALUE clerk_count
                               ) ) ) )
FROM
    (SELECT
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number,
            SUM(1) online_contacts_count,
            SUM(CASE WHEN tab_data.position_id = '0095' THEN  1 ELSE 0 END) tax_count,
            SUM(CASE    WHEN tab_data.position_id = '0100' THEN 1 ELSE 0 END) attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0090' THEN 1 ELSE 0 END) non_attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0050' THEN 1 ELSE 0 END) clerk_count
        FROM aws_test_table scco,JSON_TABLE ( json_doc, '$' ERROR ON ERROR         COLUMNS (
          parent_account_number NUMBER PATH
           '$.data.account.parentAccountNumber',
            account_number NUMBER PATH '$.data.account.accountNumber',
            business_unit_id NUMBER PATH '$.data.account.businessUnitId',
            position_id VARCHAR2 ( 4 ) PATH '$.data.positionId'    )
            ) AS tab_data
            INNER JOIN JSON_TABLE ( '{
        "accounts": [{
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }, {
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }]
      }', '$.accounts[*]' ERROR ON ERROR
      COLUMNS (
      parent_account_number PATH '$.parentAccountNumber',
      account_number PATH '$.accountNumber',
      business_unit_id PATH '$.businessUnitId')
      ) static_data
      ON ( static_data.parent_account_number = tab_data.parent_account_number
           AND static_data.account_number = tab_data.account_number
           AND static_data.business_unit_id = tab_data.business_unit_id )
        GROUP BY
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number
    );
```

To convert the row-level data into JSON format, Oracle has built-in functions such as `JSON_OBJECT`, `JSON_ARRAY`, `JSON_OBJECTAGG`, and `JSON_ARRAYAGG`.
+ `JSON_OBJECT` accepts two parameters: `KEY` and `VALUE`. The  `KEY` parameter should be hardcoded or static in nature. The `VALUE` parameter is derived from table output.
+ `JSON_ARRAYAGG` accepts `JSON_OBJECT` as a parameter. This helps in grouping the set of `JSON_OBJECT` elements as a list. For example, if you have a `JSON_OBJECT` element that has multiple records (multiple `KEY` and `VALUE` pairs in the dataset), `JSON_ARRAYAGG` appends the dataset and creates a list. According to the Data Structure language, `LIST` is group of elements. In this context, `LIST` is a group of `JSON_OBJECT` elements.

The following example shows one `JSON_OBJECT` element.

```
{
   "taxProfessionalCount": 0,
   "attorneyCount": 0,
   "nonAttorneyCount": 1,
   "clerkCount": 0
}
```

This next example shows two `JSON_OBJECT` elements, with `LIST` indicated by square braces (`[ ]`).

```
[
    {
        "taxProfessionalCount": 0,
        "attorneyCount": 0,
        "nonAttorneyCount": 1,
        "clerkCount": 0
      }
,
    {
        "taxProfessionalCount": 2,
        "attorneyCount": 1,
        "nonAttorneyCount": 3,
        "clerkCount":4
      }
]
```

*Example SQL query*

```
SELECT
    JSON_OBJECT(
        'accountCounts' VALUE JSON_ARRAYAGG(
            JSON_OBJECT(
                'businessUnitId' VALUE business_unit_id,
                        'parentAccountNumber' VALUE parent_account_number,
                        'accountNumber' VALUE account_number,
                        'totalOnlineContactsCount' VALUE online_contacts_count,
                        'countByPosition' VALUE
                    JSON_OBJECT(
                        'taxProfessionalCount' VALUE tax_count,
                        'attorneyCount' VALUE attorney_count,
                        'nonAttorneyCount' VALUE non_attorney_count,
                        'clerkCount' VALUE clerk_count
                               )
                        )
                                           )
              )
FROM
    (SELECT
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number,
            SUM(1) online_contacts_count,
            SUM(CASE WHEN tab_data.position_id = '0095' THEN  1 ELSE   0 END
            )      tax_count,
            SUM(CASE    WHEN tab_data.position_id = '0100' THEN        1    ELSE        0 END
            )      attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0090' THEN        1    ELSE        0 END
            )      non_attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0050' THEN        1    ELSE        0 END
            )      clerk_count
        FROM
            aws_test_table scco,  JSON_TABLE ( json_doc, '$' ERROR ON ERROR
            COLUMNS (
            parent_account_number NUMBER PATH '$.data.account.parentAccountNumber',
            account_number NUMBER PATH '$.data.account.accountNumber',
            business_unit_id NUMBER PATH '$.data.account.businessUnitId',
            position_id VARCHAR2 ( 4 ) PATH '$.data.positionId'    )
            ) AS tab_data
            INNER JOIN JSON_TABLE ( '{
        "accounts": [{
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }, {
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }]
      }', '$.accounts[*]' ERROR ON ERROR
      COLUMNS (
      parent_account_number PATH '$.parentAccountNumber',
      account_number PATH '$.accountNumber',
      business_unit_id PATH '$.businessUnitId')
      ) static_data ON ( static_data.parent_account_number = tab_data.parent_account_number
                         AND static_data.account_number = tab_data.account_number
                         AND static_data.business_unit_id = tab_data.business_unit_id )
        GROUP BY
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number
    );
```

*Example output from the previous SQL query*

```
{
  "accountCounts": [
    {
      "businessUnitId": 6,
      "parentAccountNumber": 32001,
      "accountNumber": 42001,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 0,
        "nonAttorneyCount": 1,
        "clerkCount": 0
      }
    },
    {
      "businessUnitId": 7,
      "parentAccountNumber": 32000,
      "accountNumber": 42000,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 1,
        "nonAttorneyCount": 0,
        "clerkCount": 0
      }
    }
  ]
}
```

**6.  Postgres\_SQL\_JSON\_Aggregation\_Join**

The PostgreSQL built-in functions `JSON_BUILD_OBJECT` and `JSON_AGG` convert the ROW-level data into JSON format.  PostgreSQL `JSON_BUILD_OBJECT` and `JSON_AGG` are equivalent to Oracle `JSON_OBJECT` and `JSON_ARRAYAGG`.

*Example query*

```
select
JSON_BUILD_OBJECT ('accountCounts',
    JSON_AGG(
        JSON_BUILD_OBJECT ('businessUnitId',businessUnitId
        ,'parentAccountNumber',parentAccountNumber
        ,'accountNumber',accountNumber
        ,'totalOnlineContactsCount',online_contacts_count,
        'countByPosition',
            JSON_BUILD_OBJECT (
            'taxProfessionalCount',tax_professional_count
            ,'attorneyCount',attorney_count
            ,'nonAttorneyCount',non_attorney_count
            ,'clerkCount',clerk_count
            )
        )
    )
)
from (
with tab as (select * from (
select (json_doc::json->'data'->'account'->>'parentAccountNumber')::INTEGER as parentAccountNumber,
(json_doc::json->'data'->'account'->>'accountNumber')::INTEGER as accountNumber,
(json_doc::json->'data'->'account'->>'businessUnitId')::INTEGER as businessUnitId,
(json_doc::json->'data'->>'positionId')::varchar as positionId
from aws_test_pg_table) a ) ,
tab1 as ( select
(json_array_elements(b.jc -> 'accounts') ->> 'accountNumber')::integer accountNumber,
(json_array_elements(b.jc -> 'accounts') ->> 'businessUnitId')::integer businessUnitId,
(json_array_elements(b.jc -> 'accounts') ->> 'parentAccountNumber')::integer parentAccountNumber
from (
select '{
        "accounts": [{
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }, {
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }]
      }'::json as jc) b)
select
tab.businessUnitId::text,
tab.parentAccountNumber::text,
tab.accountNumber::text,
SUM(1) online_contacts_count,
SUM(CASE WHEN tab.positionId::text = '0095' THEN 1 ELSE 0  END)      tax_professional_count,
SUM(CASE WHEN tab.positionId::text = '0100' THEN 1 ELSE 0  END)      attorney_count,
SUM(CASE  WHEN tab.positionId::text = '0090' THEN      1  ELSE      0 END)      non_attorney_count,
SUM(CASE  WHEN tab.positionId::text = '0050' THEN      1  ELSE      0 END)      clerk_count
from tab1,tab
where tab.parentAccountNumber::INTEGER=tab1.parentAccountNumber::INTEGER
and tab.accountNumber::INTEGER=tab1.accountNumber::INTEGER
and tab.businessUnitId::INTEGER=tab1.businessUnitId::INTEGER
GROUP BY      tab.businessUnitId::text,
            tab.parentAccountNumber::text,
            tab.accountNumber::text) a;
```

*Example output from the preceding query*

Output from Oracle and PostgreSQL is exactly the same.

```
{
  "accountCounts": [
    {
      "businessUnitId": 6,
      "parentAccountNumber": 32001,
      "accountNumber": 42001,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 0,
        "nonAttorneyCount": 1,
        "clerkCount": 0
      }
    },
    {
      "businessUnitId": 7,
      "parentAccountNumber": 32000,
      "accountNumber": 42000,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 1,
        "nonAttorneyCount": 0,
        "clerkCount": 0
      }
    }
  ]
}
```

**7.Oracle\_procedure\_with\_JSON\_Query**

This code converts the Oracle procedure into a PostgreSQL function that has JSON SQL queries. It shows how the query transposes JSON into rows and the reverse.

```
CREATE OR REPLACE PROCEDURE p_json_test(p_in_accounts_json IN varchar2,   p_out_accunts_json  OUT varchar2)
IS
BEGIN
/*
p_in_accounts_json paramter should have following format:
       {
        "accounts": [{
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }, {
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }]
      }
*/
SELECT
    JSON_OBJECT(
        'accountCounts' VALUE JSON_ARRAYAGG(
            JSON_OBJECT(
                'businessUnitId' VALUE business_unit_id,
                        'parentAccountNumber' VALUE parent_account_number,
                        'accountNumber' VALUE account_number,
                        'totalOnlineContactsCount' VALUE online_contacts_count,
                        'countByPosition' VALUE
                    JSON_OBJECT(
                        'taxProfessionalCount' VALUE tax_count,
                        'attorneyCount' VALUE attorney_count,
                        'nonAttorneyCount' VALUE non_attorney_count,
                        'clerkCount' VALUE clerk_count
                               ) ) ) )
into p_out_accunts_json
FROM
    (SELECT
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number,
            SUM(1) online_contacts_count,
            SUM(CASE WHEN tab_data.position_id = '0095' THEN  1 ELSE 0 END) tax_count,
            SUM(CASE    WHEN tab_data.position_id = '0100' THEN 1 ELSE 0 END) attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0090' THEN 1 ELSE 0 END) non_attorney_count,
            SUM(CASE    WHEN tab_data.position_id = '0050' THEN 1 ELSE 0 END) clerk_count
        FROM aws_test_table scco,JSON_TABLE ( json_doc, '$' ERROR ON ERROR
            COLUMNS (
            parent_account_number NUMBER PATH '$.data.account.parentAccountNumber',
            account_number NUMBER PATH '$.data.account.accountNumber',
            business_unit_id NUMBER PATH '$.data.account.businessUnitId',
            position_id VARCHAR2 ( 4 ) PATH '$.data.positionId'    )
            ) AS tab_data
            INNER JOIN JSON_TABLE ( p_in_accounts_json, '$.accounts[*]' ERROR ON ERROR
      COLUMNS (
      parent_account_number PATH '$.parentAccountNumber',
      account_number PATH '$.accountNumber',
      business_unit_id PATH '$.businessUnitId')
      ) static_data
      ON ( static_data.parent_account_number = tab_data.parent_account_number
           AND static_data.account_number = tab_data.account_number
           AND static_data.business_unit_id = tab_data.business_unit_id )
        GROUP BY
            tab_data.business_unit_id,
            tab_data.parent_account_number,
            tab_data.account_number
    );
EXCEPTION
WHEN OTHERS THEN
   raise_application_error(-20001,'Error while running the JSON query');
END;
/
```

*Running the procedure*

The following code block explains how you can run the previously created Oracle procedure with example JSON input to the procedure. It also gives you the result or output from this procedure.

```
set serveroutput on;
declare
v_out varchar2(30000);
v_in varchar2(30000):= '{
        "accounts": [{
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }, {
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }]
      }';
begin
  p_json_test(v_in,v_out);
  dbms_output.put_line(v_out);
end;
/
```

*Procedure output*

```
{
  "accountCounts": [
    {
      "businessUnitId": 6,
      "parentAccountNumber": 32001,
      "accountNumber": 42001,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 0,
        "nonAttorneyCount": 1,
        "clerkCount": 0
      }
    },
    {
      "businessUnitId": 7,
      "parentAccountNumber": 32000,
      "accountNumber": 42000,
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 1,
        "nonAttorneyCount": 0,
        "clerkCount": 0
      }
    }
  ]
}
```

**8.Postgres\_function\_with\_JSON\_Query**

*Example function*

```
CREATE OR REPLACE  FUNCTION f_pg_json_test(p_in_accounts_json  text)
RETURNS text
LANGUAGE plpgsql
AS
$$
DECLARE
 v_out_accunts_json   text;
BEGIN
SELECT
JSON_BUILD_OBJECT ('accountCounts',
    JSON_AGG(
        JSON_BUILD_OBJECT ('businessUnitId',businessUnitId
        ,'parentAccountNumber',parentAccountNumber
        ,'accountNumber',accountNumber
        ,'totalOnlineContactsCount',online_contacts_count,
        'countByPosition',
            JSON_BUILD_OBJECT (
            'taxProfessionalCount',tax_professional_count
            ,'attorneyCount',attorney_count
            ,'nonAttorneyCount',non_attorney_count
            ,'clerkCount',clerk_count
            ))))
INTO v_out_accunts_json
FROM (
WITH tab AS (SELECT * FROM (
SELECT (json_doc::json->'data'->'account'->>'parentAccountNumber')::INTEGER AS parentAccountNumber,
(json_doc::json->'data'->'account'->>'accountNumber')::INTEGER AS accountNumber,
(json_doc::json->'data'->'account'->>'businessUnitId')::INTEGER AS businessUnitId,
(json_doc::json->'data'->>'positionId')::varchar AS positionId
FROM aws_test_pg_table) a ) ,
tab1 AS ( SELECT
(json_array_elements(b.jc -> 'accounts') ->> 'accountNumber')::integer accountNumber,
(json_array_elements(b.jc -> 'accounts') ->> 'businessUnitId')::integer businessUnitId,
(json_array_elements(b.jc -> 'accounts') ->> 'parentAccountNumber')::integer parentAccountNumber
FROM (
SELECT p_in_accounts_json::json AS jc) b)
SELECT
tab.businessUnitId::text,
tab.parentAccountNumber::text,
tab.accountNumber::text,
SUM(1) online_contacts_count,
SUM(CASE WHEN tab.positionId::text = '0095' THEN 1 ELSE 0  END)      tax_professional_count,
SUM(CASE WHEN tab.positionId::text = '0100' THEN 1 ELSE 0  END)      attorney_count,
SUM(CASE  WHEN tab.positionId::text = '0090' THEN      1  ELSE      0 END)      non_attorney_count,
SUM(CASE  WHEN tab.positionId::text = '0050' THEN      1  ELSE      0 END)      clerk_count
FROM tab1,tab
WHERE tab.parentAccountNumber::INTEGER=tab1.parentAccountNumber::INTEGER
AND tab.accountNumber::INTEGER=tab1.accountNumber::INTEGER
AND tab.businessUnitId::INTEGER=tab1.businessUnitId::INTEGER
GROUP BY      tab.businessUnitId::text,
            tab.parentAccountNumber::text,
            tab.accountNumber::text) a;
RETURN v_out_accunts_json;
END;
$$;
```

*Running the function*

```
select    f_pg_json_test('{
        "accounts": [{
          "accountNumber": 42001,
          "parentAccountNumber": 32001,
          "businessUnitId": 6
        }, {
          "accountNumber": 42000,
          "parentAccountNumber": 32000,
          "businessUnitId": 7
        }]
      }')   ;
```

*Function output *

The following output is similar to the Oracle procedure output. The difference is that this output is in Text format.

```
{
  "accountCounts": [
    {
      "businessUnitId": "6",
      "parentAccountNumber": "32001",
      "accountNumber": "42001",
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 0,
        "nonAttorneyCount": 1,
        "clerkCount": 0
      }
    },
    {
      "businessUnitId": "7",
      "parentAccountNumber": "32000",
      "accountNumber": "42000",
      "totalOnlineContactsCount": 1,
      "countByPosition": {
        "taxProfessionalCount": 0,
        "attorneyCount": 1,
        "nonAttorneyCount": 0,
        "clerkCount": 0
      }
    }
  ]
}
```

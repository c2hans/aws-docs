---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/rds-function-reference.html
---

# AWS AppSync JavaScript function reference for Amazon RDS
<a name="rds-function-reference"></a>

The AWS AppSync RDS function enables you to send SQL queries to an Amazon Aurora cluster database using the RDS Data API and get back the result of these queries. You can write SQL statements that are sent to the Data API by using AWS AppSync's `rds` module `sql`-tagged template or by using the `rds` module's `select`, `insert`, `update`, and `remove` helper functions. AWS AppSync utilizes the RDS Data Service's [https://docs.aws.amazon.com//rdsdataservice/latest/APIReference/API_ExecuteStatement.html](https://docs.aws.amazon.com//rdsdataservice/latest/APIReference/API_ExecuteStatement.html) action to run SQL statements against the database.

## SQL tagged template
<a name="sql-tagged-templates"></a>

AWS AppSync's `sql` tagged template enables you to create a static statement that can receive dynamic values at runtime by using template expressions. AWS AppSync builds a variable map from the expression values to construct a [https://docs.aws.amazon.com//rdsdataservice/latest/APIReference/API_SqlParameter.html](https://docs.aws.amazon.com//rdsdataservice/latest/APIReference/API_SqlParameter.html) query that is sent to the Amazon Aurora Serverless Data API. With this method, it isn't possible for dynamic values passed at run time to modify the original statement, which could cause unintented execution. All dynamic values are passed as parameters, can't modify the original statement, and aren't executed by the database. This makes your query less vulnerable to SQL injection attacks.

**Note**
In all cases, when writing SQL statements, you should follow security guidelines to properly handle data that you receive as input.

**Note**
The `sql` tagged template only supports passing variable values. You can't use an expression to dynamically specify the column or table names. However, you can use utility functions to build dynamic statements.

**Filtering Database Results Securely with Dynamic Channel Paths**

When building AWS AppSync applications, you often need to filter database queries based on dynamic values. This pattern shows how to safely incorporate run-time values into your SQL queries while maintaining security. In the following example, we create a query that filters based on the value of channel path that is set dynamically at run time. The value can easily be added to the statement using the tag expression.

```
import { sql, createMySQLStatement as mysql } from '@aws-appsync/utils/rds';

    export const onPublish = {
      request(ctx) {
        const query = sql`
    SELECT * FROM table
    WHERE column = ${ctx.info.channel.path}`;
        return mysql(query);
      }
    }
```

The database engine automatically protects against SQL injection attacks by sanitizing all values passed through the variable map.

## Creating statements
<a name="creating-statements"></a>

Handlers can interact with MySQL and PostgreSQL databases. Use `createMySQLStatement` and `createPgStatement` respectively to build statements. For example, `createMySQLStatement` can create a MySQL query. These functions accept up to two statements, useful when a request should retrieve results immediately. With MySQL, you can do the following:

```
import { sql, createMySQLStatement } from '@aws-appsync/utils/rds';

export const onSubscribe = {
  request(ctx) {
    const { id, text } = ctx.events[0].payload;
    const s1 = sql`insert into Post(id, text) values(${id}, ${text})`;
    const s2 = sql`select * from Post where id = ${id}`;
    return createMySQLStatement(s1, s2);
  }
}
```

**Note**
`createPgStatement` and `createMySQLStatement` does not escape or quote statements built with the `sql` tagged template.

## Retrieving data
<a name="retrieving-data"></a>

The result of your executed SQL statement is available in your response handler in the `context.result` object. The result is a JSON string with the [response elements](https://docs.aws.amazon.com//rdsdataservice/latest/APIReference/API_ExecuteStatement.html#API_ExecuteStatement_ResponseElements) from the `ExecuteStatement` action. When parsed, the result has the following shape:

```
type SQLStatementResults = {
    sqlStatementResults: {
        records: any[];
        columnMetadata: any[];
        numberOfRecordsUpdated: number;
        generatedFields?: any[]
    }[]
}
```

The following example demonstrates how you can use the `toJsonObject` utility to transform the result into a list of JSON objects representing the returned rows.

```
import { toJsonObject } from '@aws-appsync/utils/rds';

export const onSubscribe = {
  response(ctx) {
    const { error, result } = ctx;
    if (error) {
      return util.error(
        error.message,
        error.type,
        result
      )
    }
    const result =  toJsonObject(result)[1][0]
  }
}
```

Note that `toJsonObject` returns an array of statement results. If you provided one statement, the array length is `1`. If you provided two statements, the array length is `2`. Each result in the array contains `0` or more rows. `toJsonObject` returns `null` if the result value is invalid or unexpected.

## Utility functions
<a name="utility-functions"></a>

You can use the AWS AppSync RDS module's utility helpers to interact with your database. To learn more, see [Amazon RDS module functions](built-in-modules.md#built-in-rds-modules).

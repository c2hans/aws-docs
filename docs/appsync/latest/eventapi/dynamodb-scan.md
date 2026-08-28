---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-scan.html
---

# Scan
<a name="dynamodb-scan"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `Scan` request scans for items across a DynamoDB table. The request specifies the following:
+ A filter to exclude results
+ Which index to use
+ How many items to return
+ Whether to use consistent reads
+ Pagination token
+ Parallel scans

The `Scan` request object has the following structure:

```
type DynamoDBScanRequest = {
  operation: 'Scan';
  index?: string;
  limit?: number;
  consistentRead?: boolean;
  nextToken?: string;
  totalSegments?: number;
  segment?: number;
  filter?: {
    expression: string;
    expressionNames?: { [key: string]: string };
    expressionValues?: { [key: string]: any };
  };
  projection?: {
    expression: string;
    expressionNames?: { [key: string]: string };
  };
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## Scan fields
<a name="js-scan-list"></a>

** `operation` **
The DynamoDB operation to perform. To perform the `Scan` DynamoDB operation, this must be set to `Scan`. This value is required.

** `filter` **
A filter that can be used to filter the results from DynamoDB before they are returned. For more information about filters, see [Filters](dynamodb-filter.md). This field is optional.

** `index` **
The name of the index to query. The DynamoDB query operation allows you to scan on Local Secondary Indexes and Global Secondary Indexes in addition to the primary key index for a hash key. If specified, this tells DynamoDB to query the specified index. If omitted, the primary key index is queried.

** `limit` **
The maximum number of items to evaluate at a single time. This field is optional.

** `consistentRead` **
A Boolean that indicates whether to use consistent reads when querying DynamoDB. This field is optional, and defaults to `false`.

** `nextToken` **
The pagination token to continue a previous query. This would have been obtained from a previous query. This field is optional.

** `select` **
By default, the AWS AppSync DynamoDB function only returns whatever attributes are projected into the index. If more attributes are required, then this field can be set. This field is optional. The supported values are:
** `ALL_ATTRIBUTES` **
Returns all of the item attributes from the specified table or index. If you query a local secondary index, DynamoDB fetches the entire item from the parent table for each matching item in the index. If the index is configured to project all item attributes, all of the data can be obtained from the local secondary index and no fetching is required.
** `ALL_PROJECTED_ATTRIBUTES` **
Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES`.
**`SPECIFIC_ATTRIBUTES`**
Returns only the attributes listed in the `projection`'s `expression`. This return value is equivalent to specifying the `projection`'s `expression` without specifying any value for `Select`.

** `totalSegments` **
The number of segments to partition the table by when performing a parallel scan. This field is optional, but must be specified if `segment` is specified.

** `segment` **
The table segment in this operation when performing a parallel scan. This field is optional, but must be specified if `totalSegments` is specified.

**`projection`**
A projection that's used to specify the attributes to return from the DynamoDB operation. For more information about projections, see [Projections](dynamodb-projections.md). This field is optional.

The results have the following structure:

```
{
    items = [ ... ],
    nextToken = "a pagination token",
    scannedCount = 10
}
```

The fields are defined as follows:

** `items` **
A list containing the items returned by the DynamoDB scan.

** `nextToken` **
If there might be more results, `nextToken` contains a pagination token that you can use in another request. AWS AppSync encrypts and obfuscates the pagination token returned from DynamoDB. This prevents your table data from being inadvertently leaked to the caller. Also, these pagination tokens can’t be used across different functions.

** `scannedCount` **
The number of items that were retrieved by DynamoDB before a filter expression (if present) was applied.

For more information about the DynamoDB `Scan` API, see the [DynamoDB API documentation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

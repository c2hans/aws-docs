---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-supported-data-types.html
---

# Supported data types for Iceberg tables in Athena
<a name="querying-iceberg-supported-data-types"></a>

Athena can query Iceberg tables that contain the following data types:

```
binary
boolean
date
decimal
double
float
int
list
long
map
string
struct
timestamp without time zone
```

For more information about Iceberg table types, see the [schemas page for Iceberg](https://iceberg.apache.org/docs/latest/schemas/) in the Apache documentation.

The following table shows the relationship between Athena data types and Iceberg table data types.

****

<table>
<thead>
  <tr><th>Iceberg type</th><th>Athena type</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td>boolean</td><td>boolean</td><td></td></tr>
  <tr><td>-</td><td>tinyint</td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td>-</td><td>smallint</td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td>int</td><td>int</td><td>In Athena DML statements, this type is INTEGER.</td></tr>
  <tr><td>long</td><td>bigint</td><td></td></tr>
  <tr><td>double</td><td>double</td><td></td></tr>
  <tr><td>float</td><td>float</td><td></td></tr>
  <tr><td>decimal(P, S)</td><td>decimal(P, S)</td><td>P is precision, S is scale.</td></tr>
  <tr><td>-</td><td>char</td><td>Not supported for Iceberg tables in Athena.</td></tr>
  <tr><td>string</td><td>string</td><td>In Athena DML statements, this type is VARCHAR.</td></tr>
  <tr><td>binary</td><td>binary</td><td></td></tr>
  <tr><td>date</td><td>date</td><td></td></tr>
  <tr><td>time</td><td>-</td><td rowspan="3">Only Iceberg timestamp (without time zone) is supported for Athena Iceberg DDL statements like CREATE TABLE, but all timestamp types can be queried through Athena.</td></tr>
  <tr><td>timestamp</td><td>timestamp</td></tr>
  <tr><td>timestamptz</td><td>timestamptz</td></tr>
  <tr><td>list<E></td><td>array</td><td></td></tr>
  <tr><td>map<K,V></td><td>map</td><td></td></tr>
  <tr><td>struct<...></td><td>struct</td><td></td></tr>
  <tr><td>fixed(L)</td><td>-</td><td>The fixed(L) type is not currently supported in Athena.</td></tr>
</tbody>
</table>

For more information about data types in Athena, see [Data types in Amazon Athena](data-types.md).

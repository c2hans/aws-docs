---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-column-names.html
---

# Column names in Cryptographic Computing for Clean Rooms
<a name="crypto-computing-column-names"></a>

By default, the names of columns are important in Cryptographic Computing for Clean Rooms.

If the value of the **Allow JOIN of columns with different names** parameter is **false**, column names are used during the encryption of fingerprint columns. For this reason, by default, collaborators must coordinate in advance and use the same target column names for data that will use JOIN statements in queries. By default, columns encrypted for JOIN with different names don't successfully JOIN on any values.

If the value of the **Allow JOIN of columns with different names** parameter is **true**, JOIN statements across columns encrypted as fingerprint columns succeed. Encrypting data with this parameter might allow some inference of the cleartext values. For example, if a row has the same Hash-based Message Authentication Code (HMAC) value in both the `City` column and `State` column, the value might be `New York`.

## Normalization of column header names
<a name="column-header-names-normalization"></a>

Column header names are normalized by the C3R encryption client. Any leading and trailing white space is removed, and the column name is made lowercase for the transformed output.

Normalization is applied before all other computations, calculations, or other operations which could possibly be impacted by column names. The emitted output file only contains the normalized names.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

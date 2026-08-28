---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Reference.DataTypes.html
---

# Data types for AWS Database Migration Service
<a name="CHAP_Reference.DataTypes"></a>

AWS Database Migration Service uses built-in data types to migrate data from a source database engine type to a target database engine type. The following table shows the built-in data types and their descriptions.

|  AWS DMS data types  |  Description  |
| --- | --- |
| STRING | A character string. |
| WSTRING | A double-byte character string. |
| BOOLEAN | A Boolean value. |
| BYTE | A binary data value. |
| DATE | A date value: year, month, day. |
| TIME | A time value: hour, minutes, seconds. |
| DATETIME | A timestamp value: year, month, day, hour, minute, second, fractional seconds. The fractional seconds have a maximum scale of 9 digits. The following format is supported: YYYY:MM:DD HH:MM:SS.F(9). For Amazon S3 Select and Amazon S3 Glacier Select, the DATETIME data type format is different. For more information, see the description of the `timestamp` primitive data type in [ Supported Data Types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-glacier-select-sql-reference-data-types.html) of the *Amazon Simple Storage Service User Guide*. |
| INT1 | A one-byte, signed integer. |
| INT2 | A two-byte, signed integer. |
| INT4 | A four-byte, signed integer. |
| INT8 | An eight-byte, signed integer. |
| NUMERIC  | An exact numeric value with a fixed precision and scale. |
| REAL4 | A single-precision floating-point value. |
| REAL8 | A double-precision floating-point value. |
| UINT1 | A one-byte, unsigned integer. |
| UINT2 | A two-byte, unsigned integer. |
| UINT4 | A four-byte, unsigned integer. |
| UINT8 | An eight-byte, unsigned integer. |
| BLOB | Binary large object. |
| CLOB | Character large object.  |
| NCLOB | Native character large object.  |

**Note**
AWS DMS can't migrate any LOB data type to an Apache Kafka endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

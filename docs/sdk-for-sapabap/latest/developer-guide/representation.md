---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/representation.html
---

# Representation of data in ABAP
<a name="representation"></a>

This section covers the following topics.

**Topics**
+ [Data types](#data-types)
+ [AWS data types](#aws-api)

## Data types
<a name="data-types"></a>

AWS services have a standard set of data types that must be mapped to ABAP data types. See the following table for more details.

<table>
<thead>
  <tr><th>AWS data type</th><th>ABAP data type</th><th>Comments</th></tr>
</thead>
<tbody>
  <tr><td>boolean</td><td>C</td><td>Single character <code>"X"</code> and <code>" "</code></td></tr>
  <tr><td>String</td><td>STRING</td><td></td></tr>
  <tr><td>Byte</td><td>INT2</td><td>INT2 has a larger range than 0-255. Most AWS services will truncate overflows but this behavior is not formally defined.</td></tr>
  <tr><td>Short</td><td>INT2</td><td></td></tr>
  <tr><td>Integer</td><td>INT4</td><td></td></tr>
  <tr><td>Long</td><td>DEC19</td><td>INT8 is not available until ABAP 750. DEC19 is used for compatibility and consistency across all supported ABAP platforms.</td></tr>
  <tr><td>Blob</td><td>XSTRING</td><td>Represents binary data</td></tr>
  <tr><td>Float</td><td>STRING</td><td rowspan="2">While ABAP supports DECFLOATs, it cannot represent values such as  NaN, Infinity  and -Infinity. AWS SDK represents these internally as STRINGs, and converts them to DECFLOAT16 at runtime. If NaN, Infinity or +Infinity are represented, the developer may process these in response to a special set of exceptions or mappings.</td></tr>
  <tr><td>Double</td><td>STRING</td></tr>
  <tr><td>bigInteger</td><td>STRING</td><td rowspan="2">These values represent infinite-length numbers that cannot be represented in ABAP, and STRINGs are used instead of bigInteger.</td></tr>
  <tr><td>bigDecimal</td><td>STRING</td></tr>
  <tr><td>Timestamp</td><td> <code>TZNTSTMPS</code> </td><td><code>TZNTSTMPS</code> enables processing with native ABAP timestamp functions.</td></tr>
</tbody>
</table>

AWS services also return the following aggregate data types.

| AWS data type | ABAP data type | Comments |
| --- | --- | --- |
| Structure | Class |  |
| Union | Class | A union is the same as a structure, except that a union will never have more than one field set. All other fields will be set to No Value. |
| Array | STANDARD TABLE |  |
| Hash | HASHED TABLE | The hashed table will only have two columns: a KEY (string) and a VALUE (class).  |

## AWS data types
<a name="aws-api"></a>

The following approaches have been integrated to support AWS services in ABAP.
+ Certain AWS data types cannot be represented in ABAP. For examples, the `float` data type in ABAP does not support the `NaN`, `Infinity`, or `-Infinity` values. Therefore, the `float` data type is represented as `STRING` and is translated to `DECFLOAT16` at runtime.
+ AWS data is represented on the wire as JSON or XML, and the values are optional. For example, see the following examples returned by an AWS service in JSON.

  ```
  Fullname: {
     Firstname:  "Ana",
     Middlename: "Carolina",
     Lastname:  "Silva"
  }
  ```

  If Ana doesn't have a middle name, the service returns the following output.

  ```
  Fullname: {
     Firstname:  "Ana",
     Lastname:  "Silva"
  }
  ```

  ABAP does not distinguish between *a string of length 0* and *a string that has no value*. Other languages might assign a NULL value to the string or wrap the string in a construct (such as, Java's `Optional<>` wrapper). These are not supported in ABAP. Therefore, SDK for SAP ABAP facilitates the distinction in values by providing variants of the *getter* method.

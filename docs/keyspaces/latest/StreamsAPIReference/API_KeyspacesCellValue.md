---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCellValue.html
---

# KeyspacesCellValue
<a name="API_KeyspacesCellValue"></a>

Represents the value of a cell in an Amazon Keyspaces table, supporting various data types with type-specific fields.

## Contents
<a name="API_KeyspacesCellValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** asciiT **   <a name="keyspaces-Type-KeyspacesCellValue-asciiT"></a>
A value of ASCII text type, containing US-ASCII characters.
Type: String
Required: No

 ** bigintT **   <a name="keyspaces-Type-KeyspacesCellValue-bigintT"></a>
A 64-bit signed integer value.
Type: String
Required: No

 ** blobT **   <a name="keyspaces-Type-KeyspacesCellValue-blobT"></a>
A binary large object (BLOB) value stored as a Base64-encoded string.
Type: Base64-encoded binary data object
Required: No

 ** boolT **   <a name="keyspaces-Type-KeyspacesCellValue-boolT"></a>
A Boolean value, either `true` or `false`.
Type: Boolean
Required: No

 ** counterT **   <a name="keyspaces-Type-KeyspacesCellValue-counterT"></a>
A distributed counter value that can be incremented and decremented.
Type: String
Required: No

 ** dateT **   <a name="keyspaces-Type-KeyspacesCellValue-dateT"></a>
A date value without a time component, represented as days since epoch (January 1, 1970).
Type: String
Required: No

 ** decimalT **   <a name="keyspaces-Type-KeyspacesCellValue-decimalT"></a>
A variable-precision decimal number value.
Type: String
Required: No

 ** doubleT **   <a name="keyspaces-Type-KeyspacesCellValue-doubleT"></a>
A 64-bit double-precision floating point value.
Type: String
Required: No

 ** durationT **   <a name="keyspaces-Type-KeyspacesCellValue-durationT"></a>
A duration value with nanosecond precision, representing a period of time encoded as 32-bit months, 32-bit days, and 64-bit nanoseconds.
Type: String
Required: No

 ** floatT **   <a name="keyspaces-Type-KeyspacesCellValue-floatT"></a>
A 32-bit single-precision floating point value.
Type: String
Required: No

 ** inetT **   <a name="keyspaces-Type-KeyspacesCellValue-inetT"></a>
An IP address value, either IPv4 or IPv6 format.
Type: String
Required: No

 ** intT **   <a name="keyspaces-Type-KeyspacesCellValue-intT"></a>
A 32-bit signed integer value.
Type: String
Required: No

 ** listT **   <a name="keyspaces-Type-KeyspacesCellValue-listT"></a>
An ordered collection of elements that can contain duplicate values.
Type: Array of [KeyspacesCell](API_KeyspacesCell.md) objects
Required: No

 ** mapT **   <a name="keyspaces-Type-KeyspacesCellValue-mapT"></a>
A collection of key-value pairs where each key is unique.
Type: Array of [KeyspacesCellMapDefinition](API_KeyspacesCellMapDefinition.md) objects
Required: No

 ** setT **   <a name="keyspaces-Type-KeyspacesCellValue-setT"></a>
An unordered collection of unique elements.
Type: Array of [KeyspacesCell](API_KeyspacesCell.md) objects
Required: No

 ** smallintT **   <a name="keyspaces-Type-KeyspacesCellValue-smallintT"></a>
A 16-bit signed integer value.
Type: String
Required: No

 ** textT **   <a name="keyspaces-Type-KeyspacesCellValue-textT"></a>
A UTF-8 encoded string value.
Type: String
Required: No

 ** timestampT **   <a name="keyspaces-Type-KeyspacesCellValue-timestampT"></a>
A timestamp value representing date and time with millisecond precision.
Type: String
Required: No

 ** timeT **   <a name="keyspaces-Type-KeyspacesCellValue-timeT"></a>
A time value without a date component, with nanosecond precision.
Type: String
Required: No

 ** timeuuidT **   <a name="keyspaces-Type-KeyspacesCellValue-timeuuidT"></a>
A universally unique identifier (UUID) that includes a timestamp component, ensuring both uniqueness and time ordering.
Type: String
Required: No

 ** tinyintT **   <a name="keyspaces-Type-KeyspacesCellValue-tinyintT"></a>
An 8-bit signed integer value.
Type: String
Required: No

 ** tupleT **   <a name="keyspaces-Type-KeyspacesCellValue-tupleT"></a>
A fixed-length ordered list of elements, where each element can be of a different data type.
Type: Array of [KeyspacesCell](API_KeyspacesCell.md) objects
Required: No

 ** udtT **   <a name="keyspaces-Type-KeyspacesCellValue-udtT"></a>
A user-defined type (UDT) value consisting of named fields, each with its own data type.
Type: String to [KeyspacesCell](API_KeyspacesCell.md) object map
Required: No

 ** uuidT **   <a name="keyspaces-Type-KeyspacesCellValue-uuidT"></a>
A universally unique identifier (UUID) value.
Type: String
Required: No

 ** varcharT **   <a name="keyspaces-Type-KeyspacesCellValue-varcharT"></a>
A UTF-8 encoded string value, functionally equivalent to text type.
Type: String
Required: No

 ** varintT **   <a name="keyspaces-Type-KeyspacesCellValue-varintT"></a>
An integer value within the \+/-10^38 range.
Type: String
Required: No

## See Also
<a name="API_KeyspacesCellValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/KeyspacesCellValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/KeyspacesCellValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/KeyspacesCellValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

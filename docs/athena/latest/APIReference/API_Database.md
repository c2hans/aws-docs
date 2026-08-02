---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_Database.html
---

# Database
<a name="API_Database"></a>

Contains metadata information for a database in a data catalog.

## Contents
<a name="API_Database_Contents"></a>

 ** Name **   <a name="athena-Type-Database-Name"></a>
The name of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Description **   <a name="athena-Type-Database-Description"></a>
An optional description of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Parameters **   <a name="athena-Type-Database-Parameters"></a>
A set of custom key/value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 51200.
Required: No

## See Also
<a name="API_Database_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/Database)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/Database)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/Database)

---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_NamedQuery.html
---

# NamedQuery
<a name="API_NamedQuery"></a>

A query, where `QueryString` contains the SQL statements that make up the query.

## Contents
<a name="API_NamedQuery_Contents"></a>

 ** Database **   <a name="athena-Type-NamedQuery-Database"></a>
The database to which the query belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Name **   <a name="athena-Type-NamedQuery-Name"></a>
The query name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** QueryString **   <a name="athena-Type-NamedQuery-QueryString"></a>
The SQL statements that make up the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** Description **   <a name="athena-Type-NamedQuery-Description"></a>
The query description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** NamedQueryId **   <a name="athena-Type-NamedQuery-NamedQueryId"></a>
The unique identifier of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: No

 ** WorkGroup **   <a name="athena-Type-NamedQuery-WorkGroup"></a>
The name of the workgroup that contains the named query.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## See Also
<a name="API_NamedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/NamedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/NamedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/NamedQuery)

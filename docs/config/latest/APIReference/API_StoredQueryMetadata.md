---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StoredQueryMetadata.html
---

# StoredQueryMetadata
<a name="API_StoredQueryMetadata"></a>

Returns details of a specific query.

## Contents
<a name="API_StoredQueryMetadata_Contents"></a>

 ** QueryArn **   <a name="config-Type-StoredQueryMetadata-QueryArn"></a>
Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:stored-query/[a-zA-Z0-9-_]+/query-[a-zA-Z\d-_/]+$`
Required: Yes

 ** QueryId **   <a name="config-Type-StoredQueryMetadata-QueryId"></a>
The ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^\S+$`
Required: Yes

 ** QueryName **   <a name="config-Type-StoredQueryMetadata-QueryName"></a>
The name of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** Description **   <a name="config-Type-StoredQueryMetadata-Description"></a>
A unique description for the query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_StoredQueryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StoredQueryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StoredQueryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StoredQueryMetadata)

---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StoredQuery.html
---

# StoredQuery
<a name="API_StoredQuery"></a>

Provides the details of a stored query.

## Contents
<a name="API_StoredQuery_Contents"></a>

 ** QueryName **   <a name="config-Type-StoredQuery-QueryName"></a>
The name of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** Description **   <a name="config-Type-StoredQuery-Description"></a>
A unique description for the query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Expression **   <a name="config-Type-StoredQuery-Expression"></a>
The expression of the query. For example, `SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** QueryArn **   <a name="config-Type-StoredQuery-QueryArn"></a>
Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:stored-query/[a-zA-Z0-9-_]+/query-[a-zA-Z\d-_/]+$`
Required: No

 ** QueryId **   <a name="config-Type-StoredQuery-QueryId"></a>
The ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^\S+$`
Required: No

## See Also
<a name="API_StoredQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StoredQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StoredQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StoredQuery)

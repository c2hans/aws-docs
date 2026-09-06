---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollectionDetail.html
---

# DeleteCollectionDetail
<a name="API_DeleteCollectionDetail"></a>

Details about a deleted OpenSearch Serverless collection.

## Contents
<a name="API_DeleteCollectionDetail_Contents"></a>

 ** deletionProtection **   <a name="opensearchserverless-Type-DeleteCollectionDetail-deletionProtection"></a>
Indicates whether deletion protection is `ENABLED` or `DISABLED` for the collection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** id **   <a name="opensearchserverless-Type-DeleteCollectionDetail-id"></a>
The unique identifier of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** name **   <a name="opensearchserverless-Type-DeleteCollectionDetail-name"></a>
The name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-DeleteCollectionDetail-status"></a>
The current status of the collection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED | UPDATE_FAILED`
Required: No

## See Also
<a name="API_DeleteCollectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteCollectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteCollectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteCollectionDetail)

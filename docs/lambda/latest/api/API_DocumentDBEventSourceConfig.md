---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DocumentDBEventSourceConfig.html
---

# DocumentDBEventSourceConfig
<a name="API_DocumentDBEventSourceConfig"></a>

 Specific configuration settings for a DocumentDB event source.

## Contents
<a name="API_DocumentDBEventSourceConfig_Contents"></a>

 ** CollectionName **   <a name="lambda-Type-DocumentDBEventSourceConfig-CollectionName"></a>
 The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes all collections.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 57.
Pattern: `(^(?!(system\x2e)))(^[_a-zA-Z0-9])([^$]*)`
Required: No

 ** DatabaseName **   <a name="lambda-Type-DocumentDBEventSourceConfig-DatabaseName"></a>
 The name of the database to consume within the DocumentDB cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[^ /\.$\x22]*`
Required: No

 ** FullDocument **   <a name="lambda-Type-DocumentDBEventSourceConfig-FullDocument"></a>
 Determines what DocumentDB sends to your event stream during document update operations. If set to UpdateLookup, DocumentDB sends a delta describing the changes, along with a copy of the entire document. Otherwise, DocumentDB sends only a partial document that contains the changes.
Type: String
Valid Values: `UpdateLookup | Default`
Required: No

## See Also
<a name="API_DocumentDBEventSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DocumentDBEventSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DocumentDBEventSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DocumentDBEventSourceConfig)

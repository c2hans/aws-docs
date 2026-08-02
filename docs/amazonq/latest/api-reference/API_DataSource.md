---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSource.html
---

# DataSource
<a name="API_DataSource"></a>

A data source in an Amazon Q Business application.

## Contents
<a name="API_DataSource_Contents"></a>

 ** createdAt **   <a name="qbusiness-Type-DataSource-createdAt"></a>
The Unix timestamp when the Amazon Q Business data source was created.
Type: Timestamp
Required: No

 ** dataSourceId **   <a name="qbusiness-Type-DataSource-dataSourceId"></a>
The identifier of the Amazon Q Business data source.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** displayName **   <a name="qbusiness-Type-DataSource-displayName"></a>
The name of the Amazon Q Business data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** status **   <a name="qbusiness-Type-DataSource-status"></a>
The status of the Amazon Q Business data source.
Type: String
Valid Values: `PENDING_CREATION | CREATING | ACTIVE | DELETING | FAILED | UPDATING`
Required: No

 ** type **   <a name="qbusiness-Type-DataSource-type"></a>
The type of the Amazon Q Business data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** updatedAt **   <a name="qbusiness-Type-DataSource-updatedAt"></a>
The Unix timestamp when the Amazon Q Business data source was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataSource)

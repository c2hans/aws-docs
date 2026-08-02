---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeNamespace.html
---

# DataLakeNamespace
<a name="API_DataLakeNamespace"></a>

The data lake namespace details.

## Contents
<a name="API_DataLakeNamespace_Contents"></a>

 ** arn **   <a name="supplychain-Type-DataLakeNamespace-arn"></a>
The arn of the namespace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1011.
Pattern: `arn:aws:scn(?::([a-z0-9-]+):([0-9]+):instance)?/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})[-_./A-Za-z0-9]*`
Required: Yes

 ** createdTime **   <a name="supplychain-Type-DataLakeNamespace-createdTime"></a>
The creation time of the namespace.
Type: Timestamp
Required: Yes

 ** instanceId **   <a name="supplychain-Type-DataLakeNamespace-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="supplychain-Type-DataLakeNamespace-lastModifiedTime"></a>
The last modified time of the namespace.
Type: Timestamp
Required: Yes

 ** name **   <a name="supplychain-Type-DataLakeNamespace-name"></a>
The name of the namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** description **   <a name="supplychain-Type-DataLakeNamespace-description"></a>
The description of the namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_DataLakeNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataLakeNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataLakeNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataLakeNamespace)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DataSource.html
---

# DataSource
<a name="API_DataSource"></a>

Data sources that are associated with an OpenSearch application.

## Contents
<a name="API_DataSource_Contents"></a>

 ** dataSourceArn **   <a name="opensearchservice-Type-DataSource-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** dataSourceDescription **   <a name="opensearchservice-Type-DataSource-dataSourceDescription"></a>
Detailed description of a data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
Required: No

 ** iamRoleForDataSourceArn **   <a name="opensearchservice-Type-DataSource-iamRoleForDataSourceArn"></a>
The ARN of the IAM role to be used for cross account/region data source association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DataSource)

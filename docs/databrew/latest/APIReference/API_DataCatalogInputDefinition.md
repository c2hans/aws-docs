---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DataCatalogInputDefinition.html
---

# DataCatalogInputDefinition
<a name="API_DataCatalogInputDefinition"></a>

Represents how metadata stored in the AWS Glue Data Catalog is defined in a DataBrew dataset.

## Contents
<a name="API_DataCatalogInputDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatabaseName **   <a name="databrew-Type-DataCatalogInputDefinition-DatabaseName"></a>
The name of a database in the Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** TableName **   <a name="databrew-Type-DataCatalogInputDefinition-TableName"></a>
The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** CatalogId **   <a name="databrew-Type-DataCatalogInputDefinition-CatalogId"></a>
The unique identifier of the AWS account that holds the Data Catalog that stores the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** TempDirectory **   <a name="databrew-Type-DataCatalogInputDefinition-TempDirectory"></a>
Represents an Amazon location where DataBrew can store intermediate results.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_DataCatalogInputDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DataCatalogInputDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DataCatalogInputDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DataCatalogInputDefinition)

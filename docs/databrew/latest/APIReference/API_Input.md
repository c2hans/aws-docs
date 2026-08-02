---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Input.html
---

# Input
<a name="API_Input"></a>

Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or Amazon S3.

## Contents
<a name="API_Input_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatabaseInputDefinition **   <a name="databrew-Type-Input-DatabaseInputDefinition"></a>
Connection information for dataset input files stored in a database.
Type: [DatabaseInputDefinition](API_DatabaseInputDefinition.md) object
Required: No

 ** DataCatalogInputDefinition **   <a name="databrew-Type-Input-DataCatalogInputDefinition"></a>
The AWS Glue Data Catalog parameters for the data.
Type: [DataCatalogInputDefinition](API_DataCatalogInputDefinition.md) object
Required: No

 ** Metadata **   <a name="databrew-Type-Input-Metadata"></a>
Contains additional resource information needed for specific datasets.
Type: [Metadata](API_Metadata.md) object
Required: No

 ** S3InputDefinition **   <a name="databrew-Type-Input-S3InputDefinition"></a>
The Amazon S3 location where the data is stored.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_Input_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Input)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Input)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Input)

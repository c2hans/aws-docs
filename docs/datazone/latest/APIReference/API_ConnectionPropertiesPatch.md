---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectionPropertiesPatch.html
---

# ConnectionPropertiesPatch
<a name="API_ConnectionPropertiesPatch"></a>

The connection properties patch.

## Contents
<a name="API_ConnectionPropertiesPatch_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** amazonQProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-amazonQProperties"></a>
The Amazon Q properties of the connection.
Type: [AmazonQPropertiesPatch](API_AmazonQPropertiesPatch.md) object
Required: No

 ** athenaProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-athenaProperties"></a>
The Amazon Athena properties of a connection properties patch.
Type: [AthenaPropertiesPatch](API_AthenaPropertiesPatch.md) object
Required: No

 ** glueProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-glueProperties"></a>
The AWS Glue properties of a connection properties patch.
Type: [GluePropertiesPatch](API_GluePropertiesPatch.md) object
Required: No

 ** iamProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-iamProperties"></a>
The IAM properties of a connection properties patch.
Type: [IamPropertiesPatch](API_IamPropertiesPatch.md) object
Required: No

 ** lakehouseProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-lakehouseProperties"></a>
The lakehouse properties of a connection properties patch.
Type: [LakehousePropertiesPatch](API_LakehousePropertiesPatch.md) object
Required: No

 ** mlflowProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-mlflowProperties"></a>
The MLflow properties of a connection.
Type: [MlflowPropertiesPatch](API_MlflowPropertiesPatch.md) object
Required: No

 ** redshiftProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-redshiftProperties"></a>
The Amazon Redshift properties of a connection properties patch.
Type: [RedshiftPropertiesPatch](API_RedshiftPropertiesPatch.md) object
Required: No

 ** s3Properties **   <a name="datazone-Type-ConnectionPropertiesPatch-s3Properties"></a>
The Amazon S3 properties of a connection properties patch.
Type: [S3PropertiesPatch](API_S3PropertiesPatch.md) object
Required: No

 ** sparkEmrProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-sparkEmrProperties"></a>
The Spark EMR properties of a connection properties patch.
Type: [SparkEmrPropertiesPatch](API_SparkEmrPropertiesPatch.md) object
Required: No

 ** vpcProperties **   <a name="datazone-Type-ConnectionPropertiesPatch-vpcProperties"></a>
The VPC properties of a connection properties patch.
Type: [VpcPropertiesPatch](API_VpcPropertiesPatch.md) object
Required: No

## See Also
<a name="API_ConnectionPropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectionPropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectionPropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectionPropertiesPatch)

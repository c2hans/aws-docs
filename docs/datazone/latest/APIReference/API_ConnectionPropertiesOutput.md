---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectionPropertiesOutput.html
---

# ConnectionPropertiesOutput
<a name="API_ConnectionPropertiesOutput"></a>

The properties of a connection.

## Contents
<a name="API_ConnectionPropertiesOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** amazonQProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-amazonQProperties"></a>
The Amazon Q properties of the connection.
Type: [AmazonQPropertiesOutput](API_AmazonQPropertiesOutput.md) object
Required: No

 ** athenaProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-athenaProperties"></a>
The Amazon Athena properties of a connection.
Type: [AthenaPropertiesOutput](API_AthenaPropertiesOutput.md) object
Required: No

 ** glueProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-glueProperties"></a>
The AWS Glue properties of a connection.
Type: [GluePropertiesOutput](API_GluePropertiesOutput.md) object
Required: No

 ** hyperPodProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-hyperPodProperties"></a>
The hyper pod properties of a connection.
Type: [HyperPodPropertiesOutput](API_HyperPodPropertiesOutput.md) object
Required: No

 ** iamProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-iamProperties"></a>
The IAM properties of a connection.
Type: [IamPropertiesOutput](API_IamPropertiesOutput.md) object
Required: No

 ** lakehouseProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-lakehouseProperties"></a>
The lakehouse properties of a connection.
Type: [LakehousePropertiesOutput](API_LakehousePropertiesOutput.md) object
Required: No

 ** mlflowProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-mlflowProperties"></a>
The MLflow properties of a connection.
Type: [MlflowPropertiesOutput](API_MlflowPropertiesOutput.md) object
Required: No

 ** redshiftProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-redshiftProperties"></a>
The Amazon Redshift properties of a connection.
Type: [RedshiftPropertiesOutput](API_RedshiftPropertiesOutput.md) object
Required: No

 ** s3Properties **   <a name="datazone-Type-ConnectionPropertiesOutput-s3Properties"></a>
The Amazon S3 properties of a connection.
Type: [S3PropertiesOutput](API_S3PropertiesOutput.md) object
Required: No

 ** sparkEmrProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-sparkEmrProperties"></a>
The Spark EMR properties of a connection.
Type: [SparkEmrPropertiesOutput](API_SparkEmrPropertiesOutput.md) object
Required: No

 ** sparkGlueProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-sparkGlueProperties"></a>
The Spark AWS Glue properties of a connection.
Type: [SparkGluePropertiesOutput](API_SparkGluePropertiesOutput.md) object
Required: No

 ** vpcProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-vpcProperties"></a>
The VPC properties of a connection.
Type: [VpcPropertiesOutput](API_VpcPropertiesOutput.md) object
Required: No

 ** workflowsMwaaProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-workflowsMwaaProperties"></a>
The Amazon MWAA properties of a connection.
Type: [WorkflowsMwaaPropertiesOutput](API_WorkflowsMwaaPropertiesOutput.md) object
Required: No

 ** workflowsServerlessProperties **   <a name="datazone-Type-ConnectionPropertiesOutput-workflowsServerlessProperties"></a>
The MWAA serverless properties of a connection.
Type: [WorkflowsServerlessPropertiesOutput](API_WorkflowsServerlessPropertiesOutput.md) object
Required: No

## See Also
<a name="API_ConnectionPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectionPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectionPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectionPropertiesOutput)

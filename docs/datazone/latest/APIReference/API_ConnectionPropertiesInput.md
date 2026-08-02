---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectionPropertiesInput.html
---

# ConnectionPropertiesInput
<a name="API_ConnectionPropertiesInput"></a>

The properties of a connection.

## Contents
<a name="API_ConnectionPropertiesInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** amazonQProperties **   <a name="datazone-Type-ConnectionPropertiesInput-amazonQProperties"></a>
The Amazon Q properties of the connection.
Type: [AmazonQPropertiesInput](API_AmazonQPropertiesInput.md) object
Required: No

 ** athenaProperties **   <a name="datazone-Type-ConnectionPropertiesInput-athenaProperties"></a>
The Amazon Athena properties of a connection.
Type: [AthenaPropertiesInput](API_AthenaPropertiesInput.md) object
Required: No

 ** glueProperties **   <a name="datazone-Type-ConnectionPropertiesInput-glueProperties"></a>
The AWS Glue properties of a connection.
Type: [GluePropertiesInput](API_GluePropertiesInput.md) object
Required: No

 ** hyperPodProperties **   <a name="datazone-Type-ConnectionPropertiesInput-hyperPodProperties"></a>
The hyper pod properties of a connection.
Type: [HyperPodPropertiesInput](API_HyperPodPropertiesInput.md) object
Required: No

 ** iamProperties **   <a name="datazone-Type-ConnectionPropertiesInput-iamProperties"></a>
The IAM properties of a connection.
Type: [IamPropertiesInput](API_IamPropertiesInput.md) object
Required: No

 ** lakehouseProperties **   <a name="datazone-Type-ConnectionPropertiesInput-lakehouseProperties"></a>
The lakehouse properties of a connection.
Type: [LakehousePropertiesInput](API_LakehousePropertiesInput.md) object
Required: No

 ** mlflowProperties **   <a name="datazone-Type-ConnectionPropertiesInput-mlflowProperties"></a>
The MLflow properties of a connection.
Type: [MlflowPropertiesInput](API_MlflowPropertiesInput.md) object
Required: No

 ** redshiftProperties **   <a name="datazone-Type-ConnectionPropertiesInput-redshiftProperties"></a>
The Amazon Redshift properties of a connection.
Type: [RedshiftPropertiesInput](API_RedshiftPropertiesInput.md) object
Required: No

 ** s3Properties **   <a name="datazone-Type-ConnectionPropertiesInput-s3Properties"></a>
The Amazon S3 properties of a connection.
Type: [S3PropertiesInput](API_S3PropertiesInput.md) object
Required: No

 ** sparkEmrProperties **   <a name="datazone-Type-ConnectionPropertiesInput-sparkEmrProperties"></a>
The Spark EMR properties of a connection.
Type: [SparkEmrPropertiesInput](API_SparkEmrPropertiesInput.md) object
Required: No

 ** sparkGlueProperties **   <a name="datazone-Type-ConnectionPropertiesInput-sparkGlueProperties"></a>
The Spark AWS Glue properties of a connection.
Type: [SparkGluePropertiesInput](API_SparkGluePropertiesInput.md) object
Required: No

 ** vpcProperties **   <a name="datazone-Type-ConnectionPropertiesInput-vpcProperties"></a>
The VPC properties of a connection.
Type: [VpcPropertiesInput](API_VpcPropertiesInput.md) object
Required: No

 ** workflowsMwaaProperties **   <a name="datazone-Type-ConnectionPropertiesInput-workflowsMwaaProperties"></a>
The Amazon MWAA properties of a connection.
Type: [WorkflowsMwaaPropertiesInput](API_WorkflowsMwaaPropertiesInput.md) object
Required: No

 ** workflowsServerlessProperties **   <a name="datazone-Type-ConnectionPropertiesInput-workflowsServerlessProperties"></a>
The MWAA serverless properties of a connection.
Type: [WorkflowsServerlessPropertiesInput](API_WorkflowsServerlessPropertiesInput.md) object
Required: No

## See Also
<a name="API_ConnectionPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectionPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectionPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectionPropertiesInput)

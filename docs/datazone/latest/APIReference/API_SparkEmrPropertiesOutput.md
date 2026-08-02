---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SparkEmrPropertiesOutput.html
---

# SparkEmrPropertiesOutput
<a name="API_SparkEmrPropertiesOutput"></a>

The Spark EMR properties.

## Contents
<a name="API_SparkEmrPropertiesOutput_Contents"></a>

 ** certificateData **   <a name="datazone-Type-SparkEmrPropertiesOutput-certificateData"></a>
The certificate data of the EMR on EKS cluster.
Type: String
Required: No

 ** computeArn **   <a name="datazone-Type-SparkEmrPropertiesOutput-computeArn"></a>
The compute ARN of the Spark EMR.
Type: String
Required: No

 ** credentials **   <a name="datazone-Type-SparkEmrPropertiesOutput-credentials"></a>
The credentials of the Spark EMR.
Type: [UsernamePassword](API_UsernamePassword.md) object
Required: No

 ** credentialsExpiration **   <a name="datazone-Type-SparkEmrPropertiesOutput-credentialsExpiration"></a>
The credential expiration of the Spark EMR.
Type: Timestamp
Required: No

 ** governanceType **   <a name="datazone-Type-SparkEmrPropertiesOutput-governanceType"></a>
The governance type of the Spark EMR.
Type: String
Valid Values: `AWS_MANAGED | USER_MANAGED`
Required: No

 ** instanceProfileArn **   <a name="datazone-Type-SparkEmrPropertiesOutput-instanceProfileArn"></a>
The instance profile ARN of the Spark EMR.
Type: String
Required: No

 ** javaVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesOutput-javaVirtualEnv"></a>
The Java virtual env of the Spark EMR.
Type: String
Required: No

 ** livyEndpoint **   <a name="datazone-Type-SparkEmrPropertiesOutput-livyEndpoint"></a>
The livy endpoint of the Spark EMR.
Type: String
Required: No

 ** logUri **   <a name="datazone-Type-SparkEmrPropertiesOutput-logUri"></a>
The log URI of the Spark EMR.
Type: String
Required: No

 ** managedEndpointArn **   <a name="datazone-Type-SparkEmrPropertiesOutput-managedEndpointArn"></a>
The managed endpoint ARN of the EMR on EKS cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** managedEndpointCredentials **   <a name="datazone-Type-SparkEmrPropertiesOutput-managedEndpointCredentials"></a>
The managed endpoint credentials of the EMR on EKS cluster.
Type: [ManagedEndpointCredentials](API_ManagedEndpointCredentials.md) object
Required: No

 ** pythonVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesOutput-pythonVirtualEnv"></a>
The Python virtual env of the Spark EMR.
Type: String
Required: No

 ** runtimeRole **   <a name="datazone-Type-SparkEmrPropertiesOutput-runtimeRole"></a>
The runtime role of the Spark EMR.
Type: String
Required: No

 ** trustedCertificatesS3Uri **   <a name="datazone-Type-SparkEmrPropertiesOutput-trustedCertificatesS3Uri"></a>
The trusted certificate S3 URL of the Spark EMR.
Type: String
Required: No

## See Also
<a name="API_SparkEmrPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SparkEmrPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SparkEmrPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SparkEmrPropertiesOutput)

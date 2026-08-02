---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SparkEmrPropertiesPatch.html
---

# SparkEmrPropertiesPatch
<a name="API_SparkEmrPropertiesPatch"></a>

The Spark EMR properties patch.

## Contents
<a name="API_SparkEmrPropertiesPatch_Contents"></a>

 ** computeArn **   <a name="datazone-Type-SparkEmrPropertiesPatch-computeArn"></a>
The compute ARN in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:(elasticmapreduce|emr-serverless|emr-containers):.*`
Required: No

 ** instanceProfileArn **   <a name="datazone-Type-SparkEmrPropertiesPatch-instanceProfileArn"></a>
The instance profile ARN in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** javaVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesPatch-javaVirtualEnv"></a>
The Java virtual evn in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** logUri **   <a name="datazone-Type-SparkEmrPropertiesPatch-logUri"></a>
The log URI in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** managedEndpointArn **   <a name="datazone-Type-SparkEmrPropertiesPatch-managedEndpointArn"></a>
The managed endpoint ARN of the EMR on EKS cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** pythonVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesPatch-pythonVirtualEnv"></a>
The Python virtual env in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** runtimeRole **   <a name="datazone-Type-SparkEmrPropertiesPatch-runtimeRole"></a>
The runtime role in the Spark EMR properties patch.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

 ** trustedCertificatesS3Uri **   <a name="datazone-Type-SparkEmrPropertiesPatch-trustedCertificatesS3Uri"></a>
The trusted certificates S3 URI in the Spark EMR properties patch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SparkEmrPropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SparkEmrPropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SparkEmrPropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SparkEmrPropertiesPatch)

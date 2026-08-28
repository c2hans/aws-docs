---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SparkEmrPropertiesInput.html
---

# SparkEmrPropertiesInput
<a name="API_SparkEmrPropertiesInput"></a>

The Spark EMR properties.

## Contents
<a name="API_SparkEmrPropertiesInput_Contents"></a>

 ** computeArn **   <a name="datazone-Type-SparkEmrPropertiesInput-computeArn"></a>
The compute ARN of Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:(elasticmapreduce|emr-serverless|emr-containers):.*`
Required: No

 ** instanceProfileArn **   <a name="datazone-Type-SparkEmrPropertiesInput-instanceProfileArn"></a>
The instance profile ARN of Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** javaVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesInput-javaVirtualEnv"></a>
The java virtual env of the Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** logUri **   <a name="datazone-Type-SparkEmrPropertiesInput-logUri"></a>
The log URI of the Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** managedEndpointArn **   <a name="datazone-Type-SparkEmrPropertiesInput-managedEndpointArn"></a>
The managed endpoint ARN of the EMR on EKS cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** pythonVirtualEnv **   <a name="datazone-Type-SparkEmrPropertiesInput-pythonVirtualEnv"></a>
The Python virtual env of the Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** runtimeRole **   <a name="datazone-Type-SparkEmrPropertiesInput-runtimeRole"></a>
The runtime role of the Spark EMR.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

 ** trustedCertificatesS3Uri **   <a name="datazone-Type-SparkEmrPropertiesInput-trustedCertificatesS3Uri"></a>
The certificates S3 URI of the Spark EMR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SparkEmrPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SparkEmrPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SparkEmrPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SparkEmrPropertiesInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

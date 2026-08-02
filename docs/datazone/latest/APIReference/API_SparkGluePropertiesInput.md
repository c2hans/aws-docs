---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SparkGluePropertiesInput.html
---

# SparkGluePropertiesInput
<a name="API_SparkGluePropertiesInput"></a>

The Spark AWS Glue properties.

## Contents
<a name="API_SparkGluePropertiesInput_Contents"></a>

 ** additionalArgs **   <a name="datazone-Type-SparkGluePropertiesInput-additionalArgs"></a>
The additional args in the Spark AWS Glue properties.
Type: [SparkGlueArgs](API_SparkGlueArgs.md) object
Required: No

 ** glueConnectionName **   <a name="datazone-Type-SparkGluePropertiesInput-glueConnectionName"></a>
The AWS Glue connection name in the Spark AWS Glue properties. Specify either `glueConnectionName` or `glueConnectionNames`, but not both.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** glueConnectionNames **   <a name="datazone-Type-SparkGluePropertiesInput-glueConnectionNames"></a>
The AWS Glue connection names in the Spark AWS Glue properties. Specify either `glueConnectionName` or `glueConnectionNames`, but not both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** glueVersion **   <a name="datazone-Type-SparkGluePropertiesInput-glueVersion"></a>
The AWS Glue version in the Spark AWS Glue properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** idleTimeout **   <a name="datazone-Type-SparkGluePropertiesInput-idleTimeout"></a>
The idle timeout in the Spark AWS Glue properties.
Type: Integer
Required: No

 ** javaVirtualEnv **   <a name="datazone-Type-SparkGluePropertiesInput-javaVirtualEnv"></a>
The Java virtual env in the Spark AWS Glue properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** numberOfWorkers **   <a name="datazone-Type-SparkGluePropertiesInput-numberOfWorkers"></a>
The number of workers in the Spark AWS Glue properties.
Type: Integer
Required: No

 ** pythonVirtualEnv **   <a name="datazone-Type-SparkGluePropertiesInput-pythonVirtualEnv"></a>
The Python virtual env in the Spark AWS Glue properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** workerType **   <a name="datazone-Type-SparkGluePropertiesInput-workerType"></a>
The worker type in the Spark AWS Glue properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SparkGluePropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SparkGluePropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SparkGluePropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SparkGluePropertiesInput)

---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobTemplateData.html
---

# JobTemplateData
<a name="API_JobTemplateData"></a>

The values of StartJobRun API requests used in job runs started using the job template.

## Contents
<a name="API_JobTemplateData_Contents"></a>

 ** executionRoleArn **   <a name="emroneks-Type-JobTemplateData-executionRoleArn"></a>
The execution role ARN of the job run.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `(^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$)|([\.\-_\#A-Za-z0-9\$\{\}]+)`
Required: Yes

 ** jobDriver **   <a name="emroneks-Type-JobTemplateData-jobDriver"></a>
Specify the driver that the job runs on. Exactly one of the two available job drivers is required, either sparkSqlJobDriver or sparkSubmitJobDriver.
Type: [JobDriver](API_JobDriver.md) object
Required: Yes

 ** releaseLabel **   <a name="emroneks-Type-JobTemplateData-releaseLabel"></a>
 The release version of Amazon EMR.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([\.\-_/A-Za-z0-9]+|\$\{[a-zA-Z]\w*\})`
Required: Yes

 ** configurationOverrides **   <a name="emroneks-Type-JobTemplateData-configurationOverrides"></a>
 The configuration settings that are used to override defaults configuration.
Type: [ParametricConfigurationOverrides](API_ParametricConfigurationOverrides.md) object
Required: No

 ** jobTags **   <a name="emroneks-Type-JobTemplateData-jobTags"></a>
The tags assigned to jobs started using the job template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** parameterConfiguration **   <a name="emroneks-Type-JobTemplateData-parameterConfiguration"></a>
The configuration of parameters existing in the job template.
Type: String to [TemplateParameterConfiguration](API_TemplateParameterConfiguration.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 512.
Key Pattern: `[\.\-_\#A-Za-z0-9]+`
Required: No

## See Also
<a name="API_JobTemplateData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/JobTemplateData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/JobTemplateData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/JobTemplateData)

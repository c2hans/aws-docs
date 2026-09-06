---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JobCommand.html
---

# JobCommand
<a name="API_JobCommand"></a>

Specifies code that runs when a job is run.

## Contents
<a name="API_JobCommand_Contents"></a>

 ** Name **   <a name="Glue-Type-JobCommand-Name"></a>
The name of the job command. For an Apache Spark ETL job, this must be `glueetl`. For a Python shell job, it must be `pythonshell`. For an Apache Spark streaming ETL job, this must be `gluestreaming`. For a Ray job, this must be `glueray`.
Type: String
Required: No

 ** PythonVersion **   <a name="Glue-Type-JobCommand-PythonVersion"></a>
The Python version being used to run a Python shell job. Allowed values are 2 or 3.
Type: String
Pattern: `^([2-3]|3[.]9)$`
Required: No

 ** Runtime **   <a name="Glue-Type-JobCommand-Runtime"></a>
In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment. This field is not used in other job types. For supported runtime environment values, see [Supported Ray runtime environments](https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html) in the AWS Glue Developer Guide.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `.*`
Required: No

 ** ScriptLocation **   <a name="Glue-Type-JobCommand-ScriptLocation"></a>
Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that runs a job.
Type: String
Length Constraints: Maximum length of 400000.
Required: No

## See Also
<a name="API_JobCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JobCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JobCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JobCommand)

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SessionCommand.html
---

# SessionCommand
<a name="API_SessionCommand"></a>

The `SessionCommand` that runs the job.

## Contents
<a name="API_SessionCommand_Contents"></a>

 ** Name **   <a name="Glue-Type-SessionCommand-Name"></a>
Specifies the name of the SessionCommand. Can be 'glueetl' or 'gluestreaming'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PythonVersion **   <a name="Glue-Type-SessionCommand-PythonVersion"></a>
Specifies the Python version. The Python version indicates the version supported for jobs of type Spark.
Type: String
Pattern: `^([2-3]|3[.]9)$`
Required: No

## See Also
<a name="API_SessionCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SessionCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SessionCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SessionCommand)

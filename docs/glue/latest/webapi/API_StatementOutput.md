---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StatementOutput.html
---

# StatementOutput
<a name="API_StatementOutput"></a>

The code execution output in JSON format.

## Contents
<a name="API_StatementOutput_Contents"></a>

 ** Data **   <a name="Glue-Type-StatementOutput-Data"></a>
The code execution output.
Type: [StatementOutputData](API_StatementOutputData.md) object
Required: No

 ** ErrorName **   <a name="Glue-Type-StatementOutput-ErrorName"></a>
The name of the error in the output.
Type: String
Required: No

 ** ErrorValue **   <a name="Glue-Type-StatementOutput-ErrorValue"></a>
The error value of the output.
Type: String
Required: No

 ** ExecutionCount **   <a name="Glue-Type-StatementOutput-ExecutionCount"></a>
The execution count of the output.
Type: Integer
Required: No

 ** Status **   <a name="Glue-Type-StatementOutput-Status"></a>
The status of the code execution output.
Type: String
Valid Values: `WAITING | RUNNING | AVAILABLE | CANCELLING | CANCELLED | ERROR`
Required: No

 ** Traceback **   <a name="Glue-Type-StatementOutput-Traceback"></a>
The traceback of the output.
Type: Array of strings
Required: No

## See Also
<a name="API_StatementOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StatementOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StatementOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StatementOutput)

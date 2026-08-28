---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Processor.html
---

# Processor
<a name="API_Processor"></a>

This structure contains the information about one processor in a log transformer.

## Contents
<a name="API_Processor_Contents"></a>

 ** addKeys **   <a name="CWL-Type-Processor-addKeys"></a>
Use this parameter to include the [ addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys) processor in your transformer.
Type: [AddKeys](API_AddKeys.md) object
Required: No

 ** copyValue **   <a name="CWL-Type-Processor-copyValue"></a>
Use this parameter to include the [ copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copyValue) processor in your transformer.
Type: [CopyValue](API_CopyValue.md) object
Required: No

 ** csv **   <a name="CWL-Type-Processor-csv"></a>
Use this parameter to include the [ CSV](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV) processor in your transformer.
Type: [CSV](API_CSV.md) object
Required: No

 ** dateTimeConverter **   <a name="CWL-Type-Processor-dateTimeConverter"></a>
Use this parameter to include the [ datetimeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-datetimeConverter) processor in your transformer.
Type: [DateTimeConverter](API_DateTimeConverter.md) object
Required: No

 ** deleteKeys **   <a name="CWL-Type-Processor-deleteKeys"></a>
Use this parameter to include the [ deleteKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys) processor in your transformer.
Type: [DeleteKeys](API_DeleteKeys.md) object
Required: No

 ** grok **   <a name="CWL-Type-Processor-grok"></a>
Use this parameter to include the [ grok](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-grok) processor in your transformer.
Type: [Grok](API_Grok.md) object
Required: No

 ** listToMap **   <a name="CWL-Type-Processor-listToMap"></a>
Use this parameter to include the [ listToMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap) processor in your transformer.
Type: [ListToMap](API_ListToMap.md) object
Required: No

 ** lowerCaseString **   <a name="CWL-Type-Processor-lowerCaseString"></a>
Use this parameter to include the [ lowerCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-lowerCaseString) processor in your transformer.
Type: [LowerCaseString](API_LowerCaseString.md) object
Required: No

 ** moveKeys **   <a name="CWL-Type-Processor-moveKeys"></a>
Use this parameter to include the [ moveKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKeys) processor in your transformer.
Type: [MoveKeys](API_MoveKeys.md) object
Required: No

 ** parseCloudfront **   <a name="CWL-Type-Processor-parseCloudfront"></a>
Use this parameter to include the [ parseCloudfront](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseCloudfront) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
Type: [ParseCloudfront](API_ParseCloudfront.md) object
Required: No

 ** parseJSON **   <a name="CWL-Type-Processor-parseJSON"></a>
Use this parameter to include the [ parseJSON](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseJSON) processor in your transformer.
Type: [ParseJSON](API_ParseJSON.md) object
Required: No

 ** parseKeyValue **   <a name="CWL-Type-Processor-parseKeyValue"></a>
Use this parameter to include the [ parseKeyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue) processor in your transformer.
Type: [ParseKeyValue](API_ParseKeyValue.md) object
Required: No

 ** parsePostgres **   <a name="CWL-Type-Processor-parsePostgres"></a>
Use this parameter to include the [ parsePostGres](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
Type: [ParsePostgres](API_ParsePostgres.md) object
Required: No

 ** parseRoute53 **   <a name="CWL-Type-Processor-parseRoute53"></a>
Use this parameter to include the [ parseRoute53](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseRoute53) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
Type: [ParseRoute53](API_ParseRoute53.md) object
Required: No

 ** parseToOCSF **   <a name="CWL-Type-Processor-parseToOCSF"></a>
Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.
Type: [ParseToOCSF](API_ParseToOCSF.md) object
Required: No

 ** parseVPC **   <a name="CWL-Type-Processor-parseVPC"></a>
Use this parameter to include the [ parseVPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
Type: [ParseVPC](API_ParseVPC.md) object
Required: No

 ** parseWAF **   <a name="CWL-Type-Processor-parseWAF"></a>
Use this parameter to include the [ parseWAF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
Type: [ParseWAF](API_ParseWAF.md) object
Required: No

 ** renameKeys **   <a name="CWL-Type-Processor-renameKeys"></a>
Use this parameter to include the [ renameKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys) processor in your transformer.
Type: [RenameKeys](API_RenameKeys.md) object
Required: No

 ** splitString **   <a name="CWL-Type-Processor-splitString"></a>
Use this parameter to include the [ splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString) processor in your transformer.
Type: [SplitString](API_SplitString.md) object
Required: No

 ** substituteString **   <a name="CWL-Type-Processor-substituteString"></a>
Use this parameter to include the [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString) processor in your transformer.
Type: [SubstituteString](API_SubstituteString.md) object
Required: No

 ** trimString **   <a name="CWL-Type-Processor-trimString"></a>
Use this parameter to include the [ trimString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-trimString) processor in your transformer.
Type: [TrimString](API_TrimString.md) object
Required: No

 ** typeConverter **   <a name="CWL-Type-Processor-typeConverter"></a>
Use this parameter to include the [ typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter) processor in your transformer.
Type: [TypeConverter](API_TypeConverter.md) object
Required: No

 ** upperCaseString **   <a name="CWL-Type-Processor-upperCaseString"></a>
Use this parameter to include the [ upperCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-upperCaseString) processor in your transformer.
Type: [UpperCaseString](API_UpperCaseString.md) object
Required: No

## See Also
<a name="API_Processor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Processor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Processor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Processor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

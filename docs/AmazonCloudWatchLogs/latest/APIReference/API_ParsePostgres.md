---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParsePostgres.html
---

# ParsePostgres
<a name="API_ParsePostgres"></a>

Use this processor to parse RDS for PostgreSQL vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message. For more information about this processor including examples, see [ parsePostGres](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres).

For more information about RDS for PostgreSQL log format, see [ RDS for PostgreSQL database log filesTCP flag sequence](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Contents
<a name="API_ParsePostgres_Contents"></a>

 ** source **   <a name="CWL-Type-ParsePostgres-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ParsePostgres_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ParsePostgres)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ParsePostgres)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ParsePostgres)

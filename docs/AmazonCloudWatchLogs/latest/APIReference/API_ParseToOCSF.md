---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParseToOCSF.html
---

# ParseToOCSF
<a name="API_ParseToOCSF"></a>

This processor converts logs into [Open Cybersecurity Schema Framework (OCSF)](https://ocsf.io) events.

For more information about this processor including examples, see [parseToOCSF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseToOCSF) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_ParseToOCSF_Contents"></a>

 ** eventSource **   <a name="CWL-Type-ParseToOCSF-eventSource"></a>
Specify the service or process that produces the log events that will be converted with this processor.
Type: String
Valid Values: `CloudTrail | Route53Resolver | VPCFlow | EKSAudit | AWSWAF`
Required: Yes

 ** ocsfVersion **   <a name="CWL-Type-ParseToOCSF-ocsfVersion"></a>
Specify which version of the OCSF schema to use for the transformed log events.
Type: String
Valid Values: `V1.1 | V1.5`
Required: Yes

 ** mappingVersion **   <a name="CWL-Type-ParseToOCSF-mappingVersion"></a>
The version of the OCSF mapping to use for parsing log data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^\d+\.\d+(\.\d+)?$`
Required: No

 ** source **   <a name="CWL-Type-ParseToOCSF-source"></a>
The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ParseToOCSF_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ParseToOCSF)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ParseToOCSF)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ParseToOCSF)

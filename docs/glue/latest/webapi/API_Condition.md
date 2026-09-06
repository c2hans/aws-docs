---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

Defines a condition under which a trigger fires.

## Contents
<a name="API_Condition_Contents"></a>

 ** CrawlerName **   <a name="Glue-Type-Condition-CrawlerName"></a>
The name of the crawler to which this condition applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CrawlState **   <a name="Glue-Type-Condition-CrawlState"></a>
The state of the crawler to which this condition applies.
Type: String
Valid Values: `RUNNING | CANCELLING | CANCELLED | SUCCEEDED | FAILED | ERROR`
Required: No

 ** JobName **   <a name="Glue-Type-Condition-JobName"></a>
The name of the job whose `JobRuns` this condition applies to, and on which this trigger waits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LogicalOperator **   <a name="Glue-Type-Condition-LogicalOperator"></a>
A logical operator.
Type: String
Valid Values: `EQUALS`
Required: No

 ** State **   <a name="Glue-Type-Condition-State"></a>
The condition state. Currently, the only job states that a trigger can listen for are `SUCCEEDED`, `STOPPED`, `FAILED`, and `TIMEOUT`. The only crawler states that a trigger can listen for are `SUCCEEDED`, `FAILED`, and `CANCELLED`.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT | ERROR | WAITING | EXPIRED`
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Condition)

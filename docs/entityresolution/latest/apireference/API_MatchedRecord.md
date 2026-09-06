---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_MatchedRecord.html
---

# MatchedRecord
<a name="API_MatchedRecord"></a>

 The matched record.

## Contents
<a name="API_MatchedRecord_Contents"></a>

 ** inputSourceARN **   <a name="API-Type-MatchedRecord-inputSourceARN"></a>
 The input source ARN of the matched record.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** recordId **   <a name="API-Type-MatchedRecord-recordId"></a>
 The record ID of the matched record.
Type: String
Required: Yes

## See Also
<a name="API_MatchedRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/MatchedRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/MatchedRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/MatchedRecord)

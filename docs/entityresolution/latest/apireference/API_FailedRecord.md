---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_FailedRecord.html
---

# FailedRecord
<a name="API_FailedRecord"></a>

The record that didn't generate a Match ID.

## Contents
<a name="API_FailedRecord_Contents"></a>

 ** errorMessage **   <a name="API-Type-FailedRecord-errorMessage"></a>
 The error message for the record that didn't generate a Match ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** inputSourceARN **   <a name="API-Type-FailedRecord-inputSourceARN"></a>
 The input source ARN of the record that didn't generate a Match ID.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** uniqueId **   <a name="API-Type-FailedRecord-uniqueId"></a>
 The unique ID of the record that didn't generate a Match ID.
Type: String
Required: Yes

## See Also
<a name="API_FailedRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/FailedRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/FailedRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/FailedRecord)

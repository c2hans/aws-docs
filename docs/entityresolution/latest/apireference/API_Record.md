---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Record.html
---

# Record
<a name="API_Record"></a>

 The record.

## Contents
<a name="API_Record_Contents"></a>

 ** inputSourceARN **   <a name="API-Type-Record-inputSourceARN"></a>
 The input source ARN of the record.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** recordAttributeMap **   <a name="API-Type-Record-recordAttributeMap"></a>
 The record's attribute map.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 255.
Value Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** uniqueId **   <a name="API-Type-Record-uniqueId"></a>
 The unique ID of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 38.
Pattern: `[a-zA-Z0-9_-]*`
Required: Yes

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/Record)

---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DataAccessTarget.html
---

# DataAccessTarget
<a name="API_DataAccessTarget"></a>

One requested scope: an explicit list of actions for one service. All actions in an entry share one service prefix. The same service may appear in more than one entry.

## Contents
<a name="API_DataAccessTarget_Contents"></a>

 ** actions **   <a name="cloudwatchomni-Type-DataAccessTarget-actions"></a>
The actions of one service, each with its service prefix, for example "logs:StartQuery".
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-z0-9][a-z0-9-]*:[A-Za-z][A-Za-z0-9]*`
Required: Yes

## See Also
<a name="API_DataAccessTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/DataAccessTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/DataAccessTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/DataAccessTarget)

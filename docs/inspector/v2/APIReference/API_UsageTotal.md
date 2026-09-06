---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UsageTotal.html
---

# UsageTotal
<a name="API_UsageTotal"></a>

The total of usage for an account ID.

## Contents
<a name="API_UsageTotal_Contents"></a>

 ** accountId **   <a name="inspector2-Type-UsageTotal-accountId"></a>
The account ID of the account that usage data was retrieved for.
Type: String
Pattern: `.*[0-9]{12}.*`
Required: No

 ** usage **   <a name="inspector2-Type-UsageTotal-usage"></a>
An object representing the total usage for an account.
Type: Array of [Usage](API_Usage.md) objects
Required: No

## See Also
<a name="API_UsageTotal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UsageTotal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UsageTotal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UsageTotal)

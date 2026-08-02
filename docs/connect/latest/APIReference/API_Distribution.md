---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Distribution.html
---

# Distribution
<a name="API_Distribution"></a>

Information about a traffic distribution.

## Contents
<a name="API_Distribution_Contents"></a>

 ** Percentage **   <a name="connect-Type-Distribution-Percentage"></a>
The percentage of the traffic that is distributed, in increments of 10.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** Region **   <a name="connect-Type-Distribution-Region"></a>
The AWS Region where the traffic is distributed.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: Yes

## See Also
<a name="API_Distribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Distribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Distribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Distribution)

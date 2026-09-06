---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PatternToken.html
---

# PatternToken
<a name="API_PatternToken"></a>

A structure that contains information about one pattern token related to an anomaly.

For more information about patterns and tokens, see [CreateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.html).

## Contents
<a name="API_PatternToken_Contents"></a>

 ** dynamicTokenPosition **   <a name="CWL-Type-PatternToken-dynamicTokenPosition"></a>
For a dynamic token, this indicates where in the pattern that this token appears, related to other dynamic tokens. The dynamic token that appears first has a value of `1`, the one that appears second is `2`, and so on.
Type: Integer
Required: No

 ** enumerations **   <a name="CWL-Type-PatternToken-enumerations"></a>
Contains the values found for a dynamic token, and the number of times each value was found.
Type: String to long map
Key Length Constraints: Minimum length of 1.
Required: No

 ** inferredTokenName **   <a name="CWL-Type-PatternToken-inferredTokenName"></a>
A name that CloudWatch Logs assigned to this dynamic token to make the pattern more readable. The string part of the `inferredTokenName` gives you a clearer idea of the content of this token. The number part of the `inferredTokenName` shows where in the pattern this token appears, compared to other dynamic tokens. CloudWatch Logs assigns the string part of the name based on analyzing the content of the log events that contain it.
For example, an inferred token name of `IPAddress-3` means that the token represents an IP address, and this token is the third dynamic token in the pattern.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** isDynamic **   <a name="CWL-Type-PatternToken-isDynamic"></a>
Specifies whether this is a dynamic token.
Type: Boolean
Required: No

 ** tokenString **   <a name="CWL-Type-PatternToken-tokenString"></a>
The string represented by this token. If this is a dynamic token, the value will be `<*>`
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_PatternToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PatternToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PatternToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PatternToken)

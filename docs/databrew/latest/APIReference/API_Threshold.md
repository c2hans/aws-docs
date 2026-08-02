---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Threshold.html
---

# Threshold
<a name="API_Threshold"></a>

The threshold used with a non-aggregate check expression. The non-aggregate check expression will be applied to each row in a specific column. Then the threshold will be used to determine whether the validation succeeds.

## Contents
<a name="API_Threshold_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Value **   <a name="databrew-Type-Threshold-Value"></a>
The value of a threshold.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** Type **   <a name="databrew-Type-Threshold-Type"></a>
The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.
Type: String
Valid Values: `GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | GREATER_THAN | LESS_THAN`
Required: No

 ** Unit **   <a name="databrew-Type-Threshold-Unit"></a>
Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.
Type: String
Valid Values: `COUNT | PERCENTAGE`
Required: No

## See Also
<a name="API_Threshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Threshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Threshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Threshold)

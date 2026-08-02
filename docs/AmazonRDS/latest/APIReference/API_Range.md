---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Range.html
---

# Range
<a name="API_Range"></a>

A range of integer values.

## Contents
<a name="API_Range_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** From **
The minimum value in the range.
Type: Integer
Required: No

 ** Step **
The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isn't a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000...
Type: Integer
Required: No

 ** To **
The maximum value in the range.
Type: Integer
Required: No

## See Also
<a name="API_Range_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Range)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Range)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Range)

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Spigot.html
---

# Spigot
<a name="API_Spigot"></a>

Specifies a transform that writes samples of the data to an Amazon S3 bucket.

## Contents
<a name="API_Spigot_Contents"></a>

 ** Inputs **   <a name="Glue-Type-Spigot-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Spigot-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Path **   <a name="Glue-Type-Spigot-Path"></a>
A path in Amazon S3 where the transform will write a subset of records from the dataset to a JSON file in an Amazon S3 bucket.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Prob **   <a name="Glue-Type-Spigot-Prob"></a>
The probability (a decimal value with a maximum value of 1) of picking any given record. A value of 1 indicates that each row read from the dataset should be included in the sample output.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Topk **   <a name="Glue-Type-Spigot-Topk"></a>
Specifies a number of records to write starting from the beginning of the dataset.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_Spigot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Spigot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Spigot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Spigot)

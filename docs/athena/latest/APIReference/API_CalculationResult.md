---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CalculationResult.html
---

# CalculationResult
<a name="API_CalculationResult"></a>

Contains information about an application-specific calculation result.

## Contents
<a name="API_CalculationResult_Contents"></a>

 ** ResultS3Uri **   <a name="athena-Type-CalculationResult-ResultS3Uri"></a>
The Amazon S3 location of the folder for the calculation results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(https|s3|S3)://([^/]+)/?(.*)$`
Required: No

 ** ResultType **   <a name="athena-Type-CalculationResult-ResultType"></a>
The data format of the calculation result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\w+\/[-+.\w]+`
Required: No

 ** StdErrorS3Uri **   <a name="athena-Type-CalculationResult-StdErrorS3Uri"></a>
The Amazon S3 location of the `stderr` error messages file for the calculation.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(https|s3|S3)://([^/]+)/?(.*)$`
Required: No

 ** StdOutS3Uri **   <a name="athena-Type-CalculationResult-StdOutS3Uri"></a>
The Amazon S3 location of the `stdout` file for the calculation.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(https|s3|S3)://([^/]+)/?(.*)$`
Required: No

## See Also
<a name="API_CalculationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CalculationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CalculationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CalculationResult)

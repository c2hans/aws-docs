---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsLambdaLayerVersionDetails.html
---

# AwsLambdaLayerVersionDetails
<a name="API_AwsLambdaLayerVersionDetails"></a>

Details about a Lambda layer version.

## Contents
<a name="API_AwsLambdaLayerVersionDetails_Contents"></a>

 ** CompatibleRuntimes **   <a name="securityhub-Type-AwsLambdaLayerVersionDetails-CompatibleRuntimes"></a>
The layer's compatible [function runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).
The following list includes deprecated runtimes. For more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy) in the * AWS Lambda Developer Guide*.
Array Members: Maximum number of 5 items.
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CreatedDate **   <a name="securityhub-Type-AwsLambdaLayerVersionDetails-CreatedDate"></a>
Indicates when the version was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsLambdaLayerVersionDetails-Version"></a>
The version number.
Type: Long
Required: No

## See Also
<a name="API_AwsLambdaLayerVersionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsLambdaLayerVersionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsLambdaLayerVersionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsLambdaLayerVersionDetails)

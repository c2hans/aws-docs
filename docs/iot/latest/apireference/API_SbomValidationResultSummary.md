---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SbomValidationResultSummary.html
---

# SbomValidationResultSummary
<a name="API_SbomValidationResultSummary"></a>

A summary of the validation results for a specific software bill of materials (SBOM) attached to a software package version.

## Contents
<a name="API_SbomValidationResultSummary_Contents"></a>

 ** errorCode **   <a name="iot-Type-SbomValidationResultSummary-errorCode"></a>
The `errorCode` representing the validation failure error if the SBOM validation failed.
Type: String
Valid Values: `INCOMPATIBLE_FORMAT | FILE_SIZE_LIMIT_EXCEEDED`
Required: No

 ** errorMessage **   <a name="iot-Type-SbomValidationResultSummary-errorMessage"></a>
The `errorMessage` representing the validation failure error if the SBOM validation failed.
Type: String
Required: No

 ** fileName **   <a name="iot-Type-SbomValidationResultSummary-fileName"></a>
The name of the SBOM file.
Type: String
Required: No

 ** validationResult **   <a name="iot-Type-SbomValidationResultSummary-validationResult"></a>
The end result of the SBOM validation.
Type: String
Valid Values: `FAILED | SUCCEEDED`
Required: No

## See Also
<a name="API_SbomValidationResultSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SbomValidationResultSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SbomValidationResultSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SbomValidationResultSummary)

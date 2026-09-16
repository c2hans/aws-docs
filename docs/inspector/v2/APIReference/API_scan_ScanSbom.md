---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_scan_ScanSbom.html
---

# ScanSbom
<a name="API_scan_ScanSbom"></a>

 Scans a provided CycloneDX 1.5 SBOM and reports on any discovered vulnerabilities. You can generate compatible SBOMs for resources using the [Amazon Inspector SBOM generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html).

 The output of this action reports NVD and CVSS scores when NVD and CVSS scores are available. Because the output reports both scores, you might notice a discrepency between them. However, you can triage the severity of either score depending on your chosen vendor.

**Note**
 This action supports a maximum of 5,000 components per request and supports a maximum response size of 10MB (compressed or uncompressed).

 For information about the operating systems this API supports, see [Supported operating systems: Amazon Inspector Scans](https://docs.aws.amazon.com/inspector/latest/user/supported.html#supported-os) in the *Amazon Inspector User Guide*.

## Request Syntax
<a name="API_scan_ScanSbom_RequestSyntax"></a>

```
POST /scan/sbom HTTP/1.1
Content-type: application/json

{
   "outputFormat": "{{string}}",
   "sbom": {{JSON value}}
}
```

## URI Request Parameters
<a name="API_scan_ScanSbom_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_scan_ScanSbom_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [outputFormat](#API_scan_ScanSbom_RequestSyntax) **   <a name="inspector2-scan_ScanSbom-request-outputFormat"></a>
The output format for the vulnerability report.
Type: String
Valid Values: `CYCLONE_DX_1_5 | INSPECTOR | INSPECTOR_ALT`
Required: No

 ** [sbom](#API_scan_ScanSbom_RequestSyntax) **   <a name="inspector2-scan_ScanSbom-request-sbom"></a>
The JSON file for the SBOM you want to scan. The SBOM must be in CycloneDX 1.5 format. This format limits you to passing 5000 components before throwing a `ValidException` error.
Type: JSON value
Required: Yes

## Response Syntax
<a name="API_scan_ScanSbom_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sbom": JSON value
}
```

## Response Elements
<a name="API_scan_ScanSbom_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sbom](#API_scan_ScanSbom_ResponseSyntax) **   <a name="inspector2-scan_ScanSbom-response-sbom"></a>
The vulnerability report for the scanned SBOM.
Type: JSON value

## Errors
<a name="API_scan_ScanSbom_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** reason **
The reason for the validation failure.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_scan_ScanSbom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector-scan-2023-08-08/ScanSbom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-scan-2023-08-08/ScanSbom)

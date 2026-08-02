---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetCredentialReport.html
---

# GetCredentialReport
<a name="API_GetCredentialReport"></a>

 Retrieves a credential report for the AWS account. For more information about the credential report, see [Getting credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html) in the *IAM User Guide*.

## Response Elements
<a name="API_GetCredentialReport_ResponseElements"></a>

The following elements are returned by the service.

 ** Content **
Contains the credential report. The report is Base64-encoded.
Type: Base64-encoded binary data object

 ** GeneratedTime **
 The date and time when the credential report was created, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601).
Type: Timestamp

 ** ReportFormat **
The format (MIME type) of the credential report.
Type: String
Valid Values: `text/csv`

## Errors
<a name="API_GetCredentialReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReportExpired **
The request was rejected because the most recent credential report has expired. To generate a new credential report, use [GenerateCredentialReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html). For more information about credential report expiration, see [Getting credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html) in the *IAM User Guide*.
HTTP Status Code: 410

 ** ReportInProgress **
The request was rejected because the credential report is still being generated.
HTTP Status Code: 404

 ** ReportNotPresent **
The request was rejected because the credential report does not exist. To generate a credential report, use [GenerateCredentialReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html).
HTTP Status Code: 410

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetCredentialReport_Examples"></a>

### Example
<a name="API_GetCredentialReport_Example_1"></a>

This example illustrates one usage of GetCredentialReport.

#### Sample Request
<a name="API_GetCredentialReport_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetCredentialReport
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCredentialReport_Example_1_Response"></a>

```
<GetCredentialReportResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<GetCredentialReportResult>
  <Content>BASE-64 ENCODED FILE CONTENTS</Content>
  <ReportFormat>text/csv</ReportFormat>
  <GeneratedTime>2014-08-28T21:42:50Z</GeneratedTime>
</GetCredentialReportResult>
<ResponseMetadata>
  <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</GetCredentialReportResponse>
```

## See Also
<a name="API_GetCredentialReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetCredentialReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetCredentialReport)

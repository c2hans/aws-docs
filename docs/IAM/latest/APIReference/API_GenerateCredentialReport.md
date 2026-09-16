---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html
---

# GenerateCredentialReport
<a name="API_GenerateCredentialReport"></a>

 Generates a credential report for the AWS account. For more information about the credential report, see [Getting credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html) in the *IAM User Guide*.

## Response Elements
<a name="API_GenerateCredentialReport_ResponseElements"></a>

The following elements are returned by the service.

 ** Description **
Information about the credential report.
Type: String

 ** State **
Information about the state of the credential report.
Type: String
Valid Values: `STARTED | INPROGRESS | COMPLETE`

## Errors
<a name="API_GenerateCredentialReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GenerateCredentialReport_Examples"></a>

### Example
<a name="API_GenerateCredentialReport_Example_1"></a>

This example illustrates one usage of GenerateCredentialReport.

#### Sample Request
<a name="API_GenerateCredentialReport_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GenerateCredentialReport
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GenerateCredentialReport_Example_1_Response"></a>

```
<GenerateCredentialReportResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GenerateCredentialReportResult>
    <Description>No report exists. Starting a new report generation task</Description>
    <State>STARTED</State>
  </GenerateCredentialReportResult>
  <ResponseMetadata>
    <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</GenerateCredentialReportResponse>
```

## See Also
<a name="API_GenerateCredentialReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GenerateCredentialReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GenerateCredentialReport)

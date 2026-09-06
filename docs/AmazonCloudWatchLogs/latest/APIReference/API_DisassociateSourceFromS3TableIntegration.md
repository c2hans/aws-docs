---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DisassociateSourceFromS3TableIntegration.html
---

# DisassociateSourceFromS3TableIntegration
<a name="API_DisassociateSourceFromS3TableIntegration"></a>

Disassociates a data source from an S3 Table Integration, removing query access and deleting all associated data from the integration.

## Request Syntax
<a name="API_DisassociateSourceFromS3TableIntegration_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateSourceFromS3TableIntegration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_DisassociateSourceFromS3TableIntegration_RequestSyntax) **   <a name="CWL-DisassociateSourceFromS3TableIntegration-request-identifier"></a>
The unique identifier of the association to remove between the data source and S3 Table Integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_DisassociateSourceFromS3TableIntegration_ResponseSyntax"></a>

```
{
   "identifier": "string"
}
```

## Response Elements
<a name="API_DisassociateSourceFromS3TableIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [identifier](#API_DisassociateSourceFromS3TableIntegration_ResponseSyntax) **   <a name="CWL-DisassociateSourceFromS3TableIntegration-response-identifier"></a>
The unique identifier of the association that was removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DisassociateSourceFromS3TableIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateSourceFromS3TableIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DisassociateSourceFromS3TableIntegration)

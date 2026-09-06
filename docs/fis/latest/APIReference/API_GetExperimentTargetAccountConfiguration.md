---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperimentTargetAccountConfiguration.html
---

# GetExperimentTargetAccountConfiguration
<a name="API_GetExperimentTargetAccountConfiguration"></a>

Gets information about the specified target account configuration of the experiment.

## Request Syntax
<a name="API_GetExperimentTargetAccountConfiguration_RequestSyntax"></a>

```
GET /experiments/{{id}}/targetAccountConfigurations/{{accountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetExperimentTargetAccountConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_GetExperimentTargetAccountConfiguration_RequestSyntax) **   <a name="fis-GetExperimentTargetAccountConfiguration-request-uri-accountId"></a>
The AWS account ID of the target account.
Length Constraints: Minimum length of 12. Maximum length of 48.
Pattern: `[\S]+`
Required: Yes

 ** [id](#API_GetExperimentTargetAccountConfiguration_RequestSyntax) **   <a name="fis-GetExperimentTargetAccountConfiguration-request-uri-experimentId"></a>
The ID of the experiment.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_GetExperimentTargetAccountConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExperimentTargetAccountConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "targetAccountConfiguration": {
      "accountId": "string",
      "description": "string",
      "roleArn": "string"
   }
}
```

## Response Elements
<a name="API_GetExperimentTargetAccountConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [targetAccountConfiguration](#API_GetExperimentTargetAccountConfiguration_ResponseSyntax) **   <a name="fis-GetExperimentTargetAccountConfiguration-response-targetAccountConfiguration"></a>
Information about the target account configuration.
Type: [ExperimentTargetAccountConfiguration](API_ExperimentTargetAccountConfiguration.md) object

## Errors
<a name="API_GetExperimentTargetAccountConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_GetExperimentTargetAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/GetExperimentTargetAccountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/GetExperimentTargetAccountConfiguration)

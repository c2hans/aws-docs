---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTargetAccountConfigurations.html
---

# ListExperimentTargetAccountConfigurations
<a name="API_ListExperimentTargetAccountConfigurations"></a>

Lists the target account configurations of the specified experiment.

## Request Syntax
<a name="API_ListExperimentTargetAccountConfigurations_RequestSyntax"></a>

```
GET /experiments/{{id}}/targetAccountConfigurations?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExperimentTargetAccountConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListExperimentTargetAccountConfigurations_RequestSyntax) **   <a name="fis-ListExperimentTargetAccountConfigurations-request-uri-experimentId"></a>
The ID of the experiment.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

 ** [nextToken](#API_ListExperimentTargetAccountConfigurations_RequestSyntax) **   <a name="fis-ListExperimentTargetAccountConfigurations-request-uri-nextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`

## Request Body
<a name="API_ListExperimentTargetAccountConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExperimentTargetAccountConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "targetAccountConfigurations": [
      {
         "accountId": "string",
         "description": "string",
         "roleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListExperimentTargetAccountConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListExperimentTargetAccountConfigurations_ResponseSyntax) **   <a name="fis-ListExperimentTargetAccountConfigurations-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`

 ** [targetAccountConfigurations](#API_ListExperimentTargetAccountConfigurations_ResponseSyntax) **   <a name="fis-ListExperimentTargetAccountConfigurations-response-targetAccountConfigurations"></a>
The target account configurations.
Type: Array of [ExperimentTargetAccountConfigurationSummary](API_ExperimentTargetAccountConfigurationSummary.md) objects

## Errors
<a name="API_ListExperimentTargetAccountConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_ListExperimentTargetAccountConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/ListExperimentTargetAccountConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ListExperimentTargetAccountConfigurations)

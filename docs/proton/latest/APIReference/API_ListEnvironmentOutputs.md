---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentOutputs.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListEnvironmentOutputs
<a name="API_ListEnvironmentOutputs"></a>

List the infrastructure as code outputs for your environment.

## Request Syntax
<a name="API_ListEnvironmentOutputs_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "environmentName": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEnvironmentOutputs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_ListEnvironmentOutputs_RequestSyntax) **   <a name="proton-ListEnvironmentOutputs-request-deploymentId"></a>
The ID of the deployment whose outputs you want.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [environmentName](#API_ListEnvironmentOutputs_RequestSyntax) **   <a name="proton-ListEnvironmentOutputs-request-environmentName"></a>
The environment name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [nextToken](#API_ListEnvironmentOutputs_RequestSyntax) **   <a name="proton-ListEnvironmentOutputs-request-nextToken"></a>
A token that indicates the location of the next environment output in the array of environment outputs, after the list of environment outputs that was previously requested.
Type: String
Length Constraints: Fixed length of 0.
Required: No

## Response Syntax
<a name="API_ListEnvironmentOutputs_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "outputs": [
      {
         "key": "string",
         "valueString": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListEnvironmentOutputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListEnvironmentOutputs_ResponseSyntax) **   <a name="proton-ListEnvironmentOutputs-response-nextToken"></a>
A token that indicates the location of the next environment output in the array of environment outputs, after the current requested list of environment outputs.
Type: String
Length Constraints: Fixed length of 0.

 ** [outputs](#API_ListEnvironmentOutputs_ResponseSyntax) **   <a name="proton-ListEnvironmentOutputs-response-outputs"></a>
An array of environment outputs with detail data.
Type: Array of [Output](API_Output.md) objects

## Errors
<a name="API_ListEnvironmentOutputs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentOutputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListEnvironmentOutputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListEnvironmentOutputs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponentOutputs.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListComponentOutputs
<a name="API_ListComponentOutputs"></a>

Get a list of component Infrastructure as Code (IaC) outputs.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_ListComponentOutputs_RequestSyntax"></a>

```
{
   "componentName": "{{string}}",
   "deploymentId": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListComponentOutputs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [componentName](#API_ListComponentOutputs_RequestSyntax) **   <a name="proton-ListComponentOutputs-request-componentName"></a>
The name of the component whose outputs you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [deploymentId](#API_ListComponentOutputs_RequestSyntax) **   <a name="proton-ListComponentOutputs-request-deploymentId"></a>
The ID of the deployment whose outputs you want.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [nextToken](#API_ListComponentOutputs_RequestSyntax) **   <a name="proton-ListComponentOutputs-request-nextToken"></a>
A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.
Type: String
Length Constraints: Fixed length of 0.
Required: No

## Response Syntax
<a name="API_ListComponentOutputs_ResponseSyntax"></a>

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
<a name="API_ListComponentOutputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListComponentOutputs_ResponseSyntax) **   <a name="proton-ListComponentOutputs-response-nextToken"></a>
A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.
Type: String
Length Constraints: Fixed length of 0.

 ** [outputs](#API_ListComponentOutputs_ResponseSyntax) **   <a name="proton-ListComponentOutputs-response-outputs"></a>
An array of component Infrastructure as Code (IaC) outputs.
Type: Array of [Output](API_Output.md) objects

## Errors
<a name="API_ListComponentOutputs_Errors"></a>

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
<a name="API_ListComponentOutputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListComponentOutputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListComponentOutputs)

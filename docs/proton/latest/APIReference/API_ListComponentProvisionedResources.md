---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponentProvisionedResources.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListComponentProvisionedResources
<a name="API_ListComponentProvisionedResources"></a>

List provisioned resources for a component with details.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_ListComponentProvisionedResources_RequestSyntax"></a>

```
{
   "componentName": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListComponentProvisionedResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [componentName](#API_ListComponentProvisionedResources_RequestSyntax) **   <a name="proton-ListComponentProvisionedResources-request-componentName"></a>
The name of the component whose provisioned resources you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [nextToken](#API_ListComponentProvisionedResources_RequestSyntax) **   <a name="proton-ListComponentProvisionedResources-request-nextToken"></a>
A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.
Type: String
Length Constraints: Fixed length of 0.
Required: No

## Response Syntax
<a name="API_ListComponentProvisionedResources_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "provisionedResources": [
      {
         "identifier": "string",
         "name": "string",
         "provisioningEngine": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListComponentProvisionedResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListComponentProvisionedResources_ResponseSyntax) **   <a name="proton-ListComponentProvisionedResources-response-nextToken"></a>
A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the current requested list of provisioned resources.
Type: String
Length Constraints: Fixed length of 0.

 ** [provisionedResources](#API_ListComponentProvisionedResources_ResponseSyntax) **   <a name="proton-ListComponentProvisionedResources-response-provisionedResources"></a>
An array of provisioned resources for a component.
Type: Array of [ProvisionedResource](API_ProvisionedResource.md) objects

## Errors
<a name="API_ListComponentProvisionedResources_Errors"></a>

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
<a name="API_ListComponentProvisionedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListComponentProvisionedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListComponentProvisionedResources)

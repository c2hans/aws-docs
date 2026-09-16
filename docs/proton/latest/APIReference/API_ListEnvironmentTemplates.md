---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentTemplates.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListEnvironmentTemplates
<a name="API_ListEnvironmentTemplates"></a>

List environment templates.

## Request Syntax
<a name="API_ListEnvironmentTemplates_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEnvironmentTemplates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListEnvironmentTemplates_RequestSyntax) **   <a name="proton-ListEnvironmentTemplates-request-maxResults"></a>
The maximum number of environment templates to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnvironmentTemplates_RequestSyntax) **   <a name="proton-ListEnvironmentTemplates-request-nextToken"></a>
A token that indicates the location of the next environment template in the array of environment templates, after the list of environment templates that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

## Response Syntax
<a name="API_ListEnvironmentTemplates_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "templates": [
      {
         "arn": "string",
         "createdAt": number,
         "description": "string",
         "displayName": "string",
         "lastModifiedAt": number,
         "name": "string",
         "provisioning": "string",
         "recommendedVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListEnvironmentTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListEnvironmentTemplates_ResponseSyntax) **   <a name="proton-ListEnvironmentTemplates-response-nextToken"></a>
A token that indicates the location of the next environment template in the array of environment templates, after the current requested list of environment templates.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

 ** [templates](#API_ListEnvironmentTemplates_ResponseSyntax) **   <a name="proton-ListEnvironmentTemplates-response-templates"></a>
An array of environment templates with detail data.
Type: Array of [EnvironmentTemplateSummary](API_EnvironmentTemplateSummary.md) objects

## Errors
<a name="API_ListEnvironmentTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListEnvironmentTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListEnvironmentTemplates)

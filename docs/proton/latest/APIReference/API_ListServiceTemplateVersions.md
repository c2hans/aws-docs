---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceTemplateVersions.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListServiceTemplateVersions
<a name="API_ListServiceTemplateVersions"></a>

List major or minor versions of a service template with detail data.

## Request Syntax
<a name="API_ListServiceTemplateVersions_RequestSyntax"></a>

```
{
   "majorVersion": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServiceTemplateVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [majorVersion](#API_ListServiceTemplateVersions_RequestSyntax) **   <a name="proton-ListServiceTemplateVersions-request-majorVersion"></a>
To view a list of minor of versions under a major version of a service template, include `major Version`.
To view a list of major versions of a service template, *exclude* `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [maxResults](#API_ListServiceTemplateVersions_RequestSyntax) **   <a name="proton-ListServiceTemplateVersions-request-maxResults"></a>
The maximum number of major or minor versions of a service template to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListServiceTemplateVersions_RequestSyntax) **   <a name="proton-ListServiceTemplateVersions-request-nextToken"></a>
A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the list of major or minor versions that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

 ** [templateName](#API_ListServiceTemplateVersions_RequestSyntax) **   <a name="proton-ListServiceTemplateVersions-request-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListServiceTemplateVersions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "templateVersions": [
      {
         "arn": "string",
         "createdAt": number,
         "description": "string",
         "lastModifiedAt": number,
         "majorVersion": "string",
         "minorVersion": "string",
         "recommendedMinorVersion": "string",
         "status": "string",
         "statusMessage": "string",
         "templateName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceTemplateVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServiceTemplateVersions_ResponseSyntax) **   <a name="proton-ListServiceTemplateVersions-response-nextToken"></a>
A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the current requested list of service major or minor versions.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

 ** [templateVersions](#API_ListServiceTemplateVersions_ResponseSyntax) **   <a name="proton-ListServiceTemplateVersions-response-templateVersions"></a>
An array of major or minor versions of a service template with detail data.
Type: Array of [ServiceTemplateVersionSummary](API_ServiceTemplateVersionSummary.md) objects

## Errors
<a name="API_ListServiceTemplateVersions_Errors"></a>

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
<a name="API_ListServiceTemplateVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListServiceTemplateVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListServiceTemplateVersions)

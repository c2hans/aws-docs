---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

Modifies the definition of an existing DataBrew project.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
PUT /projects/{{name}} HTTP/1.1
Content-type: application/json

{
   "RoleArn": "{{string}}",
   "Sample": {
      "Size": {{number}},
      "Type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateProject_RequestSyntax) **   <a name="databrew-UpdateProject-request-uri-Name"></a>
The name of the project to be updated.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_UpdateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RoleArn](#API_UpdateProject_RequestSyntax) **   <a name="databrew-UpdateProject-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [Sample](#API_UpdateProject_RequestSyntax) **   <a name="databrew-UpdateProject-request-Sample"></a>
Represents the sample size and sampling type for DataBrew to use for interactive data analysis.
Type: [Sample](API_Sample.md) object
Required: No

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastModifiedDate": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateProject_ResponseSyntax) **   <a name="databrew-UpdateProject-response-Name"></a>
The name of the project that you updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LastModifiedDate](#API_UpdateProject_ResponseSyntax) **   <a name="databrew-UpdateProject-response-LastModifiedDate"></a>
The date and time that the project was last modified.
Type: Timestamp

## Errors
<a name="API_UpdateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateProject)

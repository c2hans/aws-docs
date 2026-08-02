---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateProject.html
---

# CreateProject
<a name="API_CreateProject"></a>

Creates a new DataBrew project.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
POST /projects HTTP/1.1
Content-type: application/json

{
   "DatasetName": "{{string}}",
   "Name": "{{string}}",
   "RecipeName": "{{string}}",
   "RoleArn": "{{string}}",
   "Sample": {
      "Size": {{number}},
      "Type": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DatasetName](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-DatasetName"></a>
The name of an existing dataset to associate this project with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Name](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-Name"></a>
A unique name for the new project. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [RecipeName](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-RecipeName"></a>
The name of an existing recipe to associate with the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [RoleArn](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed for this request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [Sample](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-Sample"></a>
Represents the sample size and sampling type for DataBrew to use for interactive data analysis.
Type: [Sample](API_Sample.md) object
Required: No

 ** [Tags](#API_CreateProject_RequestSyntax) **   <a name="databrew-CreateProject-request-Tags"></a>
Metadata tags to apply to this project.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateProject_ResponseSyntax) **   <a name="databrew-CreateProject-response-Name"></a>
The name of the project that you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An internal service failure occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateProject)

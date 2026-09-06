---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html
---

# CreateProject
<a name="API_CreateProject"></a>

Creates a new Amazon Rekognition project. A project is a group of resources (datasets, model versions) that you use to create and manage a Amazon Rekognition Custom Labels Model or custom adapter. You can specify a feature to create the project with, if no feature is specified then Custom Labels is used by default. For adapters, you can also choose whether or not to have the project auto update by using the AutoUpdate argument. This operation requires permissions to perform the `rekognition:CreateProject` action.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
{
   "AutoUpdate": "{{string}}",
   "Feature": "{{string}}",
   "ProjectName": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoUpdate](#API_CreateProject_RequestSyntax) **   <a name="rekognition-CreateProject-request-AutoUpdate"></a>
Specifies whether automatic retraining should be attempted for the versions of the project. Automatic retraining is done as a best effort. Required argument for Content Moderation. Applicable only to adapters.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Feature](#API_CreateProject_RequestSyntax) **   <a name="rekognition-CreateProject-request-Feature"></a>
Specifies feature that is being customized. If no value is provided CUSTOM\_LABELS is used as a default.
Type: String
Valid Values: `CONTENT_MODERATION | CUSTOM_LABELS`
Required: No

 ** [ProjectName](#API_CreateProject_RequestSyntax) **   <a name="rekognition-CreateProject-request-ProjectName"></a>
The name of the project to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [Tags](#API_CreateProject_RequestSyntax) **   <a name="rekognition-CreateProject-request-Tags"></a>
A set of tags (key-value pairs) that you want to attach to the project.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
{
   "ProjectArn": "string"
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProjectArn](#API_CreateProject_ResponseSyntax) **   <a name="rekognition-CreateProject-response-ProjectArn"></a>
The Amazon Resource Name (ARN) of the new project. You can use the ARN to configure IAM access to the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`

## Errors
<a name="API_CreateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is already being used.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateProject)

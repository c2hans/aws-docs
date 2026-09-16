---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DescribeProject.html
---

# DescribeProject
<a name="API_DescribeProject"></a>

Returns the definition of a specific DataBrew project.

## Request Syntax
<a name="API_DescribeProject_RequestSyntax"></a>

```
GET /projects/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeProject_RequestSyntax) **   <a name="databrew-DescribeProject-request-uri-Name"></a>
The name of the project to be described.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_DescribeProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": number,
   "CreatedBy": "string",
   "DatasetName": "string",
   "LastModifiedBy": "string",
   "LastModifiedDate": number,
   "Name": "string",
   "OpenDate": number,
   "OpenedBy": "string",
   "RecipeName": "string",
   "ResourceArn": "string",
   "RoleArn": "string",
   "Sample": {
      "Size": number,
      "Type": "string"
   },
   "SessionStatus": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-Name"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreateDate](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-CreateDate"></a>
The date and time that the project was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-CreatedBy"></a>
The identifier (user name) of the user who created the project.
Type: String

 ** [DatasetName](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-DatasetName"></a>
The dataset associated with the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LastModifiedBy](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-LastModifiedBy"></a>
The identifier (user name) of the user who last modified the project.
Type: String

 ** [LastModifiedDate](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-LastModifiedDate"></a>
The date and time that the project was last modified.
Type: Timestamp

 ** [OpenDate](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-OpenDate"></a>
The date and time when the project was opened.
Type: Timestamp

 ** [OpenedBy](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-OpenedBy"></a>
The identifier (user name) of the user that opened the project for use.
Type: String

 ** [RecipeName](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-RecipeName"></a>
The recipe associated with this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ResourceArn](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [RoleArn](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Sample](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-Sample"></a>
Represents the sample size and sampling type for DataBrew to use for interactive data analysis.
Type: [Sample](API_Sample.md) object

 ** [SessionStatus](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-SessionStatus"></a>
Describes the current state of the session:
+  `PROVISIONING` - allocating resources for the session.
+  `INITIALIZING` - getting the session ready for first use.
+  `ASSIGNED` - the session is ready for use.
Type: String
Valid Values: `ASSIGNED | FAILED | INITIALIZING | PROVISIONING | READY | RECYCLING | ROTATING | TERMINATED | TERMINATING | UPDATING`

 ** [Tags](#API_DescribeProject_ResponseSyntax) **   <a name="databrew-DescribeProject-response-Tags"></a>
Metadata tags associated with this project.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DescribeProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DescribeProject)

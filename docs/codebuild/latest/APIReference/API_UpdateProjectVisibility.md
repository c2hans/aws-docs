---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProjectVisibility.html
---

# UpdateProjectVisibility
<a name="API_UpdateProjectVisibility"></a>

Changes the public visibility for a project. The project's build results, logs, and artifacts are available to the general public. For more information, see [Public build projects](https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html) in the * AWS CodeBuild User Guide*.

**Important**
The following should be kept in mind when making your projects public:
All of a project's build results, logs, and artifacts, including builds that were run when the project was private, are available to the general public.
All build logs and artifacts are available to the public. Environment variables, source code, and other sensitive information may have been output to the build logs and artifacts. You must be careful about what information is output to the build logs. Some best practice are:
Do not store sensitive values in environment variables. We recommend that you use an Amazon EC2 Systems Manager Parameter Store or AWS Secrets Manager to store sensitive values.
Follow [Best practices for using webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/webhooks.html#webhook-best-practices) in the * AWS CodeBuild User Guide* to limit which entities can trigger a build, and do not store the buildspec in the project itself, to ensure that your webhooks are as secure as possible.
A malicious user can use public builds to distribute malicious artifacts. We recommend that you review all pull requests to verify that the pull request is a legitimate change. We also recommend that you validate any artifacts with their checksums to make sure that the correct artifacts are being downloaded.

## Request Syntax
<a name="API_UpdateProjectVisibility_RequestSyntax"></a>

```
{
   "projectArn": "{{string}}",
   "projectVisibility": "{{string}}",
   "resourceAccessRole": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProjectVisibility_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectArn](#API_UpdateProjectVisibility_RequestSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-request-projectArn"></a>
The Amazon Resource Name (ARN) of the build project.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [projectVisibility](#API_UpdateProjectVisibility_RequestSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-request-projectVisibility"></a>
Specifies the visibility of the project's builds. Possible values are:
PUBLIC\_READ
The project builds are visible to the public.
PRIVATE
The project builds are not visible to the public.
Type: String
Valid Values: `PUBLIC_READ | PRIVATE`
Required: Yes

 ** [resourceAccessRole](#API_UpdateProjectVisibility_RequestSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-request-resourceAccessRole"></a>
The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_UpdateProjectVisibility_ResponseSyntax"></a>

```
{
   "projectArn": "string",
   "projectVisibility": "string",
   "publicProjectAlias": "string"
}
```

## Response Elements
<a name="API_UpdateProjectVisibility_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [projectArn](#API_UpdateProjectVisibility_ResponseSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-response-projectArn"></a>
The Amazon Resource Name (ARN) of the build project.
Type: String
Length Constraints: Minimum length of 1.

 ** [projectVisibility](#API_UpdateProjectVisibility_ResponseSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-response-projectVisibility"></a>
Specifies the visibility of the project's builds. Possible values are:
PUBLIC\_READ
The project builds are visible to the public.
PRIVATE
The project builds are not visible to the public.
Type: String
Valid Values: `PUBLIC_READ | PRIVATE`

 ** [publicProjectAlias](#API_UpdateProjectVisibility_ResponseSyntax) **   <a name="CodeBuild-UpdateProjectVisibility-response-publicProjectAlias"></a>
Contains the project identifier used with the public build APIs.
For more information, see [Public build](https://docs.aws.amazon.com/codebuild/latest/userguide/public-build.html).
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_UpdateProjectVisibility_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProjectVisibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/UpdateProjectVisibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/UpdateProjectVisibility)

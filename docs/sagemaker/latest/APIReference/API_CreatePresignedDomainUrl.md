---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedDomainUrl.html
---

# CreatePresignedDomainUrl
<a name="API_CreatePresignedDomainUrl"></a>

Creates a URL for a specified UserProfile in a Domain. When accessed in a web browser, the user will be automatically signed in to the domain, and granted access to all of the Apps and files associated with the Domain's Amazon Elastic File System volume. This operation can only be called when the authentication mode equals IAM.

The IAM role or user passed to this API defines the permissions to access the app. Once the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request and WebSocket frame that attempts to connect to the app.

You can restrict access to this API and to the URL that it returns to a list of IP addresses, Amazon VPCs or Amazon VPC Endpoints that you specify. For more information, see [Connect to Amazon SageMaker AI Studio Through an Interface VPC Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-interface-endpoint.html) .

**Note**
The URL that you get from a call to `CreatePresignedDomainUrl` has a default timeout of 5 minutes. You can configure this value using `ExpiresInSeconds`. If you try to use the URL after the timeout limit expires, you are directed to the AWS console sign-in page.
The JupyterLab session default expiration time is 12 hours. You can configure this value using SessionExpirationDurationInSeconds.

## Request Syntax
<a name="API_CreatePresignedDomainUrl_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "ExpiresInSeconds": {{number}},
   "LandingUri": "{{string}}",
   "SessionExpirationDurationInSeconds": {{number}},
   "SpaceName": "{{string}}",
   "UserProfileName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePresignedDomainUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [ExpiresInSeconds](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-ExpiresInSeconds"></a>
The number of seconds until the pre-signed URL expires. This value defaults to 300.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** [LandingUri](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-LandingUri"></a>
The landing page that the user is directed to when accessing the presigned URL. Using this value, users can access Studio or Studio Classic, even if it is not the default experience for the domain. The supported values are:
+  `studio::relative/path`: Directs users to the relative path in Studio.
+  `app:JupyterServer:relative/path`: Directs users to the relative path in the Studio Classic application.
+  `app:JupyterLab:relative/path`: Directs users to the relative path in the JupyterLab application.
+  `app:RStudioServerPro:relative/path`: Directs users to the relative path in the RStudio application.
+  `app:CodeEditor:relative/path`: Directs users to the relative path in the Code Editor, based on Code-OSS, Visual Studio Code - Open Source application.
+  `app:Canvas:relative/path`: Directs users to the relative path in the Canvas application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

 ** [SessionExpirationDurationInSeconds](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-SessionExpirationDurationInSeconds"></a>
The session expiration duration in seconds. This value defaults to 43200.
Type: Integer
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

 ** [SpaceName](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [UserProfileName](#API_CreatePresignedDomainUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-request-UserProfileName"></a>
The name of the UserProfile to sign-in as.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_CreatePresignedDomainUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string"
}
```

## Response Elements
<a name="API_CreatePresignedDomainUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreatePresignedDomainUrl_ResponseSyntax) **   <a name="sagemaker-CreatePresignedDomainUrl-response-AuthorizedUrl"></a>
The presigned URL.
Type: String

## Errors
<a name="API_CreatePresignedDomainUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePresignedDomainUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePresignedDomainUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePresignedDomainUrl)

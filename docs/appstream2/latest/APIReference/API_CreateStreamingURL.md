---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html
---

# CreateStreamingURL
<a name="API_CreateStreamingURL"></a>

Creates a temporary URL to start an WorkSpaces Applications streaming session for the specified user. A streaming URL enables application streaming to be tested without user setup.

## Request Syntax
<a name="API_CreateStreamingURL_RequestSyntax"></a>

```
{
   "ApplicationId": "{{string}}",
   "FleetName": "{{string}}",
   "SessionContext": "{{string}}",
   "StackName": "{{string}}",
   "UserId": "{{string}}",
   "Validity": {{number}}
}
```

## Request Parameters
<a name="API_CreateStreamingURL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-ApplicationId"></a>
The name of the application to launch after the session starts. This is the name that you specified as **Name** in the Image Assistant. If your fleet is enabled for the **Desktop** stream view, you can also choose to launch directly to the operating system desktop. To do so, specify **Desktop**.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [FleetName](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-FleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [SessionContext](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-SessionContext"></a>
The session context. For more information, see [Session Context](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-StackName"></a>
The name of the stack.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [UserId](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-UserId"></a>
The identifier of the user.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 32.
Pattern: `[\w+=,.@-]*`
Required: Yes

 ** [Validity](#API_CreateStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-request-Validity"></a>
The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.
Type: Long
Required: No

## Response Syntax
<a name="API_CreateStreamingURL_ResponseSyntax"></a>

```
{
   "Expires": number,
   "StreamingURL": "string"
}
```

## Response Elements
<a name="API_CreateStreamingURL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Expires](#API_CreateStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-response-Expires"></a>
The elapsed time, in seconds after the Unix epoch, when this URL expires.
Type: Timestamp

 ** [StreamingURL](#API_CreateStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateStreamingURL-response-StreamingURL"></a>
The URL to start the WorkSpaces Applications streaming session.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateStreamingURL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotAvailableException **
The specified resource exists and is not in use, but isn't available.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateStreamingURL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateStreamingURL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateStreamingURL)

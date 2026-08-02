---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StartFleet.html
---

# StartFleet
<a name="API_StartFleet"></a>

Starts the specified fleet.

## Request Syntax
<a name="API_StartFleet_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_StartFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_StartFleet_RequestSyntax) **   <a name="WorkSpacesApplications-StartFleet-request-Name"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Elements
<a name="API_StartFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** RequestLimitExceededException **
WorkSpaces Applications can't process the request right now because this operation is being throttled. Try again later.
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
<a name="API_StartFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/StartFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/StartFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/StartFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/StartFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/StartFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/StartFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/StartFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/StartFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/StartFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/StartFleet)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_DeleteApplication.html
---

# DeleteApplication
<a name="API_connect-app-integrations_DeleteApplication"></a>

Deletes an application. If the application has associations, you must delete them first. Alternatively, use the `force` option to delete the application and remove its associations.

## Request Syntax
<a name="API_connect-app-integrations_DeleteApplication_RequestSyntax"></a>

```
DELETE /applications/{{ApplicationIdentifier}}?force={{Force}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_DeleteApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_connect-app-integrations_DeleteApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_DeleteApplication-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(:[\w\$]+)?$`
Required: Yes

 ** [Force](#API_connect-app-integrations_DeleteApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_DeleteApplication-request-uri-Force"></a>
Specifies whether to delete the application even if it still has application associations. If `true`, the operation removes the application and its associations. If `false` or absent, the delete fails when associations exist.
Setting this parameter to `true` permanently removes all of the application's associations. Doing so might impact other resources that rely on and reference the application. This action can't be undone.

## Request Body
<a name="API_connect-app-integrations_DeleteApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_DeleteApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_DeleteApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/DeleteApplication)

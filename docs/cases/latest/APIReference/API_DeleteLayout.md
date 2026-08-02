---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteLayout.html
---

# DeleteLayout
<a name="API_connect-cases_DeleteLayout"></a>

Deletes a layout from a cases template. You can delete up to 100 layouts per domain.

After a layout is deleted:
+ You can still retrieve the layout by calling `GetLayout`.
+ You cannot update a deleted layout by calling `UpdateLayout`; it throws a `ValidationException`.
+ Deleted layouts are not included in the `ListLayouts` response.

## Request Syntax
<a name="API_connect-cases_DeleteLayout_RequestSyntax"></a>

```
DELETE /domains/{{domainId}}/layouts/{{layoutId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_DeleteLayout_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_DeleteLayout_RequestSyntax) **   <a name="connect-connect-cases_DeleteLayout-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [layoutId](#API_connect-cases_DeleteLayout_RequestSyntax) **   <a name="connect-connect-cases_DeleteLayout-request-uri-layoutId"></a>
The unique identifier of the layout.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_DeleteLayout_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_DeleteLayout_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_DeleteLayout_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_DeleteLayout_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_connect-cases_DeleteLayout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/DeleteLayout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/DeleteLayout)

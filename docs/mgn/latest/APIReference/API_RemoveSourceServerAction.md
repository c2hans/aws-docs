---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_RemoveSourceServerAction.html
---

# RemoveSourceServerAction
<a name="API_RemoveSourceServerAction"></a>

Remove source server post migration custom action.

## Request Syntax
<a name="API_RemoveSourceServerAction_RequestSyntax"></a>

```
POST /RemoveSourceServerAction HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "actionID": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RemoveSourceServerAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RemoveSourceServerAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_RemoveSourceServerAction_RequestSyntax) **   <a name="mgn-RemoveSourceServerAction-request-accountID"></a>
Source server post migration account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [actionID](#API_RemoveSourceServerAction_RequestSyntax) **   <a name="mgn-RemoveSourceServerAction-request-actionID"></a>
Source server post migration custom action ID to remove.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`
Required: Yes

 ** [sourceServerID](#API_RemoveSourceServerAction_RequestSyntax) **   <a name="mgn-RemoveSourceServerAction-request-sourceServerID"></a>
Source server ID of the post migration custom action to remove.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_RemoveSourceServerAction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_RemoveSourceServerAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_RemoveSourceServerAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_RemoveSourceServerAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/RemoveSourceServerAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/RemoveSourceServerAction)

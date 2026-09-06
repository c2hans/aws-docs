---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteGroup.html
---

# DeleteGroup
<a name="API_DeleteGroup"></a>

Deletes a group. The group doesn't need to be empty to be deleted. If there are canaries in the group, they are not deleted when you delete the group.

Groups are a global resource that appear in all Regions, but the request to delete a group must be made from its home Region. You can find the home Region of a group within its ARN.

## Request Syntax
<a name="API_DeleteGroup_RequestSyntax"></a>

```
DELETE /group/{{groupIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupIdentifier](#API_DeleteGroup_RequestSyntax) **   <a name="synthetics-DeleteGroup-request-uri-GroupIdentifier"></a>
Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the `GroupIdentifier`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_DeleteGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DeleteGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DeleteGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DeleteGroup)

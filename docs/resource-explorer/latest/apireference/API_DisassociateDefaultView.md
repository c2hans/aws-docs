---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DisassociateDefaultView.html
---

# DisassociateDefaultView
<a name="API_DisassociateDefaultView"></a>

After you call this operation, the affected AWS Region no longer has a default view. All [Search](API_Search.md) operations in that Region must explicitly specify a view or the operation fails. You can configure a new default by calling the [AssociateDefaultView](API_AssociateDefaultView.md) operation.

If an AWS Region doesn't have a default view configured, then users must explicitly specify a view with every `Search` operation performed in that Region.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:DisassociateDefaultView`

   **Resource**: No specific resource (\*). However, an index must be present in the AWS Region in which you call the operation.

 **Related operations**
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md).
+ To create a view, use [CreateView](API_CreateView.md).
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To get details about your views, use [GetView](API_GetView.md) or [BatchGetView](API_BatchGetView.md).
+ To update the definition of a view, use [UpdateView](API_UpdateView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).

## Request Syntax
<a name="API_DisassociateDefaultView_RequestSyntax"></a>

```
POST /DisassociateDefaultView HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateDefaultView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateDefaultView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateDefaultView_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateDefaultView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateDefaultView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_DisassociateDefaultView_Examples"></a>

### Example
<a name="API_DisassociateDefaultView_Example_1"></a>

The following example disassociates the current default view in the AWS Region in which you invoke the operation. After performing this operation, all search operations in the Region must explicitly specify a view or they fail.

#### Sample Request
<a name="API_DisassociateDefaultView_Example_1_Request"></a>

```
POST /DisassociateDefaultView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
```

#### Sample Response
<a name="API_DisassociateDefaultView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>
```

## See Also
<a name="API_DisassociateDefaultView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/DisassociateDefaultView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/DisassociateDefaultView)

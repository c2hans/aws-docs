---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetDefaultView.html
---

# GetDefaultView
<a name="API_GetDefaultView"></a>

Retrieves the Amazon Resource Name (ARN) of the view that is the default for the AWS Region in which you call this operation. You can then call [GetView](API_GetView.md) to retrieve the details of that view.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:GetDefaultView`

   **Resource**: No specific resource (\*). However, an index must be present in the AWS Region in which you call the operation.

 **Related operations**
+ To get details about more than one view, use [BatchGetView](API_BatchGetView.md).
+ To create a view, use [CreateView](API_CreateView.md).
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To see details about a specific view, use [GetView](API_GetView.md).
+ To update the definition of a view, use [UpdateView](API_UpdateView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md). To remove the default view for a Region, use [DisassociateDefaultView](API_DisassociateDefaultView.md).

## Request Syntax
<a name="API_GetDefaultView_RequestSyntax"></a>

```
POST /GetDefaultView HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDefaultView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDefaultView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDefaultView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ViewArn": "string"
}
```

## Response Elements
<a name="API_GetDefaultView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ViewArn](#API_GetDefaultView_ResponseSyntax) **   <a name="resourceexplorer-GetDefaultView-response-ViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view that is the current default for the AWS Region in which you called this operation.
Type: String

## Errors
<a name="API_GetDefaultView_Errors"></a>

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
<a name="API_GetDefaultView_Examples"></a>

### Example
<a name="API_GetDefaultView_Example_1"></a>

The following example retrieves the ARN of the view that is the default view for the AWS Region in which you call the operation.

#### Sample Request
<a name="API_GetDefaultView_Example_1_Request"></a>

```
POST /GetDefaultView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
```

#### Sample Response
<a name="API_GetDefaultView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012::view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

## See Also
<a name="API_GetDefaultView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetDefaultView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetDefaultView)

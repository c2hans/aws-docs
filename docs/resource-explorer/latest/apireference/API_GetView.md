---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetView.html
---

# GetView
<a name="API_GetView"></a>

Retrieves details of the specified view.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:GetView`

   **Resource**: The ARN of the specified view.

   [This action supports using condition keys to check the tags attached to the view to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To get details about more than one view, use [BatchGetView](API_BatchGetView.md).
+ To create a view, use [CreateView](API_CreateView.md).
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To update the definition of a view, use [UpdateView](API_UpdateView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md). To remove the default view for a Region, use [DisassociateDefaultView](API_DisassociateDefaultView.md).

## Request Syntax
<a name="API_GetView_RequestSyntax"></a>

```
POST /GetView HTTP/1.1
Content-type: application/json

{
   "ViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ViewArn](#API_GetView_RequestSyntax) **   <a name="resourceexplorer-GetView-request-ViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view that you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_GetView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": {
      "string" : "string"
   },
   "View": {
      "Filters": {
         "FilterString": "string"
      },
      "IncludedProperties": [
         {
            "Name": "string"
         }
      ],
      "LastUpdatedAt": "string",
      "Owner": "string",
      "Scope": "string",
      "ViewArn": "string"
   }
}
```

## Response Elements
<a name="API_GetView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_GetView_ResponseSyntax) **   <a name="resourceexplorer-GetView-response-Tags"></a>
Tag key and value pairs that are attached to the view.
Type: String to string map

 ** [View](#API_GetView_ResponseSyntax) **   <a name="resourceexplorer-GetView-response-View"></a>
A structure that contains the details for the requested view.
Type: [View](API_View.md) object

## Errors
<a name="API_GetView_Errors"></a>

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

 ** UnauthorizedException **
The principal making the request isn't permitted to perform the operation.
HTTP Status Code: 401

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_GetView_Examples"></a>

### Example
<a name="API_GetView_Example_1"></a>

The following example retrieves the details about the specified view. You can get the ARN of the view you want to inspect by calling the [ListViews](API_ListViews.md) operation.

#### Sample Request
<a name="API_GetView_Example_1_Request"></a>

```
POST /GetView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_GetView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
  "Tags" : { },
  "View" : {
    "Filters" : {
      "FilterString" : "service:ec2"
    },
    "IncludedProperties" : [ {
      "Name" : "tags"
    } ],
    "LastUpdatedAt" : "2022-07-13T21:33:45.249Z",
    "Owner" : "123456789012",
    "Scope" : "arn:aws:iam::123456789012:root",
    "ViewArn" : "arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
  }
}
```

## See Also
<a name="API_GetView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetView)

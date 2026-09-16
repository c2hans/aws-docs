---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateView.html
---

# UpdateView
<a name="API_UpdateView"></a>

Modifies some of the details of a view. You can change the filter string and the list of included properties. You can't change the name of the view.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:UpdateView`

   **Resource**: The ARN of the specified view.

   [This action supports using condition keys to check the tags attached to the view to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To create a view, use [CreateView](API_CreateView.md).
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To get details about your views, use [GetView](API_GetView.md) or [BatchGetView](API_BatchGetView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md). To remove the default for a Region, use [DisassociateDefaultView](API_DisassociateDefaultView.md).

## Request Syntax
<a name="API_UpdateView_RequestSyntax"></a>

```
POST /UpdateView HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "FilterString": "{{string}}"
   },
   "IncludedProperties": [
      {
         "Name": "{{string}}"
      }
   ],
   "ViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ViewArn](#API_UpdateView_RequestSyntax) **   <a name="resourceexplorer-UpdateView-request-ViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view that you want to modify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** [Filters](#API_UpdateView_RequestSyntax) **   <a name="resourceexplorer-UpdateView-request-Filters"></a>
An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a [Search](API_Search.md) operation, the filter string is combined with the search's `QueryString` parameter using a logical `AND` operator.
For information about the supported syntax, see [Search query reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the * AWS Resource Explorer User Guide*.
This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators). It doesn't support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any AWS Region that begins with the letters `us` and is *not* tagged with a key `Stage` that has the value `prod`.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** [IncludedProperties](#API_UpdateView_RequestSyntax) **   <a name="resourceexplorer-UpdateView-request-IncludedProperties"></a>
Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.
The default is an empty list, with no optional fields included in the results.
Type: Array of [IncludedProperty](API_IncludedProperty.md) objects
Required: No

## Response Syntax
<a name="API_UpdateView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_UpdateView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_UpdateView_ResponseSyntax) **   <a name="resourceexplorer-UpdateView-response-View"></a>
Details about the view that you changed with this operation.
Type: [View](API_View.md) object

## Errors
<a name="API_UpdateView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request failed because it exceeds a service quota.
 ** Name **
The name of the service quota that was exceeded by the request.
 ** Value **
The current value for the quota that the request tried to exceed.
HTTP Status Code: 402

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
<a name="API_UpdateView_Examples"></a>

### Example 1: Update the IncludedProperties field of a view
<a name="API_UpdateView_Example_1"></a>

The following example updates the specified view by adding `tags` to its `IncludedProperties` field. After running this operation, search operations that use this view include information about any tags attached to the resources that appear in the results.

#### Sample Request
<a name="API_UpdateView_Example_1_Request"></a>

```
POST /UpdateView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "IncludedProperties": [
        {
            "Name": "tags"
        }
    ],
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222
}
```

#### Sample Response
<a name="API_UpdateView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "View": {
        "Filters": {
            "FilterString": ""
        },
        "IncludedProperties": [
            {
                "Name":"tags"
            }
        ],
        "LastUpdatedAt": "2022-07-19T17:41:21.710Z",
        "Owner": "123456789012",
        "Scope": "arn:aws:iam::123456789012:root",
        "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
    }
}
```

### Example 2: Update the filters attached to a view
<a name="API_UpdateView_Example_2"></a>

The following example updates the specified view to use a filter that limits results to only resource types that are associated with the Amazon EC2 service.

#### Sample Request
<a name="API_UpdateView_Example_2_Request"></a>

```
POST /UpdateView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "Filters": {
        "FilterString": "service:ec2"
    },
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222
}
```

#### Sample Response
<a name="API_UpdateView_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "View": {
        "Filters": {
            "FilterString": "service:ec2"
        },
        "IncludedProperties": [],
        "LastUpdatedAt": "2022-07-19T17:41:21.710Z",
        "Owner": "123456789012",
        "Scope": "arn:aws:iam::123456789012:root",
        "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
    }
}
```

## See Also
<a name="API_UpdateView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/UpdateView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/UpdateView)

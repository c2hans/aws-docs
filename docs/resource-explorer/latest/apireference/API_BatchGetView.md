---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_BatchGetView.html
---

# BatchGetView
<a name="API_BatchGetView"></a>

Retrieves details about a list of views.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:BatchGetView`

   **Resource**: No specific resource (\*).

   [This action supports using condition keys to check the tags attached to the view to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)
+  **Action**: `resource-explorer-2:GetView`

   **Resource**: the ARN of each view you want to retrieve.

   [This action supports using condition keys to check the tags attached to the view to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To create a view, use [CreateView](API_CreateView.md).
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To get details about your views, use [GetView](API_GetView.md) or [BatchGetView](#API_BatchGetView).
+ To update a view, use [UpdateView](API_UpdateView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md). To remove the default for a Region, use [DisassociateDefaultView](API_DisassociateDefaultView.md).

## Request Syntax
<a name="API_BatchGetView_RequestSyntax"></a>

```
POST /BatchGetView HTTP/1.1
Content-type: application/json

{
   "ViewArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ViewArns](#API_BatchGetView_RequestSyntax) **   <a name="resourceexplorer-BatchGetView-request-ViewArns"></a>
A list of [Amazon resource names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) that identify the views you want details for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_BatchGetView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorMessage": "string",
         "ViewArn": "string"
      }
   ],
   "Views": [
      {
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
   ]
}
```

## Response Elements
<a name="API_BatchGetView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetView_ResponseSyntax) **   <a name="resourceexplorer-BatchGetView-response-Errors"></a>
If any of the specified ARNs result in an error, then this structure describes the error.
Type: Array of [BatchGetViewError](API_BatchGetViewError.md) objects

 ** [Views](#API_BatchGetView_ResponseSyntax) **   <a name="resourceexplorer-BatchGetView-response-Views"></a>
A structure with a list of objects with details for each of the specified views.
Type: Array of [View](API_View.md) objects

## Errors
<a name="API_BatchGetView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

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
<a name="API_BatchGetView_Examples"></a>

### Example
<a name="API_BatchGetView_Example_1"></a>

The following example returns details about two views, as specified by their ARNs.

#### Sample Request
<a name="API_BatchGetView_Example_1_Request"></a>

```
POST /BatchGetView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "ViewArns": [
        "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222",
        "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
    ]
}
```

#### Sample Response
<a name="API_BatchGetView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Views": [
        {
            "Filters": {
                "FilterString": "service:ec2"
            },
            "IncludedProperties": [
                {
                    "Name": "tags"
                }
            ],
            "LastUpdatedAt": "2022-07-13T21:33:45.249Z",
            "Owner": "123456789012",
            "Scope": "arn:aws:iam::123456789012:root",
            "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
        },
        {
            "Filters": {
                "FilterString": ""
            },
            "IncludedProperties": [
                {
                    "Name":"tags"
                }
            ],
            "LastUpdatedAt":"2022-07-13T20:34:11.314Z",
            "Owner":"123456789012",
            "Scope":"arn:aws:iam::123456789012:root",
            "ViewArn":"arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
        }
    ],
    "Errors": []
}
```

## See Also
<a name="API_BatchGetView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/BatchGetView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/BatchGetView)

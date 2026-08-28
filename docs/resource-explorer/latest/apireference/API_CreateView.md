---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateView.html
---

# CreateView
<a name="API_CreateView"></a>

Creates a view that users can query by using the [Search](API_Search.md) operation. Results from queries that you make using this view include only resources that match the view's `Filters`. For more information about AWS Resource Explorer views, see [Managing views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html) in the * AWS Resource Explorer User Guide*.

Only the principals with an IAM identity-based policy that grants `Allow` to the `Search` action on a `Resource` with the [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of this view can [Search](API_Search.md) using views you create with this operation.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:CreateView`

   **Resource**:
  + This can be `*` to allow creation of a view in any AWS Region in the account.
  + The ARN of the view as it exists after the view is created. This can be `*` to allow creating a view in any AWS Region in the account with any name. It can also be similar to the following example that restricts a role's or user's ability to create a view in only the specified AWS Region and with only the specified name prefix.

     `arn:aws:resource-explorer-2:<region>:<AccountId>:view/NamePrefix*`

   [This action supports using condition keys to check the tags attached to the index to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To list the views in an AWS Region, use [ListViews](API_ListViews.md).
+ To get details about your views, use [GetView](API_GetView.md) or [BatchGetView](API_BatchGetView.md).
+ To update a view, use [UpdateView](API_UpdateView.md).
+ To delete a view, use [DeleteView](API_DeleteView.md).
+ To make a view the default for an AWS Region, use [AssociateDefaultView](API_AssociateDefaultView.md). To remove the default for a Region, use [DisassociateDefaultView](API_DisassociateDefaultView.md).

## Request Syntax
<a name="API_CreateView_RequestSyntax"></a>

```
POST /CreateView HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Filters": {
      "FilterString": "{{string}}"
   },
   "IncludedProperties": [
      {
         "Name": "{{string}}"
      }
   ],
   "Scope": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "ViewName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ViewName](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-ViewName"></a>
The name of the new view. This name appears in the list of views in Resource Explorer.
The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its AWS Region.
Type: String
Pattern: `[a-zA-Z0-9\-]{1,64}`
Required: Yes

 ** [ClientToken](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-ClientToken"></a>
This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a [UUID-type value](https://wikipedia.org/wiki/Universally_unique_identifier) to ensure the uniqueness of your views.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Filters](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-Filters"></a>
An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a [Search](API_Search.md) operation, the filter string is combined with the search's `QueryString` parameter using a logical `AND` operator.
For information about the supported syntax, see [Search query reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the * AWS Resource Explorer User Guide*.
This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators). It doesn't support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any AWS Region that begins with the letters `us` and is *not* tagged with a key `Stage` that has the value `prod`.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** [IncludedProperties](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-IncludedProperties"></a>
Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.
The default is an empty list, with no optional fields included in the results.
Type: Array of [IncludedProperty](API_IncludedProperty.md) objects
Required: No

 ** [Scope](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-Scope"></a>
The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Tags](#API_CreateView_RequestSyntax) **   <a name="resourceexplorer-CreateView-request-Tags"></a>
Tag key and value pairs that are attached to the view.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateView_ResponseSyntax"></a>

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
<a name="API_CreateView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_CreateView_ResponseSyntax) **   <a name="resourceexplorer-CreateView-response-View"></a>
A structure that contains the details about the new view.
Type: [View](API_View.md) object

## Errors
<a name="API_CreateView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** ConflictException **
If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this AWS Region.
If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current AWS Region.
If you attempted to update an index type to `AGGREGATOR`, then the request failed because you already have an `AGGREGATOR` index in a different AWS Region.
HTTP Status Code: 409

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
<a name="API_CreateView_Examples"></a>

### Example 1 – Create a view that performs no filtering
<a name="API_CreateView_Example_1"></a>

The following example creates a view in AWS Region `us-east-1` that returns all resources in the Region without any filtering. The `ClientToken` parameter value is a randomly generated UUID. Because this view is in the Region that contains the aggregator index, it can include results from all Regions in the account that contain a Resource Explorer index.

#### Sample Request
<a name="API_CreateView_Example_1_Request"></a>

```
POST /CreateView HTTP/1.1
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
    "ViewName": "My-Main-View",
    "ClientToken": "EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_CreateView_Example_1_Response"></a>

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
                "Name": "tags"
            }
        ],
        "LastUpdatedAt": "2022-07-13T20:34:11.314Z",
        "Owner": "123456789012",
        "Scope":"arn:aws:iam::123456789012:root",
        "ViewArn":"arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111
    }
}
```

### Example 2 – Create a view that filters to only resource types for a single service
<a name="API_CreateView_Example_2"></a>

The following example creates a view in AWS Region `us-east-1` that returns only those resources in the Region that are associated with the Amazon EC2 service. The `ClientToken` parameter value is a randomly generated UUID. Because this view is in the Region that contains the aggregator index, it can include results that match the filter from all Regions in the account that contain a Resource Explorer index.

#### Sample Request
<a name="API_CreateView_Example_2_Request"></a>

```
POST /CreateView HTTP/1.1
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
        },
        "Filters": {
            "FilterString": "service:ec2"
        }
    ],
    "ViewName": "My-EC2-Only-View",
    "ClientToken": "EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_CreateView_Example_2_Response"></a>

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
        "IncludedProperties": [
            {
                "Name": "tags"
            }
        ],
        "LastUpdatedAt": "2022-07-13T20:36:15.661Z",
        "Owner": "123456789012",
        "Scope":"arn:aws:iam::123456789012:root",
        "ViewArn":"arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222
    }
}
```

## See Also
<a name="API_CreateView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/CreateView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/CreateView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

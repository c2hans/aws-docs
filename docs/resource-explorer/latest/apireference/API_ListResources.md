---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

Returns a list of resources and their details that match the specified criteria. This query must use a view. If you don’t explicitly specify a view, then Resource Explorer uses the default view for the AWS Region in which you call this operation.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:Search`

   **Resource**: No specific resource (\*).

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
POST /ListResources HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "FilterString": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListResources_RequestSyntax) **   <a name="resourceexplorer-ListResources-request-Filters"></a>
An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a [Search](API_Search.md) operation, the filter string is combined with the search's `QueryString` parameter using a logical `AND` operator.
For information about the supported syntax, see [Search query reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the * AWS Resource Explorer User Guide*.
This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators). It doesn't support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any AWS Region that begins with the letters `us` and is *not* tagged with a key `Stage` that has the value `prod`.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** [MaxResults](#API_ListResources_RequestSyntax) **   <a name="resourceexplorer-ListResources-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListResources_RequestSyntax) **   <a name="resourceexplorer-ListResources-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
The `ListResources` operation does not generate a `NextToken` if you set `MaxResults` to 1000.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ViewArn](#API_ListResources_RequestSyntax) **   <a name="resourceexplorer-ListResources-request-ViewArn"></a>
Specifies the Amazon resource name (ARN) of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the AWS Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a 401 Unauthorized exception.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Resources": [
      {
         "Arn": "string",
         "LastReportedAt": "string",
         "OwningAccountId": "string",
         "Properties": [
            {
               "Data": JSON value,
               "LastReportedAt": "string",
               "Name": "string"
            }
         ],
         "Region": "string",
         "ResourceType": "string",
         "Service": "string"
      }
   ],
   "ViewArn": "string"
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResources_ResponseSyntax) **   <a name="resourceexplorer-ListResources-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Resources](#API_ListResources_ResponseSyntax) **   <a name="resourceexplorer-ListResources-response-Resources"></a>
The list of structures that describe the resources that match the query.
Type: Array of [Resource](API_Resource.md) objects

 ** [ViewArn](#API_ListResources_ResponseSyntax) **   <a name="resourceexplorer-ListResources-response-ViewArn"></a>
The Amazon resource name (ARN) of the view that this operation used to perform the search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.

## Errors
<a name="API_ListResources_Errors"></a>

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
<a name="API_ListResources_Examples"></a>

### Example
<a name="API_ListResources_Example_1"></a>

The following example shows how to list of all supported resource types, across all AWS services, within your account or organization. The example response includes a `NextToken` value, which indicates that there is more output available to retrieve with additional calls.

#### Sample Request
<a name="API_ListResources_Example_1_Request"></a>

```
POST /ListResources HTTP/1.1
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
   "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/my-default-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "MaxResults": 2,
    "NextToken": "AG9VOEF1KLEXAMPLEOhJHVwo5chEXAMPLER5XiEpNrgsEXAMPLE...b0CmOFOryHEXAMPLE"
}
```

#### Sample Response
<a name="API_ListResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "NextToken": "AG9VOEF1KLEXAMPLEOhJHVwo5chEXAMPLER5XiEpNrgsEXAMPLE...b0CmOFOryHEXAMPLE",
    "Resources": [
        {
            "Arn": "arn:aws:iam::123456789012:policy/service-role/Policy-For-A-Service-Role",
            "LastReportedAt": "2024-07-21T12:34:42Z",
            "OwningAccountId": "111122223333",
            "Properties": [
                {
                    "Data": [
                        {
                            "Key": "Name",
                            "Value": "Example-Name"
                        },
                        {
                            "Key": "aws:cloudformation:stack-name",
                            "Value": "Stack-Name"
                        },
                        {
                            "Key": "aws:cloudformation:stack-id",
                            "Value": "arn:aws:cloudformation:us-east-1:111122223333:stack/stack-name-username-region/EXAMPLE8-90ab-cdef-fedc-EXAMPLE33333"
                        },
                        {
                            "Key": "aws:cloudformation:logical-id",
                            "Value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
                        }
                    ],
                    "LastReportedAt": "2024-02-26T13:47:30Z",
                    "Name": "tags"
                }
            ],
            "Region": "us-east-1",
            "ResourceType": "ec2:natgateway",
            "Service": "ec2"
        },
        {
            "Arn": "arn:aws:iam::111122223333:policy/service-role/Policy-For-A-Service-Role",
            "LastReportedAt": "2024-07-21T12:34:42Z",
            "OwningAccountId": "111122223333",
            "Properties": [],
            "Region": "us-east-1",
            "ResourceType": "ec2:internet-gateway",
            "Service": "ec2"
        }
    ],
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/my-default-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
}
```

## See Also
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

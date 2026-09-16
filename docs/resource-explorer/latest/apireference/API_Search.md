---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html
---

# Search
<a name="API_Search"></a>

Searches for resources and displays details about all resources that match the specified criteria. You must specify a query string.

All search queries must use a view. If you don't explicitly specify a view, then AWS Resource Explorer uses the default view for the AWS Region in which you call this operation. The results are the logical intersection of the results that match both the `QueryString` parameter supplied to this operation and the `SearchFilter` parameter attached to the view.

For the complete syntax supported by the `QueryString` parameter, see [Search query syntax reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html).

If your search results are empty, or are missing results that you think should be there, see [Troubleshooting Resource Explorer search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html).

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:Search`

   **Resource**: The ARN of the specified view, or if a view isn't specified, the default view for the AWS Region in which you call this operation.

   [This action supports using condition keys to check the tags attached to the view to limit permissions.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

 **Related operations**
+ To list the views that you can use with this operation, use [ListViews](API_ListViews.md).

## Request Syntax
<a name="API_Search_RequestSyntax"></a>

```
POST /Search HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueryString": "{{string}}",
   "ViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_Search_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_Search_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryString](#API_Search_RequestSyntax) **   <a name="resourceexplorer-Search-request-QueryString"></a>
A string that includes keywords and filters that specify the resources that you want to include in the results.
For the complete syntax supported by the `QueryString` parameter, see [Search query syntax reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html).
The search is completely case insensitive. You can specify an empty string to return all results up to the limit of 1,000 total results.
The operation can return only the first 1,000 results. If the resource you want is not included, then use a different value for `QueryString` to refine the results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1280.
Required: Yes

 ** [MaxResults](#API_Search_RequestSyntax) **   <a name="resourceexplorer-Search-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_Search_RequestSyntax) **   <a name="resourceexplorer-Search-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ViewArn](#API_Search_RequestSyntax) **   <a name="resourceexplorer-Search-request-ViewArn"></a>
Specifies the [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the AWS Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a `401 Unauthorized` exception.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_Search_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Count": {
      "Complete": boolean,
      "TotalResources": number
   },
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
<a name="API_Search_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Count](#API_Search_ResponseSyntax) **   <a name="resourceexplorer-Search-response-Count"></a>
The number of resources that match the query.
Type: [ResourceCount](API_ResourceCount.md) object

 ** [NextToken](#API_Search_ResponseSyntax) **   <a name="resourceexplorer-Search-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Resources](#API_Search_ResponseSyntax) **   <a name="resourceexplorer-Search-response-Resources"></a>
The list of structures that describe the resources that match the query.
Type: Array of [Resource](API_Resource.md) objects

 ** [ViewArn](#API_Search_ResponseSyntax) **   <a name="resourceexplorer-Search-response-ViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view that this operation used to perform the search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.

## Errors
<a name="API_Search_Errors"></a>

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
<a name="API_Search_Examples"></a>

### Example 1: Search using the default view
<a name="API_Search_Example_1"></a>

The following example search displays all resources in the specified AWS Region that are associated with the IAM service. The search uses the default view for the Region.

The example output includes a `NextToken`, which indicates that there is more output available to retrieve with additional calls.

#### Sample Request
<a name="API_Search_Example_1_Request"></a>

```
POST /Search HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{"QueryString": "service:IAM"}
```

#### Sample Response
<a name="API_Search_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Count": {
        "Complete": true,
        "TotalResources": 55
    },
    "NextToken": "AG9VOEF1KLEXAMPLEOhJHVwo5chEXAMPLER5XiEpNrgsEXAMPLE...b0CmOFOryHEXAMPLE",
    "Resources": [{
        "Arn": "arn:aws:iam::123456789012:policy/service-role/Some-Policy-For-A-Service-Role",
        "LastReportedAt": "2022-07-21T12:34:42Z",
        "OwningAccountId": "123456789012",
        "Properties": [],
        "Region": "global",
        "ResourceType": "iam:policy",
        "Service": "iam"
    }, {
        "Arn": "arn:aws:iam::123456789012:policy/service-role/Another-Policy-For-A-Service-Role",
        "LastReportedAt": "2022-07-21T12:34:42Z",
        "OwningAccountId": "123456789012",
        "Properties": [],
        "Region": "global",
        "ResourceType": "iam:policy",
        "Service": "iam"
    }, {
       ... TRUNCATED FOR BREVITY ...
    }],
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/my-default-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

### Example 2: Search using a specified view
<a name="API_Search_Example_2"></a>

The following example search displays all resources ("\*") in the specified AWS Region that are visible through the specified view.

The results include only resources associated with Amazon EC2 because of the filters attached to the view.

#### Sample Request
<a name="API_Search_Example_2_Request"></a>

```
POST /Search HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    "QueryString": "*",
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
}
```

#### Sample Response
<a name="API_Search_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Count": {
        "Complete": true,
        "TotalResources": 24
    },
    "Resources": [{
        "Arn": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-1a2b3c4d",
        "LastReportedAt": "2022-07-21T18:52:02Z",
        "OwningAccountId": "123456789012",
        "Properties": [{
            "Data": [{
                "Key": "Department",
                "Value": "AppDevelopment"
            }, {
                "Key": "Environment",
                "Value": "Production"
            }],
            "LastReportedAt": "2021-11-15T14:48:29Z",
            "Name": "tags"
        }],
        "Region": "us-east-1",
        "ResourceType": "ec2:network-acl",
        "Service": "ec2"
    }, {
        "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-1a2b3c4d",
        "LastReportedAt": "2022-07-21T21:22:23Z",
        "OwningAccountId": "123456789012",
        "Properties": [{
            "Data": [{
                "Key": "Department",
                "Value": "AppDevelopment"
            }, {
                "Key": "Environment",
                "Value": "Production"
            }],
            "LastReportedAt": "2021-07-29T19:02:39Z",
            "Name": "tags"
        }],
        "Region": "us-east-1",
        "ResourceType": "ec2:subnet",
        "Service": "ec2"
    }, {
        "Arn": "arn:aws:ec2:us-east-1:123456789012:dhcp-options/dopt-1a2b3c4d",
        "LastReportedAt": "2022-07-21T06:08:53Z",
        "OwningAccountId": "123456789012",
        "Properties": [{
            "Data": [{
                "Key": "Department",
                "Value": "AppDevelopment"
            }, {
                "Key": "Environment",
                "Value": "Production"
            }],
            "LastReportedAt": "2021-11-15T15:11:05Z",
            "Name": "tags"
        }],
        "Region": "us-east-1",
        "ResourceType": "ec2:dhcp-options",
        "Service": "ec2"
    }, {
        ... TRUNCATED FOR BREVITY ...
    }],
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
}
```

## See Also
<a name="API_Search_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/Search)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/Search)

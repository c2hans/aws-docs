---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_SearchResources.html
---

# SearchResources
<a name="API_SearchResources"></a>

Returns a list of AWS resource identifiers that matches the specified query. The query uses the same format as a resource query in a [CreateGroup](API_CreateGroup.md) or [UpdateGroupQuery](API_UpdateGroupQuery.md) operation.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:SearchResources`
+  `cloudformation:DescribeStacks`
+  `cloudformation:ListStackResources`
+  `tag:GetResources`

## Request Syntax
<a name="API_SearchResources_RequestSyntax"></a>

```
POST /resources/search HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceQuery": {
      "Query": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_SearchResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceQuery](#API_SearchResources_RequestSyntax) **   <a name="ARG-SearchResources-request-ResourceQuery"></a>
The search query, using the same formats that are supported for resource group definition. For more information, see [CreateGroup](API_CreateGroup.md).
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: Yes

 ** [MaxResults](#API_SearchResources_RequestSyntax) **   <a name="ARG-SearchResources-request-MaxResults"></a>
The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_SearchResources_RequestSyntax) **   <a name="ARG-SearchResources-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value provided by a previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`
Required: No

## Response Syntax
<a name="API_SearchResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "QueryErrors": [
      {
         "ErrorCode": "string",
         "Message": "string"
      }
   ],
   "ResourceIdentifiers": [
      {
         "ResourceArn": "string",
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchResources_ResponseSyntax) **   <a name="ARG-SearchResources-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`

 ** [QueryErrors](#API_SearchResources_ResponseSyntax) **   <a name="ARG-SearchResources-response-QueryErrors"></a>
A list of `QueryError` objects. Each error contains an `ErrorCode` and `Message`.
Possible values for `ErrorCode`:
+  `CLOUDFORMATION_STACK_INACTIVE`
+  `CLOUDFORMATION_STACK_NOT_EXISTING`
+  `CLOUDFORMATION_STACK_UNASSUMABLE_ROLE `
Type: Array of [QueryError](API_QueryError.md) objects

 ** [ResourceIdentifiers](#API_SearchResources_ResponseSyntax) **   <a name="ARG-SearchResources-response-ResourceIdentifiers"></a>
The ARNs and resource types of resources that are members of the group that you specified.
Type: Array of [ResourceIdentifier](API_ResourceIdentifier.md) objects

## Errors
<a name="API_SearchResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 401

## Examples
<a name="API_SearchResources_Examples"></a>

### Example
<a name="API_SearchResources_Example_1"></a>

The following example retrieves a list of resources of all types that are tagged with a key of `Stage` and a value of either `Test` or `Prod`.

#### Sample Request
<a name="API_SearchResources_Example_1_Request"></a>

```
POST /resources/search HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.search-resources
X-Amz-Date: 20220120T213215Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 176

{
    "ResourceQuery": {
        "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\",\"Prod\"]}]}",
        "Type": "TAG_FILTERS_1_0"
    }
}
```

#### Sample Response
<a name="API_SearchResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 21:32:15 GMT
Content-Type: application/json
Content-Length: 161
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "ResourceIdentifiers": [
        {
            "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:dhcp-options/dopt-1a2b3c4d",
            "ResourceType": "AWS::EC2::DHCPOptions"
        }
    ],
    "QueryErrors": []
}
```

## See Also
<a name="API_SearchResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/SearchResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/SearchResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

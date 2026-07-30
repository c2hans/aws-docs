---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroupQuery.html
---

# UpdateGroupQuery
<a name="API_UpdateGroupQuery"></a>

Updates the resource query of a group. For more information about resource queries, see [Create a tag-based group in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag).

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:UpdateGroupQuery`

## Request Syntax
<a name="API_UpdateGroupQuery_RequestSyntax"></a>

```
POST /update-group-query HTTP/1.1
Content-type: application/json

{
   "Group": "{{string}}",
   "GroupName": "{{string}}",
   "ResourceQuery": {
      "Query": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateGroupQuery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateGroupQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceQuery](#API_UpdateGroupQuery_RequestSyntax) **   <a name="ARG-UpdateGroupQuery-request-ResourceQuery"></a>
The resource query to determine which AWS resources are members of this resource group.
A resource group can contain either a `Configuration` or a `ResourceQuery`, but not both.
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: Yes

 ** [Group](#API_UpdateGroupQuery_RequestSyntax) **   <a name="ARG-UpdateGroupQuery-request-Group"></a>
The name or the Amazon resource name (ARN) of the resource group to query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

 ** [GroupName](#API_UpdateGroupQuery_RequestSyntax) **   <a name="ARG-UpdateGroupQuery-request-GroupName"></a>
 *This parameter has been deprecated.*
Don't use this parameter. Use `Group` instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: No

## Response Syntax
<a name="API_UpdateGroupQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupQuery": {
      "GroupName": "string",
      "ResourceQuery": {
         "Query": "string",
         "Type": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateGroupQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupQuery](#API_UpdateGroupQuery_ResponseSyntax) **   <a name="ARG-UpdateGroupQuery-response-GroupQuery"></a>
The updated resource query associated with the resource group after the update.
Type: [GroupQuery](API_GroupQuery.md) object

## Errors
<a name="API_UpdateGroupQuery_Errors"></a>

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

 ** NotFoundException **
One or more of the specified resources don't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

## Examples
<a name="API_UpdateGroupQuery_Examples"></a>

### Example
<a name="API_UpdateGroupQuery_Example_1"></a>

The following example updates the query of the specified resource group. A resource group query requires that you supply both a `Type` parameter and a `Query` string parameter. The `Query` parameter is a JSON representation of the query as a single string.

#### Sample Request
<a name="API_UpdateGroupQuery_Example_1_Request"></a>

```
POST /update-group-query HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.update-group-query
X-Amz-Date: 20220120T225422Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 197

{
    "GroupName": "MyTest",
    "ResourceQuery": {
        "Type": "TAG_FILTERS_1_0",
        "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}"}}
```

#### Sample Response
<a name="API_UpdateGroupQuery_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 22:54:23 GMT
Content-Type: application/json
Content-Length: 206
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "GroupQuery":{
        "GroupName":"MyTest",
        "ResourceQuery":{
            "Type":"TAG_FILTERS_1_0",
            "Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}"
        }
    }
}
```

## See Also
<a name="API_UpdateGroupQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/UpdateGroupQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/UpdateGroupQuery)

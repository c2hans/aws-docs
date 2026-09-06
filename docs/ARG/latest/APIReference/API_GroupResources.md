---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupResources.html
---

# GroupResources
<a name="API_GroupResources"></a>

Adds the specified resources to the specified group.

**Important**
You can only use this operation with the following groups:
 `AWS::EC2::HostManagement`
 `AWS::EC2::CapacityReservationPool`
 `AWS::ResourceGroups::ApplicationGroup`
Other resource group types and resource types are not currently supported by this operation.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:GroupResources`

## Request Syntax
<a name="API_GroupResources_RequestSyntax"></a>

```
POST /group-resources HTTP/1.1
Content-type: application/json

{
   "Group": "{{string}}",
   "ResourceArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GroupResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GroupResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Group](#API_GroupResources_RequestSyntax) **   <a name="ARG-GroupResources-request-Group"></a>
The name or the Amazon resource name (ARN) of the resource group to add resources to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

 ** [ResourceArns](#API_GroupResources_RequestSyntax) **   <a name="ARG-GroupResources-request-ResourceArns"></a>
The list of Amazon resource names (ARNs) of the resources to be added to the group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_GroupResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Failed": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ResourceArn": "string"
      }
   ],
   "Pending": [
      {
         "ResourceArn": "string"
      }
   ],
   "Succeeded": [ "string" ]
}
```

## Response Elements
<a name="API_GroupResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_GroupResources_ResponseSyntax) **   <a name="ARG-GroupResources-response-Failed"></a>
A list of Amazon resource names (ARNs) of any resources that this operation failed to add to the group.
Type: Array of [FailedResource](API_FailedResource.md) objects

 ** [Pending](#API_GroupResources_ResponseSyntax) **   <a name="ARG-GroupResources-response-Pending"></a>
A list of Amazon resource names (ARNs) of any resources that this operation is still in the process adding to the group. These pending additions continue asynchronously. You can check the status of pending additions by using the ` ListGroupResources ` operation, and checking the `Resources` array in the response and the `Status` field of each object in that array.
Type: Array of [PendingResource](API_PendingResource.md) objects

 ** [Succeeded](#API_GroupResources_ResponseSyntax) **   <a name="ARG-GroupResources-response-Succeeded"></a>
A list of Amazon resource names (ARNs) of the resources that this operation successfully added to the group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`

## Errors
<a name="API_GroupResources_Errors"></a>

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
<a name="API_GroupResources_Examples"></a>

### Example
<a name="API_GroupResources_Example_1"></a>

The following example adds two Amazon EC2 capacity reservations to the specified resource group. The group is configured to allow only capacity reservations as group members.

#### Sample Request
<a name="API_GroupResources_Example_1_Request"></a>

```
POST /group-resources HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.group-resources
X-Amz-Date: 20220114T203701Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 199

{
    "Group": "CRPGroup",
    "ResourceArns": [
        "arn:aws:ec2:us-west-2:123456789012:capacity-reservation/cr-0070b00d13EXAMPLE",
        "arn:aws:ec2:us-west-2:123456789012:capacity-reservation/cr-061abec820EXAMPLE"
    ]
}
```

#### Sample Response
<a name="API_GroupResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 14 Jan 2022 20:37:01 GMT
Content-Type: application/json
Content-Length: 119
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Succeeded":[
        "arn:aws:ec2:us-west-2:123456789012:capacity-reservation/cr-0070b00d13EXAMPLE",
        "arn:aws:ec2:us-west-2:123456789012:capacity-reservation/cr-061abec820EXAMPLE"
    ],
    "Failed":[],
    "Pending":[]
}
```

## See Also
<a name="API_GroupResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/GroupResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupResources)

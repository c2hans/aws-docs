---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroups.html
---

# ListGroups
<a name="API_ListGroups"></a>

Returns a list of existing Resource Groups in your account.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:ListGroups`

## Request Syntax
<a name="API_ListGroups_RequestSyntax"></a>

```
POST /groups-list?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_ListGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListGroups_RequestSyntax) **   <a name="ARG-ListGroups-request-uri-MaxResults"></a>
The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListGroups_RequestSyntax) **   <a name="ARG-ListGroups-request-uri-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value provided by a previous call's `NextToken` response to indicate where the output should continue from.
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`

## Request Body
<a name="API_ListGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListGroups_RequestSyntax) **   <a name="ARG-ListGroups-request-Filters"></a>
Filters, formatted as [GroupFilter](API_GroupFilter.md) objects, that you want to apply to a `ListGroups` operation.
+  `resource-type` - Filter the results to include only those resource groups that have the specified resource type in their `ResourceTypeFilter`. For example, `AWS::EC2::Instance` would return any resource group with a `ResourceTypeFilter` that includes `AWS::EC2::Instance`.
+  `configuration-type` - Filter the results to include only those groups that have the specified configuration types attached. The current supported values are:
  +  `AWS::ResourceGroups::ApplicationGroup`
  +  `AWS::AppRegistry::Application`
  +  `AWS::AppRegistry::ApplicationResourceGroup`
  +  `AWS::CloudFormation::Stack`
  +  `AWS::EC2::CapacityReservationPool`
  +  `AWS::EC2::HostManagement`
  +  `AWS::NetworkFirewall::RuleGroup`
Type: Array of [GroupFilter](API_GroupFilter.md) objects
Required: No

## Response Syntax
<a name="API_ListGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupIdentifiers": [
      {
         "Criticality": number,
         "Description": "string",
         "DisplayName": "string",
         "GroupArn": "string",
         "GroupName": "string",
         "Owner": "string"
      }
   ],
   "Groups": [
      {
         "ApplicationTag": {
            "string" : "string"
         },
         "Criticality": number,
         "Description": "string",
         "DisplayName": "string",
         "GroupArn": "string",
         "Name": "string",
         "Owner": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupIdentifiers](#API_ListGroups_ResponseSyntax) **   <a name="ARG-ListGroups-response-GroupIdentifiers"></a>
A list of [GroupIdentifier](API_GroupIdentifier.md) objects. Each identifier is an object that contains both the `Name` and the `GroupArn`.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects

 ** [Groups](#API_ListGroups_ResponseSyntax) **   <a name="ARG-ListGroups-response-Groups"></a>
 * **Deprecated - don't use this field. Use the `GroupIdentifiers` response field instead.** *
Type: Array of [Group](API_Group.md) objects

 ** [NextToken](#API_ListGroups_ResponseSyntax) **   <a name="ARG-ListGroups-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`

## Errors
<a name="API_ListGroups_Errors"></a>

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

## Examples
<a name="API_ListGroups_Examples"></a>

### Example
<a name="API_ListGroups_Example_1"></a>

The following example lists all of the resource groups in the specified AWS Region and account.

#### Sample Request
<a name="API_ListGroups_Example_1_Request"></a>

```
POST /groups-list HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.list-groups
X-Amz-Date: 20220119T231526Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 0
```

#### Sample Response
<a name="API_ListGroups_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 19 Jan 2022 23:15:26 GMT
Content-Type: application/json
Content-Length: 5655
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "GroupIdentifiers": [
        {
            "GroupName": "Group1",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/Group1",
            "OwnerId": "123456789012"
        },
        {
            "GroupName": "Group2",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/Group2",
            "OwnerId": "123456789012"
        },
        {
            "GroupName": "Group3",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/Group3",
            "OwnerId": "123456789012"
        }
    ],
    "Groups": [  ... DEPRECATED ... DO NOT USE ... ]
}
```

### Example
<a name="API_ListGroups_Example_2"></a>

The following example lists all resource groups that are configured with a configure type of `AWS::EC2::HostMangement`.

#### Sample Request
<a name="API_ListGroups_Example_2_Request"></a>

```
POST /groups-list HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.list-groups
X-Amz-Date: 20220119T232648Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 85

{
    "Filters": [
        {
            "Name": "configuration-type",
            "Values": [
                "AWS::EC2::HostManagement"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListGroups_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 19 Jan 2022 23:26:48 GMT
Content-Type: application/json
Content-Length: 621
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "GroupIdentifiers": [
        {
            "GroupName": "HostManagementGroup1",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/HostManagementGroup1",
            "OwnerId": "123456789012"
        },
        {
            "GroupName": "HostManagementGroup2",
            "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/HostManagementGroup2",
            "OwnerId": "123456789012"
        }
    ],
    "Groups": [ ... DEPRECATED ... DO NOT USE ... ]
}
```

## See Also
<a name="API_ListGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/ListGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListGroups)

---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_CreateGroup.html
---

# CreateGroup
<a name="API_CreateGroup"></a>

Creates a resource group with the specified name and description. You can optionally include either a resource query or a service configuration. For more information about constructing a resource query, see [Build queries and groups in AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/getting_started-query.html) in the * AWS Resource Groups User Guide*. For more information about service-linked groups and service configurations, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:CreateGroup`

## Request Syntax
<a name="API_CreateGroup_RequestSyntax"></a>

```
POST /groups HTTP/1.1
Content-type: application/json

{
   "Configuration": [
      {
         "Parameters": [
            {
               "Name": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "Type": "{{string}}"
      }
   ],
   "Criticality": {{number}},
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "Name": "{{string}}",
   "Owner": "{{string}}",
   "ResourceQuery": {
      "Query": "{{string}}",
      "Type": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Name"></a>
The name of the group, which is the identifier of the group in other operations. You can't change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with `AWS`, `aws`, or any other possible capitalization; these are reserved. A resource group name must be unique within each AWS Region in your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]+`
Required: Yes

 ** [Configuration](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Configuration"></a>
A configuration associates the resource group with an AWS service and specifies how the service can interact with the resources in the group. A configuration is an array of [GroupConfigurationItem](API_GroupConfigurationItem.md) elements. For details about the syntax of service configurations, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).
A resource group can contain either a `Configuration` or a `ResourceQuery`, but not both.
Type: Array of [GroupConfigurationItem](API_GroupConfigurationItem.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** [Criticality](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Criticality"></a>
The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [Description](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Description"></a>
The description of the resource group. Descriptions can consist of letters, numbers, hyphens, underscores, periods, and spaces.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\sa-zA-Z0-9_\.-]*`
Required: No

 ** [DisplayName](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-DisplayName"></a>
The name of the application group, which you can change at any time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [Owner](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Owner"></a>
A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [ResourceQuery](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-ResourceQuery"></a>
The resource query that determines which AWS resources are members of this group. For more information about resource queries, see [Create a tag-based group in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag).
A resource group can contain either a `ResourceQuery` or a `Configuration`, but not both.
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: No

 ** [Tags](#API_CreateGroup_RequestSyntax) **   <a name="ARG-CreateGroup-request-Tags"></a>
The tags to add to the group. A tag is key-value pair string.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": {
      "ApplicationTag": {
         "string" : "string"
      },
      "Criticality": number,
      "Description": "string",
      "DisplayName": "string",
      "GroupArn": "string",
      "Name": "string",
      "Owner": "string"
   },
   "GroupConfiguration": {
      "Configuration": [
         {
            "Parameters": [
               {
                  "Name": "string",
                  "Values": [ "string" ]
               }
            ],
            "Type": "string"
         }
      ],
      "FailureReason": "string",
      "ProposedConfiguration": [
         {
            "Parameters": [
               {
                  "Name": "string",
                  "Values": [ "string" ]
               }
            ],
            "Type": "string"
         }
      ],
      "Status": "string"
   },
   "ResourceQuery": {
      "Query": "string",
      "Type": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_CreateGroup_ResponseSyntax) **   <a name="ARG-CreateGroup-response-Group"></a>
The description of the resource group.
Type: [Group](API_Group.md) object

 ** [GroupConfiguration](#API_CreateGroup_ResponseSyntax) **   <a name="ARG-CreateGroup-response-GroupConfiguration"></a>
The service configuration associated with the resource group. For details about the syntax of a service configuration, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).
Type: [GroupConfiguration](API_GroupConfiguration.md) object

 ** [ResourceQuery](#API_CreateGroup_ResponseSyntax) **   <a name="ARG-CreateGroup-response-ResourceQuery"></a>
The resource query associated with the group. For more information about resource queries, see [Create a tag-based group in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag).
Type: [ResourceQuery](API_ResourceQuery.md) object

 ** [Tags](#API_CreateGroup_ResponseSyntax) **   <a name="ARG-CreateGroup-response-Tags"></a>
The tags associated with the group.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_CreateGroup_Errors"></a>

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
<a name="API_CreateGroup_Examples"></a>

### Example
<a name="API_CreateGroup_Example_1"></a>

The following example creates a resource group in the `us-west-2` Region of the calling account. The resource group has a query that specifies that any resources in the account that are tagged with the key `Stage` and a value of `Test` are members of the group. The group itself (not its members) is tagged with a key named `Department` and a value of `Finance`.

#### Sample Request
<a name="API_CreateGroup_Example_1_Request"></a>

```
POST /groups HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.create-group
X-Amz-Date: 20220113T175008Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 283

{
    "Description": "Resources created for the testing stage.",
    "Name": "QueryGroup",
    "ResourceQuery": {
        "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}",
         "Type": "TAG_FILTERS_1_0"
    },
    "Tags": {"Department": "Finance"}
}
```

```
HTTP/1.1 200 OK
Date: Thu, 13 Jan 2022 17:50:08 GMT
Content-Type: application/json
Content-Length: 384
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Group":{
        "GroupArn":"arn:aws:resource-groups:us-west-2:123456789012:group/QueryGroup",
        "Name":"QueryGroup",
        "Description":"Resources created for the testing stage.",
        "OwnerId":"123456789012"
    },
    "ResourceQuery":{
        "Type":"TAG_FILTERS_1_0",
        "Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"
    },
    "Tags":{"Department":"Finance"}
}
```

### Example
<a name="API_CreateGroup_Example_2"></a>

The following example creates a resource group with a configuration that makes the group serve as a capacity reservation pool by Amazon Elastic Compute Cloud. This group can contain only Amazon EC2 capacity reservations that you add by using the [GroupResources](API_GroupResources.md) operation.

#### Sample Request
<a name="API_CreateGroup_Example_2_Request"></a>

```
POST /groups HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.create-group
X-Amz-Date: 20220113T180534Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>Content-Length: 320
Content-Length: 320

{
    "Name": "CRPGroup",
    "Description": "Resource group for capacity reservations.",
    "Configuration": [
        {
            "Type": "AWS::EC2::CapacityReservationPool"
        },
        {
            "Type": "AWS::ResourceGroups::Generic",
            "Parameters": [
                {
                    "Name": "allowed-resource-types",
                    "Values": [
                        "AWS::EC2::CapacityReservation"
                    ]
                }
            ]
        }
    ],
    "Tags": {
        "Department": "Finance"
    }
}
```

#### Sample Response
<a name="API_CreateGroup_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 13 Jan 2022 18:05:34 GMT
Content-Type: application/json
Content-Length: 561
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "Group":{
        "GroupArn":"arn:aws:resource-groups:us-west-2:123456789012:group/CRPGroup",
        "Name":"CRPGroup",
        "Description":"Resource group for capacity reservations.",
        "OwnerId":"123456789012"
    },
    "Tags":{
        "Department":"Finance"
    },
    "GroupConfiguration":{
        "GroupParameters":[
            {
                "Name":"allowed-resource-types",
                "Values":[
                    "AWS::EC2::CapacityReservation"
                ]
            }
        ],
        "Configuration":[
            {
                "Type":"AWS::EC2::CapacityReservationPool"
            },
            {
                "Type":"AWS::ResourceGroups::Generic",
                "Parameters":[
                    {
                        "Name":"allowed-resource-types",
                        "Values":[
                            "AWS::EC2::CapacityReservation"
                        ]
                    }
                ]
            }
        ],
        "Status": "UPDATE_COMPLETE"
    }
}
```

### Example
<a name="API_CreateGroup_Example_3"></a>

The following example creates a resource group that can contain only Amazon EC2 hosts. Each instance launched into the group is automatically configured to use any of the available core/socket based license configurations you have defined in AWS License Manager.

#### Sample Request
<a name="API_CreateGroup_Example_3_Request"></a>

```
POST /groups HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.create-group
X-Amz-Date: 20220113T182832Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 362

{
    "Name": "HostManagementGroup",
    "Configuration": [
        {
            "Type": "AWS::EC2::HostManagement",
            "Parameters": [
                {
                    "Name": "any-host-based-license-configuration",
                    "Values": [
                        "true"
                    ]
                }
            ]
        },
        {
            "Type": "AWS::ResourceGroups::Generic",
            "Parameters": [
                {
                    "Name": "allowed-resource-types",
                    "Values": [
                        "AWS::EC2::Host"
                    ]
                },
                {
                    "Name": "deletion-protection",
                    "Values": [
                        "UNLESS_EMPTY"
                    ]
                }
            ]
        }
    ]
}
```

```
 role="response">HTTP/1.1 200 OK
Date: Thu, 13 Jan 2022 18:28:33 GMT
Content-Type: application/json
Content-Length: 881
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    Group":{
        "GroupArn":"arn:aws:resource-groups:us-west-2:123456789012:group/HostManagementGroup",
        "Name":"HostManagementGroup",
        "OwnerId":"123456789012"
    },
    "GroupConfiguration":{
        "GroupParameters":[
            {
                "Name":"allowed-resource-types",
                "Values":[
                    "AWS::EC2::Host"
                ]
            },
            {
                "Name":"deletion-protection",
                "Values":[
                    "UNLESS_EMPTY"
                ]
            }
        ],
        "ResourceTypeParameters":[
            {
                "ResourceType":"AWS::EC2::Host",
                "Name":"exclusive-membership",
                "Values":[
                    "ACROSS_SAME_SERVICE_LINK_TYPE"
                ]
            }
        ],
        "ServiceLinkParameters":[
            {
                "Name":"any-host-based-license-configuration",
                "Values":[
                    "true"
                ]
            }
        ],
        "Configuration":[
            {
                "Type":"AWS::EC2::HostManagement",
                "Parameters":[
                    {
                        "Name":"any-host-based-license-configuration",
                        "Values":[
                            "true"
                        ]
                    }
                ]
            },
            {
                "Type":"AWS::ResourceGroups::Generic",
                "Parameters":[
                    {
                        "Name":"allowed-resource-types",
                        "Values":[
                            "AWS::EC2::Host"
                        ]
                    },
                    {
                        "Name":"deletion-protection",
                        "Values":[
                            "UNLESS_EMPTY"
                        ]
                    }
                ]
            }
        ],
        "Status":"UPDATE_COMPLETE"
    }
}
```

## See Also
<a name="API_CreateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/CreateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/CreateGroup)

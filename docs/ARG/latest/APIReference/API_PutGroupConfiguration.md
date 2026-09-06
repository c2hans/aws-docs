---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_PutGroupConfiguration.html
---

# PutGroupConfiguration
<a name="API_PutGroupConfiguration"></a>

Attaches a service configuration to the specified group. This occurs asynchronously, and can take time to complete. You can use [GetGroupConfiguration](API_GetGroupConfiguration.md) to check the status of the update.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:PutGroupConfiguration`

## Request Syntax
<a name="API_PutGroupConfiguration_RequestSyntax"></a>

```
POST /put-group-configuration HTTP/1.1
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
   "Group": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutGroupConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutGroupConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Configuration](#API_PutGroupConfiguration_RequestSyntax) **   <a name="ARG-PutGroupConfiguration-request-Configuration"></a>
The new configuration to associate with the specified group. A configuration associates the resource group with an AWS service and specifies how the service can interact with the resources in the group. A configuration is an array of [GroupConfigurationItem](API_GroupConfigurationItem.md) elements.
For information about the syntax of a service configuration, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html).
A resource group can contain either a `Configuration` or a `ResourceQuery`, but not both.
Type: Array of [GroupConfigurationItem](API_GroupConfigurationItem.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** [Group](#API_PutGroupConfiguration_RequestSyntax) **   <a name="ARG-PutGroupConfiguration-request-Group"></a>
The name or Amazon resource name (ARN) of the resource group with the configuration that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

## Response Syntax
<a name="API_PutGroupConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_PutGroupConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_PutGroupConfiguration_Errors"></a>

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
<a name="API_PutGroupConfiguration_Examples"></a>

### Example 1: Configure a resource group to contain Amazon EC2 capacity reservations
<a name="API_PutGroupConfiguration_Example_1"></a>

The following example attaches a configuration that limits the group to containing Amazon EC2 capacity reservations.

#### Sample Request
<a name="API_PutGroupConfiguration_Example_1_Request"></a>

```
POST /put-group-configuration HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.put-group-configuration
X-Amz-Date: 20220120T204033Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 226

{
    "Group": "CRPGroup",
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
    ]
}
```

#### Sample Response
<a name="API_PutGroupConfiguration_Example_1_Response"></a>

```
HTTP/1.1 202 Accepted
Date: Thu, 20 Jan 2022 20:40:33 GMT
Content-Type: application/json
Content-Length: 337
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "GroupIdentifier": {
        "GroupName": "CRPGroup",
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/CRPGroup"
    },
    "GroupConfiguration": {
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
        ]
    }
}
```

### Example 2: Configure a resource group to contain Amazon EC2 hosts of family type C5 with license support
<a name="API_PutGroupConfiguration_Example_2"></a>

The following example attaches a configuration to the resource group that limits the group to containing only Amazon EC2 hosts and provides settings that are enforced on any Amazon EC2 instances that are launched into this group.

#### Sample Request
<a name="API_PutGroupConfiguration_Example_2_Request"></a>

```
POST /put-group-configuration HTTP/1.1
Host: resource-groups.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.40 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/resource-groups.put-group-configuration
X-Amz-Date: 20220120T204033Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 314

{
    "Group": "HostManagementGroup",
    "Configuration": [
        {
          "Type": "AWS::EC2::HostManagement",
          "Parameters": [
            {
              "Name":"any-host-based-license-configuration",
              "Values":["true"]
            },
            {
              "Name":"allowed-host-families",
              "Values":["c5"]
            }
          ]
        },
        {
          "Type": "AWS::ResourceGroups::Generic",
          "Parameters": [
            {
              "Name": "allowed-resource-types",
              "Values": ["AWS::EC2::Host"]
            },
            {
              "Name": "deletion-protection",
              "Values": ["UNLESS_EMPTY"]
            }
          ]
        }
    ]
}
```

#### Sample Response
<a name="API_PutGroupConfiguration_Example_2_Response"></a>

```
HTTP/1.1 202 Accepted
Date: Thu, 20 Jan 2022 20:40:33 GMT
Content-Type: application/json
Content-Length: 337
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "GroupIdentifier": {
        "GroupName": "HostManagementGroup",
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/HostManagementGroup"
    },
    "GroupConfiguration": {
        "Configuration": [
            {
                "Type": "AWS::EC2::HostManagement",
                "Parameters": [
                    {
                        "Name":"any-host-based-license-configuration",
                        "Values":["true"]
                    },
                    {
                        "Name":"allowed-host-families",
                        "Values":["c5"]
                    }
                ]
            },
            {
              "Type": "AWS::ResourceGroups::Generic",
              "Parameters": [
                {
                  "Name": "allowed-resource-types",
                  "Values": ["AWS::EC2::Host"]
                },
                {
                  "Name": "deletion-protection",
                  "Values": ["UNLESS_EMPTY"]
                }
              ]
            }
        ]
    }
}
```

## See Also
<a name="API_PutGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/PutGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/PutGroupConfiguration)

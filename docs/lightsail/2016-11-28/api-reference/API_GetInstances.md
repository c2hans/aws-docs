---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstances.html
---

# GetInstances
<a name="API_GetInstances"></a>

Returns information about all Amazon Lightsail virtual private servers, or *instances*.

## Request Syntax
<a name="API_GetInstances_RequestSyntax"></a>

```
{
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pageToken](#API_GetInstances_RequestSyntax) **   <a name="Lightsail-GetInstances-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetInstances` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetInstances_ResponseSyntax"></a>

```
{
   "instances": [
      {
         "addOns": [
            {
               "duration": "string",
               "name": "string",
               "nextSnapshotTimeOfDay": "string",
               "snapshotTimeOfDay": "string",
               "status": "string",
               "threshold": "string"
            }
         ],
         "arn": "string",
         "blueprintId": "string",
         "blueprintName": "string",
         "bundleId": "string",
         "createdAt": number,
         "hardware": {
            "cpuCount": number,
            "disks": [
               {
                  "addOns": [
                     {
                        "duration": "string",
                        "name": "string",
                        "nextSnapshotTimeOfDay": "string",
                        "snapshotTimeOfDay": "string",
                        "status": "string",
                        "threshold": "string"
                     }
                  ],
                  "arn": "string",
                  "attachedTo": "string",
                  "attachmentState": "string",
                  "autoMountStatus": "string",
                  "createdAt": number,
                  "gbInUse": number,
                  "iops": number,
                  "isAttached": boolean,
                  "isSystemDisk": boolean,
                  "location": {
                     "availabilityZone": "string",
                     "regionName": "string"
                  },
                  "name": "string",
                  "path": "string",
                  "resourceType": "string",
                  "sizeInGb": number,
                  "state": "string",
                  "supportCode": "string",
                  "tags": [
                     {
                        "key": "string",
                        "value": "string"
                     }
                  ]
               }
            ],
            "ramSizeInGb": number
         },
         "ipAddressType": "string",
         "ipv6Addresses": [ "string" ],
         "isStaticIp": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "metadataOptions": {
            "httpEndpoint": "string",
            "httpProtocolIpv6": "string",
            "httpPutResponseHopLimit": number,
            "httpTokens": "string",
            "state": "string"
         },
         "name": "string",
         "networking": {
            "monthlyTransfer": {
               "gbPerMonthAllocated": number
            },
            "ports": [
               {
                  "accessDirection": "string",
                  "accessFrom": "string",
                  "accessType": "string",
                  "cidrListAliases": [ "string" ],
                  "cidrs": [ "string" ],
                  "commonName": "string",
                  "fromPort": number,
                  "ipv6Cidrs": [ "string" ],
                  "protocol": "string",
                  "toPort": number
               }
            ]
         },
         "privateIpAddress": "string",
         "publicIpAddress": "string",
         "resourceType": "string",
         "sshKeyName": "string",
         "state": {
            "code": number,
            "name": "string"
         },
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "username": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instances](#API_GetInstances_ResponseSyntax) **   <a name="Lightsail-GetInstances-response-instances"></a>
An array of key-value pairs containing information about your instances.
Type: Array of [Instance](API_Instance.md) objects

 ** [nextPageToken](#API_GetInstances_ResponseSyntax) **   <a name="Lightsail-GetInstances-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetInstances` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## Examples
<a name="API_GetInstances_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Get instances
<a name="API_GetInstances_Example_1"></a>

The following example returns all instances in the `us-west-2` AWS Region.

#### Sample Request
<a name="API_GetInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: lightsail.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Lightsail_20161128.GetInstances
Content-Type: application/x-amz-json-1.1
User-Agent: AGENT
X-Amz-Date: 20201019T144314Z
Authorization: AUTHPARAMS
Signature=AUTHPARAMS
Content-Length: 2

{}
```

#### Sample Response
<a name="API_GetInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 22 Apr 2024 14:43:17 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2750
x-amzn-RequestId: aaa1993d-8d60-4a13-899c-bEXAMPLE9bc7
Connection: keep-alive

{
    "instances": [
        {
            "addOns": [
                {
                    "name": "AutoSnapshot",
                    "snapshotTimeOfDay": "06:00",
                    "status": "Enabled"
                }
            ],
            "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/93d19bc4-bd2a-4deb-9048-4EXAMPLE4236",
            "blueprintId": "wordpress",
            "blueprintName": "WordPress",
            "bundleId": "micro_3_0",
            "createdAt": 1.590771192493E9,
            "hardware": {
                "cpuCount": 2,
                "disks": [
                    {
                        "attachedTo": "WordPress-1",
                        "attachmentState": "attached",
                        "createdAt": 1.590771192493E9,
                        "iops": 120,
                        "isSystemDisk": true,
                        "path": "/dev/xvda",
                        "sizeInGb": 40
                    }
                ],
                "ramSizeInGb": 1.0
            },
            "isStaticIp": true,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "name": "WordPress-1",
            "networking": {
                "monthlyTransfer": {"gbPerMonthAllocated": 2048},
                "ports": [
                    {
                        "accessDirection": "inbound",
                        "accessFrom": "Anywhere (0.0.0.0/0)",
                        "accessType": "public",
                        "cidrListAliases": [],
                        "cidrs": ["0.0.0.0/0"],
                        "commonName": "",
                        "fromPort": 80,
                        "protocol": "tcp",
                        "toPort": 80
                    },
                    {
                        "accessDirection": "inbound",
                        "accessFrom": "Anywhere (0.0.0.0/0)",
                        "accessType": "public",
                        "cidrListAliases": [],
                        "cidrs": ["0.0.0.0/0"],
                        "commonName": "",
                        "fromPort": 22,
                        "protocol": "tcp",
                        "toPort": 22
                    },
                    {
                        "accessDirection": "inbound",
                        "accessFrom": "Anywhere (0.0.0.0/0)",
                        "accessType": "public",
                        "cidrListAliases": [],
                        "cidrs": ["0.0.0.0/0"],
                        "commonName": "",
                        "fromPort": 443,
                        "protocol": "tcp",
                        "toPort": 443
                    }
                ]
            },
            "privateIpAddress": "192.0.2.1",
            "publicIpAddress": "192.0.2.2",
            "resourceType": "Instance",
            "sshKeyName": "LightsailDefaultKeyPair",
            "state": {
                "code": 16,
                "name": "running"
            },
            "supportCode": "1234567890/i-0dEXAMPLE1abad00e",
            "tags": [],
            "username": "bitnami"
        },
        {
            "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd08b156-5c35-4b89-9e90-8EXAMPLEd006",
            "blueprintId": "amazon_linux_2023",
            "blueprintName": "Amazon Linux 2023",
            "bundleId": "nano_3_0",
            "createdAt": 1.591802416964E9,
            "hardware": {
                "cpuCount": 2,
                "disks": [
                    {
                        "attachedTo": "Amazon_Linux-2023",
                        "attachmentState": "attached",
                        "createdAt": 1.591802416964E9,
                        "iops": 3000,
                        "isSystemDisk": true,
                        "path": "/dev/xvda",
                        "sizeInGb": 20
                    }
                ],
                "ramSizeInGb": 0.5
            },
            "isStaticIp": true,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "name": "Amazon_Linux-1",
            "networking": {
                "monthlyTransfer": {"gbPerMonthAllocated": 1024},
                "ports": [
                    {
                        "accessDirection": "inbound",
                        "accessFrom": "Anywhere (0.0.0.0/0)",
                        "accessType": "public",
                        "cidrListAliases": [],
                        "cidrs": ["0.0.0.0/0"],
                        "commonName": "",
                        "fromPort": 80,
                        "protocol": "tcp",
                        "toPort": 80
                    },
                    {
                        "accessDirection": "inbound",
                        "accessFrom": "Anywhere (0.0.0.0/0)",
                        "accessType": "public",
                        "cidrListAliases": [],
                        "cidrs": ["0.0.0.0/0"],
                        "commonName": "",
                        "fromPort": 22,
                        "protocol": "tcp",
                        "toPort": 22
                    }
                ]
            },
            "privateIpAddress": "192.0.2.3",
            "publicIpAddress": "192.0.2.4",
            "resourceType": "Instance",
            "sshKeyName": "LightsailDefaultKeyPair",
            "state": {
                "code": 16,
                "name": "running"
            },
            "supportCode": "1234567890/i-0dEXAMPLE1abad00e",
            "tags": [],
            "username": "ec2-user"
        }
    ]
}
```

## See Also
<a name="API_GetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceInformation.html
---

# DescribeInstanceInformation
<a name="API_DescribeInstanceInformation"></a>

Provides information about one or more of your managed nodes, including the operating system platform, SSM Agent version, association status, and IP address. This operation does not return information for nodes that are either Stopped or Terminated.

If you specify one or more node IDs, the operation returns information for those managed nodes. If you don't specify node IDs, it returns information for all your managed nodes. If you specify a node ID that isn't valid or a node that you don't own, you receive an error.

**Note**
The `IamRole` field returned for this API operation is the role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.

## Request Syntax
<a name="API_DescribeInstanceInformation_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "InstanceInformationFilterList": [
      {
         "key": "{{string}}",
         "valueSet": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstanceInformation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeInstanceInformation_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-request-Filters"></a>
One or more filters. Use a filter to return a more specific list of managed nodes. You can filter based on tags applied to your managed nodes. Tag filters can't be combined with other filter types. Use this `Filters` data type instead of `InstanceInformationFilterList`, which is deprecated.
Type: Array of [InstanceInformationStringFilter](API_InstanceInformationStringFilter.md) objects
Array Members: Minimum number of 0 items.
Required: No

 ** [InstanceInformationFilterList](#API_DescribeInstanceInformation_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-request-InstanceInformationFilterList"></a>
This is a legacy method. We recommend that you don't use this method. Instead, use the `Filters` data type. `Filters` enables you to return node information by filtering based on tags applied to managed nodes.
Attempting to use `InstanceInformationFilterList` and `Filters` leads to an exception error.
Type: Array of [InstanceInformationFilter](API_InstanceInformationFilter.md) objects
Array Members: Minimum number of 0 items.
Required: No

 ** [MaxResults](#API_DescribeInstanceInformation_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. The default value is 10 items.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeInstanceInformation_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInstanceInformation_ResponseSyntax"></a>

```
{
   "InstanceInformationList": [
      {
         "ActivationId": "string",
         "AgentVersion": "string",
         "AssociationOverview": {
            "DetailedStatus": "string",
            "InstanceAssociationStatusAggregatedCount": {
               "string" : number
            }
         },
         "AssociationStatus": "string",
         "ComputerName": "string",
         "IamRole": "string",
         "InstanceId": "string",
         "IPAddress": "string",
         "IsLatestVersion": boolean,
         "LastAssociationExecutionDate": number,
         "LastPingDateTime": number,
         "LastSuccessfulAssociationExecutionDate": number,
         "Name": "string",
         "PingStatus": "string",
         "PlatformName": "string",
         "PlatformType": "string",
         "PlatformVersion": "string",
         "RegistrationDate": number,
         "ResourceType": "string",
         "SourceId": "string",
         "SourceLocation": "string",
         "SourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInstanceInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceInformationList](#API_DescribeInstanceInformation_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-response-InstanceInformationList"></a>
The managed node information list.
Type: Array of [InstanceInformation](API_InstanceInformation.md) objects

 ** [NextToken](#API_DescribeInstanceInformation_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceInformation-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeInstanceInformation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidInstanceInformationFilterValue **
The specified filter value isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstanceInformation_Examples"></a>

### Example
<a name="API_DescribeInstanceInformation_Example_1"></a>

This example illustrates one usage of DescribeInstanceInformation.

#### Sample Request
<a name="API_DescribeInstanceInformation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeInstanceInformation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T234247Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 72

{
    "Filters": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-02573cafcfEXAMPLE"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeInstanceInformation_Example_1_Response"></a>

```
{
    "InstanceInformationList": [
        {
            "AgentVersion": "2.3.871.0",
            "AssociationOverview": {
                "DetailedStatus": "Failed",
                "InstanceAssociationStatusAggregatedCount": {
                    "Failed": 1,
                    "Success": 1
                }
            },
            "AssociationStatus": "Failed",
            "ComputerName": "WIN-11RMS222RPK.WORKGROUP",
            "IPAddress": "203.0.113.0",
            "InstanceId": "i-02573cafcfEXAMPLE",
            "IsLatestVersion": false,
            "LastAssociationExecutionDate": 1582242019,
            "LastPingDateTime": 1582242018.094,
            "PingStatus": "Online",
            "PlatformName": "Microsoft Windows Server 2008 R2 Datacenter",
            "PlatformType": "Windows",
            "PlatformVersion": "6.1.7601",
            "ResourceType": "EC2Instance"
        }
    ]
}
```

## See Also
<a name="API_DescribeInstanceInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstanceInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstanceInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

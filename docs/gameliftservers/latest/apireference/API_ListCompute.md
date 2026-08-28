---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListCompute.html
---

# ListCompute
<a name="API_ListCompute"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves information on the compute resources in an Amazon GameLift Servers fleet. Use the pagination parameters to retrieve results in a set of sequential pages.

 **Request options**
+ Retrieve a list of all computes in a fleet. Specify a fleet ID.
+ Retrieve a list of all computes in a specific fleet location. Specify a fleet ID and location.
+ Retrieve a list of managed container fleets based on compute status. Specify a fleet ID, status, and (optionally) location.

 **Results**

If successful, this operation returns information on a set of computes. Depending on the type of fleet, the result includes the following information:
+ For a managed EC2 fleet (compute type `EC2`), this operation returns information about the EC2 instance. Compute names are EC2 instance IDs.
+ For an Anywhere fleet (compute type `ANYWHERE`), this operation returns compute names and details from when the compute was registered with `RegisterCompute`. This includes `GameLiftServiceSdkEndpoint` or `GameLiftAgentEndpoint`.
+ For a managed container fleet, this operation returns information about the fleet's container groups and the instances they're running on. Compute names refer to game server container groups, which can include multiple containers.

## Request Syntax
<a name="API_ListCompute_RequestSyntax"></a>

```
{
   "ComputeStatus": "{{string}}",
   "ContainerGroupDefinitionName": "{{string}}",
   "FleetId": "{{string}}",
   "Limit": {{number}},
   "Location": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCompute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-FleetId"></a>
A unique identifier for the fleet to retrieve compute resources for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [ComputeStatus](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-ComputeStatus"></a>
The status of computes in a managed container fleet, based on the success of the latest update deployment.
+  `ACTIVE` -- The compute is deployed with the correct container definitions. It is ready to process game servers and host game sessions.
+  `IMPAIRED` -- An update deployment to the compute failed, and the compute is deployed with incorrect container definitions.
Type: String
Valid Values: `ACTIVE | IMPAIRED`
Required: No

 ** [ContainerGroupDefinitionName](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-ContainerGroupDefinitionName"></a>
For computes in a managed container fleet, the name of the deployed container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [Limit](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Location](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-Location"></a>
The name of a location to retrieve compute resources for. For an Amazon GameLift Servers Anywhere fleet, use a custom location. For a managed fleet, provide a AWS Region or Local Zone code (for example: `us-west-2` or `us-west-2-lax-1`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_ListCompute_RequestSyntax) **   <a name="gameliftservers-ListCompute-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListCompute_ResponseSyntax"></a>

```
{
   "ComputeList": [
      {
         "ComputeArn": "string",
         "ComputeName": "string",
         "ComputeStatus": "string",
         "ContainerAttributes": [
            {
               "ContainerName": "string",
               "ContainerRuntimeId": "string"
            }
         ],
         "CreationTime": number,
         "DnsName": "string",
         "FleetArn": "string",
         "FleetId": "string",
         "GameLiftAgentEndpoint": "string",
         "GameLiftServiceSdkEndpoint": "string",
         "GameServerContainerGroupDefinitionArn": "string",
         "InstanceId": "string",
         "IpAddress": "string",
         "Location": "string",
         "OperatingSystem": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCompute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeList](#API_ListCompute_ResponseSyntax) **   <a name="gameliftservers-ListCompute-response-ComputeList"></a>
A list of compute resources in the specified fleet.
Type: Array of [Compute](API_Compute.md) objects

 ** [NextToken](#API_ListCompute_ResponseSyntax) **   <a name="gameliftservers-ListCompute-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListCompute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_ListCompute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListCompute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListCompute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

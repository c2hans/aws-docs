---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceProperties.html
---

# DescribeInstanceProperties
<a name="API_DescribeInstanceProperties"></a>

An API operation used by the Systems Manager console to display information about Systems Manager managed nodes.

## Request Syntax
<a name="API_DescribeInstanceProperties_RequestSyntax"></a>

```
{
   "FiltersWithOperator": [
      {
         "Key": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "InstancePropertyFilterList": [
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
<a name="API_DescribeInstanceProperties_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FiltersWithOperator](#API_DescribeInstanceProperties_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-request-FiltersWithOperator"></a>
The request filters to use with the operator.
Type: Array of [InstancePropertyStringFilter](API_InstancePropertyStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: No

 ** [InstancePropertyFilterList](#API_DescribeInstanceProperties_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-request-InstancePropertyFilterList"></a>
An array of instance property filters.
Type: Array of [InstancePropertyFilter](API_InstancePropertyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: No

 ** [MaxResults](#API_DescribeInstanceProperties_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-request-MaxResults"></a>
The maximum number of items to return for the call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 ** [NextToken](#API_DescribeInstanceProperties_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-request-NextToken"></a>
The token provided by a previous request to use to return the next set of properties.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInstanceProperties_ResponseSyntax"></a>

```
{
   "InstanceProperties": [
      {
         "ActivationId": "string",
         "AgentVersion": "string",
         "Architecture": "string",
         "AssociationOverview": {
            "DetailedStatus": "string",
            "InstanceAssociationStatusAggregatedCount": {
               "string" : number
            }
         },
         "AssociationStatus": "string",
         "AvailabilityZone": "string",
         "ComputerName": "string",
         "IamRole": "string",
         "InstanceId": "string",
         "InstanceRole": "string",
         "InstanceState": "string",
         "InstanceType": "string",
         "IPAddress": "string",
         "KeyName": "string",
         "LastAssociationExecutionDate": number,
         "LastPingDateTime": number,
         "LastSuccessfulAssociationExecutionDate": number,
         "LaunchTime": number,
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
<a name="API_DescribeInstanceProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceProperties](#API_DescribeInstanceProperties_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-response-InstanceProperties"></a>
Properties for the managed instances.
Type: Array of [InstanceProperty](API_InstanceProperty.md) objects

 ** [NextToken](#API_DescribeInstanceProperties_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceProperties-response-NextToken"></a>
The token for the next set of properties to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeInstanceProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidActivationId **
The activation ID isn't valid. Verify that you entered the correct ActivationId or ActivationCode and try again.
HTTP Status Code: 400

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

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

 ** InvalidInstancePropertyFilterValue **
The specified filter value isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInstanceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstanceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstanceProperties)

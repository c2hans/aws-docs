---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeregisterCompute.html
---

# DeregisterCompute
<a name="API_DeregisterCompute"></a>

 **This API works with the following fleet types:** Anywhere

Removes a compute resource from an Anywhere fleet. Deregistered computes can no longer host game sessions through Amazon GameLift Servers. Use this operation with an Anywhere fleet that doesn't use the Amazon GameLift Servers Agent For Anywhere fleets with the Agent, the Agent handles all compute registry tasks for you.

To deregister a compute, call this operation from the compute that's being deregistered and specify the compute name and the fleet ID.

## Request Syntax
<a name="API_DeregisterCompute_RequestSyntax"></a>

```
{
   "ComputeName": "{{string}}",
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterCompute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ComputeName](#API_DeregisterCompute_RequestSyntax) **   <a name="gameliftservers-DeregisterCompute-request-ComputeName"></a>
The unique identifier of the compute resource to deregister. For an Anywhere fleet compute, use the registered compute name.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: Yes

 ** [FleetId](#API_DeregisterCompute_RequestSyntax) **   <a name="gameliftservers-DeregisterCompute-request-FleetId"></a>
A unique identifier for the fleet the compute resource is currently registered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Elements
<a name="API_DeregisterCompute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterCompute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterCompute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeregisterCompute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeregisterCompute)

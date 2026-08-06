---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteScalingPolicy.html
---

# DeleteScalingPolicy
<a name="API_DeleteScalingPolicy"></a>

 **This API works with the following fleet types:** EC2, Container

Deletes a fleet scaling policy. Once deleted, the policy is no longer in force and Amazon GameLift Servers removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.

To temporarily suspend scaling policies, use [StopFleetActions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html). This operation suspends all policies for the fleet.

## Request Syntax
<a name="API_DeleteScalingPolicy_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DeleteScalingPolicy_RequestSyntax) **   <a name="gameliftservers-DeleteScalingPolicy-request-FleetId"></a>
A unique identifier for the fleet to be deleted. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Name](#API_DeleteScalingPolicy_RequestSyntax) **   <a name="gameliftservers-DeleteScalingPolicy-request-Name"></a>
A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Elements
<a name="API_DeleteScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteScalingPolicy_Errors"></a>

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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteScalingPolicy_Examples"></a>

### Delete a scaling policy
<a name="API_DeleteScalingPolicy_Example_1"></a>

To delete a policy, we must specify both the fleet ID and name. The combination of these two values is what uniquely identifies the policy. Once a delete request is received, the policy is put into status DELETING and no longer affects the fleet's scaling activity.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DeleteScalingPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 336
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.DeleteScalingPolicy

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Name": "My_Target_Policy_1"
    }
}

CLI syntax:

$aws gamelift delete-scaling-policy
--fleet-id "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
--name "My_Target_Policy_1"
```

#### Sample Response
<a name="API_DeleteScalingPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK undefined
```

## See Also
<a name="API_DeleteScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteScalingPolicy)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateTrafficDistributionGroupUser.html
---

# AssociateTrafficDistributionGroupUser
<a name="API_AssociateTrafficDistributionGroupUser"></a>

Associates an agent with a traffic distribution group. This API can be called only in the Region where the traffic distribution group is created.

## Request Syntax
<a name="API_AssociateTrafficDistributionGroupUser_RequestSyntax"></a>

```
PUT /traffic-distribution-group/{{TrafficDistributionGroupId}}/user HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateTrafficDistributionGroupUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrafficDistributionGroupId](#API_AssociateTrafficDistributionGroupUser_RequestSyntax) **   <a name="connect-AssociateTrafficDistributionGroupUser-request-uri-TrafficDistributionGroupId"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_AssociateTrafficDistributionGroupUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_AssociateTrafficDistributionGroupUser_RequestSyntax) **   <a name="connect-AssociateTrafficDistributionGroupUser-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_AssociateTrafficDistributionGroupUser_RequestSyntax) **   <a name="connect-AssociateTrafficDistributionGroupUser-request-UserId"></a>
The identifier of the user account. This can be the ID or the ARN of the user.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateTrafficDistributionGroupUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateTrafficDistributionGroupUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateTrafficDistributionGroupUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_AssociateTrafficDistributionGroupUser_Examples"></a>

### Example
<a name="API_AssociateTrafficDistributionGroupUser_Example_1"></a>

The following example associates an agent with a traffic distribution group.

#### Sample Request
<a name="API_AssociateTrafficDistributionGroupUser_Example_1_Request"></a>

```
PUT connect.[region].amazonaws.com/traffic-distribution-group/[traffic_distribution_group_id]/user
{
   "InstanceId": "[instance_id]",
   "UserId": "[user_id]"
}
```

#### Sample Response
<a name="API_AssociateTrafficDistributionGroupUser_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_AssociateTrafficDistributionGroupUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateTrafficDistributionGroupUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateTrafficDistributionGroupUser)

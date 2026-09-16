---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeInstance.html
---

# DescribeInstance
<a name="API_DescribeInstance"></a>

This API is in preview release for Connect Customer and is subject to change.

Returns the current state of the specified instance identifier. It tracks the instance while it is being created and returns an error status, if applicable.

If an instance is not created successfully, the instance status reason field returns details relevant to the reason. The instance in a failed state is returned only for 24 hours after the CreateInstance API was invoked.

## Request Syntax
<a name="API_DescribeInstance_RequestSyntax"></a>

```
GET /instance/{{InstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeInstance_RequestSyntax) **   <a name="connect-DescribeInstance-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Instance": {
      "Arn": "string",
      "CreatedTime": number,
      "Id": "string",
      "IdentityManagementType": "string",
      "InboundCallsEnabled": boolean,
      "InstanceAccessUrl": "string",
      "InstanceAlias": "string",
      "InstanceStatus": "string",
      "OutboundCallsEnabled": boolean,
      "ServiceRole": "string",
      "StatusReason": {
         "Message": "string"
      },
      "Tags": {
         "string" : "string"
      }
   },
   "ReplicationConfiguration": {
      "GlobalSignInEndpoint": "string",
      "ReplicationStatusSummaryList": [
         {
            "Region": "string",
            "ReplicationStatus": "string",
            "ReplicationStatusReason": "string"
         }
      ],
      "SourceRegion": "string"
   }
}
```

## Response Elements
<a name="API_DescribeInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instance](#API_DescribeInstance_ResponseSyntax) **   <a name="connect-DescribeInstance-response-Instance"></a>
The name of the instance.
Type: [Instance](API_Instance.md) object

 ** [ReplicationConfiguration](#API_DescribeInstance_ResponseSyntax) **   <a name="connect-DescribeInstance-response-ReplicationConfiguration"></a>
Status information about the replication process. This field is included only when you are using the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API to replicate an Connect Customer instance across AWS Regions. For information about replicating Connect Customer instances, see [Create a replica of your existing Connect Customer instance](https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html) in the *Connect Customer Administrator Guide*.
Type: [ReplicationConfiguration](API_ReplicationConfiguration.md) object

## Errors
<a name="API_DescribeInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_DescribeInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeInstance)

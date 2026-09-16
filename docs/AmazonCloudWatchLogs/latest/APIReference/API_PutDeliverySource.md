---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html
---

# PutDeliverySource
<a name="API_PutDeliverySource"></a>

Creates or updates a logical *delivery source*. A delivery source represents an AWS resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, Firehose or X-Ray for sending traces.

To configure logs delivery between a delivery destination and an AWS service that is supported as a delivery source, you must do the following:
+ Use `PutDeliverySource` to create a delivery source, which is a logical object that represents the resource that is actually sending the logs.
+ Use `PutDeliveryDestination` to create a *delivery destination*, which is a logical object that represents the actual delivery destination. For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).
+ If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
+ Use `CreateDelivery` to create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

Only some AWS services support being configured as a delivery source. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

If you use this operation to update an existing delivery source, all the current delivery source parameters are overwritten with the new parameter values that you specify.

## Request Syntax
<a name="API_PutDeliverySource_RequestSyntax"></a>

```
{
   "deliverySourceConfiguration": {
      "{{string}}" : "{{string}}"
   },
   "logType": "{{string}}",
   "name": "{{string}}",
   "resourceArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PutDeliverySource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliverySourceConfiguration](#API_PutDeliverySource_RequestSyntax) **   <a name="CWL-PutDeliverySource-request-deliverySourceConfiguration"></a>
A map of key-value pairs to configure the delivery source. Both keys and values must be between 1 and 255 characters in length. For example, `{"samplingRate": "50"}`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [logType](#API_PutDeliverySource_RequestSyntax) **   <a name="CWL-PutDeliverySource-request-logType"></a>
Defines the type of log that the source is sending.
+ For Application Load Balancer, the valid values are `ALB_ACCESS_LOGS`, `ALB_CONNECTION_LOGS`, and `ALB_HEALTH_CHECK_LOGS`.
+ For Amazon Bedrock Agents, the valid values are `APPLICATION_LOGS` and `EVENT_LOGS`.
+ For Amazon Bedrock Knowledge Bases, the valid values are `APPLICATION_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Runtime, the valid values are `APPLICATION_LOGS`, `USAGE_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Tools, the valid values are `APPLICATION_LOGS`, `USAGE_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Identity, the valid values are `APPLICATION_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Memory, the valid values are `APPLICATION_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Gateway, the valid values are `APPLICATION_LOGS` and `TRACES`.
+ For Amazon Bedrock AgentCore Payments, the valid values are `APPLICATION_LOGS` and `TRACES`.
+ For CloudFront, the valid value is `ACCESS_LOGS`.
+ For DevOps Agent, the valid value is `APPLICATION_LOGS`.
+ For Amazon CodeWhisperer, the valid value is `EVENT_LOGS`.
+ For Elemental MediaPackage, the valid values are `EGRESS_ACCESS_LOGS` and `INGRESS_ACCESS_LOGS`.
+ For Elemental MediaTailor, the valid values are `AD_DECISION_SERVER_LOGS`, `MANIFEST_SERVICE_LOGS`, and `TRANSCODE_LOGS`.
+ For Amazon EKS Auto Mode, the valid values are `AUTO_MODE_BLOCK_STORAGE_LOGS`, `AUTO_MODE_COMPUTE_LOGS`, `AUTO_MODE_IPAM_LOGS`, and `AUTO_MODE_LOAD_BALANCING_LOGS`.
+ For Amazon EKS Capability Logs, the valid values are `EKS_CAPABILITY_ACK_LOGS`, `EKS_CAPABILITY_ARGOCD_APPLICATION_LOGS`, `EKS_CAPABILITY_ARGOCD_APPLICATIONSET_LOGS`, `EKS_CAPABILITY_ARGOCD_COMMITSERVER_LOGS`, `EKS_CAPABILITY_ARGOCD_REPOSERVER_LOGS`, `EKS_CAPABILITY_ARGOCD_SERVER_LOGS`, and `EKS_CAPABILITY_KRO_LOGS`.
+ For AWS Entity Resolution, the valid value is `WORKFLOW_LOGS`.
+ For IAM Identity Center, the valid value is `ERROR_LOGS`.
+ For Network Firewall Proxy, the valid values are `ALERT_LOGS`, `ALLOW_LOGS`, and `DENY_LOGS`.
+ For Network Load Balancer, the valid value is `NLB_ACCESS_LOGS`.
+ For AWS PCS, the valid values are `PCS_SCHEDULER_LOGS`, `PCS_JOBCOMP_LOGS`, and `PCS_SCHEDULER_AUDIT_LOGS`.
+ For Quick, the valid values are `AGENT_HOURS_LOGS`, `CHAT_LOGS`, `FEEDBACK_LOGS`, and `INDEX_USAGE_LOGS`.
+ For AWS RTB Fabric, the valid values is `APPLICATION_LOGS`.
+ For Amazon Q, the valid values are `EVENT_LOGS` and `SYNC_JOB_LOGS`.
+ For Amazon S3, the valid value is `S3_SERVER_ACCESS_LOGS`.
+ For AWS Security Hub CSPM, the valid value is `SECURITY_FINDING_LOGS`.
+ For AWS Security Hub, the valid value is `SECURITY_FINDING_LOGS`.
+ For Amazon SES mail manager, the valid values are `APPLICATION_LOGS` and `TRAFFIC_POLICY_DEBUG_LOGS`.
+ For Amazon WorkMail, the valid values are `ACCESS_CONTROL_LOGS`, `AUTHENTICATION_LOGS`, `WORKMAIL_AVAILABILITY_PROVIDER_LOGS`, `WORKMAIL_MAILBOX_ACCESS_LOGS`, and `WORKMAIL_PERSONAL_ACCESS_TOKEN_LOGS`.
+ For Amazon VPC Route Server, the valid value is `EVENT_LOGS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w]*`
Required: Yes

 ** [name](#API_PutDeliverySource_RequestSyntax) **   <a name="CWL-PutDeliverySource-request-name"></a>
A name for this delivery source. This name must be unique for all delivery sources in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

 ** [resourceArn](#API_PutDeliverySource_RequestSyntax) **   <a name="CWL-PutDeliverySource-request-resourceArn"></a>
The ARN of the AWS resource that is generating and sending logs. For example, `arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234`
For the `SECURITY_FINDING_LOGS` logType, use a wildcard ARN for the hub resource. For AWS Security Hub CSPM, use `arn:aws:securityhub:us-east-1:111122223333:hub/*` and for AWS Security Hub, use `arn:aws:securityhub:us-east-1:111122223333:hubv2/*`
Type: String
Required: Yes

 ** [tags](#API_PutDeliverySource_RequestSyntax) **   <a name="CWL-PutDeliverySource-request-tags"></a>
An optional list of key-value pairs to associate with the resource.
For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_PutDeliverySource_ResponseSyntax"></a>

```
{
   "deliverySource": {
      "arn": "string",
      "deliverySourceConfiguration": {
         "string" : "string"
      },
      "logType": "string",
      "name": "string",
      "resourceArns": [ "string" ],
      "service": "string",
      "status": "string",
      "statusReason": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_PutDeliverySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliverySource](#API_PutDeliverySource_ResponseSyntax) **   <a name="CWL-PutDeliverySource-response-deliverySource"></a>
A structure containing information about the delivery source that was just created or updated.
Type: [DeliverySource](API_DeliverySource.md) object

## Errors
<a name="API_PutDeliverySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutDeliverySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutDeliverySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutDeliverySource)

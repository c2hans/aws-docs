---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateCampaign.html
---

# UpdateCampaign
<a name="API_UpdateCampaign"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Updates a campaign.

## Request Syntax
<a name="API_UpdateCampaign_RequestSyntax"></a>

```
{
   "action": "{{string}}",
   "dataExtraDimensions": [ "{{string}}" ],
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCampaign_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [action](#API_UpdateCampaign_RequestSyntax) **   <a name="iotfleetwise-UpdateCampaign-request-action"></a>
 Specifies how to update a campaign. The action can be one of the following:
+  `APPROVE` - To approve delivering a data collection scheme to vehicles.
+  `SUSPEND` - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data.
+  `RESUME` - To reactivate the `SUSPEND` campaign. The campaign is set to be redeployed to all vehicles on next check-in and the vehicles will resume sending data.
+  `UPDATE` - To update a campaign.
Type: String
Valid Values: `APPROVE | SUSPEND | RESUME | UPDATE`
Required: Yes

 ** [dataExtraDimensions](#API_UpdateCampaign_RequestSyntax) **   <a name="iotfleetwise-UpdateCampaign-request-dataExtraDimensions"></a>
 A list of vehicle attributes to associate with a signal.
Default: An empty array
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [description](#API_UpdateCampaign_RequestSyntax) **   <a name="iotfleetwise-UpdateCampaign-request-description"></a>
The description of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [name](#API_UpdateCampaign_RequestSyntax) **   <a name="iotfleetwise-UpdateCampaign-request-name"></a>
 The name of the campaign to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_UpdateCampaign_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateCampaign_ResponseSyntax) **   <a name="iotfleetwise-UpdateCampaign-response-arn"></a>
 The Amazon Resource Name (ARN) of the campaign.
Type: String
Pattern: `arn:aws:iotfleetwise:[a-z0-9-]+:[0-9]{12}:campaign/[a-zA-Z\d\-_:]{1,100}`

 ** [name](#API_UpdateCampaign_ResponseSyntax) **   <a name="iotfleetwise-UpdateCampaign-response-name"></a>
The name of the updated campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

 ** [status](#API_UpdateCampaign_ResponseSyntax) **   <a name="iotfleetwise-UpdateCampaign-response-status"></a>
The state of a campaign. The status can be one of:
+  `CREATING` - AWS IoT FleetWise is processing your request to create the campaign.
+  `WAITING_FOR_APPROVAL` - After you create a campaign, it enters this state. Use the [UpdateCampaign](#API_UpdateCampaign) API operation to approve the campaign for deployment to the target vehicle or fleet.
+  `RUNNING` - The campaign is active.
+  `SUSPENDED` - The campaign is suspended. To resume the campaign, use the [UpdateCampaign](#API_UpdateCampaign) API operation.
Type: String
Valid Values: `CREATING | WAITING_FOR_APPROVAL | RUNNING | SUSPENDED`

## Errors
<a name="API_UpdateCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/UpdateCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateCampaign)

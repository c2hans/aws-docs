---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxScalingGroup.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxScalingGroup
<a name="API_GetKxScalingGroup"></a>

 Retrieves details of a scaling group.

## Request Syntax
<a name="API_GetKxScalingGroup_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/scalingGroups/{{scalingGroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxScalingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetKxScalingGroup_RequestSyntax) **   <a name="finspace-GetKxScalingGroup-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** [scalingGroupName](#API_GetKxScalingGroup_RequestSyntax) **   <a name="finspace-GetKxScalingGroup-request-uri-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

## Request Body
<a name="API_GetKxScalingGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxScalingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availabilityZoneId": "string",
   "clusters": [ "string" ],
   "createdTimestamp": number,
   "hostType": "string",
   "lastModifiedTimestamp": number,
   "scalingGroupArn": "string",
   "scalingGroupName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetKxScalingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availabilityZoneId](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-availabilityZoneId"></a>
The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [clusters](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-clusters"></a>
 The list of Managed kdb clusters that are currently active in the given scaling group.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [createdTimestamp](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-createdTimestamp"></a>
 The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [hostType](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-hostType"></a>
 The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.
It can have one of the following values:
+  `kx.sg.large` – The host type with a configuration of 16 GiB memory and 2 vCPUs.
+  `kx.sg.xlarge` – The host type with a configuration of 32 GiB memory and 4 vCPUs.
+  `kx.sg.2xlarge` – The host type with a configuration of 64 GiB memory and 8 vCPUs.
+  `kx.sg.4xlarge` – The host type with a configuration of 108 GiB memory and 16 vCPUs.
+  `kx.sg.8xlarge` – The host type with a configuration of 216 GiB memory and 32 vCPUs.
+  `kx.sg.16xlarge` – The host type with a configuration of 432 GiB memory and 64 vCPUs.
+  `kx.sg.32xlarge` – The host type with a configuration of 864 GiB memory and 128 vCPUs.
+  `kx.sg1.16xlarge` – The host type with a configuration of 1949 GiB memory and 64 vCPUs.
+  `kx.sg1.24xlarge` – The host type with a configuration of 2948 GiB memory and 96 vCPUs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._]+`

 ** [lastModifiedTimestamp](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-lastModifiedTimestamp"></a>
 The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [scalingGroupArn](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-scalingGroupArn"></a>
 The ARN identifier for the scaling group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:*:*:*:*:*`

 ** [scalingGroupName](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [status](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-status"></a>
The status of scaling group.
+ CREATING – The scaling group creation is in progress.
+ CREATE\_FAILED – The scaling group creation has failed.
+ ACTIVE – The scaling group is active.
+ UPDATING – The scaling group is in the process of being updated.
+ UPDATE\_FAILED – The update action failed.
+ DELETING – The scaling group is in the process of being deleted.
+ DELETE\_FAILED – The system failed to delete the scaling group.
+ DELETED – The scaling group is successfully deleted.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED | DELETE_FAILED`

 ** [statusReason](#API_GetKxScalingGroup_ResponseSyntax) **   <a name="finspace-GetKxScalingGroup-response-statusReason"></a>
 The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

## Errors
<a name="API_GetKxScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetKxScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxScalingGroup)

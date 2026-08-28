---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxScalingGroup.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxScalingGroup
<a name="API_CreateKxScalingGroup"></a>

Creates a new scaling group.

## Request Syntax
<a name="API_CreateKxScalingGroup_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/scalingGroups HTTP/1.1
Content-type: application/json

{
   "availabilityZoneId": "{{string}}",
   "clientToken": "{{string}}",
   "hostType": "{{string}}",
   "scalingGroupName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateKxScalingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-uri-environmentId"></a>
A unique identifier for the kdb environment, where you want to create the scaling group.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_CreateKxScalingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilityZoneId](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-availabilityZoneId"></a>
The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [clientToken](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`
Required: Yes

 ** [hostType](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-hostType"></a>
 The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.
You can add one of the following values:
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
Required: Yes

 ** [scalingGroupName](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [tags](#API_CreateKxScalingGroup_RequestSyntax) **   <a name="finspace-CreateKxScalingGroup-request-tags"></a>
 A list of key-value pairs to label the scaling group. You can add up to 50 tags to a scaling group.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxScalingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availabilityZoneId": "string",
   "createdTimestamp": number,
   "environmentId": "string",
   "hostType": "string",
   "lastModifiedTimestamp": number,
   "scalingGroupName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateKxScalingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availabilityZoneId](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-availabilityZoneId"></a>
The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [createdTimestamp](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-createdTimestamp"></a>
 The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [environmentId](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-environmentId"></a>
A unique identifier for the kdb environment, where you create the scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`

 ** [hostType](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-hostType"></a>
 The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._]+`

 ** [lastModifiedTimestamp](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-lastModifiedTimestamp"></a>
 The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [scalingGroupName](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [status](#API_CreateKxScalingGroup_ResponseSyntax) **   <a name="finspace-CreateKxScalingGroup-response-status"></a>
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

## Errors
<a name="API_CreateKxScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_CreateKxScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxScalingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

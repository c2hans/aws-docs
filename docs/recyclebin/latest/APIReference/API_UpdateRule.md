---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UpdateRule.html
---

# UpdateRule
<a name="API_UpdateRule"></a>

Updates an existing Recycle Bin retention rule. You can update a retention rule's description, resource tags, and retention period at any time after creation. You can't update a retention rule's resource type after creation. For more information, see [ Update Recycle Bin retention rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-working-with-rules.html#recycle-bin-update-rule) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Syntax
<a name="API_UpdateRule_RequestSyntax"></a>

```
PATCH /rules/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "ExcludeResourceTags": [
      {
         "ResourceTagKey": "{{string}}",
         "ResourceTagValue": "{{string}}"
      }
   ],
   "ResourceTags": [
      {
         "ResourceTagKey": "{{string}}",
         "ResourceTagValue": "{{string}}"
      }
   ],
   "ResourceType": "{{string}}",
   "RetentionPeriod": {
      "RetentionPeriodUnit": "{{string}}",
      "RetentionPeriodValue": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-uri-Identifier"></a>
The unique ID of the retention rule.
Pattern: `[0-9a-zA-Z]{11}`
Required: Yes

## Request Body
<a name="API_UpdateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`
Required: No

 ** [ExcludeResourceTags](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-ExcludeResourceTags"></a>
[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.
You can't specify exclusion tags for tag-level retention rules.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [ResourceTags](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-ResourceTags"></a>
[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.
You can add the same tag key and value pair to a maximum or five retention rules.
To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [ResourceType](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-ResourceType"></a>
This parameter is currently not supported. You can't update a retention rule's resource type after creation.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`
Required: No

 ** [RetentionPeriod](#API_UpdateRule_RequestSyntax) **   <a name="recyclebin-UpdateRule-request-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object
Required: No

## Response Syntax
<a name="API_UpdateRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Description": "string",
   "ExcludeResourceTags": [
      {
         "ResourceTagKey": "string",
         "ResourceTagValue": "string"
      }
   ],
   "Identifier": "string",
   "LockEndTime": number,
   "LockState": "string",
   "ResourceTags": [
      {
         "ResourceTagKey": "string",
         "ResourceTagValue": "string"
      }
   ],
   "ResourceType": "string",
   "RetentionPeriod": {
      "RetentionPeriodUnit": "string",
      "RetentionPeriodValue": number
   },
   "RuleArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`

 ** [ExcludeResourceTags](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-ExcludeResourceTags"></a>
[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [Identifier](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-Identifier"></a>
The unique ID of the retention rule.
Type: String
Pattern: `[0-9a-zA-Z]{11}`

 ** [LockEndTime](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-LockEndTime"></a>
The date and time at which the unlock delay is set to expire. Only returned for retention rules that have been unlocked and that are still within the unlock delay period.
Type: Timestamp

 ** [LockState](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-LockState"></a>
[Region-level retention rules only] The lock state for the retention rule.
+  `locked` - The retention rule is locked and can't be modified or deleted.
+  `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
+  `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
+  `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null`.
Type: String
Valid Values: `locked | pending_unlock | unlocked`

 ** [ResourceTags](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-ResourceTags"></a>
[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [ResourceType](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-ResourceType"></a>
The resource type retained by the retention rule.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`

 ** [RetentionPeriod](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object

 ** [RuleArn](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-RuleArn"></a>
The Amazon Resource Name (ARN) of the retention rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `^arn:\S+:rbin:[a-z\-0-9]{0,63}:[0-9]{12}:rule/[0-9a-zA-Z]{11}{0,1011}$`

 ** [Status](#API_UpdateRule_ResponseSyntax) **   <a name="recyclebin-UpdateRule-response-Status"></a>
The state of the retention rule. Only retention rules that are in the `available` state retain resources.
Type: String
Valid Values: `pending | available`

## Errors
<a name="API_UpdateRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The specified retention rule lock request can't be completed.
 ** Reason **
The reason for the exception.
HTTP Status Code: 409

 ** InternalServerException **
The service could not respond to the request due to an internal problem.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Reason **
The reason for the exception.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota for the number of tags per resource to be exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ValidationException **
One or more of the parameters in the request is not valid.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rbin-2021-06-15/UpdateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/UpdateRule)

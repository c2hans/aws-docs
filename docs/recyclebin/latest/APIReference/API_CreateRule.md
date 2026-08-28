---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

Creates a Recycle Bin retention rule. You can create two types of retention rules:
+  **Tag-level retention rules** - These retention rules use resource tags to identify the resources to protect. For each retention rule, you specify one or more tag key and value pairs. Resources (of the specified type) that have at least one of these tag key and value pairs are automatically retained in the Recycle Bin upon deletion. Use this type of retention rule to protect specific resources in your account based on their tags.
+  **Region-level retention rules** - These retention rules, by default, apply to all of the resources (of the specified type) in the Region, even if the resources are not tagged. However, you can specify exclusion tags to exclude resources that have specific tags. Use this type of retention rule to protect all resources of a specific type in a Region.

For more information, see [ Create Recycle Bin retention rules](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin.html) in the *Amazon EBS User Guide*.

## Request Syntax
<a name="API_CreateRule_RequestSyntax"></a>

```
POST /rules HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "ExcludeResourceTags": [
      {
         "ResourceTagKey": "{{string}}",
         "ResourceTagValue": "{{string}}"
      }
   ],
   "LockConfiguration": {
      "UnlockDelay": {
         "UnlockDelayUnit": "{{string}}",
         "UnlockDelayValue": {{number}}
      }
   },
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
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`
Required: No

 ** [ExcludeResourceTags](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-ExcludeResourceTags"></a>
[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.
You can't specify exclusion tags for tag-level retention rules.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [LockConfiguration](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-LockConfiguration"></a>
Information about the retention rule lock configuration.
Type: [LockConfiguration](API_LockConfiguration.md) object
Required: No

 ** [ResourceTags](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-ResourceTags"></a>
[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.
You can add the same tag key and value pair to a maximum or five retention rules.
To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [ResourceType](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-ResourceType"></a>
The resource type to be retained by the retention rule. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.
+ To retain EBS volumes, specify `EBS_VOLUME`.
+ To retain EBS snapshots, specify `EBS_SNAPSHOT`
+ To retain EBS-backed AMIs, specify `EC2_IMAGE`.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`
Required: Yes

 ** [RetentionPeriod](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object
Required: Yes

 ** [Tags](#API_CreateRule_RequestSyntax) **   <a name="recyclebin-CreateRule-request-Tags"></a>
Information about the tags to assign to the retention rule.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateRule_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "LockConfiguration": {
      "UnlockDelay": {
         "UnlockDelayUnit": "string",
         "UnlockDelayValue": number
      }
   },
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
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`

 ** [ExcludeResourceTags](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-ExcludeResourceTags"></a>
[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [Identifier](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-Identifier"></a>
The unique ID of the retention rule.
Type: String
Pattern: `[0-9a-zA-Z]{11}`

 ** [LockConfiguration](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-LockConfiguration"></a>
Information about the retention rule lock configuration.
Type: [LockConfiguration](API_LockConfiguration.md) object

 ** [LockState](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-LockState"></a>
[Region-level retention rules only] The lock state for the retention rule.
+  `locked` - The retention rule is locked and can't be modified or deleted.
+  `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
+  `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
+  `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null`.
Type: String
Valid Values: `locked | pending_unlock | unlocked`

 ** [ResourceTags](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-ResourceTags"></a>
[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [ResourceType](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-ResourceType"></a>
The resource type retained by the retention rule.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`

 ** [RetentionPeriod](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object

 ** [RuleArn](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-RuleArn"></a>
The Amazon Resource Name (ARN) of the retention rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `^arn:\S+:rbin:[a-z\-0-9]{0,63}:[0-9]{12}:rule/[0-9a-zA-Z]{11}{0,1011}$`

 ** [Status](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-Status"></a>
The state of the retention rule. Only retention rules that are in the `available` state retain resources.
Type: String
Valid Values: `pending | available`

 ** [Tags](#API_CreateRule_ResponseSyntax) **   <a name="recyclebin-CreateRule-response-Tags"></a>
Information about the tags assigned to the retention rule.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_CreateRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service could not respond to the request due to an internal problem.
HTTP Status Code: 500

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
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rbin-2021-06-15/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rbin-2021-06-15/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rbin-2021-06-15/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rbin-2021-06-15/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rbin-2021-06-15/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rbin-2021-06-15/CreateRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rbin-2021-06-15/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/CreateRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

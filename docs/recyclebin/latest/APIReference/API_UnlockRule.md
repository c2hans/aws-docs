---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockRule.html
---

# UnlockRule
<a name="API_UnlockRule"></a>

Unlocks a retention rule. After a retention rule is unlocked, it can be modified or deleted only after the unlock delay period expires.

## Request Syntax
<a name="API_UnlockRule_RequestSyntax"></a>

```
PATCH /rules/{{identifier}}/unlock HTTP/1.1
```

## URI Request Parameters
<a name="API_UnlockRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_UnlockRule_RequestSyntax) **   <a name="recyclebin-UnlockRule-request-uri-Identifier"></a>
The unique ID of the retention rule.
Pattern: `[0-9a-zA-Z]{11}`
Required: Yes

## Request Body
<a name="API_UnlockRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UnlockRule_ResponseSyntax"></a>

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
   "LockConfiguration": {
      "UnlockDelay": {
         "UnlockDelayUnit": "string",
         "UnlockDelayValue": number
      }
   },
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
<a name="API_UnlockRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-Description"></a>
The retention rule description.
Type: String
Pattern: `^[\S ]{0,255}$`

 ** [ExcludeResourceTags](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-ExcludeResourceTags"></a>
[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [Identifier](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-Identifier"></a>
The unique ID of the retention rule.
Type: String
Pattern: `[0-9a-zA-Z]{11}`

 ** [LockConfiguration](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-LockConfiguration"></a>
Information about the retention rule lock configuration.
Type: [LockConfiguration](API_LockConfiguration.md) object

 ** [LockEndTime](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-LockEndTime"></a>
The date and time at which the unlock delay is set to expire. Only returned for retention rules that have been unlocked and that are still within the unlock delay period.
Type: Timestamp

 ** [LockState](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-LockState"></a>
[Region-level retention rules only] The lock state for the retention rule.
+  `locked` - The retention rule is locked and can't be modified or deleted.
+  `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
+  `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
+  `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null`.
Type: String
Valid Values: `locked | pending_unlock | unlocked`

 ** [ResourceTags](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-ResourceTags"></a>
[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [ResourceType](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-ResourceType"></a>
The resource type retained by the retention rule.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`

 ** [RetentionPeriod](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-RetentionPeriod"></a>
Information about the retention period for which the retention rule is to retain resources.
Type: [RetentionPeriod](API_RetentionPeriod.md) object

 ** [RuleArn](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-RuleArn"></a>
The Amazon Resource Name (ARN) of the retention rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `^arn:\S+:rbin:[a-z\-0-9]{0,63}:[0-9]{12}:rule/[0-9a-zA-Z]{11}{0,1011}$`

 ** [Status](#API_UnlockRule_ResponseSyntax) **   <a name="recyclebin-UnlockRule-response-Status"></a>
The state of the retention rule. Only retention rules that are in the `available` state retain resources.
Type: String
Valid Values: `pending | available`

## Errors
<a name="API_UnlockRule_Errors"></a>

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

 ** ValidationException **
One or more of the parameters in the request is not valid.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UnlockRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rbin-2021-06-15/UnlockRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/UnlockRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListRules.html
---

# ListRules
<a name="API_ListRules"></a>

Lists the Recycle Bin retention rules in the Region.

## Request Syntax
<a name="API_ListRules_RequestSyntax"></a>

```
POST /list-rules HTTP/1.1
Content-type: application/json

{
   "ExcludeResourceTags": [
      {
         "ResourceTagKey": "{{string}}",
         "ResourceTagValue": "{{string}}"
      }
   ],
   "LockState": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceTags": [
      {
         "ResourceTagKey": "{{string}}",
         "ResourceTagValue": "{{string}}"
      }
   ],
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExcludeResourceTags](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-ExcludeResourceTags"></a>
[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [LockState](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-LockState"></a>
The lock state of the retention rules to list. Only retention rules with the specified lock state are returned.
Type: String
Valid Values: `locked | pending_unlock | unlocked`
Required: No

 ** [MaxResults](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-NextToken"></a>
The token for the next page of results.
Type: String
Pattern: `^[A-Za-z0-9+/=]{1,2048}$`
Required: No

 ** [ResourceTags](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-ResourceTags"></a>
[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [ResourceType](#API_ListRules_RequestSyntax) **   <a name="recyclebin-ListRules-request-ResourceType"></a>
The resource type retained by the retention rule. Only retention rules that retain the specified resource type are listed. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.
+ To list retention rules that retain EBS volumes, specify `EBS_VOLUME`.
+ To list retention rules that retain EBS snapshots, specify `EBS_SNAPSHOT`.
+ To list retention rules that retain EBS-backed AMIs, specify `EC2_IMAGE`.
Type: String
Valid Values: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`
Required: Yes

## Response Syntax
<a name="API_ListRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Rules": [
      {
         "Description": "string",
         "Identifier": "string",
         "LockState": "string",
         "RetentionPeriod": {
            "RetentionPeriodUnit": "string",
            "RetentionPeriodValue": number
         },
         "RuleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRules_ResponseSyntax) **   <a name="recyclebin-ListRules-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Pattern: `^[A-Za-z0-9+/=]{1,2048}$`

 ** [Rules](#API_ListRules_ResponseSyntax) **   <a name="recyclebin-ListRules-response-Rules"></a>
Information about the retention rules.
Type: Array of [RuleSummary](API_RuleSummary.md) objects

## Errors
<a name="API_ListRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service could not respond to the request due to an internal problem.
HTTP Status Code: 500

 ** ValidationException **
One or more of the parameters in the request is not valid.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rbin-2021-06-15/ListRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rbin-2021-06-15/ListRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/ListRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rbin-2021-06-15/ListRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/ListRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rbin-2021-06-15/ListRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rbin-2021-06-15/ListRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rbin-2021-06-15/ListRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rbin-2021-06-15/ListRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/ListRules)

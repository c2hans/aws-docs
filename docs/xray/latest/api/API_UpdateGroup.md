---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_UpdateGroup.html
---

# UpdateGroup
<a name="API_UpdateGroup"></a>

Updates a group resource.

## Request Syntax
<a name="API_UpdateGroup_RequestSyntax"></a>

```
POST /UpdateGroup HTTP/1.1
Content-type: application/json

{
   "FilterExpression": "{{string}}",
   "GroupARN": "{{string}}",
   "GroupName": "{{string}}",
   "InsightsConfiguration": {
      "InsightsEnabled": {{boolean}},
      "NotificationsEnabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FilterExpression](#API_UpdateGroup_RequestSyntax) **   <a name="xray-UpdateGroup-request-FilterExpression"></a>
The updated filter expression defining criteria by which to group traces.
Type: String
Required: No

 ** [GroupARN](#API_UpdateGroup_RequestSyntax) **   <a name="xray-UpdateGroup-request-GroupARN"></a>
The ARN that was generated upon creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [GroupName](#API_UpdateGroup_RequestSyntax) **   <a name="xray-UpdateGroup-request-GroupName"></a>
The case-sensitive name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [InsightsConfiguration](#API_UpdateGroup_RequestSyntax) **   <a name="xray-UpdateGroup-request-InsightsConfiguration"></a>
The structure containing configurations related to insights.
+ The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.
+ The NotificationsEnabled boolean can be set to true to enable insights notifications for the group. Notifications can only be enabled on a group with InsightsEnabled set to true.
Type: [InsightsConfiguration](API_InsightsConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": {
      "FilterExpression": "string",
      "GroupARN": "string",
      "GroupName": "string",
      "InsightsConfiguration": {
         "InsightsEnabled": boolean,
         "NotificationsEnabled": boolean
      }
   }
}
```

## Response Elements
<a name="API_UpdateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_UpdateGroup_ResponseSyntax) **   <a name="xray-UpdateGroup-response-Group"></a>
The group that was updated. Contains the name of the group that was updated, the ARN of the group that was updated, the updated filter expression, and the updated insight configuration assigned to the group.
Type: [Group](API_Group.md) object

## Errors
<a name="API_UpdateGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_UpdateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/UpdateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/UpdateGroup)

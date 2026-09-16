---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_CreateGroup.html
---

# CreateGroup
<a name="API_CreateGroup"></a>

Creates a group resource with a name and a filter expression.

## Request Syntax
<a name="API_CreateGroup_RequestSyntax"></a>

```
POST /CreateGroup HTTP/1.1
Content-type: application/json

{
   "FilterExpression": "{{string}}",
   "GroupName": "{{string}}",
   "InsightsConfiguration": {
      "InsightsEnabled": {{boolean}},
      "NotificationsEnabled": {{boolean}}
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
<a name="API_CreateGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FilterExpression](#API_CreateGroup_RequestSyntax) **   <a name="xray-CreateGroup-request-FilterExpression"></a>
The filter expression defining criteria by which to group traces.
Type: String
Required: No

 ** [GroupName](#API_CreateGroup_RequestSyntax) **   <a name="xray-CreateGroup-request-GroupName"></a>
The case-sensitive name of the new group. Default is a reserved name and names must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [InsightsConfiguration](#API_CreateGroup_RequestSyntax) **   <a name="xray-CreateGroup-request-InsightsConfiguration"></a>
The structure containing configurations related to insights.
+ The InsightsEnabled boolean can be set to true to enable insights for the new group or false to disable insights for the new group.
+ The NotificationsEnabled boolean can be set to true to enable insights notifications for the new group. Notifications may only be enabled on a group with InsightsEnabled set to true.
Type: [InsightsConfiguration](API_InsightsConfiguration.md) object
Required: No

 ** [Tags](#API_CreateGroup_RequestSyntax) **   <a name="xray-CreateGroup-request-Tags"></a>
A map that contains one or more tag keys and tag values to attach to an X-Ray group. For more information about ways to use tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
The following restrictions apply to tags:
+ Maximum number of user-applied tags per resource: 50
+ Maximum tag key length: 128 Unicode characters
+ Maximum tag value length: 256 Unicode characters
+ Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: \_ . : / = \+ - and @
+ Tag keys and values are case sensitive.
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateGroup_ResponseSyntax"></a>

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
<a name="API_CreateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_CreateGroup_ResponseSyntax) **   <a name="xray-CreateGroup-response-Group"></a>
The group that was created. Contains the name of the group that was created, the Amazon Resource Name (ARN) of the group that was generated based on the group name, the filter expression, and the insight configuration that was assigned to the group.
Type: [Group](API_Group.md) object

## Errors
<a name="API_CreateGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_CreateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/CreateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/CreateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/CreateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/CreateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/CreateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/CreateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/CreateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/CreateGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/CreateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/CreateGroup)

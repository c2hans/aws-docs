---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetGroup.html
---

# GetGroup
<a name="API_GetGroup"></a>

Retrieves group resource details.

## Request Syntax
<a name="API_GetGroup_RequestSyntax"></a>

```
POST /GetGroup HTTP/1.1
Content-type: application/json

{
   "GroupARN": "{{string}}",
   "GroupName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GroupARN](#API_GetGroup_RequestSyntax) **   <a name="xray-GetGroup-request-GroupARN"></a>
The ARN of the group that was generated on creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [GroupName](#API_GetGroup_RequestSyntax) **   <a name="xray-GetGroup-request-GroupName"></a>
The case-sensitive name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## Response Syntax
<a name="API_GetGroup_ResponseSyntax"></a>

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
<a name="API_GetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_GetGroup_ResponseSyntax) **   <a name="xray-GetGroup-response-Group"></a>
The group that was requested. Contains the name of the group, the ARN of the group, the filter expression, and the insight configuration assigned to the group.
Type: [Group](API_Group.md) object

## Errors
<a name="API_GetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

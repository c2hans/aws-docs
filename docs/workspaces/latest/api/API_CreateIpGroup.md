---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateIpGroup.html
---

# CreateIpGroup
<a name="API_CreateIpGroup"></a>

Creates an IP access control group.

An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using [AuthorizeIpRules](API_AuthorizeIpRules.md).

There is a default IP access control group associated with your directory. If you don't associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.

## Request Syntax
<a name="API_CreateIpGroup_RequestSyntax"></a>

```
{
   "GroupDesc": "{{string}}",
   "GroupName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserRules": [
      {
         "ipRule": "{{string}}",
         "ruleDesc": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateIpGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [GroupDesc](#API_CreateIpGroup_RequestSyntax) **   <a name="WorkSpaces-CreateIpGroup-request-GroupDesc"></a>
The description of the group.
Type: String
Required: No

 ** [GroupName](#API_CreateIpGroup_RequestSyntax) **   <a name="WorkSpaces-CreateIpGroup-request-GroupName"></a>
The name of the group.
Type: String
Required: Yes

 ** [Tags](#API_CreateIpGroup_RequestSyntax) **   <a name="WorkSpaces-CreateIpGroup-request-Tags"></a>
The tags. Each WorkSpaces resource can have a maximum of 50 tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [UserRules](#API_CreateIpGroup_RequestSyntax) **   <a name="WorkSpaces-CreateIpGroup-request-UserRules"></a>
The rules to add to the group.
Type: Array of [IpRuleItem](API_IpRuleItem.md) objects
Required: No

## Response Syntax
<a name="API_CreateIpGroup_ResponseSyntax"></a>

```
{
   "GroupId": "string"
}
```

## Response Elements
<a name="API_CreateIpGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupId](#API_CreateIpGroup_ResponseSyntax) **   <a name="WorkSpaces-CreateIpGroup-response-GroupId"></a>
The identifier of the group.
Type: String
Pattern: `wsipg-[0-9a-z]{8,63}$`

## Errors
<a name="API_CreateIpGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceCreationFailedException **
The resource could not be created.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateIpGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateIpGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateIpGroup)

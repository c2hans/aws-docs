---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteIpGroup.html
---

# DeleteIpGroup
<a name="API_DeleteIpGroup"></a>

Deletes the specified IP access control group.

You cannot delete an IP access control group that is associated with a directory.

## Request Syntax
<a name="API_DeleteIpGroup_RequestSyntax"></a>

```
{
   "GroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteIpGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [GroupId](#API_DeleteIpGroup_RequestSyntax) **   <a name="WorkSpaces-DeleteIpGroup-request-GroupId"></a>
The identifier of the IP access control group.
Type: String
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: Yes

## Response Elements
<a name="API_DeleteIpGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteIpGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceAssociatedException **
The resource is associated with a directory.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteIpGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DeleteIpGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DeleteIpGroup)

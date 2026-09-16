---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspacesPool.html
---

# StopWorkspacesPool
<a name="API_StopWorkspacesPool"></a>

**Note**
End of support notice: On December 31, 2027, AWS will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html).

Stops the specified pool.

You cannot stop a WorkSpace pool unless it has a running mode of `AutoStop` and a state of `AVAILABLE`, `IMPAIRED`, `UNHEALTHY`, or `ERROR`.

## Request Syntax
<a name="API_StopWorkspacesPool_RequestSyntax"></a>

```
{
   "PoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopWorkspacesPool_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PoolId](#API_StopWorkspacesPool_RequestSyntax) **   <a name="WorkSpaces-StopWorkspacesPool-request-PoolId"></a>
The identifier of the pool.
Type: String
Pattern: `^wspool-[0-9a-z]{9}$`
Required: Yes

## Response Elements
<a name="API_StopWorkspacesPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopWorkspacesPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** OperationInProgressException **
The properties of this WorkSpace are currently being modified. Try again in a moment.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_StopWorkspacesPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/StopWorkspacesPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/StopWorkspacesPool)

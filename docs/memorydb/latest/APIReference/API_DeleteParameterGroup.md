---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteParameterGroup.html
---

# DeleteParameterGroup
<a name="API_DeleteParameterGroup"></a>

Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any clusters. You cannot delete the default parameter groups in your account.

## Request Syntax
<a name="API_DeleteParameterGroup_RequestSyntax"></a>

```
{
   "ParameterGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteParameterGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ParameterGroupName](#API_DeleteParameterGroup_RequestSyntax) **   <a name="MemoryDB-DeleteParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteParameterGroup_ResponseSyntax"></a>

```
{
   "ParameterGroup": {
      "ARN": "string",
      "Description": "string",
      "Family": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_DeleteParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_DeleteParameterGroup_ResponseSyntax) **   <a name="MemoryDB-DeleteParameterGroup-response-ParameterGroup"></a>
The parameter group that has been deleted.
Type: [ParameterGroup](API_ParameterGroup.md) object

## Errors
<a name="API_DeleteParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterGroupStateFault **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DeleteParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteParameterGroup)

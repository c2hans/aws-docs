---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateParameterGroup.html
---

# CreateParameterGroup
<a name="API_CreateParameterGroup"></a>

Creates a new MemoryDB parameter group. A parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster. For more information, see [Configuring engine parameters using parameter groups](https://docs.aws.amazon.com/MemoryDB/latest/devguide/parametergroups.html).

## Request Syntax
<a name="API_CreateParameterGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Family": "{{string}}",
   "ParameterGroupName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateParameterGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateParameterGroup_RequestSyntax) **   <a name="MemoryDB-CreateParameterGroup-request-Description"></a>
An optional description of the parameter group.
Type: String
Required: No

 ** [Family](#API_CreateParameterGroup_RequestSyntax) **   <a name="MemoryDB-CreateParameterGroup-request-Family"></a>
The name of the parameter group family that the parameter group can be used with.
Type: String
Required: Yes

 ** [ParameterGroupName](#API_CreateParameterGroup_RequestSyntax) **   <a name="MemoryDB-CreateParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [Tags](#API_CreateParameterGroup_RequestSyntax) **   <a name="MemoryDB-CreateParameterGroup-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateParameterGroup_ResponseSyntax"></a>

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
<a name="API_CreateParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_CreateParameterGroup_ResponseSyntax) **   <a name="MemoryDB-CreateParameterGroup-response-ParameterGroup"></a>
The newly-created parameter group.
Type: [ParameterGroup](API_ParameterGroup.md) object

## Errors
<a name="API_CreateParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterGroupStateFault **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ParameterGroupAlreadyExistsFault **

HTTP Status Code: 400

 ** ParameterGroupQuotaExceededFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CreateParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateParameterGroup)

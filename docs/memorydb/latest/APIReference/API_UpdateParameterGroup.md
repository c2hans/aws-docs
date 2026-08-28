---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateParameterGroup.html
---

# UpdateParameterGroup
<a name="API_UpdateParameterGroup"></a>

Updates the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

## Request Syntax
<a name="API_UpdateParameterGroup_RequestSyntax"></a>

```
{
   "ParameterGroupName": "{{string}}",
   "ParameterNameValues": [
      {
         "ParameterName": "{{string}}",
         "ParameterValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateParameterGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ParameterGroupName](#API_UpdateParameterGroup_RequestSyntax) **   <a name="MemoryDB-UpdateParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group to update.
Type: String
Required: Yes

 ** [ParameterNameValues](#API_UpdateParameterGroup_RequestSyntax) **   <a name="MemoryDB-UpdateParameterGroup-request-ParameterNameValues"></a>
An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be updated per request.
Type: Array of [ParameterNameValue](API_ParameterNameValue.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateParameterGroup_ResponseSyntax"></a>

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
<a name="API_UpdateParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_UpdateParameterGroup_ResponseSyntax) **   <a name="MemoryDB-UpdateParameterGroup-response-ParameterGroup"></a>
The updated parameter group
Type: [ParameterGroup](API_ParameterGroup.md) object

## Errors
<a name="API_UpdateParameterGroup_Errors"></a>

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
<a name="API_UpdateParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

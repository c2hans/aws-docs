---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ListTags.html
---

# ListTags
<a name="API_dax_ListTags"></a>

List all of the tags for a DAX cluster. You can call `ListTags` up to 10 times per second, per account.

## Request Syntax
<a name="API_dax_ListTags_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "ResourceName": "{{string}}"
}
```

## Request Parameters
<a name="API_dax_ListTags_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceName](#API_dax_ListTags_RequestSyntax) **   <a name="DDB-dax_ListTags-request-ResourceName"></a>
The name of the DAX resource to which the tags belong.
Type: String
Required: Yes

 ** [NextToken](#API_dax_ListTags_RequestSyntax) **   <a name="DDB-dax_ListTags-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.
Type: String
Required: No

## Response Syntax
<a name="API_dax_ListTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_dax_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_dax_ListTags_ResponseSyntax) **   <a name="DDB-dax_ListTags-response-NextToken"></a>
If this value is present, there are additional results to be displayed. To retrieve them, call `ListTags` again, with `NextToken` set to this value.
Type: String

 ** [Tags](#API_dax_ListTags_ResponseSyntax) **   <a name="DDB-dax_ListTags-response-Tags"></a>
A list of tags currently associated with the DAX cluster.
Type: Array of [Tag](API_dax_Tag.md) objects

## Errors
<a name="API_dax_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **
The requested cluster ID does not refer to an existing DAX cluster.
HTTP Status Code: 400

 ** InvalidARNFault **
The Amazon Resource Name (ARN) supplied in the request is not valid.
HTTP Status Code: 400

 ** InvalidClusterStateFault **
The requested DAX cluster is not in the *available* state.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Two or more incompatible parameters were specified.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value for a parameter is invalid.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/ListTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/ListTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/ListTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/ListTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/ListTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/ListTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/ListTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/ListTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/ListTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/ListTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

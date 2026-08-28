---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_TagResource.html
---

# TagResource
<a name="API_dax_TagResource"></a>

Associates a set of tags with a DAX resource. You can call `TagResource` up to 5 times per second, per account.

## Request Syntax
<a name="API_dax_TagResource_RequestSyntax"></a>

```
{
   "ResourceName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_dax_TagResource_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceName](#API_dax_TagResource_RequestSyntax) **   <a name="DDB-dax_TagResource-request-ResourceName"></a>
The name of the DAX resource to which tags should be added.
Type: String
Required: Yes

 ** [Tags](#API_dax_TagResource_RequestSyntax) **   <a name="DDB-dax_TagResource-request-Tags"></a>
The tags to be assigned to the DAX resource.
Type: Array of [Tag](API_dax_Tag.md) objects
Required: Yes

## Response Syntax
<a name="API_dax_TagResource_ResponseSyntax"></a>

```
{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_dax_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_dax_TagResource_ResponseSyntax) **   <a name="DDB-dax_TagResource-response-Tags"></a>
The list of tags that are associated with the DAX resource.
Type: Array of [Tag](API_dax_Tag.md) objects

## Errors
<a name="API_dax_TagResource_Errors"></a>

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

 ** TagQuotaPerResourceExceeded **
You have exceeded the maximum number of tags for this DAX cluster.
HTTP Status Code: 400

## See Also
<a name="API_dax_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

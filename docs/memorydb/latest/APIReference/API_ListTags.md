---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListTags.html
---

# ListTags
<a name="API_ListTags"></a>

Lists all tags currently on a named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track your MemoryDB resources. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html).

When you add or remove tags from multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html).

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_ListTags_RequestSyntax) **   <a name="MemoryDB-ListTags-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which you want the list of tags.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
{
   "TagList": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TagList](#API_ListTags_ResponseSyntax) **   <a name="MemoryDB-ListTags-response-TagList"></a>
A list of tags as key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidARNFault **

HTTP Status Code: 400

 ** InvalidClusterStateFault **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

 ** MultiRegionParameterGroupNotFoundFault **
The specified multi-Region parameter group does not exist.
HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotNotFoundFault **

HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/ListTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/ListTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ListTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/ListTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ListTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/ListTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/ListTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/ListTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/ListTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ListTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

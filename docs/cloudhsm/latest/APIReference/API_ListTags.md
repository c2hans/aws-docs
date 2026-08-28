---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ListTags.html
---

# ListTags
<a name="API_ListTags"></a>

Gets a list of tags for the specified AWS CloudHSM cluster.

This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a `NextToken` value. Use this value in a subsequent `ListTags` request to get more tags. When you receive a response with no `NextToken` (or an empty or null value), that means there are no more tags to get.

 **Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM resource in a different AWS account.

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTags_RequestSyntax) **   <a name="CloudHSMV2-ListTags-request-MaxResults"></a>
The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTags_RequestSyntax) **   <a name="CloudHSMV2-ListTags-request-NextToken"></a>
The `NextToken` value that you received in the previous response. Use this value to get more tags.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** [ResourceId](#API_ListTags_RequestSyntax) **   <a name="CloudHSMV2-ListTags-request-ResourceId"></a>
The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use [DescribeClusters](API_DescribeClusters.md).
Type: String
Pattern: `(?:cluster|backup)-[2-7a-zA-Z]{11,16}`
Required: Yes

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
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

 ** [NextToken](#API_ListTags_ResponseSyntax) **   <a name="CloudHSMV2-ListTags-response-NextToken"></a>
An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent `ListTags` request to get more tags.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`

 ** [TagList](#API_ListTags_ResponseSyntax) **   <a name="CloudHSMV2-ListTags-response-TagList"></a>
A list of tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmAccessDeniedException **
The request was rejected because the requester does not have permission to perform the requested operation.
HTTP Status Code: 400

 ** CloudHsmInternalFailureException **
The request was rejected because of an AWS CloudHSM internal failure. The request can be retried.
HTTP Status Code: 500

 ** CloudHsmInvalidRequestException **
The request was rejected because it is not a valid request.
HTTP Status Code: 400

 ** CloudHsmResourceNotFoundException **
The request was rejected because it refers to a resource that cannot be found.
HTTP Status Code: 400

 ** CloudHsmServiceException **
The request was rejected because an error occurred.
HTTP Status Code: 400

 ** CloudHsmTagException **
The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/ListTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/ListTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

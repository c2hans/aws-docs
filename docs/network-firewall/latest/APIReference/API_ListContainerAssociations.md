---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListContainerAssociations.html
---

# ListContainerAssociations
<a name="API_ListContainerAssociations"></a>

Lists the container associations in your account and Region. Use the `NextToken` parameter in subsequent requests to retrieve additional results.

## Request Syntax
<a name="API_ListContainerAssociations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListContainerAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListContainerAssociations_RequestSyntax) **   <a name="networkfirewall-ListContainerAssociations-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListContainerAssociations_RequestSyntax) **   <a name="networkfirewall-ListContainerAssociations-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:\/+=]+$`
Required: No

## Response Syntax
<a name="API_ListContainerAssociations_ResponseSyntax"></a>

```
{
   "ContainerAssociations": [
      {
         "Arn": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContainerAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerAssociations](#API_ListContainerAssociations_ResponseSyntax) **   <a name="networkfirewall-ListContainerAssociations-response-ContainerAssociations"></a>
The container association metadata objects for the account and Region.
Type: Array of [ContainerAssociationSummary](API_ContainerAssociationSummary.md) objects

 ** [NextToken](#API_ListContainerAssociations_ResponseSyntax) **   <a name="networkfirewall-ListContainerAssociations-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:\/+=]+$`

## Errors
<a name="API_ListContainerAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_ListContainerAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListContainerAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListContainerAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

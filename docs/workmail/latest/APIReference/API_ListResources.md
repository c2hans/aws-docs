---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Returns summaries of the organization's resources.

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
{
   "Filters": {
      "NamePrefix": "{{string}}",
      "PrimaryEmailPrefix": "{{string}}",
      "State": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListResources_RequestSyntax) **   <a name="workmail-ListResources-request-Filters"></a>
Limit the resource search results based on the filter criteria. You can only use one filter per request.
Type: [ListResourcesFilters](API_ListResourcesFilters.md) object
Required: No

 ** [MaxResults](#API_ListResources_RequestSyntax) **   <a name="workmail-ListResources-request-MaxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResources_RequestSyntax) **   <a name="workmail-ListResources-request-NextToken"></a>
The token to use to retrieve the next page of results. The first call does not contain any tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
Required: No

 ** [OrganizationId](#API_ListResources_RequestSyntax) **   <a name="workmail-ListResources-request-OrganizationId"></a>
The identifier for the organization under which the resources exist.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Resources": [
      {
         "Description": "string",
         "DisabledDate": number,
         "Email": "string",
         "EnabledDate": number,
         "Id": "string",
         "Name": "string",
         "State": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResources_ResponseSyntax) **   <a name="workmail-ListResources-response-NextToken"></a>
 The token used to paginate through all the organization's resources. While results are still available, it has an associated value. When the last page is reached, the token is empty.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`

 ** [Resources](#API_ListResources_ResponseSyntax) **   <a name="workmail-ListResources-response-Resources"></a>
One page of the organization's resource representation.
Type: Array of [Resource](API_Resource.md) objects

## Errors
<a name="API_ListResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** UnsupportedOperationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You can't perform a write operation against a read-only directory.
HTTP Status Code: 400

## See Also
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

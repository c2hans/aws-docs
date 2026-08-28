---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeItems.html
---

# ListChangeTypeItems
<a name="API_ListChangeTypeItems"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns the available change type item values for the specified category and subcategory values.

## Request Syntax
<a name="API_ListChangeTypeItems_RequestSyntax"></a>

```
{
   "Category": "{{string}}",
   "Locale": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Subcategory": "{{string}}"
}
```

## Request Parameters
<a name="API_ListChangeTypeItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Category](#API_ListChangeTypeItems_RequestSyntax) **   <a name="amscm-ListChangeTypeItems-request-Category"></a>
The change type category value to return the item values for.
Type: String
Required: Yes

 ** [Locale](#API_ListChangeTypeItems_RequestSyntax) **   <a name="amscm-ListChangeTypeItems-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [MaxResults](#API_ListChangeTypeItems_RequestSyntax) **   <a name="amscm-ListChangeTypeItems-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListChangeTypeItems_RequestSyntax) **   <a name="amscm-ListChangeTypeItems-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

 ** [Subcategory](#API_ListChangeTypeItems_RequestSyntax) **   <a name="amscm-ListChangeTypeItems-request-Subcategory"></a>
The change type subcategory value to return the item values for.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListChangeTypeItems_ResponseSyntax"></a>

```
{
   "ChangeTypeItems": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChangeTypeItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeTypeItems](#API_ListChangeTypeItems_ResponseSyntax) **   <a name="amscm-ListChangeTypeItems-response-ChangeTypeItems"></a>
The change type item values for the specified category and subcategory values.
Type: Array of strings

 ** [NextToken](#API_ListChangeTypeItems_ResponseSyntax) **   <a name="amscm-ListChangeTypeItems-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

## Errors
<a name="API_ListChangeTypeItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListChangeTypeItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListChangeTypeItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListChangeTypeItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeClassificationSummaries.html
---

# ListChangeTypeClassificationSummaries
<a name="API_ListChangeTypeClassificationSummaries"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns the classifications (category, subcategory, item, and operation) for all change types that meet the specified (optional) filter criteria.

## Request Syntax
<a name="API_ListChangeTypeClassificationSummaries_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Attribute": "{{string}}",
         "Condition": "{{string}}",
         "Value": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Locale": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListChangeTypeClassificationSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListChangeTypeClassificationSummaries_RequestSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-request-Filters"></a>
Attribute/value pairs to narrow the results returned. Filter criteria are combined in a logical OR operation, and values that contain spaces are also combined in an OR operation. For example, a `Value` of "read-only access" matches all values that contain "read-only" OR "access". Valid filter attributes: `Category`, `Subcategory`, `Item`, `Operation`, `ChangeTypeId`.
For more information and examples, see [Finding a change type, using the query option](https://docs.aws.amazon.com/managedservices/latest/userguide/ug-find-ct-ex-section.html) in the *AWS Managed Services User Guide*.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Locale](#API_ListChangeTypeClassificationSummaries_RequestSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [MaxResults](#API_ListChangeTypeClassificationSummaries_RequestSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListChangeTypeClassificationSummaries_RequestSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

## Response Syntax
<a name="API_ListChangeTypeClassificationSummaries_ResponseSyntax"></a>

```
{
   "ChangeTypeClassificationSummaries": [
      {
         "Category": "string",
         "ChangeTypeId": "string",
         "Item": "string",
         "Operation": "string",
         "Subcategory": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChangeTypeClassificationSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeTypeClassificationSummaries](#API_ListChangeTypeClassificationSummaries_ResponseSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-response-ChangeTypeClassificationSummaries"></a>
The change type classifications that satisfy the filter criteria.
Type: Array of [ChangeTypeClassificationSummary](API_ChangeTypeClassificationSummary.md) objects

 ** [NextToken](#API_ListChangeTypeClassificationSummaries_ResponseSyntax) **   <a name="amscm-ListChangeTypeClassificationSummaries-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

## Errors
<a name="API_ListChangeTypeClassificationSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListChangeTypeClassificationSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListChangeTypeClassificationSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListChangeTypeClassificationSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

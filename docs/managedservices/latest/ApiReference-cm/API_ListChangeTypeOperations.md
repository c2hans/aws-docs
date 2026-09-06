---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListChangeTypeOperations.html
---

# ListChangeTypeOperations
<a name="API_ListChangeTypeOperations"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns the available change type operation values for the specified category and subcategory values.

## Request Syntax
<a name="API_ListChangeTypeOperations_RequestSyntax"></a>

```
{
   "Category": "{{string}}",
   "Item": "{{string}}",
   "Locale": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Subcategory": "{{string}}"
}
```

## Request Parameters
<a name="API_ListChangeTypeOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Category](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-Category"></a>
The change type category value to return the operation values for.
Type: String
Required: Yes

 ** [Item](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-Item"></a>
The change type item values to return the operation values for.
Type: String
Required: Yes

 ** [Locale](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [MaxResults](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

 ** [Subcategory](#API_ListChangeTypeOperations_RequestSyntax) **   <a name="amscm-ListChangeTypeOperations-request-Subcategory"></a>
The change type subcategory values to return the operation values for.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListChangeTypeOperations_ResponseSyntax"></a>

```
{
   "ChangeTypeOperationSummaries": [
      {
         "ChangeTypeId": "string",
         "Operation": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChangeTypeOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeTypeOperationSummaries](#API_ListChangeTypeOperations_ResponseSyntax) **   <a name="amscm-ListChangeTypeOperations-response-ChangeTypeOperationSummaries"></a>
The change type operation values for the specified category, subcategory, and item values.
Type: Array of [ChangeTypeOperationSummary](API_ChangeTypeOperationSummary.md) objects

 ** [NextToken](#API_ListChangeTypeOperations_ResponseSyntax) **   <a name="amscm-ListChangeTypeOperations-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

## Errors
<a name="API_ListChangeTypeOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListChangeTypeOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListChangeTypeOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListChangeTypeOperations)

---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRfcCorrespondences.html
---

# ListRfcCorrespondences
<a name="API_ListRfcCorrespondences"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

List the existing correspondences of an RFC.

## Request Syntax
<a name="API_ListRfcCorrespondences_RequestSyntax"></a>

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
<a name="API_ListRfcCorrespondences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListRfcCorrespondences_RequestSyntax) **   <a name="amscm-ListRfcCorrespondences-request-Filters"></a>
The only valid filter attribute is `RfcId`, and a value is required.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Locale](#API_ListRfcCorrespondences_RequestSyntax) **   <a name="amscm-ListRfcCorrespondences-request-Locale"></a>
The locale (language) to return information in. The default is English. **Note:** For future use; not currently implemented.
Type: String
Required: No

 ** [MaxResults](#API_ListRfcCorrespondences_RequestSyntax) **   <a name="amscm-ListRfcCorrespondences-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListRfcCorrespondences_RequestSyntax) **   <a name="amscm-ListRfcCorrespondences-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

## Response Syntax
<a name="API_ListRfcCorrespondences_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RfcCorrespondences": [
      {
         "Content": "string",
         "CorrespondenceId": "string",
         "CreatedBy": "string",
         "CreatedTime": "string",
         "LinkedAttachments": [
            {
               "AttachmentId": "string",
               "CreatedBy": "string",
               "CreatedTime": "string",
               "FileName": "string"
            }
         ],
         "RfcId": "string",
         "UserType": {
            "Id": "string",
            "Name": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRfcCorrespondences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRfcCorrespondences_ResponseSyntax) **   <a name="amscm-ListRfcCorrespondences-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

 ** [RfcCorrespondences](#API_ListRfcCorrespondences_ResponseSyntax) **   <a name="amscm-ListRfcCorrespondences-response-RfcCorrespondences"></a>
The list of correspondences for an existing RFC.
Type: Array of [RfcCorrespondence](API_RfcCorrespondence.md) objects

## Errors
<a name="API_ListRfcCorrespondences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource could not be located. Actual status code: 404
HTTP Status Code: 400

## See Also
<a name="API_ListRfcCorrespondences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListRfcCorrespondences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListRfcCorrespondences)

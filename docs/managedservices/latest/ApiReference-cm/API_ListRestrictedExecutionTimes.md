---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRestrictedExecutionTimes.html
---

# ListRestrictedExecutionTimes
<a name="API_ListRestrictedExecutionTimes"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Returns the time ranges during which change execution is restricted.

## Request Syntax
<a name="API_ListRestrictedExecutionTimes_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRestrictedExecutionTimes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRestrictedExecutionTimes_RequestSyntax) **   <a name="amscm-ListRestrictedExecutionTimes-request-MaxResults"></a>
The maximum number of items to return in one batch. Valid values are 20-100.
Type: Integer
Required: No

 ** [NextToken](#API_ListRestrictedExecutionTimes_RequestSyntax) **   <a name="amscm-ListRestrictedExecutionTimes-request-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String
Required: No

## Response Syntax
<a name="API_ListRestrictedExecutionTimes_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RestrictedExecutionTimes": [
      {
         "TimeRange": {
            "EndTime": "string",
            "StartTime": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRestrictedExecutionTimes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRestrictedExecutionTimes_ResponseSyntax) **   <a name="amscm-ListRestrictedExecutionTimes-response-NextToken"></a>
If the response contains more items than `MaxResults`, only `MaxResults` items are returned, and a `NextToken` pagination token is returned in the response. To retrieve the next batch of items, reissue the request and include the returned token in the `NextToken` parameter. When all items have been returned, the response does not contain a pagination token value.
Type: String

 ** [RestrictedExecutionTimes](#API_ListRestrictedExecutionTimes_ResponseSyntax) **   <a name="amscm-ListRestrictedExecutionTimes-response-RestrictedExecutionTimes"></a>
The time ranges during which change execution is restricted.
Type: Array of [RestrictedExecutionTime](API_RestrictedExecutionTime.md) objects

## Errors
<a name="API_ListRestrictedExecutionTimes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListRestrictedExecutionTimes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/ListRestrictedExecutionTimes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ListRestrictedExecutionTimes)

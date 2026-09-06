---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ListStoredQueries.html
---

# ListStoredQueries
<a name="API_ListStoredQueries"></a>

Lists the stored queries for a single AWS account and a single AWS Region. The default is 100.

## Request Syntax
<a name="API_ListStoredQueries_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStoredQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListStoredQueries_RequestSyntax) **   <a name="config-ListStoredQueries-request-MaxResults"></a>
The maximum number of results to be returned with a single call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListStoredQueries_RequestSyntax) **   <a name="config-ListStoredQueries-request-NextToken"></a>
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_ListStoredQueries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "StoredQueryMetadata": [
      {
         "Description": "string",
         "QueryArn": "string",
         "QueryId": "string",
         "QueryName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStoredQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListStoredQueries_ResponseSyntax) **   <a name="config-ListStoredQueries-response-NextToken"></a>
If the previous paginated request didn't return all of the remaining results, the response object's `NextToken` parameter value is set to a token. To retrieve the next set of results, call this operation again and assign that token to the request object's `NextToken` parameter. If there are no remaining results, the previous response object's `NextToken` parameter is set to `null`.
Type: String

 ** [StoredQueryMetadata](#API_ListStoredQueries_ResponseSyntax) **   <a name="config-ListStoredQueries-response-StoredQueryMetadata"></a>
A list of `StoredQueryMetadata` objects.
Type: Array of [StoredQueryMetadata](API_StoredQueryMetadata.md) objects

## Errors
<a name="API_ListStoredQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListStoredQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/ListStoredQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ListStoredQueries)

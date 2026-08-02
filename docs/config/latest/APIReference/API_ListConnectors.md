---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

Returns a list of connectors depending on the filters you specify.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "filterName": "{{string}}",
         "filterValues": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListConnectors_RequestSyntax) **   <a name="config-ListConnectors-request-Filters"></a>
Filters the results based on a list of `ConnectorFilter` objects that you specify.
Type: Array of [ConnectorFilter](API_ConnectorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_ListConnectors_RequestSyntax) **   <a name="config-ListConnectors-request-MaxResults"></a>
The maximum number of results to include in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListConnectors_RequestSyntax) **   <a name="config-ListConnectors-request-NextToken"></a>
The `NextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
{
   "ConnectorSummaries": [
      {
         "arn": "string",
         "createdTime": number,
         "name": "string",
         "provider": "string",
         "tenantIdentifier": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorSummaries](#API_ListConnectors_ResponseSyntax) **   <a name="config-ListConnectors-response-ConnectorSummaries"></a>
A list of `ConnectorSummary` objects.
Type: Array of [ConnectorSummary](API_ConnectorSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListConnectors_ResponseSyntax) **   <a name="config-ListConnectors-response-NextToken"></a>
The `NextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/ListConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ListConnectors)

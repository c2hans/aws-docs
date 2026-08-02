---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteAggregationAuthorization.html
---

# DeleteAggregationAuthorization
<a name="API_DeleteAggregationAuthorization"></a>

Deletes the authorization granted to the specified configuration aggregator account in a specified region.

## Request Syntax
<a name="API_DeleteAggregationAuthorization_RequestSyntax"></a>

```
{
   "AuthorizedAccountId": "{{string}}",
   "AuthorizedAwsRegion": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAggregationAuthorization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthorizedAccountId](#API_DeleteAggregationAuthorization_RequestSyntax) **   <a name="config-DeleteAggregationAuthorization-request-AuthorizedAccountId"></a>
The 12-digit account ID of the account authorized to aggregate data.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [AuthorizedAwsRegion](#API_DeleteAggregationAuthorization_RequestSyntax) **   <a name="config-DeleteAggregationAuthorization-request-AuthorizedAwsRegion"></a>
The region authorized to collect aggregated data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_DeleteAggregationAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAggregationAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAggregationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteAggregationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteAggregationAuthorization)

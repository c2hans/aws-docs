---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutAggregationAuthorization.html
---

# PutAggregationAuthorization
<a name="API_PutAggregationAuthorization"></a>

Authorizes the aggregator account and region to collect data from the source account and region.

**Note**
 **Tags are added at creation and cannot be updated with this operation**
 `PutAggregationAuthorization` is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different `tags` values, AWS Config will ignore these differences and treat it as an idempotent request of the previous. In this case, `tags` will not be updated, even if they are different.
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutAggregationAuthorization_RequestSyntax"></a>

```
{
   "AuthorizedAccountId": "{{string}}",
   "AuthorizedAwsRegion": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutAggregationAuthorization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthorizedAccountId](#API_PutAggregationAuthorization_RequestSyntax) **   <a name="config-PutAggregationAuthorization-request-AuthorizedAccountId"></a>
The 12-digit account ID of the account authorized to aggregate data.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [AuthorizedAwsRegion](#API_PutAggregationAuthorization_RequestSyntax) **   <a name="config-PutAggregationAuthorization-request-AuthorizedAwsRegion"></a>
The region authorized to collect aggregated data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Tags](#API_PutAggregationAuthorization_RequestSyntax) **   <a name="config-PutAggregationAuthorization-request-Tags"></a>
An array of tag object.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_PutAggregationAuthorization_ResponseSyntax"></a>

```
{
   "AggregationAuthorization": {
      "AggregationAuthorizationArn": "string",
      "AuthorizedAccountId": "string",
      "AuthorizedAwsRegion": "string",
      "CreationTime": number
   }
}
```

## Response Elements
<a name="API_PutAggregationAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregationAuthorization](#API_PutAggregationAuthorization_ResponseSyntax) **   <a name="config-PutAggregationAuthorization-response-AggregationAuthorization"></a>
Returns an AggregationAuthorization object.
Type: [AggregationAuthorization](API_AggregationAuthorization.md) object

## Errors
<a name="API_PutAggregationAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_PutAggregationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutAggregationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutAggregationAuthorization)

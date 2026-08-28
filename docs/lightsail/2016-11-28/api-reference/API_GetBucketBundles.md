---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html
---

# GetBucketBundles
<a name="API_GetBucketBundles"></a>

Returns the bundles that you can apply to a Amazon Lightsail bucket.

The bucket bundle specifies the monthly cost, storage quota, and data transfer quota for a bucket.

Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to update the bundle for a bucket.

## Request Syntax
<a name="API_GetBucketBundles_RequestSyntax"></a>

```
{
   "includeInactive": {{boolean}}
}
```

## Request Parameters
<a name="API_GetBucketBundles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includeInactive](#API_GetBucketBundles_RequestSyntax) **   <a name="Lightsail-GetBucketBundles-request-includeInactive"></a>
A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetBucketBundles_ResponseSyntax"></a>

```
{
   "bundles": [
      {
         "bundleId": "string",
         "isActive": boolean,
         "name": "string",
         "price": number,
         "storagePerMonthInGb": number,
         "transferPerMonthInGb": number
      }
   ]
}
```

## Response Elements
<a name="API_GetBucketBundles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bundles](#API_GetBucketBundles_ResponseSyntax) **   <a name="Lightsail-GetBucketBundles-response-bundles"></a>
An object that describes bucket bundles.
Type: Array of [BucketBundle](API_BucketBundle.md) objects

## Errors
<a name="API_GetBucketBundles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetBucketBundles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetBucketBundles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetBucketBundles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

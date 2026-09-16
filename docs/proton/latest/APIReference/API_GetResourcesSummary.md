---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetResourcesSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetResourcesSummary
<a name="API_GetResourcesSummary"></a>

Get counts of AWS Proton resources.

For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it's behind the recommended version of the AWS Proton template that it uses and it needs an update to become current.

The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the `components`, `environments`, and `serviceTemplates` field descriptions.

For context, the action also returns the total number of each type of AWS Proton template in the AWS account.

For more information, see [AWS Proton dashboard](https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html) in the * AWS Proton User Guide*.

## Response Syntax
<a name="API_GetResourcesSummary_ResponseSyntax"></a>

```
{
   "counts": {
      "components": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "environments": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "environmentTemplates": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "pipelines": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "serviceInstances": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "services": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      },
      "serviceTemplates": {
         "behindMajor": number,
         "behindMinor": number,
         "failed": number,
         "total": number,
         "upToDate": number
      }
   }
}
```

## Response Elements
<a name="API_GetResourcesSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [counts](#API_GetResourcesSummary_ResponseSyntax) **   <a name="proton-GetResourcesSummary-response-counts"></a>
Summary counts of each AWS Proton resource type.
Type: [CountsSummary](API_CountsSummary.md) object

## Errors
<a name="API_GetResourcesSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetResourcesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetResourcesSummary)

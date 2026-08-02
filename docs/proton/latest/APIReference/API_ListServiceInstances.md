---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceInstances.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListServiceInstances
<a name="API_ListServiceInstances"></a>

List service instances with summary data. This action lists service instances of all services in the AWS account.

## Request Syntax
<a name="API_ListServiceInstances_RequestSyntax"></a>

```
{
   "filters": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceName": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServiceInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-filters"></a>
An array of filtering criteria that scope down the result list. By default, all service instances in the AWS account are returned.
Type: Array of [ListServiceInstancesFilter](API_ListServiceInstancesFilter.md) objects
Required: No

 ** [maxResults](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-maxResults"></a>
The maximum number of service instances to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-nextToken"></a>
A token that indicates the location of the next service in the array of service instances, after the list of service instances that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

 ** [serviceName](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-serviceName"></a>
The name of the service that the service instance belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [sortBy](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-sortBy"></a>
The field that the result list is sorted by.
When you choose to sort by `serviceName`, service instances within each service are sorted by service instance name.
Default: `serviceName`
Type: String
Valid Values: `name | deploymentStatus | templateName | serviceName | environmentName | lastDeploymentAttemptedAt | createdAt`
Required: No

 ** [sortOrder](#API_ListServiceInstances_RequestSyntax) **   <a name="proton-ListServiceInstances-request-sortOrder"></a>
Result list sort order.
Default: `ASCENDING`
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListServiceInstances_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "serviceInstances": [
      {
         "arn": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "deploymentStatusMessage": "string",
         "environmentName": "string",
         "lastAttemptedDeploymentId": "string",
         "lastDeploymentAttemptedAt": number,
         "lastDeploymentSucceededAt": number,
         "lastSucceededDeploymentId": "string",
         "name": "string",
         "serviceName": "string",
         "templateMajorVersion": "string",
         "templateMinorVersion": "string",
         "templateName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServiceInstances_ResponseSyntax) **   <a name="proton-ListServiceInstances-response-nextToken"></a>
A token that indicates the location of the next service instance in the array of service instances, after the current requested list of service instances.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

 ** [serviceInstances](#API_ListServiceInstances_ResponseSyntax) **   <a name="proton-ListServiceInstances-response-serviceInstances"></a>
An array of service instances with summary data.
Type: Array of [ServiceInstanceSummary](API_ServiceInstanceSummary.md) objects

## Errors
<a name="API_ListServiceInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListServiceInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListServiceInstances)

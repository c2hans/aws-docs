---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_UpdateOrganizationRecommendationLifecycle.html
---

# UpdateOrganizationRecommendationLifecycle
<a name="API_UpdateOrganizationRecommendationLifecycle"></a>

Update the lifecycle of a Recommendation within an Organization. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_UpdateOrganizationRecommendationLifecycle_RequestSyntax"></a>

```
PUT /v1/organization-recommendations/{{organizationRecommendationIdentifier}}/lifecycle HTTP/1.1
Content-type: application/json

{
   "lifecycleStage": "{{string}}",
   "updateReason": "{{string}}",
   "updateReasonCode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateOrganizationRecommendationLifecycle_RequestParameters"></a>

The request uses the following URI parameters.

 ** [organizationRecommendationIdentifier](#API_UpdateOrganizationRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateOrganizationRecommendationLifecycle-request-uri-organizationRecommendationIdentifier"></a>
The Recommendation identifier for AWS Trusted Advisor Priority recommendations
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+`
Required: Yes

## Request Body
<a name="API_UpdateOrganizationRecommendationLifecycle_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [lifecycleStage](#API_UpdateOrganizationRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateOrganizationRecommendationLifecycle-request-lifecycleStage"></a>
The new lifecycle stage
Type: String
Valid Values: `pending_response | in_progress | dismissed | resolved`
Required: Yes

 ** [updateReason](#API_UpdateOrganizationRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateOrganizationRecommendationLifecycle-request-updateReason"></a>
Reason for the lifecycle stage change
Type: String
Length Constraints: Minimum length of 10. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** [updateReasonCode](#API_UpdateOrganizationRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateOrganizationRecommendationLifecycle-request-updateReasonCode"></a>
Reason code for the lifecycle state change
Type: String
Valid Values: `non_critical_account | temporary_account | valid_business_case | other_methods_available | low_priority | not_applicable | other`
Required: No

## Response Syntax
<a name="API_UpdateOrganizationRecommendationLifecycle_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateOrganizationRecommendationLifecycle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateOrganizationRecommendationLifecycle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Exception that access has been denied due to insufficient access
HTTP Status Code: 403

 ** ConflictException **
Exception that the request was denied due to conflictions in state
HTTP Status Code: 409

 ** InternalServerException **
Exception to notify that an unexpected internal error occurred during processing of the request
HTTP Status Code: 500

 ** ResourceNotFoundException **
Exception that the requested resource has not been found
HTTP Status Code: 404

 ** ThrottlingException **
Exception to notify that requests are being throttled
HTTP Status Code: 429

 ** ValidationException **
Exception that the request failed to satisfy service constraints
HTTP Status Code: 400

## Examples
<a name="API_UpdateOrganizationRecommendationLifecycle_Examples"></a>

### Update the Lifecycle of an Organization Recommendation
<a name="API_UpdateOrganizationRecommendationLifecycle_Example_1"></a>

Update the lifecycle stage of an organization recommendation that is managed by AWS Trusted Advisor Priority.

#### Sample Request
<a name="API_UpdateOrganizationRecommendationLifecycle_Example_1_Request"></a>

```
{
                    "organizationRecommendationIdentifier": "arn:aws:trustedadvisor:::organization-recommendation/96b5e5ca-7930-444c-90c6-06d386128100",
                    "lifecycleStage": "dismissed",
                    "updateReasonCode": "not_applicable",
                    "updateReason": "Does not apply to this resource"
                    }
```

## See Also
<a name="API_UpdateOrganizationRecommendationLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/UpdateOrganizationRecommendationLifecycle)

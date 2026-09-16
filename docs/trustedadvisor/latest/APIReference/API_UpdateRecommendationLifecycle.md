---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_UpdateRecommendationLifecycle.html
---

# UpdateRecommendationLifecycle
<a name="API_UpdateRecommendationLifecycle"></a>

Update the lifecyle of a Recommendation. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_UpdateRecommendationLifecycle_RequestSyntax"></a>

```
PUT /v1/recommendations/{{recommendationIdentifier}}/lifecycle HTTP/1.1
Content-type: application/json

{
   "lifecycleStage": "{{string}}",
   "updateReason": "{{string}}",
   "updateReasonCode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRecommendationLifecycle_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationIdentifier](#API_UpdateRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateRecommendationLifecycle-request-uri-recommendationIdentifier"></a>
The Recommendation identifier for AWS Trusted Advisor Priority recommendations
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: Yes

## Request Body
<a name="API_UpdateRecommendationLifecycle_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [lifecycleStage](#API_UpdateRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateRecommendationLifecycle-request-lifecycleStage"></a>
The new lifecycle stage
Type: String
Valid Values: `pending_response | in_progress | dismissed | resolved`
Required: Yes

 ** [updateReason](#API_UpdateRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateRecommendationLifecycle-request-updateReason"></a>
Reason for the lifecycle stage change
Type: String
Length Constraints: Minimum length of 10. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** [updateReasonCode](#API_UpdateRecommendationLifecycle_RequestSyntax) **   <a name="ta-UpdateRecommendationLifecycle-request-updateReasonCode"></a>
Reason code for the lifecycle state change
Type: String
Valid Values: `non_critical_account | temporary_account | valid_business_case | other_methods_available | low_priority | not_applicable | other`
Required: No

## Response Syntax
<a name="API_UpdateRecommendationLifecycle_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateRecommendationLifecycle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRecommendationLifecycle_Errors"></a>

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
<a name="API_UpdateRecommendationLifecycle_Examples"></a>

### Update the Lifecycle of a Recommendation
<a name="API_UpdateRecommendationLifecycle_Example_1"></a>

Update the lifecycle stage of a recommendation managed by AWS Trusted Advisor Priority.

#### Sample Request
<a name="API_UpdateRecommendationLifecycle_Example_1_Request"></a>

```
{
                    "recommendationIdentifier": "arn:aws:trustedadvisor::000000000000:recommendation/861c9c6e-f169-405a-8b59-537a8caccd7a",
                    "lifecycleStage": "resolved",
                    "updateReasonCode": "valid_business_case",
                    "updateReason": "Resolved the recommendation"
                    }
```

## See Also
<a name="API_UpdateRecommendationLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/UpdateRecommendationLifecycle)

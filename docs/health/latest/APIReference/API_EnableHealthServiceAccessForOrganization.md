---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html
---

# EnableHealthServiceAccessForOrganization
<a name="API_EnableHealthServiceAccessForOrganization"></a>

Enables AWS Health to work with AWS Organizations. You can use the organizational view feature to aggregate events from all AWS accounts in your organization in a centralized location.

This operation also creates a service-linked role for the management account in the organization.

**Note**
To call this operation, you must meet the following requirements:
You must have a AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan from [AWS Support](http://aws.amazon.com/premiumsupport/) to use the AWS Health API. If you call the AWS Health API from an AWS account that doesn't have a AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, you receive a `SubscriptionRequiredException` error.
You must have permission to call this operation from the organization's management account. For example IAM policies, see [AWS Health identity-based policy examples](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html).

If you don't have the required support plan, you can instead use the AWS Health console to enable the organizational view feature. For more information, see [Aggregating AWS Health events](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) in the * AWS Health User Guide*.

## Response Elements
<a name="API_EnableHealthServiceAccessForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableHealthServiceAccessForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
 [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) is already in progress. Wait for the action to complete before trying again. To get the current status, use the [DescribeHealthServiceStatusForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html) operation.
HTTP Status Code: 400

## See Also
<a name="API_EnableHealthServiceAccessForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/EnableHealthServiceAccessForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EnableHealthServiceAccessForOrganization)

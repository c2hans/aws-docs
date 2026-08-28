---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SubscribedWorkteam.html
---

# SubscribedWorkteam
<a name="API_SubscribedWorkteam"></a>

Describes a work team of a vendor that does the labelling job.

## Contents
<a name="API_SubscribedWorkteam_Contents"></a>

 ** WorkteamArn **   <a name="sagemaker-Type-SubscribedWorkteam-WorkteamArn"></a>
The Amazon Resource Name (ARN) of the vendor that you have subscribed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

 ** ListingId **   <a name="sagemaker-Type-SubscribedWorkteam-ListingId"></a>
Marketplace product listing ID.
Type: String
Required: No

 ** MarketplaceDescription **   <a name="sagemaker-Type-SubscribedWorkteam-MarketplaceDescription"></a>
The description of the vendor from the Amazon Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.+`
Required: No

 ** MarketplaceTitle **   <a name="sagemaker-Type-SubscribedWorkteam-MarketplaceTitle"></a>
The title of the service provided by the vendor in the Amazon Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.+`
Required: No

 ** SellerName **   <a name="sagemaker-Type-SubscribedWorkteam-SellerName"></a>
The name of the vendor in the Amazon Marketplace.
Type: String
Required: No

## See Also
<a name="API_SubscribedWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SubscribedWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SubscribedWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SubscribedWorkteam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

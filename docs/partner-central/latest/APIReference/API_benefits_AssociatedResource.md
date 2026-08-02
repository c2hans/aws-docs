---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_AssociatedResource.html
---

# AssociatedResource
<a name="API_benefits_AssociatedResource"></a>

Represents an AWS resource that is associated with a benefit application for tracking and management.

## Contents
<a name="API_benefits_AssociatedResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceArn **   <a name="AWSPartnerCentral-Type-benefits_AssociatedResource-ResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the AWS resource.
Type: String
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`
Required: No

 ** ResourceIdentifier **   <a name="AWSPartnerCentral-Type-benefits_AssociatedResource-ResourceIdentifier"></a>
 *This member has been deprecated.*
The unique identifier of the AWS resource within its service.
Type: String
Required: No

 ** ResourceType **   <a name="AWSPartnerCentral-Type-benefits_AssociatedResource-ResourceType"></a>
The type of AWS resource (e.g., EC2 instance, S3 bucket, Lambda function).
Type: String
Valid Values: `OPPORTUNITY | BENEFIT_ALLOCATION`
Required: No

## See Also
<a name="API_benefits_AssociatedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/AssociatedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/AssociatedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/AssociatedResource)

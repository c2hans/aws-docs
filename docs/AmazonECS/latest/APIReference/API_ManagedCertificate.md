---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedCertificate.html
---

# ManagedCertificate
<a name="API_ManagedCertificate"></a>

The ACM certificate associated with the HTTPS domain created for the Express service.

## Contents
<a name="API_ManagedCertificate_Contents"></a>

 ** domainName **   <a name="ECS-Type-ManagedCertificate-domainName"></a>
The fully qualified domain name (FQDN) that is secured with this ACM certificate.
Type: String
Required: Yes

 ** status **   <a name="ECS-Type-ManagedCertificate-status"></a>
The status of the ACM; certificate.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedCertificate-updatedAt"></a>
The Unix timestamp for when the ACM certificate was last updated
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedCertificate-arn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedCertificate-statusReason"></a>
Information about why the ACM certificate is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedCertificate)

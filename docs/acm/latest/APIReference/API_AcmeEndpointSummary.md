---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_AcmeEndpointSummary.html
---

# AcmeEndpointSummary
<a name="API_AcmeEndpointSummary"></a>

Contains summary information about an ACME endpoint.

## Contents
<a name="API_AcmeEndpointSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AcmeEndpointArn **   <a name="ACM-Type-AcmeEndpointSummary-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: No

 ** AuthorizationBehavior **   <a name="ACM-Type-AcmeEndpointSummary-AuthorizationBehavior"></a>
The authorization behavior of the ACME endpoint.
Type: String
Valid Values: `PRE_APPROVED`
Required: No

 ** CertificateAuthority **   <a name="ACM-Type-AcmeEndpointSummary-CertificateAuthority"></a>
The certificate authority configuration for the ACME endpoint.
Type: [CertificateAuthority](API_CertificateAuthority.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** CertificateTags **   <a name="ACM-Type-AcmeEndpointSummary-CertificateTags"></a>
Tags applied to certificates issued through this ACME endpoint.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Contact **   <a name="ACM-Type-AcmeEndpointSummary-Contact"></a>
Whether ACME clients must provide contact information during account registration.
Type: String
Valid Values: `REQUIRED | NOT_REQUIRED`
Required: No

 ** CreatedAt **   <a name="ACM-Type-AcmeEndpointSummary-CreatedAt"></a>
The time at which the ACME endpoint was created.
Type: Timestamp
Required: No

 ** EndpointUrl **   <a name="ACM-Type-AcmeEndpointSummary-EndpointUrl"></a>
The URL of the ACME endpoint.
Type: String
Required: No

 ** FailureReason **   <a name="ACM-Type-AcmeEndpointSummary-FailureReason"></a>
The reason the ACME endpoint failed, if applicable.
Type: String
Required: No

 ** Status **   <a name="ACM-Type-AcmeEndpointSummary-Status"></a>
The status of the ACME endpoint.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** UpdatedAt **   <a name="ACM-Type-AcmeEndpointSummary-UpdatedAt"></a>
The time at which the ACME endpoint was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_AcmeEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmeEndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmeEndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmeEndpointSummary)

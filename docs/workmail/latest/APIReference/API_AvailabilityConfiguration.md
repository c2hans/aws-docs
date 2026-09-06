---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_AvailabilityConfiguration.html
---

# AvailabilityConfiguration
<a name="API_AvailabilityConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

List all the `AvailabilityConfiguration`'s for the given WorkMail organization.

## Contents
<a name="API_AvailabilityConfiguration_Contents"></a>

 ** DateCreated **   <a name="workmail-Type-AvailabilityConfiguration-DateCreated"></a>
The date and time at which the availability configuration was created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="workmail-Type-AvailabilityConfiguration-DateModified"></a>
The date and time at which the availability configuration was last modified.
Type: Timestamp
Required: No

 ** DomainName **   <a name="workmail-Type-AvailabilityConfiguration-DomainName"></a>
Displays the domain to which the provider applies.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** EwsProvider **   <a name="workmail-Type-AvailabilityConfiguration-EwsProvider"></a>
If `ProviderType` is `EWS`, then this field contains `RedactedEwsAvailabilityProvider`. Otherwise, it is not required.
Type: [RedactedEwsAvailabilityProvider](API_RedactedEwsAvailabilityProvider.md) object
Required: No

 ** LambdaProvider **   <a name="workmail-Type-AvailabilityConfiguration-LambdaProvider"></a>
If ProviderType is `LAMBDA` then this field contains `LambdaAvailabilityProvider`. Otherwise, it is not required.
Type: [LambdaAvailabilityProvider](API_LambdaAvailabilityProvider.md) object
Required: No

 ** ProviderType **   <a name="workmail-Type-AvailabilityConfiguration-ProviderType"></a>
Displays the provider type that applies to this domain.
Type: String
Valid Values: `EWS | LAMBDA`
Required: No

## See Also
<a name="API_AvailabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/AvailabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/AvailabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/AvailabilityConfiguration)

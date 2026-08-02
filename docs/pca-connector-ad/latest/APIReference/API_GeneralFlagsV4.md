---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GeneralFlagsV4.html
---

# GeneralFlagsV4
<a name="API_GeneralFlagsV4"></a>

General flags for v4 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.

## Contents
<a name="API_GeneralFlagsV4_Contents"></a>

 ** AutoEnrollment **   <a name="PcaConnectorAd-Type-GeneralFlagsV4-AutoEnrollment"></a>
Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.
Type: Boolean
Required: No

 ** MachineType **   <a name="PcaConnectorAd-Type-GeneralFlagsV4-MachineType"></a>
Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users
Type: Boolean
Required: No

## See Also
<a name="API_GeneralFlagsV4_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/GeneralFlagsV4)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/GeneralFlagsV4)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/GeneralFlagsV4)

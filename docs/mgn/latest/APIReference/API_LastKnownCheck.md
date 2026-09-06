---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_LastKnownCheck.html
---

# LastKnownCheck
<a name="API_LastKnownCheck"></a>

Last known check performed on a launched instance.

## Contents
<a name="API_LastKnownCheck_Contents"></a>

 ** checkedAt **   <a name="mgn-Type-LastKnownCheck-checkedAt"></a>
Last known check timestamp.
Type: Timestamp
Required: No

 ** error **   <a name="mgn-Type-LastKnownCheck-error"></a>
Last known check error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** name **   <a name="mgn-Type-LastKnownCheck-name"></a>
Last known check name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** status **   <a name="mgn-Type-LastKnownCheck-status"></a>
Last known check status.
Type: String
Valid Values: `PASSED | FAILED | PENDING`
Required: No

 ** type **   <a name="mgn-Type-LastKnownCheck-type"></a>
Last known check type.
Type: String
Valid Values: `EC2 | FSx`
Required: No

## See Also
<a name="API_LastKnownCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/LastKnownCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/LastKnownCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/LastKnownCheck)
